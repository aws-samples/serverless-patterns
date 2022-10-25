# Secrets Manager Lambda Extension

The AWS SAM template deploys a Lambda function in Python with the Secrets Manager Lambda extension.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```
   git clone https://github.com/aws-samples/serverless-patterns
   ```
2. Change directory to the pattern directory:
   ```
   cd lambda-secrets-manager-extension-python
   ```
3. From the command line, use AWS SAM to build the serverless application with its dependencies
   ```
   sam build
   ```
4. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
   ```
   sam deploy --guided
   ```
5. During the prompts:

   - Enter a stack name
   - Enter the AWS Region us-east-1 (Note: the secrets manager extension layer is supplied for us-east-1 in the template.yaml. You are free to change this by visting this site to obtain a layer for a different region: https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_lambda.html#retrieving-secrets_lambda_ARNs)
   - Allow SAM CLI to create IAM roles with the required permissions.

   Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

6. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

1. On line 3 of app.py we import the requests module which is used to make HTTP GET requests to the Secrets Manager extension endpoint.

2. On lines 5-11 we obtain the secret name, secrets extension http port, and aws session token from environment variables and craft our request.

3. On line 17 we make a request to the endpoint

4. On line 20 we use json.loads to parse our secret from the response and also decode special characters.

5. On line 23 and 29 we print the secret for demonstration purposes and return the secret in our response body for demostration purposes. Please remove this in production!

## Testing

Run the following Lambda CLI invoke command to invoke the function. Edit the {HelloWorldFunction} placeholder with the ARN of the deployed Lambda function. This is provided in the stack outputs.
View the secret in the function logs, edit the {stack-name} which you entered when deploying the stack.

```bash
aws lambda invoke --function-name {GetSecretFunction} --cli-binary-format raw-in-base64-out response.json
sam logs --stack-name {stack-name}
```

## Cleanup

1. Delete the stack, Enter `Y` to confirm deleting the stack and folder.

```bash
sam delete
```

---

Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
