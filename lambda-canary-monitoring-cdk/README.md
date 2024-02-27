# Canary Deployments with Lambda and CodeDeploy with Monitoring

This pattern demonstrates how to deploy a Lambda Function with CodeDeploy canary deployments through CDK. It also creates a CloudWatch Dashboard through CodeDeploys BeforeAllowTraffic Hook to monitor the traffic-shift during a canary deployment.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS CDK Toolkit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed and configured
* [Node 18+](https://nodejs.org/en/download/current) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd lambda-canary-monitoring-cdk/cdk
    ```
1. From the command line, install the required dependencies:
    ```
    npm install
    ```
1. From the command line, use AWS CDK to deploy the AWS resources for the pattern as specified in the cdk/bin/cdk.ts file:
    ```
    cdk deploy --all
    ```
1. During the prompts:
    * You have to confirm IAM related changes with y during deployment.

## How it works

After you have finished the initial deployment of the CDK application, you can increase the version Number in `cdk/bin/cdk.ts` for your next deployment. This is just a mechanism to make it easier for you to distinguish between the two versions when calling the API, or looking at the logs. However it is not necessary, since a new version will be created whenever you make changes to your Function Code.

When you do your first deployment you can go to your AWS Console, to monitor the Deployment in CodeDeploy and on the CloudWatch Dashboard.
It is recommended to run a small load test during the deployment against this Lambda function, to see the traffic gradually shift over in the CloudWatch Dashboard.

You can adjust the Deployment Strategy in `cdk/lib/lambda-canary-stack.ts`, by changing `deploymentConfig` of the `LambdaDeploymentGroup`

```
    const deploymentGroup = new codedeploy.LambdaDeploymentGroup(this,
      'LambdaCanaryMonitoringDeploymentGroup',
      {
        application: application,
        alias: aliasBusinessLambda,
        deploymentConfig: codedeploy.LambdaDeploymentConfig.CANARY_10PERCENT_5MINUTES,
        preHook: dashboardLambda,
      }
    );
```

## Testing

After the initial deployment you will get an HTTPS Endpoint from the Function URL of the Lambda function. You can send simple GET requests to this endpoint to get a response with the configured Version number of the Lambda Function.

## Cleanup
 
1. From the command line run this AWS CDK command to delete the Serverless application stack

```node
   cdk destroy
```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0