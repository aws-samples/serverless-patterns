# Creating script for bootstrapping of secrets needed for DAS to work
#!/bin/bash

aws iam create-user --user-name $1 --output json --no-cli-pager

aws iam attach-user-policy --user-name $1 --policy-arn arn:aws:iam::aws:policy/AdministratorAccess --output json --no-cli-pager

ACCESSKEY=$(aws iam create-access-key --user-name $1 --output json --no-cli-pager)

ACCESSKEYID=$(echo $ACCESSKEY | jq -r '.AccessKey.AccessKeyId')

SECRETKEYID=$(echo $ACCESSKEY | jq -r '.AccessKey.SecretAccessKey')

aws secretsmanager create-secret --name aws-access-key-id --secret-string {\"aws-access-key-id\":\"$ACCESSKEYID\"}

aws secretsmanager create-secret --name aws-secret-access-key --secret-string {\"aws-secret-access-key\":\"$SECRETKEYID\"}

aws configure set aws_access_key_id $ACCESSKEYID --profile $1

aws configure set aws_secret_access_key $SECRETKEYID --profile $1

aws configure set region $AWS_REGION --profile $1