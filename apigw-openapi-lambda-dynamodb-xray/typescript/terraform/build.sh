# This code transpiles Typescript code into Javascript and packages third party libs to be deployed as lambda layer.  
# © 2023 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.  
# This AWS Content is provided subject to the terms of the AWS Customer Agreement available at  
# http://aws.amazon.com/agreement or other written agreement between Customer and either
# Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.

#!/bin/bash
set -ex

############################################ Build ###############################################

# Layers base directory
BASE_DIR='dist/layer'
mkdir -p $BASE_DIR
cd $BASE_DIR

# Package AWS SDK
AWS_SDK_LIB_DIR='aws-sdk/nodejs/node_modules'
mkdir -p $AWS_SDK_LIB_DIR
cd $AWS_SDK_LIB_DIR
npm i @aws-sdk/client-dynamodb@3.370.0
npm i @aws-sdk/types@3.370.0
cd ../../../

# Package lambda powertools
LAMBDA_POWERTOOLS_LIB_DIR='lambda-powertools/nodejs/node_modules'
mkdir -p $LAMBDA_POWERTOOLS_LIB_DIR
cd $LAMBDA_POWERTOOLS_LIB_DIR
npm i @aws-lambda-powertools/logger@1.11.1 @aws-lambda-powertools/tracer@1.11.1 @aws-lambda-powertools/metrics@1.11.1
npm i @middy/core@3.6.2
npm i @middy/http-header-normalizer@4.6.0
npm i @middy/http-router@4.6.0
cd ../../../

# Package other extarnal third party libs
EXT_LIB_DIR='ext-libs/nodejs/node_modules'
mkdir -p $EXT_LIB_DIR
cd $EXT_LIB_DIR
npm i dynamodb-toolbox@0.8.5
npm i nanoid@3.3.4 # Specific version for the reason specified here: https://github.com/ai/nanoid/issues/365
npm i class-transformer@0.5.1
npm i reflect-metadata@0.1.13
cd ../../../../../
##################################################################################################
