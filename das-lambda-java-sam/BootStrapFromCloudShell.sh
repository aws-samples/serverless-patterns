# Creating script for bootstrapping of secrets needed for DAS to work
#!/bin/bash

aws iam create-user --user-name $0 --output json --no-cli-pager

aws iam create-login-profile --user-name $0 --password $1 --password-reset-required --output json --no-cli-pager

aws iam attach-user-policy --user-name $0 --policy-arn arn:aws:iam::aws:policy/AdministratorAccess --output json --no-cli-pager

ACCESSKEY=$(aws iam create-access-key --user-name $0 --output json --no-cli-pager)

ACCESSKEYID=$(echo $ACCESSKEY | jq -r '.AccessKey.AccessKeyId')

SECRETKEYID=$(echo $ACCESSKEY | jq -r '.AccessKey.SecretAccessKey')

aws secretsmanager create-secret --name aws-access-key-id --secret-string {\"aws-access-key-id\":\"$ACCESSKEYID\"}

aws secretsmanager create-secret --name aws-secret-access-key --secret-string {\"aws-secret-access-key\":\"$SECRETKEYID\"}