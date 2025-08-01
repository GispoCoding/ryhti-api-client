#!/bin/bash

api_dir=$1

cp -rf .generated/$api_dir/ryhti_api_client/models src/ryhti_api_client/
cp -rf .generated/$api_dir/ryhti_api_client/${api_dir}_api src/ryhti_api_client/
cp -rf .generated/$api_dir/ryhti_api_client/docs ./
# cp -rf .generated/$api_dir/ryhti_api_client/test ./
cp -f .generated/$api_dir/ryhti_api_client/* src/ryhti_api_client/ 2>/dev/null
