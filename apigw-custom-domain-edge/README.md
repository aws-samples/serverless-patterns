# Amazon API Gateway REST API Edge Custom Domain Name
The SAM template deploys an Amazon API Gateway Edge Custom Domain Name.

The Edge Custom Domain Name is mapped to a Stage in an existing API Gateway. Additionally, a Route53 A record is created to map the Edge Custom Domain Name (i.e. example.com) to the Target Domain Name created by API Gateway (i.e. d-abcde12345.execute-api.ap-southeast-2.amazonaws.com).

As prerequisites for this pattern, you must have:

* A valid certificate in ACM (Amazon Certificate Manager) in the us-east-1 Region that covers the namespace of the domain you would like to use (i.e. *.mydomain.com).
* A public Hosted Zone in Route 53 with the domain name you would like to use (i.e. mydomain.com).
* An API Gateway API (REST, HTTP or Websockets) and a deployed Stage within this API.

Note: when deploying this pattern, *CAPABILITY_IAM* is required.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/apigw-custom-domain-edge](https://serverlessland.com/patterns/apigw-custom-domain-edge)

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
2. Change directory to the pattern directory:
    ```
    cd apigw-custom-domain-edge
    ```
3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy -g
    ```
1. During the prompts:
    * Enter a stack name
    * Select the desired AWS Region
    * Enter your Custom Domain Name (i.e. test.mydomain.com) for the DomainName parameter.
    * You must have a ACM Certificate in the us-east-1 Region that covers your Custom Domain namespace (i.e. *.mydomain.com). Enter the ARN for this certificate.
    * You must have a public Hosted Zone in Route 53 with your Domain Name (i.e. mydomain.com). Enter the Hosted Zone Id for this Hosted Zone.
    * Enter the API Id in API Gateway that you would like to map to your Custom Domain Name.
    * Enter the name of the stage within your API Gateway that you would like to map to your Custom Domain Name.
    * Allow SAM to create roles with the required permissions if needed.

    Once you have run guided mode once, you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## Testing

The stack will output the **Edge Custom Domain endpoint**. You can use *curl* to send a HTTP request to the Edge Custom Domain endpoint to test the correct mapping to your API.
   
```
curl https://{DomainName}
```

## Cleanup
 
1. Delete the stack
    ```bash
    sam delete
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0