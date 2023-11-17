# Amazon VPC Lattice with AWS Lambda as weighted targets

This pattern demonstrates how to create a VPC Lattice which shifts traffic to different targets based on the weighted routing policy.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured.
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed.

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd vpc-lattice-lambda
    ```
3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam build

    sam deploy --guided
    ```
4. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

5. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

VPC Lattice is to designed to help you easily and effectively discover, secure, connect, and monitor all of the services within it. Each component within VPC Lattice communicates unidirectionally or bi-directionally within the service network based on its association with the service network and its access settings. Access settings are comprised of authentication and authorization policies required for this communication. 

This pattern creates below resources:

1. A new VPC with CIDR of 10.0.0.0/16
2. A private subnet
3. Security Group allowing inbound traffic from VPC CIDR 10.0.0.0/16
4. VPC Lattice service
5. VPC Lattice Listner
6. VPC Lattice Service Network
7. VPC Lattice Network Association and Service Association
8. Two Lambda functions (Primary and Secondary) to demonstrate traffic shift.
9. One Lambda function (Demo) to verify traffic shift by calling VPC lattice service DNS.

This pattern uses Lambda as weighted targets. VPC Lattice service shifts traffic based on the percentage of weight configured for target groups under VPC Lattice listener. User may update the weight for the targets according to their use case and requirements.  

## Testing

Invoke Demo Lambda function using CLI/Console and observe traffice shift from VPC Lattice service.

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
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
