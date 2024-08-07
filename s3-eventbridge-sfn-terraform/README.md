# Amazon S3 to AWS Step Functions with Amazon EventBridge Rule

This pattern demonstrates invoking a Step Functions state machine from an S3 event via EventBridge. Implemented with Terraform.

Learn more about this pattern at Serverless Land Patterns: [erverlessland.com/patterns/s3-eventbridge-sfn-terraform](https://serverlessland.com/patterns/s3-eventbridge-sfn-terraform)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.


## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli?in=terraform/aws-get-started) installed


## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd s3-eventbridge-sfn-terraform
    ```
1. From the command line, initialize terraform to  to downloads and installs the providers defined in the configuration:
    ```
    terraform init
    ```
1. From the command line, apply the configuration in the main.tf file:
    ```
    terraform apply
    ```
1. During the prompts:
    * Enter yes
1. Note the outputs from the deployment process. These contain the resource names and/or ARNs which are used for testing.


## How it works

- Upload a file to the newly created S3 bucket
- This sends an `Object Created` event to EventBridge
- Based on the EventBridge rule, the state machine is executed


## Testing

1. Navigate to Amazon S3 console, then choose the S3 bucket created by this Terraform template.

2. Upload a file to the S3 bucket

3. Immediately after the upload completes successfully, navigate to the Step Functions console. Select the state machine created by the template, and observe the state machine execution.


## Documentation and next step

To create a full Step Functions workflow with this pattern, search the example workflows available at [serverlessland.com/workflows](https://serverlessland.com/workflows)


## Cleanup
 
1. Change directory to the pattern directory:
    ```
    cd s3-eventbridge-sfn-terraform
    ```
1. Delete all files from the S3 bucket
1. Delete all created resources by terraform
    ```bash
    terraform destroy
    ```
1. During the prompts:
    * Enter yes
1. Confirm all created resources has been deleted
    ```bash
    terraform show
    ```

----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
