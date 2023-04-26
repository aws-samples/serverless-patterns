# Amazon EventBridge Scheduler to run Amazon Elastic Container Service Task

This pattern will create an Amazon [EventBridge Scheduler](https://docs.aws.amazon.com/scheduler/latest/UserGuide/getting-started.html) to run a task in Amazon [Elastic Container Service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/getting-started.html) cluster every 15 minutes. The pattern is deployed using the AWS Cloud Development Kit (AWS CDK) for Go. 

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/eventbridge-schedule-ecs-publish-cdk-go](https://serverlessland.com/patterns/eventbridge-schedule-ecs-cdk-go)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one
  and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS
  resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS CDK Toolkit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed and configured
* [Go](https://go.dev/dl/) (`1.18` or above) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd eventbridge-schedule-ecs-cdk-go
    ```
3. From the command line, bootstrap the CDK if you haven't already done so. 
    ```
    cdk bootstrap 
    ```
4. Deploy the CDK stack to your default AWS account and region.
    ```
    cdk deploy
    ```

## How it works

An Amazon EventBridge Schedule is created that run a task in an Amazon ECS cluster every 15 minutes. Along with a schedule, the CDK stack creates VPC, ECS Cluster, Fargate Task Definition, Container Definition, an IAM role and policy for EventBridge scheduler to assume and run task in ECS cluster.  

## Testing

A new task is running every 15 minutes in the ECS cluster showing in ECS console.

## Cleanup
 
1. Stop all running tasks in ECS Cluster
    
2. Delete the stack
    ```bash
    cdk destroy
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
