#!/bin/bash

release_tag=$1

download_api_specs() {
  mkdir -p "api_specs"
  
  wget "https://raw.githubusercontent.com/sykefi/Ryhti-rajapintakuvaukset/refs/tags/${release_tag}/OpenApi/Alueidenk%C3%A4ytt%C3%B6/Avoin/ryhti-plan-public-validate-api.json" -O "api_specs/ryhti-plan-public-validate-api.json"
  wget "https://raw.githubusercontent.com/sykefi/Ryhti-rajapintakuvaukset/refs/tags/${release_tag}/OpenApi/Alueidenk%C3%A4ytt%C3%B6/Palveluv%C3%A4yl%C3%A4/planService-OpenApi.json" -O "api_specs/planService-OpenApi.json"
}

replace_description() {
  local file_path=$1
  jq -r '.info.description |= "Rakennetun ympäristön tietojärjestelmän rajapinta"' "$file_path" > "${file_path}.tmp" && mv "${file_path}.tmp" "$file_path"
}

remove_servers(){
  local file_path=$1
  jq -r 'del(.servers)' "$file_path" > "${file_path}.tmp" && mv "${file_path}.tmp" "$file_path"
}

# The upstream specs use oneOf without a discriminator, see scripts/add_discriminators.jq
add_discriminators() {
  local file_path=$1
  jq -f "$(dirname "$0")/add_discriminators.jq" "$file_path" > "${file_path}.tmp" \
    && mv "${file_path}.tmp" "$file_path" \
    || { echo "add_discriminators.jq failed for $file_path" >&2; exit 1; }
}

generate_client() {
  local input_file=$1
  local output_dir=$2
  local api_dir=${output_dir}_api

  uv run openapi-generator-cli generate \
      -i "$input_file" \
      -g python \
      --additional-properties=packageName=ryhti_api_client \
      --additional-properties=generateSourceCodeOnly=true \
      --additional-properties=setEnsureAsciiToFalse=true \
      --additional-properties=useOneOfDiscriminatorLookup=true \
      --api-package=$api_dir \
      -o ".generated/$output_dir"

  uv run ruff check --fix --extend-fixable=F841,F401 .generated/$output_dir
  uv run ruff format .generated/$output_dir

  find .generated/$output_dir \( -type d -name .git -prune \) -o -type f -print0 | xargs -0 sed -i "s/from $api_dir/from ryhti_api_client.$api_dir/g"

  git add .generated/$output_dir
  git add $input_file
  git commit -m "Update generated client for $output_dir API"
}

download_api_specs
replace_description "api_specs/ryhti-plan-public-validate-api.json"
replace_description "api_specs/planService-OpenApi.json"
remove_servers "api_specs/ryhti-plan-public-validate-api.json"
add_discriminators "api_specs/ryhti-plan-public-validate-api.json"
add_discriminators "api_specs/planService-OpenApi.json"

generate_client "api_specs/ryhti-plan-public-validate-api.json" "public"
generate_client "api_specs/planService-OpenApi.json" "xroad"
