# Makes the polymorphic parts of the Ryhti OpenAPI specs unambiguous.
#
# The upstream specs model attribute values (AttributeValue.dataType) and GeoJSON
# geometries (.type) as oneOf without a discriminator, and every subclass' tag enum
# lists all sibling values. Code generators then have to try every variant and fail
# with "Multiple matches found". Until this is fixed upstream, this filter:
#   - narrows each oneOf variant's tag enum to its own value and moves the tag
#     property first: with a discriminator on the base class openapi-generator
#     emits the variants as subclasses and keeps the spec's property order instead
#     of putting required properties first, so the tag would otherwise move to the
#     end of the generated models and docs
#   - adds a discriminator (propertyName + mapping) to every oneOf property
#   - adds the same discriminator to the allOf base classes, makes the tag required
#     there and drops additionalProperties:false, which otherwise rejects every
#     subclass property under strict JSON Schema validation
# The tag is derived from the variant's schema name: GeoJsonPointGeometry -> Point,
# CodeValue -> Code, NumericRange -> NumericRange. The filter fails if the tag is
# not in the variant's enum, so an upstream rename breaks the build instead of
# silently producing a broken client.

def schema_name: ltrimstr("#/components/schemas/");
def schema_ref: "#/components/schemas/" + .;
def tag_of: ltrimstr("GeoJson") | rtrimstr("Value") | rtrimstr("Geometry");
def ensure_required($prop): (. // []) | if index($prop) then . else . + [$prop] end;

# Every property that is a oneOf of schema references: [{schema, prop, variants}]
def oneof_sites:
  [ .components.schemas | to_entries[] as $s
    | ($s.value.properties // {}) | to_entries[] as $p
    | select($p.value.oneOf != null)
    | { schema: $s.key, prop: $p.key,
        variants: [ $p.value.oneOf[]."$ref" | schema_name ] } ];

def fix_site($site):
  . as $spec
  | ($site.variants | map($spec.components.schemas[.].properties // {})) as $props
  | (["dataType", "type"] | map(select(. as $p | $props | all(has($p)))) | first) as $prop
  | if $prop == null
    then error("no tag property shared by the variants of \($site.schema).\($site.prop)") else . end
  | ($site.variants | map({ key: tag_of, value: schema_ref }) | from_entries) as $mapping
  # narrow every variant's tag enum to its own value and keep the tag property first
  | reduce $site.variants[] as $v (.;
      ($v | tag_of) as $tag
      | if (($spec.components.schemas[$v].properties[$prop].enum // []) | index($tag)) == null
        then error("\($v).\($prop) enum does not contain \"\($tag)\"") else . end
      | .components.schemas[$v].properties |= ({($prop): .[$prop]} + .)
      | .components.schemas[$v].properties[$prop].enum = [$tag]
      | .components.schemas[$v].properties[$prop].description |=
          (if . == null then . else sub("Pakollinen arvo: \"[^\"]*\""; "Pakollinen arvo: \"\($tag)\"") end)
      | .components.schemas[$v].required |= ensure_required($prop))
  # discriminator on the oneOf property itself
  | .components.schemas[$site.schema].properties[$site.prop].discriminator =
      { propertyName: $prop, mapping: $mapping }
  # and on the allOf base classes of the variants, if any
  | reduce ($site.variants
            | map($spec.components.schemas[.].allOf // [] | .[]."$ref" | schema_name)
            | unique | .[]) as $base (.;
      .components.schemas[$base] |= (
        .discriminator = { propertyName: $prop, mapping: $mapping }
        | .required |= ensure_required($prop)
        | if .additionalProperties == false then del(.additionalProperties) else . end));

reduce oneof_sites[] as $site (.; fix_site($site))
