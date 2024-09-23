# Private Amazon API Gateway REST API to be invoked from an Amazon instance in a different AWS Region

This pattern creates a Private Amazon API Gateway REST API, along with an Interface VPC Endpoint in an AWS Region. Subsequently, it creates a VPC, an EC2 Instance, a Private Hosted Zone, and a VPC Peering Connection in a second AWS Region. Finally, the VPC Peering connection is created in the first AWS Region. This way, a client in an AWS Region can send requests to the Private API Gateway in a different AWS Region.

Learn more about this pattern at [Serverless Land Patterns](https://serverlessland.com/patterns/apigw-rest-api-lambda-vpc-sqs). edit this

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
    cd private-apigw-cross-region
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.
    * Enter Subnets
    * Enter LambdaSecurityGroupId

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern contains three templates. Template1 deploys a Private Amazon API Gateway REST API with a Test stage, an Amazon VPC with two subnets where an AWS Interface Endpoint is deployed. This will need to forward requests to the Private API Gateway.

Template 2 needs to be deployed in a different AWS Region from the one chosen to deploy the first one. This template will create an Amazon VPC with a subnet where an Amazon EC2 Instance will be deployed. The Amazon EC2 Instance will act as the client. A Private Hosted Zone for the Interface VPC Endpoint created in the first template will be also deployed. This is needed to ensure DNS resolution between the two AWS Regions.

Additionally, a CNAME record is created so that the EC2 Instance can point to it to send requests to the Private API Gateway. Finally, a VPC Peering connection is created between the two Amazon VPCs created, along with its route table.

Finally in the template 3, the route tables for the AWS VPC in the first AWS Region are updated with the newly created Peering connection.

VPC Peering is needed to ensure Networking traffic can flow between the Amazon EC2 Instance in the first AWS Region, and the AWS Interface Endpoint in the second AWS Region.

## Testing

Once the application is deployed, retrieve the RestApiId value from CloudFormation Outputs. You can run curl command from the Amazon EC2 Instance the following way:

Example: curl -v -X GET https://{RestApiId}.execute-api.{AWS Region}.amazonaws.com/Test/test-resouece

## Documentation
- [Working with Private REST API Gateways](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-apis.html)
- [Working with Private Hosted Zones](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-private.html)
- [What is VPC Peering?](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html)
- [VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html)

## Cleanup
 
1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
This pattern was contributed by Luigi Napoleone Capasso
----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
