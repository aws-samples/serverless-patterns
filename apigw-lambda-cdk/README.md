# Amazon API Gateway REST API with AWS Lambda proxy integration

This pattern in CDK offers a boilerlate to generate an Amazon API Gateway REST API endpoint with a a greedy proxy ("{proxy+}") and "ANY" method from the specified path, meaning it will accept by default any method and any path. The Lambda function provided in TypeScript only returns the path.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-lambda-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory its source code folder:
    ```bash
      cd apigw-lambda-cdk/src
    ```
3. From the command line, use npm to install the development dependencies:
    ```bash
      npm install
    ```
4. To deploy from the command line use the following:
    ```bash
      npm run deploy
    ```
5. _Optional_ If you do not use the default profile in your configuration for aws credentials, you must edit your scripts section in the `src/package.json`, replacing `<YOUR_PROFILE_NAME>` with your named profile:
    ```json
      {
        "scripts": {
          "deploy": "cdk deploy --profile <YOUR_PROFILE_NAME>",
          "destroy": "cdk destroy --profile <YOUR_PROFILE_NAME>"
        }
      }
    ```

## Testing

1. After deployment, the output shows the API Gateway URL with the Lambda integration, for example: ```ServerlessLandApi.ServerlessLandEndpointC36EEEC4 = https://<random-id>.execute-api.us-east-1.amazonaws.com/prod/```.
1. Accessing the URL in a browser, you see: ```Hello, your path is: "/"```.
3. This page logs any path you type after "/". You can use this as a starting point as a general purpose endpoint for various types of applications.

## Cleanup

1. From the command line, use the following in the source folder
    ```bash
    npm run destroy
    ```
2. Confirm the removal and wait for the resource deletion to complete.

----

© Copyright 2022 [Ibrahim Cesar](https://ibrahimcesar.cloud)

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
