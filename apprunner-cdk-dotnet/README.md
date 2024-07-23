# AWS AppRunner: Deploying Web APIs with CDK

The CDK stack that creates an AWS App Runner service to deploy a .NET web API application.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apprunner-cdk-dotnet

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [.NET 6](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed
* [Docker](https://docs.docker.com/engine/install/) installed

## Deployment Instructions for Windows

1. Clone the project to your local working directory
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change the working directory to this pattern's directory
    ```
    cd apprunner-cdk-dotnet\src\DemoApplication.API
    ```
3. Build the application
    ```
    dotnet build
    ```
4. Return to root level folder back to the path `apprunner-cdk-dotnet`
    ```
    cd ..\..
    ```
5. Deploy the stack to your default AWS account and region.
    ```
    cdk deploy
    ```

## Testing

1. After deployment, the output shows the App Runner Service URL, for example: `ApprunnerCdkDotnetStack.AppRunnerServiceURL = https://<unique-id>.<region>.awsapprunner.com`
2. Copy this URL and append `WeatherForecast`, the URL will look like this: `https://<unique-id>.<region>.awsapprunner.com/weatherforecast`
3. Enter this URL into your browser, you should receive a JSON response with weather information.

```
[{"date":"2024-01-09T10:21:16.4618292+00:00","temperatureC":30,"temperatureF":85,"summary":"Chilly"},{"date":"2024-01-10T10:21:16.4618407+00:00","temperatureC":13,"temperatureF":55,"summary":"Mild"}]
```

## Cleanup
Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.
```
cdk destroy
```

----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0