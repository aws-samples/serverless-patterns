# Amazon API Gateway with caching enable

This pattern creates an Amazon API Gateway REST API with caching enabled at the API and method levels.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-caching-sam

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
    cd serverless-patterns/apigw-caching-sam
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

Amazon API Gateway has the ability to create and seamlessly utilize caching clusters in front of your API Gateway REST APIs.

## Testing

After deploying, hit the endpoint several times then check for cached responses by viewing the CacheHitCount and CacheMissCount. The following link should take you there. Be sure and update the region to the region you deployed to.
```
https://us-west-2.console.aws.amazon.com/cloudwatch/home?region=us-west-2#metricsV2:graph=~(metrics~(~(~'AWS*2fApiGateway~'Count~'ApiName~'cache~'Stage~'Prod)~(~'.~'CacheMissCount~'.~'.~'.~'.)~(~'.~'CacheHitCount~'.~'.~'.~'.))~period~300~stat~'Sum~region~'us-west-2~start~'-PT5M~end~'P0D~view~'bar~stacked~false);query=~'*7bAWS*2fApiGateway*2cApiName*2cStage*7d
```

## Cleanup
 
Delete the stack
```bash
sam delete --stack-name STACK_NAME
```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
