# API Gateway REST API to AWS Batch

This template creates an API Gateway REST API integration with AWS Batch and can submit jobs to AWS Batch. This pattern addresses some nuances with defining the VTL template mapping when integrating with AWS Batch. It also creates an IAM execution role with permissions to submit AWS Batch job.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-rest-batch.


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
    cd serverless-patterns/apigw-rest-api-batch-sam
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

## Testing

To test the endpoint first send data using the following command. Be sure to update the API Endpoint, Job Definition and the Job Queue from the Cloudformation Stack Output.

```
curl --location --request POST '[YOUR API ENDPOINT]' --header 'Content-Type: application/json' \
--data-raw '{
    "jobName": "[A RANDOM JOB NAME]", 
    "jobQueue": "[JOB QUEUE NAME]", 
    "jobDefinition": "[JOB DEFINITION]" }'
```

You can also run the following commands on a terminal prompt to get the API Endpoint, Job Queue and Job definition.

**API Endpoint**
```
aws cloudformation describe-stacks --stack-name [YOUR STACK NAME] --query "Stacks[0].Outputs[?OutputKey=='ApiEndpoint'].OutputValue" --output text
```

**Job Queue Name**
```
aws cloudformation describe-stacks --stack-name [YOUR STACK NAME] --query "Stacks[0].Outputs[?OutputKey=='JobQueueName'].OutputValue" --output text
```

**Job Definition**
```
aws cloudformation describe-stacks --stack-name [YOUR STACK NAME] --query "Stacks[0].Outputs[?OutputKey=='JobDefinitionName'].OutputValue" --output text
```


## Cleanup
 
1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name [YOUR STACK NAME]
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'[YOUR STACK NAME]')].StackStatus"
    ```
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
