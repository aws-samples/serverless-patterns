# Creating script for getting AWS Keys needed to set-up CLI profile on local machine
#!/bin/bash

AWS_ACCESS_KEY=$(aws configure get aws_access_key_id --profile $1)
echo $AWS_ACCESS_KEY
AWS_SECRET_ACCESS_KEY=$(aws configure get aws_secret_access_key --profile $1)
echo $AWS_SECRET_ACCESS_KEY
AWS_CLI_REGION=$(aws configure get region --profile $1)
echo $AWS_CLI_REGION