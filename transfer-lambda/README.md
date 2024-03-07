# AWS Transfer Family SFTP Server to AWS Lambda

This pattern in SAM offers an example to setup an AWS SFTP server using AWS Transfer Family for SFTP with a custom workflow step to an AWS Lambda Function. The template enables you to simply create a server, a custom workflow, set up user accounts, and an Amazon Simple Storage Service (Amazon S3) bucket. You have fine-grained control over user identity, permissions, and keys. You can create users within Transfer for SFTP. You can also use IAM policies to control the level of access granted to each user. When a user uploads a file to the SFTP server it triggers a custom document processing step.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/transfer-lambda. 

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
    cd transfer-lambda
    ```
1. Create SSH Key for you sftp server user in your pattern directory: 
    * [SSH Key Generation](https://docs.aws.amazon.com/transfer/latest/userguide/key-management.html#sshkeygen)

1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Enter desired sftp username
    * Enter the public ssh key from your key_name.pub file into the SshKey parameter.
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy -guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern deploys an Amazon Simple Storage Service (S3) bucket, an SFTP Server using AWS Transfer for SFTP configured with service managed user with fine grained access to the S3 bucket, and an Transfer Family Workflow to an AWS Lambda Function. Once the user uploads a file through the SFTP server, the file will land in the users home directory within the S3 bucket. The AWS Tranfer Family workflow will invoke the lambda function upon successful file upload. The function extracts the information regarding the execution status, and then calls the SendWorkflowStepState API operation to return the status to the workflow for the step. Before your function calls the SendWorkflowStepState API operation, you can configure Lambda to take an action based on your workflow logic.

## Testing

1. Navigate to the AWS Transfer family Console and click on servers
1. Choose the newly created sftp server id, locate the server endpoint, copy it and save it for later use.
1. Use the endpoint to test the sftp server with transferring a file using a client, the rest of this is assuming use of OPENSSH.
    Instructions for other SSH Clients can be found here:
    - [Transferring files over a server endpoint using a client](https://docs.aws.amazon.com/transfer/latest/userguide/transfer-file.html)
1. Create a test file in your pattern directory called hello.txt, inside the file enter some text such as "Hello, World!" and save the file.
1. Open a command terminal from your pattern directory and enter the following command:
    ```bash
    sftp -i transfer-key sftp_user@service_endpoint
    ```
    In the preceding command, sftp_user is the username and transfer-key is the SSH private key. Here, service_endpoint is the server's endpoint as shown in the AWS Transfer Family console for the selected server.
1. To upload a file from your file system to the Transfer Family server, use the put command. For example, to upload hello.txt (assuming that file is in your current directory on your file system), run the following command at the sftp prompt:
    ```bash
    put hello.txt
    ```
1. A message similar to the following appears, indicating that the file transfer is in progress, or complete.
    ```bash
    Uploading hello.txt to /my-bucket/home/sftp_user/hello.txt
    hello.txt 100% 127 0.1KB/s 00:00
    ```
1. Navigate to Cloudwatch Console, click on Log Groups under the Logs drop down.
1. Click on the log group named: /aws/lambda/{stack-name≈}-custom-workflow-step-lambda-function
1. Click on the latest log stream, observe the event sent from the custom workflow to the lambda function and the response from the SendWorkflowStepState API operation.

## Documentation
- [Creating SSH Keys for Service Managed Users](https://docs.aws.amazon.com/transfer/latest/userguide/key-management.html#sshkeygen)
- [Use custom file-processing steps](https://docs.aws.amazon.com/transfer/latest/userguide/custom-step-details.html)
- [Using logical directories to simplify your Transfer Family directory structures](https://docs.aws.amazon.com/transfer/latest/userguide/logical-dir-mappings.html)
- [Transferring files over a server endpoint using a client](https://docs.aws.amazon.com/transfer/latest/userguide/transfer-file.html)
- [Working with service-managed users](https://docs.aws.amazon.com/transfer/latest/userguide/service-managed-users.html)
- [AWS Transfer Family managed workflows](https://docs.aws.amazon.com/transfer/latest/userguide/transfer-workflows.html)

## Cleanup

1. Navigate to Cloudformation Console, Click on stacks and locate the stack was created with this pattern and select it.
1. Navigate to the Resources tab within your stack and copy the S3 Bucket Physical ID and use it in the following command in your terminal to empty the S3 Bucket:
    ```bash
    aws s3 rm s3://sftp-server-192828077733-us-east-1-bucket  --recursive
    ```
1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```

This pattern was contributed by Jack Jones.

----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0