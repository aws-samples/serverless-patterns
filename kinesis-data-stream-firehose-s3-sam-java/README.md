# AWS Kinesis Data Streams to Kinesis Data Firehose to S3

<img src="topology.png" alt="topology" width="65%"/>

The SAM template deploys a Kinesis Data Streams, a Kinesis Data Firehose and an S3 bucket.   
This is a Java project.

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
    aws s3 mb s3://kihqjasc8929821aosada
    ```
1. Copy the source code located in the target folder
    ```
    aws s3 cp target/sourceCode.zip s3://kihqjasc8929821aosada
    ```
1. Deploy the CloudFormation stack
    ```
    sam deploy --s3-bucket kihqjasc8929821aosada --stack-name kinesis-pattern --capabilities CAPABILITY_IAM
    ```

## How it works

The records that are captured by the Kinesis Data Streams are ingested by Kinesis Data Firehose which be stored as objects into an S3 bucket. 

## Testing

Put a new record into the Kinesis Data Streams
```
aws kinesis put-record \
    --stream-name kds-data \
    --data sampledatarecord \
    --partition-key samplepartitionkey
```

List the S3 object
```
aws s3 ls s3://deliverybucket-8938249287387 --recursive --human-readable --summarize
```

## Cleanup

```
aws cloudformation delete-stack --stack-name kds-pattern

aws s3 rm s3://rtgvhgc8279238sdcd --recursive

aws s3 rb s3://rtgvhgc8279238sdcd
```
----

## Language:
This is a Java 11 Maven project.

## Framework

The framework used to deploy the infrastructure is SAM(AWS Serverless Application Model)

## Author bio
Razvan Minciuna  
Software Architect    
https://www.linkedin.com/in/razvanminciuna/
