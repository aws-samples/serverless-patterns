# Full-stack application, CloudFront to S3, Lambda to RDS
This sample project demonstrates how to create and deploy a serverless full-stack web application.

The application is made up of 3 parts:
- The frontend developed with Javascript, Bootstrap and HTML. This is deployed as a static website to an AWS S3 bucket and delivered to end users through a CloudFront distribution.
- The backend written in Java. This is deployed as an AWS Lambda function. The lambda function has an alias. The alias is exposed through a lambda function URL to be used by the frontend when making requests to the backend. 
- The database which is actually an AWS RDS Postgres instance.

A Java CDK application was also developed and included in the project. The CDK application will create the infrastructure required. It will also build and to deploy everything to AWS.

Learn more about this pattern at Serverless Land Patterns: [full-stack-application-cloudfront-s3-lambda-rds-java-cdk](https://serverlessland.com/patterns/full-stack-application-cloudfront-s3-lambda-rds-java-cdk).

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed
* [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) installed and configured
* The JDK [Amazon Corretto 17](https://docs.aws.amazon.com/corretto/latest/corretto-17-ug/downloads-list.html) installed and configured
* [Apache Maven]() latest version installed and configured. This is required for the build (both backend and CDK application).
* [Docker](https://www.docker.com/) latest version installed and configured together with [Docker Desktop](https://www.docker.com/products/docker-desktop/). This is required because the CDK will build the backend locally in a docker container before deploying to AWS.

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```
   git clone https://github.com/aws-samples/serverless-patterns
   ```
2. Change directory to the `/infra` folder of the pattern project:
    ```
    cd serverless-patterns/full-stack-application-cloudfront-s3-lambda-rds-java-cdk/infra
    ```
3. Start the Docker daemon (you can do that from the terminal console, or you can run Docker Desktop which will also start the daemon):
    ```
    sudo systemctl start docker
    ```
    The Docker daemon must be running while you execute the next commands otherwise the maven build of the backend will fail.
    You should also create a **virtual file share** for the local `/tmp` directory (see [Synchronized file shares](https://docs.docker.com/desktop/synchronized-file-sharing/)).
    This can be done from Docker Desktop (`Settings>Resources>File sharing`).
4. As an optional step you can synthesize the CloudFormation template from the AWS CDK application:
    ```
    cdk synth
    ```
5. Deploy the stack to your default AWS account and region.
    ```
    cdk deploy
    ```
6. Note the outputs from the CDK deployment process. These will contain the lambda URL (can be used to invoke the lambda directly with curl or Postman) and the CloudFront distribution URL for the frontend (can be used to access the frontend of the application from the browser).

## How it works

After you follow the instructions above you will have the full-stack web application deployed to your AWS account.
Once the CDK deployment is successful 2 URLs will be printed to the terminal console output.
Those are :

- the lambda URL
- the CloudFront distribution URL

At this point you can use the CloudFront distribution URL to access the frontend of the application from any browser.
The application will allow end users to take flashcard tests with questions from different categories available in the RDS database created.
Instructions on how to use the application are displayed when the frontend is loaded in the browser. 

## Testing

Automatic unit tests are run by default in quiet mode (see [Maven Quiet output option](https://maven.apache.org/ref/3.9.9/maven-embedder/cli.html)) during the CDK deployment process.
Those tests cover the backend and the Java CDK application itself.
If any of those tests fail then the entire deployment will fail.
If you want to trigger those tests manually in order to observe the results you can change directory to the corresponding project folder (`\backend` or `\infra`) and execute the command:
```bash
mvn clean test
```
The unit tests for the backend application are using an [H2](https://h2database.com/html/main.html) in memory database running in Postgres mode.
Make sure the Docker daemon is running and that a **virtual file share** for the local `/tmp` directory is created before you execute the maven test commands.

If you want to test the frontend locally with mock data you will need to deploy all the files in the `\frontent` project directory to an HTTP server (perhaps use the docker images for [nginx](https://nginx.org) or [httpd](https://httpd.apache.org/)) or use an extension similar to [Live server](https://github.com/ritwickdey/vscode-live-server).

You can also do some manual integration testing for the backend lambda after it is deployed.
This can be done by sending requests to it through its function URL.
You can use `curl` to do that by modifying the next examples:
```
curl <replace-with-lambda-url>/flashcards?categoryId=1&maxItems=10
```
```
curl <replace-with-lambda-url>/categories
```
When you invoke the lambda using its function URL, the data returned will come from the actual RDS database.
The RDS database is initially populated with some sample data by applying unique change-sets managed through the [Liquibase](https://www.liquibase.com/community) API.
The sample data used to initialize the database is available in a backend resource file (`\backend\src\main\resources\liquibaseChangeLog.xml`).
You can modify the data available to the application by adding new change-sets in this file.
Every change set in the resource file will be applied only once by the Lambda function. 

Finally, you can use the application by accessing the frontend in a browser.
To do that copy the CloudFront distribution URL displayed in the terminal console after a successful CDK deployment and paste it in the address bar of a browser. 

## Cleanup
 
1. Delete the stack:
    ```bash
    cdk destroy
    ```
2. Confirm the stack has been deleted:
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
3. The S3 bucket will be retained and has to be emptied and deleted separately:
    ```bash
    aws s3 rb s3://<replace-with-s3-bucket_name> --force
    ```
----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
