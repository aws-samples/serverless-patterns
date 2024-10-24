# Private Amazon API Gateway REST API invoked by AWS Lambda function in a different AWS Region

This pattern creates a Private Amazon API Gateway REST API, along with an Interface VPC Endpoint in an AWS Region. Subsequently, it creates a VPC, an AWS Lambda function, a Private Hosted Zone, and a VPC Peering Connection in a second AWS Region. Finally, the VPC Peering connection is created in the first AWS Region. This way, a client in an AWS Region can send requests to the Private API Gateway in a different AWS Region.

Learn more about this pattern at [Serverless Land Patterns](https://serverlessland.com/patterns/apigw-rest-api-lambda-vpc-sqs). edit this

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

Follow these steps to deploy the three templates in the correct order:

### Template 1: VPC with Private API Gateway (Region A)

1. Navigate to the directory containing Template 1:

```
cd aws-samples/serverless-patterns/private-apigw-cross-region/
```

2. Deploy Template 1 using AWS SAM:

```
sam deploy --guided --template template1-regionA.yaml
```

3. During the prompts:
* Enter a stack name for Template 1 (e.g., private-api-vpc-regionA)
* Select Region A as the deployment region
* Enter the desired VPC CIDR block
* Allow SAM CLI to create IAM roles with the required permissions
* When prompted to save the configuration, choose a unique name for this template's configuration file

4. Note the outputs from the deployment, including:
* Remote VPC CIDR
* Peer VPC ID
* API Gateway ID
* VPC Endpoint URL
* Region

### Template 2: VPC with Peering Connection and Lambda Function (Region B)

1. Navigate to the directory containing Template 2:

```
cd aws-samples/serverless-patterns/private-apigw-cross-region/
```

2. Deploy Template 2 using AWS SAM:

```
sam deploy --guided --template template2-regionB.yaml --region <region 2 name>
```

3. During the prompts:
* Enter a stack name for Template 2 (e.g., client-vpc-lambda-regionB)
* Select Region B as the deployment region (different from Region A)
* Enter the VPC CIDR block (must be different from Template 1)
* Enter the API ID from Template 1's output
* Enter the Peer VPC ID from Template 1's output
* Enter the Remote VPC CIDR from Template 1's output
* Enter the VPC Endpoint URL from Template 1's output
* Enter Region A as the Peer Region
* Allow SAM CLI to create IAM roles with the required permissions
* When prompted to save the configuration, choose a unique name for this template's configuration file

4. Note the outputs from the deployment, including:
* Peering Connection ID
* VPC CIDR

### Template 3: VPC Peering Route (Region A)

1. Navigate to the directory containing Template 3:

```
cd aws-samples/serverless-patterns/private-apigw-cross-region/
```

2. Deploy Template 3 using AWS SAM:

```
sam deploy --guided --template template3-regionA.yaml
```

3. During the prompts:
* Enter a stack name for Template 3 (e.g., vpc-peering-route-regionA)
* Select Region A as the deployment region (same as Template 1)
* Enter the Peering Connection ID from Template 2's output
* Enter the Remote VPC CIDR from Template 2's output
* Allow SAM CLI to create IAM roles with the required permissions
* When prompted to save the configuration, choose a unique name for this template's configuration file

After deploying all three templates, your multi-region VPC peering with private API Gateway setup should be complete and ready for testing.

## How it works

This solution enables an AWS Lambda function in one AWS region to securely invoke a private Amazon API Gateway in another region using VPC peering and VPC endpoints. Here's an overview of the setup:

### (Client Region)

- A VPC is created to host the client AWS Lambda function.
- A Lambda function is deployed within this VPC, acting as the client.
- A Private Hosted Zone is set up for DNS resolution of the API Gateway endpoint.

### (API Region)

- A second VPC is created to host the Private API Gateway.
- A Private API Gateway is deployed and a VPC Endpoint for API Gateway Service (Execute API) is created in this VPC.

### VPC Peering

- A VPC peering connection is established between the VPCs in Region A and Region B.
- Appropriate routes are added to the route tables in both VPCs to enable traffic flow through the peering connection.

### DNS Resolution

- The Private Hosted Zone in Region A is configured to resolve the API Gateway's domain name to the VPC Endpoint in Region B.

### Invocation Process

1. The Lambda function in Region A initiates a request to the API Gateway's endpoint URL.
2. DNS resolution occurs using the Private Hosted Zone, resolving to the VPC Endpoint in Region B.
3. The request travels through the VPC peering connection to reach the VPC Endpoint in Region B.
4. The VPC Endpoint forwards the request to the private API Gateway.

This setup ensures that all traffic between the AWS  Lambda function and the Amazon API Gateway remains within the AWS network, never traversing the public internet. It provides a secure way to access private resources across regions while maintaining network isolation.

# Multi-Region VPC Peering with Private API Gateway Setup

This document outlines the process of setting up a multi-region VPC peering connection with a private API Gateway using three CloudFormation templates.

## Deployment Order and Regions

1. **Template 1**: Deployed in Region A
2. **Template 2**: Deployed in Region B (different from Region A)
3. **Template 3**: Deployed in Region A (same as Template 1)

## Important Notes

- The VPC CIDR block in Template 2 must be different from the one chosen in Template 1.
- Templates 1 and 3 are deployed in the same AWS Region.
- Template 2 is deployed in a different AWS Region from Templates 1 and 3.
- The Lambda function created in Template 2 acts as a client, sending requests to the Amazon API Gateway created in Template 1.

## Template 1: VPC with Private API Gateway

This template creates an Amazon VPC with an Amazon Private API Gateway and necessary resources in Region A. It sets up the infrastructure for a Private API that can be accessed securely from another VPC.

### Key Resources:
- VPC: Creates a new Virtual Private Cloud.
- Two Subnets: Sets up two subnets within the VPC for high availability.
- Route Table: Configures routing for the VPC.
- Security Group: Defines inbound and outbound traffic rules.
- VPC Endpoint for Execute API: Provides private access to the API Gateway.
- Private API Gateway: Creates a private API that can only be accessed within the VPC or through VPC peering.
- SSM Parameter: Stores the Route Table ID for use in Template 3.

### Outputs:
- Remote VPC CIDR: The CIDR block of the VPC created in this template.
- Peer VPC ID: The ID of the VPC created in this template.
- API Gateway ID: The ID of the created private API Gateway.
- VPC Endpoint URL: The URL of the VPC Endpoint for the Execute API service.
- Region: The region where this template is deployed.

## Template 2: VPC with Peering Connection and Lambda Function

This template creates a VPC in a different region (Region B) and configures a peering connection to the VPC created in Template 1. It also creates a Lambda function that acts as a client to the API Gateway.

### Key Resources:
- VPC: Creates a new VPC in Region B.
- Subnet: Sets up a subnet within the VPC.
- Internet Gateway: Provides internet access for the VPC.
- Route Table: Configures routing for the VPC.
- Security Group: Defines traffic rules, allowing outbound HTTPS traffic to the remote VPC.
- VPC Peering Connection: Establishes a peering connection with the VPC in Region A.
- Route53 Hosted Zone and DNS Record: Sets up DNS resolution for the private API Gateway.
- Lambda Function: Creates a function that sends requests to the private API Gateway in Region A.

### Important Parameters:
- VPC CIDR Block: Must be different from the CIDR block used in Template 1.
- API ID: The ID of the API Gateway created in Template 1.
- Peer VPC ID: The ID of the VPC created in Template 1.
- Remote VPC CIDR: The CIDR block of the VPC created in Template 1.
- VPC Endpoint URL: The URL of the VPC Endpoint created in Template 1.
- Peer Region: The region where Template 1 was deployed (Region A).

### Outputs:
- Peering Connection ID: The ID of the VPC peering connection.
- VPC CIDR: The CIDR block of the VPC created in this template.

## Template 3: VPC Peering Route

This template adds a route in the VPC created by Template 1 to enable traffic flow through the VPC peering connection.

### Key Resources:
- Route for VPC Peering: Adds a route to the Route Table in the VPC created by Template 1, directing traffic destined for the VPC in Region B through the peering connection.

### Important Parameters:
- Peering ID: The ID of the VPC peering connection created by Template 2.
- Remote VPC CIDR: The CIDR block of the VPC created by Template 2.
- Route Table ID: Retrieved from SSM Parameter Store, set by Template 1.

## Deployment Process

1. Deploy Template 1 in Region A
   - This sets up the VPC with the private API Gateway.
2. Note the outputs from Template 1
3. Deploy Template 2 in Region B
   - Use the outputs from Template 1 as input parameters.
   - This creates a VPC in Region B and establishes the peering connection.
4. Note the Peering Connection ID from the output of Template 2
5. Deploy Template 3 in Region A
   - Use the Peering Connection ID from Template 2 and the VPC CIDR from Template 2 as input parameters.
   - This adds the necessary route to complete the peering connection.

## Lambda Function as Client

The Lambda function created in Template 2 acts as a client that sends requests to the Private API Gateway created in Template 1. This setup allows the Lambda function to securely access the private API across regions through the VPC peering connection. The function uses the DNS record created in Template 2 to resolve the API Gateway's endpoint, ensuring that the traffic flows through the VPC peering connection.

This multi-region setup creates a secure, private network between two VPCs in different regions, allowing the Lambda function in one region to communicate with a private API Gateway in another region.

## Testing the Setup

To test the setup and verify that the Lambda function can successfully communicate with the API Gateway:

1. Navigate to the AWS Lambda console in Region B.
2. Locate and select the Lambda function created by Template 2.
3. In the Lambda function details page, find the "Test" tab or button.
4. Create a new test event or use the default test event configuration.
5. Click the "Test" button to invoke the Lambda function.
6. Review the execution results to confirm successful communication with the API Gateway.

This test will demonstrate that the Lambda function in Region B can successfully send requests to the private API Gateway in Region A through the VPC peering connection.


## Documentation
- [Working with Private REST API Gateways](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-apis.html)
- [Working with Private Hosted Zones](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-private.html)
- [What is VPC Peering?](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html)
- [VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html)

## Cleanup

To avoid incurring future charges, it's important to delete the resources in the correct order. Follow these steps to clean up the resources created by the three templates:

1. Delete Template 3 stack (in Region A)
    ```bash
    sam delete --stack-name STACK_NAME_TEMPLATE_3 --region REGION_A
    ```

2. Delete Template 2 stack (in Region B)
    ```bash
    sam delete --stack-name STACK_NAME_TEMPLATE_2 --region REGION_B
    ```

3. Delete Template 1 stack (in Region A)
    ```bash
    sam delete --stack-name STACK_NAME_TEMPLATE_1 --region REGION_A
    ```

4. Confirm all stacks have been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus" --region REGION_A
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus" --region REGION_B
    ```

Replace `STACK_NAME_TEMPLATE_1`, `STACK_NAME_TEMPLATE_2`, `STACK_NAME_TEMPLATE_3`, `REGION_A`, and `REGION_B` with the actual stack names and regions you used during deployment.

Note: Ensure you wait for each stack deletion to complete before proceeding to the next one. This helps avoid dependency conflicts during the cleanup process.

This pattern was contributed by Luigi Napoleone Capasso
----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
