# Automate the Creation and Deletion of NAT Gateways on a Schedule

As a best practice, AWS customers should deploy resources that don’t require direct internet access, such as EC2 instances, databases, queues, caching, or other infrastructure, into a VPC private subnet.  Those workloads can take advantage of VPC endpoints to call AWS services privately without having to traverse the public internet.  Some workloads require occaisional updates from external sources.  You can use a NAT gateway so that instances in a private subnet can connect to services outside your VPC but external services cannot initiate a connection with those instances.  Since these updates often occur during a scheduled maintenance window,  NAT Gateways aren't necessarily required to be in place all the time, and can be created and deleted only when needed.

This project contains source code and supporting files for a serverless application that allocates an Elastic IP address, creates a NAT Gateway, and adds a route to the NAT Gateway in a VPC route table.  The application also deletes the NAT Gateway and releases the Elastic IP address.  The process to create and delete a NAT Gateway is orchestrated by an AWS Step Functions State Machine, triggered by an EventBridge Scheduler.  The schedule can be defined by parameters during the SAM deployment process.

The application uses several AWS resources, including an EventBridge Scheduler, Lambda functions, a Step Function State Machine, and an SNS topic. These resources are defined in a `template.yaml` file. You can update the template to add AWS resources through the same deployment process that updates your application code.  This ReadMe.md includes deployment instructions.  Note: In order to delete your NAT Gateway, it will need to be in an available state.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

![Diagrams](./docs/CreateNGW.png)![Diagrams](./docs/DeleteNGW.png)

This project includes the following files and folders.

- * **docs** - Directory containing supporting documents
- * **create-ngw** - Directory containing a Lambda function that allocates an Elastic IP and creates a NAT Gateway
- * **create-ngw-route** - Directory containing a Lambda function that creates a route to the NAT Gateway in a VPC route table
- * **delete-ngw** - Directory containing a Lambda function that deletes a NAT Gateway
- * **ngw-state-machine** - Directory containing Amazon State Language files for an AWS Step Functions State Machine
- * **release-eip** - Directory containing a Lambda function that releases an Elastic IP 

## AWS Step Functions State Machines created by this solution
![Diagrams](./docs/CreateNGW-StateMachine.png)![Diagrams](./docs/DeleteNGW-StateMachine.png)

The Serverless Application Model Command Line Interface (SAM CLI) is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.

To use the SAM CLI, you need the following tools.

* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* Node.js - [Install Node.js 10](https://nodejs.org/en/), including the NPM package management tool.
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

To build and deploy your application for the first time, run the following in your shell:

```bash
sam build
sam deploy --guided --capabilities CAPABILITY_NAMED_IAM
```

The first command will build the source of your application. The second command will package and deploy your application to AWS, with a series of prompts:

* **Stack Name**: The name of the stack to deploy to CloudFormation. This should be unique to your account and region, and a good starting point would be something matching your project name (ex. create-and-delete-ngw).
* **AWS Region**: The region to deploy your resources.
* **SNSTopic [email@email.com]**: An email address for your Amazon SNS Topic subscription.  Amazon SNS will send an email notification upon successful NAT Gateway creation and deletion.
* **RouteTableId [rtb-XXXXXXXXXXXXXXXXX]**: A route table ID for an existing route table in your Amazon VPC.  Ensure that your route table does not have any current entries for a 0.0.0.0/0 destination.
* **Parameter SubnetId [subnet-XXXXXXXXXXXXXXXXX]**: An existing public subnet ID to deploy your NAT Gateway into.
* **ScheduleDay [SAT]**: The day of the week to create and delete your NAT Gateway.  Possible values include SUN, MON, TUE, WED, THU, FRI, SAT.
* **StartTime [12]**: The hour of the day in UTC to trigger the creation of your NAT Gateway. Possible values include numbers from 0-23.
* **DeleteTime [12]**: The hour of the day in UTC to trigger the deletion of your NAT Gateway. Possible values include numbers from 0-23.
* **Confirm changes before deploy**: If set to yes, any change sets will be shown to you before execution for manual review. If set to no, the AWS SAM CLI will automatically deploy application changes.
* **Allow SAM CLI IAM role creation**: Many AWS SAM templates, including this example, create AWS IAM roles required for the AWS Lambda function(s) included to access AWS services. By default, these are scoped down to minimum required permissions. To deploy an AWS CloudFormation stack which creates or modified IAM roles, the `CAPABILITY_IAM` value for `capabilities` must be provided. If permission isn't provided through this prompt, to deploy this example you must explicitly pass `--capabilities CAPABILITY_IAM` to the `sam deploy` command.
* **Disable rollback**: By default, if there's an error during a deployment, your AWS CloudFormation stack rolls back to the last stable state. If you specify --disable-rollback and an error occurs during a deployment, then resources that were created or updated before the error occurred aren't rolled back.
* **Save arguments to samconfig.toml**: If set to yes, your choices will be saved to a configuration file inside the project, so that in the future you can just re-run `sam deploy` without parameters to deploy changes to your application.

## Use the SAM CLI to build and test locally

Build your application with the `sam build` command.

```bash
CreateAndDeleteNGW$ sam build
```

The SAM CLI installs dependencies defined in `package.json`, creates a deployment package, and saves it in the `.aws-sam/build` folder.

Run functions locally and invoke them with the `sam local invoke` command.


## How it works

EventBridge Scheduler will invoke the CreateNGW Step Functions State Machine based on a cron expression created by the SAM/CloudFormation input parameters you specified.  A payload is sent to the Step Functions State Machine with the route table ID and subnet ID created by the CloudFormation input parameters you specified.

For the Create NAT Gateway pattern, Step Functions will orchestrate Lambda functions that allocate an Elastic IP address, create a NAT Gateway, and add the appropriate route to the NAT Gateway in the route table specified.  A success message will then be sent to the SNS Topic and the email address subscribed.

A similar workflow will occur for the DeleteNGW Step Functions State Machine.  An EventBridge Scheduler will invoke the DeleteNGW Step Functions State Machine.  A payload is sent to the Step Functions State Machine with the route table ID created by the CloudFormation input parameters you specified.

For the Delete NAT Gateway pattern, Step Functions will orchestrate Lambda functions that delete the NAT Gateway, remove the NAT Gateway route from the route table specified, and release the Elastic IP address.  A success message will then be sent to the SNS Topic and the email address subscribed.

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
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0