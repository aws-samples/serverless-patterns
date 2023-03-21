# Running Web API on ECS Fargate with custom domain backed with ALB, fronted by Route53, and secured with ACM Certificate

This CDK application demonstrates how to deploy a ASP.NET Framework application on Windows based ECS Cluster.

This pattern uses .NET as a programming language to create the entire CDK stack.

## Architecture 
![architecture diagram](images/architecture.png)

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/ecs-windows-cdk-dotnet

**Important**: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [.NET 6](https://dotnet.microsoft.com/en-us/download/dotnet/7.0) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment Instructions

1. Clone the project to your local working directory.
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```

    ```
2. Change the working directory to this pattern's directory.
    ```
    cd ecs-windows-cdk-dotnet/cdk/src/WindowsECS
    ```
3. Build the application.
    ```
    dotnet build
    ```
4. Return one level back to the path `route53-alb-fargate-cdk-dotnet`
    ```
    cd..
    ```
5. Deploy the stack to your default AWS account and region.
    ```
    cdk deploy
    ```

## Testing

1. After deployment, the output displays the following values.
   - Load Balancer URL: `Route53AlbFargateCdkDotnetStack.sampleapiserviceLoadBalancerDNS60B9DACF = Route-sampl-16MTWZYE6AGI4-1107455325.ap-south-1.elb.amazonaws.com`
   - API Custom Domain URL: `Route53AlbFargateCdkDotnetStack.sampleapiserviceServiceURLC8317C98 = https://api.YOUR-DOMAIN.com`
2. Copy the URL with custom domain and append `WeatherForecast`, the URL will look like this - https://api.YOUR-DOMAIN.com/WeatherForecast.
3. Enter this URL into your browser, you should receive a JSON response with weather information.

## Cleanup

Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.
```
cdk destroy
```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0