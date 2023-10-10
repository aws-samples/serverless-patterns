# apigw-lambda-ses

Integration of Amazon API Gateway REST API with Amazon Lambda and Amazon SES

The SAM template deploys a API Gateway REST API with Lambda function integration, an SES config set and the IAM permissions required to run the application. Whenever the REST API is invoked, the Lambda function is used to send email through SES. The AWS SAM template deploys the resources and the IAM permissions required to run the application.

- email-lambda - Folder which includes the python lambda to send an email through SES
- template.yaml - A template that defines the application's AWS resources.
- samconfig.toml - A SAM configuration file which can be used to configure different environments if you wish to use the same code to deploy.

Requirements:

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions


1. Clone the github repo
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ``` 
    
2. Change directory to the pattern directory:
    ``` 
    cd apigw-lambda-ses
    ``` 
3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yaml file:
    ``` 
    sam deploy --guided
    ``` 
4. During the prompts:
    
      * **Stack Name**: The name of the stack to deploy to CloudFormation. This should be unique to your account and region, and a good starting point would be something matching your project name.
      * **AWS Region**: The AWS region you want to deploy your app to.
      * **Confirm changes before deploy**: If set to yes, any change sets will be shown to you before execution for manual review. If set to no, the AWS SAM CLI will automatically deploy application changes.
      * **Allow SAM CLI IAM role creation**: Many AWS SAM templates, including this example, create AWS IAM roles required for the AWS Lambda function(s) included to access AWS services. By default, these are scoped down to minimum required permissions. To deploy an AWS CloudFormation stack which creates or modifies IAM roles, the `CAPABILITY_IAM` value for `capabilities` must be provided. If permission isn't provided through this prompt, to deploy this example you must explicitly pass `--capabilities CAPABILITY_IAM` to the `sam deploy` command.
      * **Save arguments to samconfig.toml**: If set to yes, your choices will be saved to a configuration file inside the project, so that in the future you can just re-run `sam deploy` without parameters to deploy changes to your application.

    
    Once you have run sam deploy -guided mode once and saved arguments to a configuration file (samconfig.toml), you can use sam deploy in future to use these defaults.


## Use the SAM CLI to build and test locally

Build your application with the `sam build --use-container` command.

```bash
apigw-lambda-ses$ sam build --use-container
```

The SAM CLI installs dependencies defined in `email-lambda/requirements.txt`, creates a deployment package, and saves it in the `.aws-sam/build` folder.

Run functions locally and invoke them with the `sam local invoke` command.

```bash
apigw-lambda-ses$ sam local invoke
```

## Cleanup


1. Delete the stack 
    ```
    aws cloudformation delete-stack —stack-name STACK_NAME
    ```
2. Confirm the stack has been deleted 
    ```
    aws cloudformation list-stacks —query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```

----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0