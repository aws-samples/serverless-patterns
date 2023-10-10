# AWS Lambda to DynamoDB to Kinesis Data Streams 

<img src="topology.png" alt="topology" width="65%"/>

The SAM template deploys a Lambda function, a DynamoDB table and a Kinesis Data Streams.
This is a Java 11 implementation of this pattern.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Compile and package the java code
    ``` 
    mvn clean package
    ```
1. Create an S3 bucket where the source code will be stored
    ```
    aws s3 mb s3://rtgvhgc8279238sdcd
    ```
1. Copy the source code located in the target folder
    ```
    aws s3 cp target/sourceCode.zip s3://rtgvhgc8279238sdcd
    ```
1. Deploy the CloudFormation stack
    ```
    sam deploy --s3-bucket rtgvhgc8279238sdcd --stack-name kds-pattern --capabilities CAPABILITY_IAM
    ```

## How it works

The Lambda function will put an JSON object into a DynamoDB table.

The DynamoDB Stream will detect the new entry and send it to the Kinesis Data Streams.

## Testing
```
aws lambda invoke --function-name DataProducer --cli-binary-format raw-in-base64-out --payload '{"sensorId": "SEN101","temperature": "57"}' response.json

aws kinesis get-shard-iterator --stream-name kds-data --shard-id shardId-000000000000 --shard-iterator-type LATEST

aws kinesis get-records --shard-iterator SHARD_ITERATOR
```

## Cleanup

```
aws cloudformation delete-stack --stack-name kds-pattern

aws s3 rm s3://rtgvhgc8279238sdcd --recursive

aws s3 rb s3://rtgvhgc8279238sdcd
```
----

## Language:
This is a Maven project which uses Java 11 and AWS SDK.

## Framework

The framework used to deploy the infrastructure is SAM(AWS Serverless Application Model)

## Author bio
Razvan Minciuna  
Software Architect    
https://www.linkedin.com/in/razvanminciuna/ 

