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

## Template 1: VPC with Private API Gateway

This template is deployed in an AWS Region you choose

### Resources:

1. **VPC (myVPC)**
   - CIDR block: Parameterized, default 10.0.0.0/16
   - DNS support and hostnames enabled

2. **Subnets (subnetA and subnetB)**
   - Two subnets in different Availability Zones
   - CIDR blocks calculated from VPC CIDR

3. **Route Table (myRouteTable)**
   - Associated with both subnets

4. **Security Group (mySecurityGroup)**
   - Allows inbound HTTPS traffic (port 443)

5. **VPC Endpoint (ExecuteApiInterfaceEndpoint)**
   - For API Gateway
   - Interface type
   - Associated with both subnets and the security group

6. **API Gateway (MyApi)**
   - Private endpoint configuration
   - Simple GET method on /test-resource path
   - Access restricted to requests from the VPC Endpoint

7. **SSM Parameters**
   - Stores Route Table ID
   - Stores API Gateway URL

### Outputs:
- VPC CIDR
- VPC ID
- API Gateway ID
- VPC Endpoint URL
- Region

## Template 2: VPC Peering and EC2 Instance

This template needs to be deployed in an AWS Region you choose, but different from the one chosen in the first template

### Resources:

1. **VPC (myVPC)**
   - CIDR block: Parameterized, default 192.168.0.0/16
   - DNS support and hostnames enabled

2. **Internet Gateway (myInternetGateway)**
   - Attached to the VPC

3. **Subnet (subnet)**
   - Single subnet in one Availability Zone

4. **Route Table (myRouteTable)**
   - Associated with the subnet
   - Route to Internet Gateway for internet access

5. **Security Group (mySecurityGroup)**
   - Allows inbound SSH (port 22)
   - Allows outbound HTTPS to the peered VPC

6. **VPC Peering Connection (VPCPeeringConnection)**
   - Connects this VPC to the VPC from Template 1

7. **Route53 Private Hosted Zone (DNS)**
   - For execute-api.{region}.amazonaws.com

8. **Route53 Record Set (myDNSRecord)**
   - CNAME record for the API Gateway

9. **EC2 Instance (myInstance)**
   - Amazon Linux 2 AMI
   - t2.micro instance type
   - Placed in the subnet with a public IP

### Outputs:
- VPC Peering Connection ID
- VPC CIDR

## Template 3: Peering Route Configuration

This template needs to be deployed in the same AWS Region as tbe first template

### Resources:

1. **Route (myRoutePeering)**
   - Adds a route to the Route Table from Template 1
   - Destination is the CIDR of the VPC from Template 2
   - Target is the VPC Peering Connection

### Outputs:
- API Gateway URL (retrieved from SSM Parameter Store)

## Overall Architecture

1. Two VPCs are created, one in each of the first two templates.
2. These VPCs are connected via a VPC Peering Connection.
3. The first VPC hosts a private API Gateway, accessible via a VPC Endpoint.
4. The second VPC contains an EC2 instance that can access the API Gateway through the peering connection.
5. DNS resolution is set up to allow the EC2 instance to resolve the API Gateway's domain name to the VPC Endpoint's private IP.
6. The third template adds the necessary route to the first VPC's route table to enable communication over the peering connection.

This setup allows for secure, private communication between resources in the two VPCs, with the API Gateway acting as a controlled access point for services in the first VPC.

## Testing

Once the application is deployed, retrieve the ApiURL value from the third CloudFormation template's Outputs section. You can run curl command from the Amazon EC2 Instance the following way:

Example: curl -v -X GET https://{RestApiId}.execute-api.{AWS Region}.amazonaws.com/Test/test-resource

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
