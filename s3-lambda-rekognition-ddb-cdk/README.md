# Detect labels in pictures using Amazon S3, AWS Lambda, Amazon Rekognition, and Amazon DynamoDB with Amazon Cloud Development Kit (AWS CDK)

This pattern shows how to detect labels using an event driven architecture.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/

# Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Node and NPM](https://nodejs.org/en/download/) installed
- [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```
   git clone https://github.com/aws-samples/serverless-patterns
   ```
2. Change directory to the pattern directory:
   ```
   cd s3-lambda-rekognition-ddb-cdk
   ```
3. Run below command to install required dependencies:

   ```
   npm install
   ```

4. Run the command below to bootstrap your account. CDK needs it to deploy

   ```
   cdk bootstrap
   ```

5. From the command line, run:
   ```
   cdk deploy --all
   ```

The CDK stack outputs the S3 bucket and DynamoDB table names which you can use for testing.

## Testing

1. Have an image that Rekognition can generate a labekl. For example a lion from [Wikipedia](https://en.wikipedia.org/wiki/Lion).
2. Run the following command to upload the image to an S3 bucket. Replace `<your_image.jpg>` with your image file name.
    Replace `<S3BucketName>` with the name of the S3 bucket from the CDK outputs.

```
   aws s3 cp <your_image.jpg> s3://<3BucketName>
```

For example: `aws s3 cp ./Lion.jpg s3://s3lambdarekognitionstack-imagesbucketd8e2a22e-123456789012`

The Lambda function triggers on the S3 object upload, calls Rekognition to get the image labels, and writes the labels to DynamoDB.

1. Retrieve the Rekognition label output from the DynamoDB table. Replace `<DDBTableName>` with the name of the DynamoDB table from the CDK outputs.

   ```
   aws dynamodb scan --table-name <DDBTableName>
   ```

For example: `aws dynamodb scan --table-name S3LambdaRekognitionStack-rekognitiontable70ADE0DF-1234567890123`

3. You should see the Rekognition label output from DynamoDB displayed.

For example: 

```
{
    "Items": [
        {
            "file_name": {
                "S": "Lion.jpg"
            },
            "labels": {
                "S": "{\"Labels\": [{\"Name\": \"Animal\", \"Confidence\": 99.99979400634766, \"Instances\": [], \"Parents\": [], \"Aliases\": [], \"Categories\": [{\"Name\": \"Animals and Pets\"}]}, {\"Name\": \"Lion\", \"Confidence\": 99.99979400634766, \"Instances\": [{\"BoundingBox\": {\"Width\": 0.650372326374054, \"Height\": 0.6257815361022949, \"Left\": 0.23760296404361725, \"Top\": 0.1613311469554901}, \"Confidence\": 99.9444808959961}], \"Parents\": [{\"Name\": \"Animal\"}, {\"Name\": \"Mammal\"}, {\"Name\": \"Wildlife\"}], \"Aliases\": [], \"Categories\": [{\"Name\": \"Animals and Pets\"}]}, {\"Name\": \"Mammal\", \"Confidence\": 99.99979400634766, \"Instances\": [], \"Parents\": [{\"Name\": \"Animal\"}], \"Aliases\": [], \"Categories\": [{\"Name\": \"Animals and Pets\"}]}, {\"Name\": \"Wildlife\", \"Confidence\": 99.99979400634766, \"Instances\": [], \"Parents\": [{\"Name\": \"Animal\"}], \"Aliases\": [], \"Categories\": [{\"Name\": \"Animals and Pets\"}]}], \"LabelModelVersion\": \"3.0\", \"ResponseMetadata\": {\"RequestId\": \"08092028-bb58-49a7-bd5d-07208646e203\", \"HTTPStatusCode\": 200, \"HTTPHeaders\": {\"x-amzn-requestid\": \"08092028-bb58-49a7-bd5d-07208646e203\", \"content-type\": \"application/x-amz-json-1.1\", \"content-length\": \"812\", \"date\": \"Fri, 04 Aug 2023 17:01:31 GMT\"}, \"RetryAttempts\": 0}}"
            }
        }
    ],
    "Count": 1,
    "ScannedCount": 1,
    "ConsumedCapacity": null
}
```

## Cleanup

1. To delete the stack, run:
   ```bash
   cdk destroy --all
   ```

---

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the AWS Pricing page for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## This project was developed with the assistance of Amazon CodeWhisperer
