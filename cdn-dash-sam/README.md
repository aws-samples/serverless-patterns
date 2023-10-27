# Create Cloudwatch custom metrics for API Gateway custom domain names using SAM

This pattern deploys Amazon Eventbridge rule and a AWS Lambda function that creates custom metrics in Amazon CloudWatch for the API mappings of the custom domain names that are present in the region.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-custom-metrics

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
    cd cdn-dash-sam
    ```
3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
4. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.



## How it works

1. This pattern creates a Lambda function that scans the custom domain names and its API mappings in the region.
2. The Lambda function then proceeds to fetch domain details from the access logs, if enabled on the APIs. In case the access logs are not enabled, the function creates the access logs for the APIs that are mapped to the custom domain name.
3. Finally, the function proceeds to create custom metrics namespace in CloudWatch metrics for 200. 4xx and 5xx errors for each API mapping. The metric data points get populated for the requests that comes in to the APIs/CDN post creation of the custom namespace.

## Testing

1. Once the setup/stack is deployed, users have to manually trigger the Lambda function that gets created in order create the custom namespace. 
2. Auto-trigger of Lambda function is not added by design to avoid unintended executions/pricing, as the number of API mappings and CDNs vary across users' accounts. Lambda also enables access logs on all API mappings of the custom domain names.
3. The eventbridge rule then monitors for changes in the custom domain name configurations based on which the Lambda function will be triggered to add additional metrics to the custom namespace accordingly.

## Cleanup
 
 ```
 sam delete
 ```
 
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
