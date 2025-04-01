# Creating script for bootstrapping of secrets needed for DAS to work
#!/bin/bash

username=$1
# Variable name to check
region=$AWS_REGION
# Default value if the variable is not set
default_value="us-east-1"

# Check if the variable is set
if [ -n "$region" ]; then
  # Variable exists, use its value
  value=$region
  echo "Variable \$AWS_REGION exists and its value is: $value"
else
  # Variable does not exist, set it to the default value
  region=$default_value
  echo "Variable \$AWS_REGION does not exist. Setting it to default value: $default_value"
fi

echo "Creating user $username"
# prompt for password
read -s -p "Enter password: " password
echo    # Move to the next line after password input

echo "Creating user $username"
aws iam create-user --user-name $username --output json --no-cli-pager
aws iam create-login-profile --user-name $username --password $password --password-reset-required --output json --no-cli-pager
aws iam attach-user-policy --user-name $username --policy-arn arn:aws:iam::aws:policy/AdministratorAccess --output json --no-cli-pager

echo "Creating access key..."
ACCESSKEY=$(aws iam create-access-key --user-name $username --output json --no-cli-pager)
ACCESSKEYID=$(echo $ACCESSKEY | jq -r '.AccessKey.AccessKeyId')
SECRETKEYID=$(echo $ACCESSKEY | jq -r '.AccessKey.SecretAccessKey')

echo "Checking if secrets exist..."
aws secretsmanager delete-secret --secret-id aws-access-key-id --force-delete-without-recovery --region $region
aws secretsmanager delete-secret --secret-id aws-secret-access-key --force-delete-without-recovery --region $region

sleep 10

echo "Creating secrets..."
aws secretsmanager create-secret --name aws-access-key-id --secret-string {\"aws-access-key-id\":\"$ACCESSKEYID\"}
aws secretsmanager create-secret --name aws-secret-access-key --secret-string {\"aws-secret-access-key\":\"$SECRETKEYID\"}

echo "Configuring profile..."
aws configure set aws_access_key_id $ACCESSKEYID --profile $username
aws configure set aws_secret_access_key $SECRETKEYID --profile $username
aws configure set region $AWS_REGION --profile $username

echo "Your access Key:"
echo $ACCESSKEYID
echo "Your secret Key:"
echo $SECRETKEYID
echo "Your region:"
echo $region
