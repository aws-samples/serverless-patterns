# AWS Lambda to AWS Secrets Manager in Private Subnet

This serverless pattern demonstrates the deployment of a AWS Lambda function in private and isolated subnets, along with allowing communication with selected AWS service API endpoints using AWS PrivateLink VPC interface endpoints. Thus, you can operate a Lambda function that doesn't have outbound public internet access but have access to Secrets Manager service endpoint. You can use this pattern as a base example to implement other VPC endpoints if you need to access other AWS services in your private and isolated Lambda function.

This pattern deploys one private VPC, one private and isolated subnet, one security group, one Python Lambda function, one VPC Interface Endpoint for Amazon Secrets Manager and one example secret.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/lambda-vpc-interface-endpoints-secrets-manager](https://serverlessland.com/patterns/lambda-vpc-interface-endpoints-secrets-manager)

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed
* [Docker](https://docs.docker.com/get-docker/) installed and running

## Deployment Instructions

1. If it's your first time with AWS CDK, run `cdk bootstrap` to initiate process called bootstrapping that needed to provision some initial resources the AWS CDK needs to perform the deployments. Check [Bootstrapping documentation](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html) page for details. 
2. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
3. Change directory to the pattern directory:
    ```
    cd serverless-patterns/lambda-vpc-interface-endpoints-secrets-manager
    ```
4. Install dependency packages:
    ```
    npm install
    ```
5. From the command line, use AWS CDK to deploy the AWS resources for the pattern as specified in the CDK project:
    ```
    cdk deploy --all
    ```

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation
## Testing

After deployment, use following AWS CLI command to invoke the Lambda function in the private subnet. The Lambda function will use the VPC Interface Endpoint to interact with Amazon Secrets Manager service. 

```
aws lambda invoke \
--function-name LambdaFunctionPrivate \
--payload '{}' \
--cli-binary-format raw-in-base64-out /dev/stdout
```

To learn more, see [Invoke Lambda CLI docs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/invoke.html)

You should see the output of `ListSecrets` API result returned through the VPC Interface Endpoint to the Lambda function in a private subnet.
## Cleanup
 
1. Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.
    ```
    cdk destroy
    ```
2. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'AwsLambdaPrivSubnetStack')].StackStatus"
    ```
----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
