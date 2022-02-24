# Load data from CSV files in S3 into DynamoDB using S3 Event Notification and Lambda

This pattern in CDK offers a complete solution to load data from CSV files stored on S3. The following resources are created:
1. S3 Bucket with event notification on object creates
2. DynamoDB Table with on-demand billing mode
3. Lambda function that runs python and env variables of bucket name, object key, and dynamodb table

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory its source code folder:
    ```bash
      cd s3-lambda-dyanmodb-cdk/cdk
    ```
3. From the command line, use npm to install the development dependencies:
    ```bash
      npm install
    ```
4. To deploy from the command line use the following:
    ```bash
      cdk deploy --parameters dataObject=products
    ```

## Testing

### Initiate the data load process
1. After deployment, in the output look for Bucket Name as below, for example:
```S3LambdaDynamodbCdkStack.BucketName = s3lambdadynamodbcdkstack-s3lambdaddbcdk<ramdom>```
2. Upload a csv file named 'products.csv'. Make sure the first column name in the file is 'id'.
3. Check the DynamoDB table 'products' and see the items inserted. Note: Depending on the size of the file, the time to load may vary. 2MB file takes approximately 4 mins to load.

## Documentation
- [Amazon S3 Event Notifications](https://docs.aws.amazon.com/AmazonS3/latest/userguide/NotificationHowTo.html)
- [Blog: Creating a scalable serverless import process for Amazon DynamoDB](https://aws.amazon.com/blogs/compute/creating-a-scalable-serverless-import-process-for-amazon-dynamodb/)

## Cleanup
 
1. From the command line, use the following in the source folder
    ```bash
    cdk destroy
    ```
2. Confirm the removal and wait for the resource deletion to complete.

