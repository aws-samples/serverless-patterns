# API Gateway to Private HTTP Endpoint via VPC Link

The SAM template in this pattern deploys the following resources. It requires a VPC id and private subnet ids as inputs. It is assumed that the VPC and subnets are already configured with the required network routes.
### Deployed resources:
* Requried Security Groups
* ECS Fargate cluster with service and task definitions
* Private Application Load Balancer with appropriate listener and target group
* VPC Link
* API gateway integration between the API endpoint and the private ALB via the VPC Link

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-vpclink-pvt-alb/

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.


## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/apigw-vpclink-pvt-alb
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Enter the VPC Id
    * Enter the comma separated list of private subnet ids
    * Allow SAM CLI to create IAM roles with the required permissions

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern allows integration of public API gateway endpoint to a private Application Load Balancer with an ECS Fargate cluster behind it. It allows to build a secure pattern without exposing the private subnet resources and can be accessed only via a VPC Link.

## Testing

The stack creates and outputs the API endpoint. Open a browser and try out the generated API endpoint. You should see the Nginx home page.
Or, run the below command with the appropriate API endpoint. You should get a 200 response code.

```bash
curl -s -o /dev/null -w "%{http_code}" <API endpoint> ; echo
```

## Cleanup
 
1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
