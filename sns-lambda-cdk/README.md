# Amazon SNS to AWS Lambda

This pattern contains a sample AWS CDK stack to create a Lambda Function, a SNS Topic and the IAM permissions required to run the application.
SNS invokes the Lambda function when new messages are available. When messages are sent to the SNS topic, they are delivered as a JSON event payload to the Lambda function.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/sns-lambda-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [Python, pip, virtuenv](https://docs.aws.amazon.com/cdk/latest/guide/work-with-cdk-python.html) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed (Only for test purpose)


## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```sh
    cd sns-lambda-cdk/src
    ```

3. Create and activate the project's virtual environment. This allows the project's dependencies to be installed locally in the project folder, instead of globally. Note that if you have multiple versions of Python installed, where the `python` command references Python 2.x, then you can reference Python 3.x by using the `python3` command. You can check which version of Python is being referenced by running the command `python --version` or `python3 --version`

   ```sh
    python -m venv .venv
    source .venv/bin/activate
   ```

4. Install the project dependencies

   ```sh
   python -m pip install -r requirements.txt
   ```

5. Deploy the stack to your default AWS account and region. 

   ```sh
   cdk deploy
   ```

## How it works

The CDK app deploys the resources and the IAM permissions required to run the application. 

## Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to send a message to the SNS topic and observe the event delivered to the Lambda function:

1. Send the SNS message:

```bash
aws sns publish --topic-arn ENTER_SNS_TOPIC_ARN_FROM_OUTPUT --subject testSubject --message "Hello world - SNS to Lambda"
```

2. Retrieve the logs from the Lambda function:
```bash
sam logs -n ENTER_HANDLER_FUNCTION_NAME_FROM_OUTPUT
```

## Cleanup
 
1. Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.

```sh
cdk destroy
```

2. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```

----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
