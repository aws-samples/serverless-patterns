# Welcome to a CDK Python project for deploying Queue-Based Leveling pattern!

This pattern also referred to as Queue-Based leveling pattern can be useful when desigining Event driven architectures (EDA). Customers facing performance issues, when processing synchronous and webhook call, during extremely high peak traffic can avoid such situations by adapting this architectural strategy. A SQS queue will acts as a buffer for these synchronous requests and permits you to decouple the sender from the receiver. This pattern offers an easy solution to bridge the gap using AWS services that can easily plugin to customers existing architecture.

![Alt text](images/apigw-arch.png?raw=true "Pattern using API gateway, SQS and Lambda Authorizer")


This CDK project is written in Python, it has 2 stacks and can synthesize 2 cloud formation templates. Customers can deploy either of the stacks based on their API authorization needs:
 
##### Stack 'ApigwSqsAuthStack' will create:
* API Gateway Rest API with a POST method acting as a proxy to SQS,
* A Token Authorizer for the API Gateway ( Lambda ARN of the function implementing the authorization is provided as a input parameter to CF and CDK)
* Amazon SQS queue to store the payload posted

##### Stack 'APigwSqsStack' will create:
* API Gateway Rest API with a POST method acting as a proxy to SQS,
* Amazon SQS queue to store the payload posted


Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [CDK Installed](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) 
* [Create Lambda authorizer from blueprint](https://github.com/awslabs/aws-apigateway-lambda-authorizer-blueprints/blob/master/blueprints/python/api-gateway-authorizer-python.py)

![Alt text](images/lambda-auth-blueprint.png?raw=true "Create lambda function using blueprint")


## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
```
git clone https://github.com/aws-samples/pattern-apigw-auth-sqs.git
```
2. Change directory
```
cd pattern-apigw-auth-sqs
```
3. To generate a cloudformation templates (optional)
* With Token Autorizer
    ```
    cdk synth ApigwSqsAuthStack -o ./cloudformation_templates
    ```
* Without a Token Autorizer
    ```
    cdk synth ApigwSqsStack -o ./cloudformation_templates
    ```
4. To deploy AWS resources as a CDK project
   ##### Paramters needed for CDK 
    * storagequeue=Name of the SQS queue where you want data to be sent
    * awsregion=AWS region where you want the APIGW, SQS and token authoizer to be created.
    * lambdaauthorizerarn=ARN of the lambda which implemented the token authorizer validation logic.

* To deploy infrastructure with a Token Authorizer
```
cdk deploy ApigwSqsAuthStack --parameters storagequeue=<queue-name> --parameters awsregion=<AWS region> --parameters lambdaauthorizerarn=<arn:aws:lambda:<AWS Region>:<AWS Account>:function:<Function name>
```
* To deploy infrastructure without a Token Authorizer
```
cdk deploy ApigwSqsAuthStack --parameters storagequeue=<queue-name> --parameters awsregion=<AWS Region> 
```

## How it works

At the end of the deployment the CDK output will list stack outputs, and an API Gateway URL. In the customer's AWS account, a REST API along with an authorizer and a SQS queue will be created.

![Alt text](images/apigw-aws-console.png?raw=true "AWS Console showing API Gateway creation")
## Testing

Test the api invocation using curl:
```
curl -X POST "https://<apigateway-id>.execute-api.us-east-1.amazonaws.com/prod/sqs" -H "Authorization:testtoken"  -H "Content-Type: application/json" --data '{"status": "ok"}'
```
If the execution is successful, you will get  response similar to
```
{"SendMessageResponse":{"ResponseMetadata":{"RequestId":"2e75dac6-4f87-52ab-8fa4-8615640b84f4"},"SendMessageResult":{"MD5OfMessageAttributes":null,"MD5OfMessageBody":"0d7ac2dec5f281678f65dcf7fe4681ba","MD5OfMessageSystemAttributes":null,"MessageId":"9d72cd66-5aaf-4c0f-8f03-8fc96b7a45e1","SequenceNumber":null}}}
```
You can poll the SQS queue for arrival of the test message.

## Cleanup
 
1. Delete the stack
    ```bash
   cdk destroy STACK-NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    cdk list
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0