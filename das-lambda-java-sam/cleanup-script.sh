# Cleanup script - removing DAS bucket, main stack, SAM bucket, SAM stack, OSI, secrets, CFT and CF template buckets
#!/bin/bash

# empty the contents of the S3 bucket that was being used to store the Database Activity Streams events by first getting the name of the bucket and then empty its contents:
echo "Emptying and deleting DAS s3 bucket..."
DAS_BUCKET_NAME=$(aws cloudformation describe-stacks --stack-name $STACK_NAME --profile $AWS_USER --query "Stacks[*].Outputs[?OutputKey=='S3BucketName'].OutputValue" --output text --no-cli-pager)
aws s3 rm s3://$DAS_BUCKET_NAME --recursive --profile $AWS_USER
echo    # Move to the next line

# delete the main CloudFormation stack and wait for it to complete.
echo "Deleting $STACK_NAME CloudFormation stack..."
aws cloudformation delete-stack --stack-name $STACK_NAME --deletion-mode STANDARD --region $AWS_REGION --profile $AWS_USER
aws cloudformation wait stack-delete-complete --profile $AWS_USER --stack-name $STACK_NAME
echo    # Move to the next line

# empty the SAM S3 bucket, including versions and delete markers.
echo "Emptying and deleting SAM s3 bucket... including all objects versions"
SAM_BUCKET_NAME=$(aws s3api list-buckets --query "Buckets[?starts_with(Name, 'aws-sam-cli-')].Name" --profile $AWS_USER --no-cli-pager --output text)
aws s3 rm s3://$SAM_BUCKET_NAME --recursive --profile $AWS_USER
aws s3api delete-objects --profile $AWS_USER --bucket $SAM_BUCKET_NAME --no-cli-pager --output text --delete "$(aws s3api list-object-versions --profile $AWS_USER --bucket $SAM_BUCKET_NAME --query='{Objects: Versions[].{Key:Key,VersionId:VersionId}}')" 
aws s3api delete-objects --profile $AWS_USER --bucket $SAM_BUCKET_NAME --no-cli-pager --output text --delete "$(aws s3api list-object-versions --profile $AWS_USER --bucket $SAM_BUCKET_NAME --query='{Objects: DeleteMarkers[].{Key:Key,VersionId:VersionId}}')"
echo    # Move to the next line

# delete the aws-sam-cli-managed-default CloudFormation stack and wait for it to complete.
echo "Deleting aws-sam-cli-managed-default CloudFormation stack..."
aws cloudformation delete-stack --stack-name aws-sam-cli-managed-default --deletion-mode STANDARD --region $AWS_REGION --profile $AWS_USER
aws cloudformation wait stack-delete-complete --profile $AWS_USER --stack-name $STACK_NAME
echo    # Move to the next line

# clean-up the OpenSearch Ingestion Pipeline that was created from the UserData of the CloudFormation templation using AWS CLI as follows:
echo "Deleting OpenSearch Pipeline..."
aws osis delete-pipeline --pipeline-name "das-osi-pipeline" --profile $AWS_USER
echo    # Move to the next line

# clean-up the two secrets for storing the credentials of the IAM user in SecretsManager:
echo "Deleting secrets..."
aws secretsmanager delete-secret --secret-id aws-access-key-id --force-delete-without-recovery --region $AWS_REGION --no-cli-pager --profile $AWS_USER
aws secretsmanager delete-secret --secret-id aws-secret-access-key --force-delete-without-recovery --region $AWS_REGION --no-cli-pager --profile $AWS_USER
echo    # Move to the next line

# cleanup the S3 bucket and its content that was created to support the CloudFormation template deployment.
echo "Emptying and deleting CFT s3 bucket..."
CFT_BUCKET_NAME=$(aws s3api list-buckets --query "Buckets[?starts_with(Name, 'cft-bucket-')].Name" --profile $AWS_USER --no-cli-pager --output text)
aws s3 rm s3://$CFT_BUCKET_NAME --recursive --profile $AWS_USER
aws s3api delete-bucket --bucket $CFT_BUCKET_NAME --region $AWS_REGION --profile $AWS_USER
echo    # Move to the next line

# empty and delete the cf-template bucket as well
echo "Emptying and deleting CF template s3 bucket..."
CF_TEMPLATE_BUCKET_NAME=$(aws s3api list-buckets --query "Buckets[?starts_with(Name, 'cf-templates-')].Name" --profile $AWS_USER --no-cli-pager --output text)
aws s3 rm s3://$CF_TEMPLATE_BUCKET_NAME --recursive --profile $AWS_USER
aws s3api delete-bucket --bucket $CF_TEMPLATE_BUCKET_NAME --profile $AWS_USER --region $AWS_REGION
echo    # Move to the next line

echo "Done!"
