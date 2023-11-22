# Integration of Application Load Balancer, Cognito and Lambda

This pattern explains how to deploy a SAM application that includes an Application Load Balancer, Cognito and Lambda to fetch Lambda regional metrics.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/alb-cognito-lambda

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* You will need a VPC (You can use Default VPC) and 2 public subnets. Set Security group for the VPC with HTTPS allowed traffic from your IP or 0.0.0.0/0
* A custom domain name (e.g., awsuser.myinstance.com). You can register domain using AWS Route 53 - https://aws.amazon.com/getting-started/hands-on/get-a-domain/
* A valid SSL certificate (e.g., Amazon Certificate Manager) for the custom domain name. You can use a wildcard certificate for *.awsuser.myinstance.com - https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains-prerequisites.html
* A PrettyTable Lambda Layer for your Lambda function. Download zip file from here - https://github.com/jainam1992/aws-lambda-code-samples/blob/main/prettyTable.zip . Once you have downloaded the Layer .zip file, you can add the layer and upload the .zip file using these steps - https://docs.aws.amazon.com/lambda/latest/dg/invocation-layers.html#invocation-layers-using. Note the ARN of the created layer.

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd alb-cognito-lambda
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided --capabilities CAPABILITY_NAMED_IAM
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.
    * Enter the VPC ID of the default VPC or your custom VPC. Example: `vpc-7caert06`
    * Enter the public subnets ID of your VPC. Example: `subnet-d1d6f0b6,subnet-f34741dd`
    * Enter the desired name for your Application Load Balancer: Example: `patternalb`
    * Enter Certificate ARN of your custom domain. Example: `arn:aws:acm:us-west-2:123456789012:certificate/12345678-8388-4033-ba79-de17d5995895`
    * Enter name of subdomain which you will access after deployment. Subdomain will be related to custom domain you created as PreReq. Example: `alb.awsuser.myinstance.com`
    * Enter R53HostedZoneId. This will be the Hosted Zone ID present in Route 53 console. Example: `Z033456933GAXUUWBYYWZ`
    * Enter ALBHostedZoneId. The host zone ID of the ALB has a specific value that must be set. According to “Elastic Load Balancing endpoints and quotas“, the value for the Tokyo (ap-northeast-1) region is `Z14GRHDCWA56QT`. You can find this information here - https://docs.aws.amazon.com/general/latest/gr/elb.html
    * Enter Name of your Lambda Function. Example: `function-alb-cognito`
    * Enter value of Lambda Layer ARN. You can find ARN in Lambda console. Eg: LambdaLayerARN = `arn:aws:lambda:us-west-2:account_id:layer:PrettyTable:1`

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults. If this command fails, you can run `sam deploy --guided --capabilities CAPABILITY_NAMED_IAM`

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This template deploys a full-stack application where Application Load Balancer will be integrated with AWS Cognito and AWS Lambda service to fetch Lambda functions regional metrics. The authentication will be handled by AWS Cognito and once user is authenticated, the user will be routed to Lambda function to fetch lambda regional metrics.

## Testing

Once the SAM deploymeny is successful, you will get a custom LoadBalancerDNSNAme as output. Eg: alb.awsuser.myinstance.com. Navigate to this domain name and you will see a Cognito authentication page. Click on Sign Up and create a user. Once the Sign Up is successful, you will be directed to a page which will show regional metrics related to Lambda functions present in your account.

## Cleanup
 
1. Delete the SAM template
    ```bash
    sam delete
    ```

2. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
