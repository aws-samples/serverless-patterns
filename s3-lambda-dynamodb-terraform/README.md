# Load data from JSON files in Amazon S3 into Amazon DynamoDB using S3 Event Notification and AWS Lambda

This pattern in [Terraform](https://www.terraform.io/) offers a complete solution to load data from JSON files uploaded to S3. The following resources are created:
1. S3 Bucket with event notification on object created
2. DynamoDB Table with on-demand billing mode
3. Lambda function that runs python with an environment variable containing the dynamodb table name 

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform installed](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) with version 1.x installed (this pattern has been tested with version 1.9.8)

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory its source code folder:
    ```bash
    cd s3-lambda-dynamodb-terraform/
    ```
3. From the command line, use Terraform to deploy the AWS resources for the pattern as specified in the main.tf file::
    ```terraform init
    terraform apply --auto-approve
    ```
4. Note the outputs from the Terraform deployment process. These contain the resource names and/or ARNs which are used for testing.

## Testing

### Initiate the data load process
1. Once deployment has completed, look for S3 Bucket Name and DynamoDB table name in the output, for example:
```module.s3_event.aws_s3_bucket.json_bucket: Creation complete after 2s [id=s3-lambda-dynamodb-terraform-json-store]```
```module.dynamodb.aws_dynamodb_table.basic-dynamodb-table: Creation complete after 7s [id=dev-test]```
2. Upload a json file to the S3 bucket. Make sure the json file is contains the key 'UserId'.
3. Check the DynamoDB table and see the item inserted.

## Documentation
- [Amazon S3 Event Notifications](https://docs.aws.amazon.com/AmazonS3/latest/userguide/NotificationHowTo.html)

## Cleanup
 
1. Delete the stack
    ```bash
    terraform destroy --auto-approve
    ```
2. Confirm the removal and wait for the resource deletion to complete.