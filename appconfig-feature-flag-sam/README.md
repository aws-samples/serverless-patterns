# AWS AppConfig Feature Flag with SAM

This pattern creates

- AWS AppConfig Feature Flag configuration
- AWS Lambda that reads the feature flags from AWS AppConfig
- Amazon API Gateway HTTP API that triggers the AWS Lambda

The feature flag configuration in this example contains two flags:

- a simple boolean flag ON/OFF
- a flag that can be ON/OFF but, when it is ON, it has a numeric value

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:

    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```

1. Change directory to the pattern directory:

    ```
    cd appconfig-feature-flag-sam
    ```

1. From the command line, use AWS SAM to build and deploy the AWS resources for the pattern as specified in the template.yml file:

    ```
    sam build
    sam deploy --guided
    ```

1. During the prompts:
    - Enter a stack name: eg. appconfig-feature-flag-sam
    - Enter the desired AWS Region: eg. us-east-1
    - Enter the Application Name to identify the application in AWS AppConfig: appconfig-feature-flag-sam
    - Enter the Environment Name: eg. dev
    - Enter the name of the Feature Flag configuration: TestConfig
    - Enter the AWS AppConfig Lambda extension arn for your Region from https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration-lambda-extensions-versions.html#appconfig-integration-lambda-extensions-enabling-x86-64
    - Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy -guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern deploys an Amazon API Gateway HTTP API that, throuogh the `config` endpoint, triggers the AWS Lambda. The function retrieves the feature flags fron AWS AppConfig.

The AWS Lambda is configured to have access to the application's configuration for a specific environment.

### Testing

Once the application is deployed, retrieve the HttpApiUrl value from CloudFormation Outputs. Either browse to the endpoint in a web browser or call the endpoint from Postman. Remeber to append the path of the endpoint that retrieves the configuration (`config`)

Example GET Request: <https://{HttpApiId}.execute-api.eu-west-1.amazonaws.com/config>

Response:
```

{
  "Pagination":{
    "Enabled":true,"PageSize":5
    },
  "WizardSwitch":{
    "Enabled":true
    }
}

```

## Documentation

- [AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html)
- [AWS AppConfig Feature Flag](https://aws.amazon.com/it/blogs/mt/using-aws-appconfig-feature-flags/)
- [AWS AppConfig integration with Lambda extensions](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration-lambda-extensions.html)
- [Learn to Use AWS AppConfig Feature Flags](https://catalog.us-east-1.prod.workshops.aws/workshops/2ee2fc71-0618-479c-86dd-1d5fb168eb20/en-US/getting-started)

## Cleanup

1. Delete the stack

    ```bash
    sam delete 
    ```

This pattern was contributed by Greg Davis.

----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
