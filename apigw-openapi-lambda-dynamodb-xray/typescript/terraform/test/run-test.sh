# This code transpiles Typescript code into Javascript and packages third party libs to be deployed as lambda layer.  
# © 2023 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.  
# This AWS Content is provided subject to the terms of the AWS Customer Agreement available at  
# http://aws.amazon.com/agreement or other written agreement between Customer and either
# Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.

#!/bin/bash
set -ex

# CLI Arguments
if [ -z $1 ]
then
    echo "API Gateway base url was not passsed."
    exit -1
else
	REST_API_URL_BASE=$1
fi

# Create new customer
customer=$(curl -d "@test/request.json" \
    -H "Content-Type: application/json" \
    -X POST $REST_API_URL_BASE/customers)

# Fetch id from response
id=$(echo $customer | jq -r '.id')

# Get customer by id
curl "$REST_API_URL_BASE/customers/$id"

