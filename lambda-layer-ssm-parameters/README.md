# AWS Lambda Layer and SSM Parameter Store - Configuration values for multiple functions

This AWS SAM application is an example of using a Lambda Layer and the SSM Parameter Store to centrally manage configuration values that can be used by multiple Lambda functions within the same account and region. Multiple AWS Serverless features and integrations are demonstrated in this application, including:

1. [Using Node.js ES modules](https://aws.amazon.com/blogs/compute/using-node-js-es-modules-and-top-level-await-in-aws-lambda/) and the [AWS SDK for JavaScript v3](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/) in AWS Lambda
1. Storing configuration data in the [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html)
1. [Using layers with your Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/invocation-layers.html) to promote code sharing and separation of responsibilities
1. Creating a [Lambda function URL](https://docs.aws.amazon.com/lambda/latest/dg/lambda-urls.html) by using [AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-functionurlconfig.html)
1. [Using nested applications in AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-template-nested-applications.html) to deploy multiple templates

This application deploys a parent stack and three nested stacks:

1. The parent stack references all of the nested stacks.
1. The "Parameters" nested stack creates parameters in the SSM Parameter Store that are used as configuration values.
1. The "Layer" nested stack creates a Lambda Layer that retrieves the configuration values from the SSM Parameter Store.
1. The "Function" nested stack creates a Lambda function that is associated with the Lambda Layer.

Invoking the Lambda function will return all of the configuration values from the SSM Parameter Store that match a ParameterPath value (eg: /Config).

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd lambda-layer-ssm-parameters
    ```
1. From the command line, use AWS SAM to build and deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam build
    sam deploy --guided --capabilities CAPABILITY_IAM CAPABILITY_AUTO_EXPAND
    ```
1. During the prompts:
    * Enter a stack name (eg: config-example).
    * Enter the desired AWS Region.
    * Enter values for the stack parameters or accept the defaults.
    * Allow SAM CLI to create IAM roles with the required permissions.
    * When prompted with "...Function Url may not have authorization defined, Is this okay?", enter Y.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

The SSM Parameter Store is used to store configuration values, each with a specific parameter path or hierachy (eg: /Config/{Parameter-Name}). The Lambda Layer uses the API command "GetParametersByPathCommand" to retrieve all of the configuration values that match the parameter path. The Lambda Layer code runs once during the intial Lambda function invocation and stores the configuration values in an object named "config". The object is stored in the execution environment's memory and is available for subsequent function invocations. The "config" object is refreshed whenever a new cold-start of the Lambda function occurs.

The following is an example of the "config" object in JSON format. The Parameters array contains the configuration, including the Name, Value, and Type. Notice how the path in the Name propery contains "/Config" followed by the parameter name "Parameter1Name" and "Parameter2Name".

```
{
  "$metadata": {
    "httpStatusCode": 200,
    "requestId": "3a721a04-c481-4909-8051-2f7bff78f155",
    "attempts": 1,
    "totalRetryDelay": 0
  },
  "Parameters": [
    {
      "ARN": "arn:aws:ssm:us-east-1:123456789012:parameter/Config/Parameter1Name",
      "DataType": "text",
      "LastModifiedDate": "2022-06-22T19:58:34.021Z",
      "Name": "/Config/Parameter1Name",
      "Type": "String",
      "Value": "Value1",
      "Version": 1
    },
    {
      "ARN": "arn:aws:ssm:us-east-1:123456789012:parameter/Config/Parameter2Name",
      "DataType": "text",
      "LastModifiedDate": "2022-06-22T19:58:34.449Z",
      "Name": "/Config/Parameter2Name",
      "Type": "String",
      "Value": "{\n  \"key1\": \"value1\",\n  \"key2\": \"value2\"\n}",
      "Version": 1
    }
  ]
}
```

## Testing

From a web browser, navigate to the Url of the Lambda function to return all of the configuration values.

Update the parameters in the "parameters/template.yml" if you want to change the configuration values. The value of a parameter can be a simple alpha-numeric string or a JSON string. Then use `sam build` and `sam deploy` to update the stack.

## Documentation

* [Building Lambda Layers in AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/building-layers.html)
* [Using nested applications in AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-template-nested-applications.html)
* [Lambda function URLs](https://docs.aws.amazon.com/lambda/latest/dg/lambda-urls.html)
* [Creating Systems Manager parameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-su-create.html)
* [Working with parameter hierachies](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-hierarchies.html)

## Cleanup
 
1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0