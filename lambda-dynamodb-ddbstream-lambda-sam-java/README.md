## Description
## Lambda - DynamoDB - Dynamodb Stream - Lambda

This pattern creates two lambda functions, a DynamoDB table and enables DynamoDB Stream using SAM and Java 11.

Important: this application uses various AWS services and there are costs associated with these services after the
Free Tier usage - please see the AWS Pricing page for details. You are responsible for any AWS costs incurred.


## Language:
#### This is a Maven project which uses Java 11 and AWS SDK

## Framework

The framework used to deploy the infrastructure is SAM

## Services used

The AWS services used in this pattern are
#### Lambda - DynamoDB - Dynamodb Stream - Lambda

Topology

<img src="topology.png" alt="topology" width="70%"/>


## Description
The SAM template contains all the information to deploy AWS resources 
and also the permission required by these service to communicate.

You will be able to create and delete the CloudFormation stack using the CLI commands.

The OrderPublisher Lambda function will be invoked with an JSON payload and the function will store the new object
into a DynamoDB table.

The DynamoDB Stream will detect the new item in the DynamoDB table and will invoke the second Lambda function, 
OrderSubscriber which will display the new record in CloudWatch Logs.

This is fully functional example developed in Java 11.


## Deployment commands

````
mvn clean package

# create an S3 bucket where the source code will be stored:
aws s3 mb s3://loasjjdk2o3dujdksk3

# copy the source code located in the target folder:
aws s3 cp target/sourceCode.zip s3://loasjjdk2o3dujdksk3

# SAM will deploy the CloudFormation stack described in the template.yml file:
sam deploy --s3-bucket loasjjdk2o3dujdksk3 --stack-name orders-stack --capabilities CAPABILITY_IAM

````

## Testing

Invoke the OrderPublisher lambda function
```
aws lambda invoke --function-name OrderPublisher --cli-binary-format raw-in-base64-out --payload '{"cliendId":"123456789","productId":"abc-def-ghi"}' response.json
```

Open CloudWatch Logs - Log groups of the OrderSubscriber Lambda and the result should look like this

```
{cliendId={S: 123456789,}, productId={S: abc-def-ghi,}, orderId={S: 592709fa-f85d-4f9c-bf97-21f0314b0d75,}}
```

## Cleanup

Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.
```
aws cloudformation delete-stack --stack-name orders-stack

aws s3 rm s3://loasjjdk2o3dujdksk3 --recursive

aws s3 rb s3://loasjjdk2o3dujdksk3
```

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed



## Author bio
Name: Razvan Minciuna
LinkedIn: https://www.linkedin.com/in/razvanminciuna/
Description: Software Architect