# Response Transformation from XML to JSON in API Gateway

This pattern explains the usage of VTL Templates within Amazon APIGateway to perform JSON to XML transformation.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-lambda-json-xml-vtl-transformation

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
    cd apigw-lambda-json-xml-vtl-transformation
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works
Many a times, we work with customers who are undergoing modernisation journey within their organisation. When modernising an application, they sometimes have to adhere to some contracts with upstream and downstream interfaces.  For example, messaging protocols, data models etc. Today we are going to address a problem where customer is modernising a system which receives and produces xml response to Serverless using Amazon API Gateway and AWS Lambda.  We will be talking more about producing and consuming XML requests in this article.
Since the contracts were in xml, we had a choice of either maintaining the contract by coding the program to handle at Lambda using libraries or Lambda will return a json response and the conversion of json to xml happens at API Gateway level.
To narrow down the purpose of this blog post further, we utilise the VTL template capability of API Gateway to do conversion of Json to XML.
As part of this article, we will be creating an AWS Lambda, and an API Gateway. The API Gateway will return xml transforming the json response from lambda with the help of mapping templates.
Note: API Gateway supports mapping templates only with lambda integration and not lambda proxy integration.

Content involved:
1.	Override status code, content headers.
2.	Loop through elements using for-each.
3.	Use intrinsic functions to parse content.

Tips:
1.	Use ## at the end of each line to show xml in single string without line breaks.


## Testing
Provide steps to trigger the integration and show what should be observed if successful.
We have hardcoded the response in Lambda and created custom format of XML in API Gateway mapping template.

1. Invoke the lambda via the console test option to view the json response of Lambda.
2. Test the APIGateway which invokes Lambda to see the corresponding XML response.

To test the endpoint:

```
curl -X GET '<your api endpoint>' 
```
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
