#!/usr/bin/env python3
"""Turn openapi-generator's oneOf wrapper classes into pydantic discriminated unions.

Run after copy_generated_client.sh (the copy script does it and runs ruff on the
result). For every generated oneOf wrapper module (the ones holding ``actual_instance``) this script:

* rewrites each variant's tag field (``dataType`` / ``type``) from ``StrictStr``
  plus an enum validator into ``Literal["<tag>"]`` and detaches the variant from
  the generated base class,
* replaces the base class module (``AttributeValue``, ``GeoJsonGeometry``) with a
  ``typing.Union`` alias of the variants,
* types the consuming fields as ``Optional[<Alias>] = Field(discriminator=...)``
  and lets pydantic parse the raw dict in ``from_dict``,
* removes the wrapper modules, their exports and their docs, and rewrites the
  alias docs.

Everything is derived from the generated code, so the tag values must already be
unambiguous (scripts/add_discriminators.jq takes care of that before generation).
Running the script again is a no-op.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

PKG = "ryhti_api_client"
CLASS_RE = re.compile(r"^class (\w+)\((\w+)\):", re.M)
# Union alias (class, module) for wrappers whose variants have no generated base
# class to take the name from: the xroad spec has no GeoJsonGeometry schema, so name
# its geometry union like the public API's.
UNION_NAMES = {"RyhtiGeometryGeometry": ("GeoJsonGeometry", "geo_json_geometry")}


@dataclass
class Wrapper:
    path: Path
    cls: str
    variants: list[str]
    module_of: dict[str, str]

    @property
    def module(self) -> str:
        return self.path.stem


@dataclass
class UnionSpec:
    alias: str
    module: str
    tag_field: str  # python field name, e.g. data_type
    tag_json: str  # wire name, e.g. dataType
    variants: dict[str, str] = field(default_factory=dict)  # class -> module
    tags: dict[str, str] = field(default_factory=dict)  # class -> tag value
    wrappers: list[Wrapper] = field(default_factory=list)
    consumers: list[tuple[str, str]] = field(default_factory=list)  # (module, field)


def die(msg: str) -> None:
    sys.exit(f"fix_discriminated_unions: {msg}")


def import_re(module: str, name: str) -> re.Pattern:
    return re.compile(
        rf"^from {PKG}\.models\.{module} import \(?\s*{name},?\s*\)?\n", re.M
    )


def rewrite_import_list(
    text: str, stmt_re: re.Pattern, prefix: str, add=(), drop_if_unused=()
) -> str:
    m = stmt_re.search(text)
    if not m:
        return (
            text
            if not add
            else text.replace("\n\n", f"\n{prefix}{', '.join(add)}\n\n", 1)
        )
    names = set(re.findall(r"\w+", m.group(1))) | set(add)
    body = text[: m.start()] + text[m.end() :]
    names -= {n for n in drop_if_unused if not re.search(rf"\b{n}\b", body)}
    return (
        text[: m.start()] + prefix + ", ".join(sorted(names)) + "\n" + text[m.end() :]
    )


PYDANTIC_IMPORT_RE = re.compile(r"^from pydantic import (\([^)]*\)|[^\n]+)\n", re.M)
TYPING_IMPORT_RE = re.compile(r"^from typing import ((?:\([^)]*\)|[^\n]+))\n", re.M)


def find_wrappers(models_dir: Path) -> list[Wrapper]:
    wrappers = []
    for path in sorted(models_dir.glob("*.py")):
        text = path.read_text()
        if "actual_instance" not in text or "_ONE_OF_SCHEMAS" not in text:
            continue
        cls = CLASS_RE.search(text).group(1)
        variants = re.findall(
            r'"(\w+)"',
            re.search(r"_ONE_OF_SCHEMAS\s*=\s*\[(.*?)\]", text, re.S).group(1),
        )
        module_of = {
            c: m
            for m, c in re.findall(
                rf"^from {PKG}\.models\.(\w+) import \(?\s*(\w+)", text, re.M
            )
        }
        missing = [v for v in variants if v not in module_of]
        if missing:
            die(f"{path.name}: cannot find modules of variants {missing}")
        wrappers.append(Wrapper(path, cls, variants, module_of))
    return wrappers


def single_value_validators(text: str) -> dict[str, str]:
    """Fields validated against a single enum value, e.g. {'data_type': 'Code'}."""
    pattern = r"^    @field_validator\([\"'](\w+)[\"']\)\n(?:.*\n)*?        if value not in set\(\[([\"'])([^\"']+)\2\]\):"
    return {m.group(1): m.group(3) for m in re.finditer(pattern, text, re.M)}


def class_maps(models_dir: Path) -> dict[str, tuple[Path, dict[str, str]]]:
    """Generated base classes carrying a discriminator map: class -> (path, {tag: class})."""
    out = {}
    for path in models_dir.glob("*.py"):
        text = path.read_text()
        m = re.search(
            r"__discriminator_value_class_map: ClassVar\[Dict\[str, str\]\] = \{(.*?)\}",
            text,
            re.S,
        )
        if m:
            mapping = dict(
                re.findall(r"[\"']([^\"']+)[\"']\s*:\s*[\"'](\w+)[\"']", m.group(1))
            )
            out[CLASS_RE.search(text).group(1)] = (path, mapping)
    return out


def build_union_specs(
    models_dir: Path, wrappers: list[Wrapper]
) -> dict[str, UnionSpec]:
    maps = class_maps(models_dir)
    specs: dict[str, UnionSpec] = {}
    for w in wrappers:
        infos = {}
        for v in w.variants:
            text = (models_dir / f"{w.module_of[v]}.py").read_text()
            infos[v] = (
                CLASS_RE.search(text).group(2),
                single_value_validators(text),
                text,
            )
        common = set.intersection(*(set(tags) for _, tags, _ in infos.values()))
        if len(common) != 1:
            die(
                f"{w.cls}: variants do not share exactly one single-valued tag field, got {sorted(common)}"
            )
        tag_field = common.pop()
        bases = {base for base, _, _ in infos.values()}
        if len(bases) == 1 and bases != {"BaseModel"}:
            alias = bases.pop()
            module = next(
                p
                for p in models_dir.glob("*.py")
                if re.search(rf"^class {alias}\(", p.read_text(), re.M)
            ).stem
        else:
            alias = next(
                (
                    c
                    for c, (_, mp) in maps.items()
                    if set(mp.values()) == set(w.variants)
                ),
                None,
            )
            if alias:
                module = maps[alias][0].stem
            else:
                alias, module = UNION_NAMES.get(w.cls, (w.cls, w.module))
        first_text = next(iter(infos.values()))[2]
        m = re.search(rf"^    {tag_field}: .*?alias=\"(\w+)\"", first_text, re.M | re.S)
        spec = specs.setdefault(
            alias, UnionSpec(alias, module, tag_field, m.group(1) if m else tag_field)
        )
        if (spec.module, spec.tag_field) != (module, tag_field):
            die(f"{w.cls}: conflicting union definition for {alias}")
        spec.wrappers.append(w)
        for v, (base, tags, _) in infos.items():
            spec.variants[v] = w.module_of[v]
            spec.tags[v] = tags[tag_field]
    return specs


def rewrite_variant(
    path: Path, spec: UnionSpec, tag: str, all_aliases: dict[str, str]
) -> None:
    text = path.read_text()
    cls, base = CLASS_RE.search(text).groups()
    if base != "BaseModel":
        text = CLASS_RE.sub(rf"class {cls}(BaseModel):", text, count=1)
        text = import_re(all_aliases.get(base, "\\w+"), base).sub("", text)
    text, n = re.subn(
        rf"^(    {spec.tag_field}): StrictStr\b",
        rf'\1: Literal["{tag}"]',
        text,
        flags=re.M,
    )
    if n != 1:
        die(f"{path.name}: expected one '{spec.tag_field}: StrictStr' field, found {n}")
    text, n = re.subn(
        rf"^    @field_validator\([\"']{spec.tag_field}[\"']\)\n(?:.*\n)*?        return value\n\n?",
        "",
        text,
        flags=re.M,
    )
    if n != 1:
        die(f"{path.name}: expected one validator for {spec.tag_field}, found {n}")
    text = rewrite_import_list(
        text,
        PYDANTIC_IMPORT_RE,
        "from pydantic import ",
        add={"BaseModel"},
        drop_if_unused={"StrictStr", "field_validator"},
    )
    if not re.search(r"^from typing import .*\bLiteral\b", text, re.M):
        text = rewrite_import_list(
            text, TYPING_IMPORT_RE, "from typing import ", add={"Literal"}
        )
    path.write_text(text)


def write_alias(models_dir: Path, spec: UnionSpec) -> None:
    lines = ["from typing import Union", ""]
    lines += [
        f"from {PKG}.models.{m} import {c}" for c, m in sorted(spec.variants.items())
    ]
    lines += [
        "",
        f"{spec.alias} = Union[",
        *[f"    {c}," for c in sorted(spec.variants)],
        "]",
        "",
        f'__all__ = ["{spec.alias}"]',
        "",
    ]
    (models_dir / f"{spec.module}.py").write_text("\n".join(lines))


def rewrite_consumer(path: Path, spec: UnionSpec) -> bool:
    text = path.read_text()
    touched = False
    for w in spec.wrappers:
        if not re.search(rf"\b{w.cls}\b", text):
            continue
        touched = True
        alias_import = f"from {PKG}.models.{spec.module} import {spec.alias}\n"
        if w.cls != spec.alias:  # otherwise the wrapper module became the alias module
            text = import_re(w.module, w.cls).sub(
                "" if alias_import in text else alias_import.replace("\\", "\\\\"),
                text,
            )

        def field_repl(m: re.Match) -> str:
            head, typ, rest = (
                m.group(1),
                f"{m.group(2) or ''}{spec.alias}{m.group(3) or ''}",
                m.group(4).strip(),
            )
            spec.consumers.append((path.stem, head.strip().split(":")[0]))
            if rest == "= None":
                return f'{head}: {typ} = Field(discriminator="{spec.tag_field}", default=None)'
            if rest == "":
                return f'{head}: {typ} = Field(discriminator="{spec.tag_field}")'
            if rest.startswith("= Field("):
                new_rest = rest.replace(
                    "= Field(", f'= Field(discriminator="{spec.tag_field}", ', 1
                )
                return f"{head}: {typ} {new_rest}"
            die(f"{path.name}: unsupported field declaration '{m.group(0).strip()}'")

        text = re.sub(
            rf"^(\s+\w+): (Optional\[)?{w.cls}(\])?(.*)$", field_repl, text, flags=re.M
        )
        text = re.sub(
            rf'{w.cls}\.from_dict\(obj\["(\w+)"\]\)\s*if obj\.get\("\1"\) is not None\s*else None',
            r'obj.get("\1")',
            text,
        )
        if w.cls != spec.alias and re.search(rf"\b{w.cls}\b", text):
            die(f"{path.name}: unhandled reference to {w.cls}")
    if touched:
        text = rewrite_import_list(
            text, PYDANTIC_IMPORT_RE, "from pydantic import ", add={"Field"}
        )
        path.write_text(text)
    return touched


def strip_exports(init: Path, wrappers: list[Wrapper]) -> None:
    text = init.read_text()
    for w in wrappers:
        text = re.sub(
            rf"^from {PKG}\.models\.{w.module} import (?:\([^)]*\)|[^\n]*)\n",
            "",
            text,
            flags=re.M,
        )
        text = re.sub(rf'^    "{w.cls}",\n', "", text, flags=re.M)
    init.write_text(text)


def write_docs(docs: Path, spec: UnionSpec, deleted: list[Wrapper]) -> None:
    for w in deleted:
        (docs / f"{w.cls}.md").unlink(missing_ok=True)
    for md in docs.glob("*.md"):
        text = md.read_text()
        for w in deleted:
            text = text.replace(
                f"[**{w.cls}**]({w.cls}.md)", f"[**{spec.alias}**]({spec.alias}.md)"
            )
        md.write_text(text)
    rows = "\n".join(
        f"`{spec.tags[c]}` | [**{c}**]({c}.md)"
        for c in sorted(spec.variants, key=lambda c: spec.tags[c])
    )
    consumer_module, consumer_field = spec.consumers[0] if spec.consumers else ("", "")
    consumer_cls = re.sub(r"(^|_)(\w)", lambda m: m.group(2).upper(), consumer_module)
    first = sorted(spec.variants)[0]
    example = (
        f"from {PKG}.models.{spec.variants[first]} import {first}\n"
        f"from {PKG}.models.{consumer_module} import {consumer_cls}\n\n"
        f'obj = {consumer_cls}.from_dict({{..., "{consumer_field}": {{"{spec.tag_json}": "{spec.tags[first]}", ...}}}})\n'
        f"assert isinstance(obj.{consumer_field}, {first})\n"
    )
    (docs / f"{spec.alias}.md").write_text(
        f"# {spec.alias}\n\n`{spec.alias}` is a `typing.Union` of the concrete models below. "
        f"The variant is chosen by the `{spec.tag_json}` field (pydantic discriminated union).\n\n"
        f"{spec.tag_json} value | Model\n------------ | -------------\n{rows}\n\n## Example\n\n```python\n{example}```\n"
        "[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)\n"
    )


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="project root",
    )
    root = ap.parse_args().root
    pkg_dir, docs = root / "src" / PKG, root / "docs"
    models_dir = pkg_dir / "models"
    wrappers = find_wrappers(models_dir)
    if not wrappers:
        print("fix_discriminated_unions: no oneOf wrappers found, nothing to do")
        return
    specs = build_union_specs(models_dir, wrappers)
    all_aliases = {s.alias: s.module for s in specs.values()}
    wrapper_paths = {w.path for w in wrappers}
    for spec in specs.values():
        for cls, module in spec.variants.items():
            rewrite_variant(
                models_dir / f"{module}.py", spec, spec.tags[cls], all_aliases
            )
        write_alias(models_dir, spec)
        consumers = [
            p
            for p in sorted(models_dir.glob("*.py"))
            if p not in wrapper_paths and p.name != "__init__.py"
        ]
        touched = [p.name for p in consumers if rewrite_consumer(p, spec)]
        deleted = [w for w in spec.wrappers if w.module != spec.module]
        for w in deleted:
            w.path.unlink()
        for init in (models_dir / "__init__.py", pkg_dir / "__init__.py"):
            strip_exports(init, deleted)
        if docs.is_dir():
            write_docs(docs, spec, deleted)
        print(
            f"{spec.alias} = Union[{len(spec.variants)} variants] (tag {spec.tag_json}); "
            f"replaced {', '.join(w.cls for w in spec.wrappers)}; consumers: {', '.join(touched)}"
        )


if __name__ == "__main__":
    main()
