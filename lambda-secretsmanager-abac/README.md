# Enable Lambda access to Secrets Manager with ABAC

In this pattern, we explore the use of [attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) to enable access to a secret in [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) by an [AWS Lambda](https://aws.amazon.com/lambda/) function. ABAC defines permissions to a resource using attributes, which are defined using tags in AWS. Compared a role-based access control (RBAC) model, ABAC permissions allow for more flexibility with growth and change. ABAC generally requires fewer policies.

The pattern creates an AWS IAM Role that is assumed by the function as its execution role. Attached to that role is a policy that allows access to get the secret using attribute conditions:

``` json
"Condition": {
  "StringEquals": {
    "secretsmanager:ResourceTag/Env": "${aws:PrincipalTag/Env}",
    "secretsmanager:ResourceTag/App": "${aws:PrincipalTag/App}"
  }
}
```

Our example uses two tags: `Env` and `App`. The values of these two tags **must match** for both the secret and the principal. Note that the evaluated **attributes (tags) are attached to the Role**, not the Lambda function.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deploy

1. Clone the project to your local working directory

   ```sh
   git clone https://github.com/aws-samples/serverless-patterns
   ```

1. Change the working directory to this pattern's directory

   ```sh
   cd lambda-secretsmanager-abac
   ```

1. From the command line, use AWS SAM to build the serverless application with its dependencies

    ```
    sam build
    ```

1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:

    ```
    sam deploy --guided
    ```

1. At prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. This contains the Lambda function name for testing

## Testing

Run the following Lambda CLI command to invoke the function. Edit the {GetSecretFunction} placeholder with the ARN of the deployed Lambda function (provided in SAM deploy outputs).

View the secret in the function output which is stored in `response.json`.

``` bash
aws lambda invoke --function-name {GetSecretFunction} --cli-binary-format raw-in-base64-out response.json

cat response.json
```

Next, update the `Env` tag on the function execution role to confirm that the function fails (Access Denied). Edit the {GetSecretFunctionRole} placeholder with the ARN of the function role (provided in SAM deploy outputs).

``` bash
aws iam tag-role --role {GetSecretFunctionRole} --tags Key=App,Value=sample-function Key=Env,Value=prod
```

Invoke the function a second time:

``` bash
aws lambda invoke --function-name {GetSecretFunction} --cli-binary-format raw-in-base64-out response.json

cat response.json
```

We expect the function to fail in this case as the resource and principal tags no longer match per the policy condition. The function will indicate a timeout (`Task timed out after 3 seconds`) in the response.

## Cleanup

Delete the resources created in this pattern:

```sh
sam delete
```

## References

1. [Securely retrieving secrets with AWS Lambda](https://aws.amazon.com/blogs/compute/securely-retrieving-secrets-with-aws-lambda/)
2. [Use AWS Secrets Manager secrets in AWS Lambda functions](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_lambda.html)

----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
