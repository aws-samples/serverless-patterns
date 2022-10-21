# Amazon API Gateway Canary Deployment

This pattern creates an Amazon [API Gateway RESTful API](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-rest-api.html), an AWS [Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html), and then creates an [APIGW Canary Deployment](https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.html) using the AWS Cloud Development Kit (AWS CDK) in Python.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/apigw-canary-deployment-cdk](https://serverlessland.com/patterns/apigw-canary-deployment-cdk).

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS CDK Toolkit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed and configured
* [Python 3.9+](https://www.python.org/downloads/) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd serverless-patterns/apigw-canary-deployment-cdk
    ```
3. Create a virtual environment for Python
    ```
    python3 -m venv .venv
    ```
4. Activate the virtual environment
    ```
    source .venv/bin/activate
    ```
    For a Windows platform, activate the virtualenv like this:
    ```
    .venv\Scripts\activate.bat
    ```
5. Install the Python required dependencies:
    ```
    pip install -r requirements.txt
    ```
6. From the command line, use AWS CDK to deploy the AWS resources for the serverless application as specified in the app.py file:
    ```
    cdk deploy MyServerlessApplicationStack
    ```
7. Note the outputs from the CDK deployment process. These contain the API Gateway ID which is used for testing.
8. Once the serverless application stack is successfully deployed, you will need to [deploy new Lambda code](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-package.html). This can be accomplished by performing the following on the Lambda page in the AWS console:

    1. On the left panel, click functions.
    2. Click on the ```MyServerlessApplicationStac-MyFunction*``` function.
    3. Under the code tab, edit the Hello World code under the EDIT ME comment.
    4. Under the file menu in the code editor, click save.
    5. In the code editor, click the deploy button. This deploys the code to the [$LATEST version](https://docs.aws.amazon.com/lambda/latest/dg/configuration-versions.html).

9. From the command line, use AWS CDK to deploy the AWS resources for the canary deployment as specified in the app.py file:
    ```
    cdk deploy CanaryDeploymentStack
    ```

## How it works

The API Gateway Canary Deployment will route 50% of the traffic to the new function version created using the updated code.

## Testing

From the command line, run the following command to send an HTTP `GET` request to APIs endpoint. Note that you must edit the {MyServerlessApplicationStack.ApigwId} and {Region} placeholder with the ID of the deployed API and Region that it is deployed in. This is provided in the MyServerlessApplicationStack deployment outputs.

```
curl -H "Origin: https://www.example.com" "https://{MyServerlessApplicationStack.ApigwId}.execute-api.{Region}.amazonaws.com/prod"
```

Since the canary deployment is set at 50% traffic, when you run the above command more than once you should see the old version's and new version's output at a rate of about 50/50.

The `-H "Origin: https://www.example.com"` is the third party domain making the request, which you can substitute for other domains.

## Cleanup

1. Delete the Canary Deployment stack
    ```
    cdk destroy CanaryDeploymentStack
    ```
2. Delete the Serverless application stack
   ```
   cdk destroy MyServerlessApplicationStack
   ```
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
