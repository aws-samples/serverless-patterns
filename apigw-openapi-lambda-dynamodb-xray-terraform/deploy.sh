# This code transpiles Typescript code into Javascript and packages third party libs to be deployed as lambda layer.  
# © 2023 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.  
# This AWS Content is provided subject to the terms of the AWS Customer Agreement available at  
# http://aws.amazon.com/agreement or other written agreement between Customer and either
# Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.

#!/bin/bash
set -ex

############################################ Build ###############################################
npm install
npm run build

# Layers base directory
BASE_DIR='dist/layer'
mkdir -p $BASE_DIR
cd $BASE_DIR

# Package AWS SDK
AWS_SDK_LIB_DIR='aws-sdk/nodejs/node_modules'
mkdir -p $AWS_SDK_LIB_DIR
cd $AWS_SDK_LIB_DIR
npm i @aws-sdk/client-dynamodb
npm i @aws-sdk/types
cd ../../../

# Package lambda powertools
LAMBDA_POWERTOOLS_LIB_DIR='lambda-powertools/nodejs/node_modules'
mkdir -p $LAMBDA_POWERTOOLS_LIB_DIR
cd $LAMBDA_POWERTOOLS_LIB_DIR
npm i @aws-lambda-powertools/logger @aws-lambda-powertools/tracer @aws-lambda-powertools/metrics
npm i @middy/core@~3
npm i @middy/http-header-normalizer
npm i @middy/http-router
cd ../../../

# Package other extarnal third party libs
EXT_LIB_DIR='ext-libs/nodejs/node_modules'
mkdir -p $EXT_LIB_DIR
cd $EXT_LIB_DIR
npm i dynamodb-toolbox
npm i nanoid@3.3.4 # Specific version for the reason specified here: https://github.com/ai/nanoid/issues/365
npm i class-transformer
npm i reflect-metadata
cd ../../../../../
##################################################################################################
############################################ Deploy ##############################################
# Teraform base directory
TF_DIR='infra'
terraform -chdir=$TF_DIR init
terraform -chdir=$TF_DIR apply -auto-approve
##################################################################################################