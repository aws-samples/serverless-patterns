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
##################################################################################################
############################################ Deploy ##############################################
# Teraform base directory
TF_DIR='infra'
terraform -chdir=$TF_DIR init
terraform -chdir=$TF_DIR apply -auto-approve
##################################################################################################