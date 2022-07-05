# AWS AppConfig integration with Lambda extensions

The AppConfig extension takes care of calling the AWS AppConfig service, managing a local cache of retrieved data, tracking the configuration tokens needed for the next service calls, and periodically checking for configuration updates in the background

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/appconfig-lambda-rust

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [Rust](https://www.rust-lang.org/) 1.56.0 or higher
* [cargo-zigbuild](https://github.com/messense/cargo-zigbuild) and [Zig](https://ziglang.org/) for cross-compilation
* [AWS AppConfig integration with Lambda extensions](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration-lambda-extensions.html)

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd appconfig-lambda-rust
    ```
3. Install dependencies and build:
    ```
    make build
    ```
4. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    make deploy
    ```
5. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy -guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

6. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

The AppConfig extension takes care of calling the AWS AppConfig service, managing a local cache of retrieved data, tracking the configuration tokens needed for the next service calls, and periodically checking for configuration updates in the background.

By default, you have 1000 TPS. After the first request, the profile is cached, so from now on, you hit the internal cache of AppConfig.
We can use the Lambda Execution Context to avoid calling the AWS AppConfig cached service having the following benefits
* reducing the call to AppConfig cache
* speeding up the Lambda execution
* saving money


## Testing

EXECUTION 1 - COLD START

```
START RequestId: cd5ccc81-6ff5-4fa2-8a38-e708e833cde9 Version: $LATEST
[appconfig agent] 2022/06/25 07:20:28 INFO AppConfig Lambda Extension 2.0.58
[appconfig agent] 2022/06/25 07:20:28 INFO serving on localhost:2772
EXTENSION Name: AppConfigAgent State: Ready Events: [INVOKE,SHUTDOWN]
ADDED INTO HASHMAP"MyTestProfile"
END RequestId: 04e5bb42-f791-4358-a7f9-0872d4424278
REPORT RequestId: 04e5bb42-f791-4358-a7f9-0872d4424278 Duration: 198.79 ms Billed Duration: 332 ms Memory Size: 256 MB Max Memory Used: 38 MB Init Duration: 132.79 ms
```

EXECUTION 1 - WARM STATE

```
START RequestId: d1f74efe-6ce2-4879-9374-b68535fb8e95 Version: $LATEST
CONFIG FROM HASHMAPMyConfig { id: 1, name: "ExampleApplication", rank: 7 }
END RequestId: d1f74efe-6ce2-4879-9374-b68535fb8e95
REPORT RequestId: 215b2f4c-2539-4c50-825d-1774bc00338c Duration: 1.56 ms Billed Duration: 2 ms Memory Size: 256 MB Max Memory Used: 38 MB
```

## Cleanup
 
1. Delete the stack
    ```bash
    make delete
    ```
2. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
