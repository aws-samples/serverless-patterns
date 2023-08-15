
# CDK Python project for deploying API Gateway integration with Amazon Connect

This CDK project is written in Python and would deploy an API Gateway resource that integrates with Amazon Connect to invoke a StartContactTask. It has a stack to synthesize cloud formation templates and customers will be able to  deploy 
    
    API Gateway Rest API with a POST method acting as a proxy to Amazon Connect,
    Amazon Connect task with Attributes 

Stack 'CdkApigwConnectStartTaskStack' will create:

    API Gateway Rest API with a POST method acting as a proxy to SQS,
    Amazon Connect task with Attributes 

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the AWS Pricing page for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [CDK Installed](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) 

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
```
git clone https://github.com/aws-samples/serverless-patterns/cdk-apigw-connect-start-task.git
```
2. Change directory
```
cd cdk-apigw-connect-start-task
```
3. To manually create a virtualenv on MacOS and Linux:
```
$ python3 -m venv .venv
```
4. After the init process completes and the virtualenv is created, you can use the following to activate virtualenv.
```
$ source .venv/bin/activate
``` 
6. After activating your virtual environment for the first time, install the app's standard dependencies:
```
python -m pip install -r requirements.txt
```
7. Install APIGateway Module
```
python -m pip install aws-cdk.aws-apigateway
```
10. To generate a cloudformation templates (optional)
```
cdk synth
```
11. To deploy AWS resources as a CDK project
```
cdk deploy 
```

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
```
git clone https://github.com/aws-samples/serverless-patterns/cdk-apigw-authorizer-sqs.git
```
2. Change directory
```
cd cdk-apigw-authorizer-sqs
```
3. To manually create a virtualenv on MacOS and Linux:
```
$ python3 -m venv .venv
```
4. After the init process completes and the virtualenv is created, you can use the following to activate virtualenv.
```
$ source .venv/bin/activate
``` 
6. After activating your virtual environment for the first time, install the app's standard dependencies:
```
python -m pip install -r requirements.txt
```
7. Install aws_sqs module
```
python -m pip install aws-cdk.aws-sqs
```
8. Install APIGateway Module
```
python -m pip install aws-cdk.aws-apigateway
```
9. To generate a cloudformation templates (optional)
```
cdk synth
```
10. To deploy AWS resources as a CDK project
```
cdk deploy 
```

## How it works

At the end of the deployment the CDK output will list stack outputs, and an API Gateway URL. In the customer's AWS account, a REST API along with an Amazon Connect integration will be created.

#### NOTE ABOUT THE JSON POST PAYLOAD
This endpoint takes a JSON payload of the following format. 
```
{
   "Attributes": {
      "Name" : "Value"
   },
   "ContactFlowId": "Amazon Connect Flow ID",
   "InstanceId": "Amazon Connect instance ID",
   "ClientToken": "Some Client token ",
   "Name": "Some name for the Agent Task",
   "Description": "Some Description for agent task",
   "References": {
      "ReferenceName" : {
         "Type": "URL | String |",
         "Value": "https://www.google.com | Some text"
      }
   }
}
```
## Testing
Test the api invocation using curl:
```
curl -X POST "https://<apigateway-id>.execute-api.<aws-region>.amazonaws.com/prod/start-task-contact" -H "Content-Type: application/json" --data '{
   "Attributes": {
      "from" : "+18009786758",
      "to":"+12123456789"
   },
   "ContactFlowId": "24aeaf6e-XXXX-XXXX-XXXX-a687aa2d6c6d",
   "InstanceId": "61d1b0fb-XXXX-XXXX-XXXX-65bce6588cc8",
   "ClientToken": "new",
   "Name": "Agent Task",
   "Description": "This is a task for agent",
   "References": {
      "FaxURL" : {
         "Type": "URL",
         "Value": "https://www.google.com"
      }
   }
}'
```
If the execution is successful, you will get  response similar to
```
{"ContactId": "39ab393d-880d-4239-9c4d-c77d72e4d16c"}
```
You will get a new task notification in the Amazon Connect Agent desktop or Contact center panel (CCP)

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