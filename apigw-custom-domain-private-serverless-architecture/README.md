# Fully Private Serverless Architecture with API Gateway Private Custom Domain


![alt text](image.png)

Architecture Overview
---

This architecture represents a **fully private serverless environment** that ensures secure communication between AWS services within a Virtual Private Cloud (VPC). It is designed to handle API requests, process messages, and manage data storage and notifications, all while leveraging private connectivity to maintain security and isolation.


Learn more about this pattern at Serverless Land Patterns



### Key Components and Workflow




1. [Route 53 (Private Hosted Zone)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-private.html):

    * A private hosted zone in Route 53 is configured to resolve the custom domain name for the API Gateway within the VPC.
    * This ensures that DNS resolution for the API Gateway's private custom domain occurs only within the VPC.

2. [Private Custom Domain for API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-custom-domains.html):

    * The API Gateway is configured with a private custom domain name, secured using an ACM certificate.
    * This domain name is accessible only via the VPC endpoint, ensuring that API traffic remains private.

3. [VPC Endpoint for API Gateway](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html):

    * An Execute-API VPC Endpoint is used to enable private communication between clients in the VPC and the API Gateway.
    * This eliminates the need for public internet exposure when accessing the API Gateway.

4. [Amazon API Gateway (Private API)](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-apis.html):

    * The API Gateway serves as the entry point for handling client requests.
    * It integrates with Amazon SQS to queue incoming requests for downstream processing.

5. [Amazon SQS (Standard Queue)](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html):
    * Messages are queued in SQS for asynchronous processing by the Lambda function.
    * This decouples the client request from downstream processing, improving scalability and reliability.

6. [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html):
    * A Lambda function processes messages from SQS.
    * Depending on the message content, it performs one of two actions:
        * Inserts data into DynamoDB.
        * Publishes notifications to an SNS topic, if there is some error in lambda function. 

7. VPC Endpoints for DynamoDB and SNS:

    * A DynamoDB VPC Endpoint ensures that all interactions with DynamoDB occur privately within the VPC.
    * An SNS VPC Endpoint allows Lambda to publish notifications to SNS without requiring public internet access.

8. [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html):

    * Used as a fully managed NoSQL database to store processed data.
    * Data is inserted into DynamoDB with attributes such as unique IDs, random values, and timestamps.

9. [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html):

    * SNS is used to send notifications based on specific conditions (e.g., when no data insertion into DynamoDB is required).
    * Notifications are sent securely via the VPC endpoint.


Use Cases
----

1. **E-Commerce Applications:**
Securely process orders through an API Gateway Private Custom Domain, queue them in SQS, process with Lambda, store in DynamoDB, and send notifications for high-priority issues via SNS without exposing any endpoints to the public internet.

2. **Monitoring Systems:** Collect logs or critical events through the private API Gateway, store them in DynamoDB, and trigger alerts via SNS for conditions like security breaches, ensuring all communication remains private within the VPC.
3. **IoT Applications:** Ingest sensor data through an API Gateway Private Custom Domain, store it in DynamoDB, and send threshold-based alerts (e.g., temperature limits) via SNS, all while maintaining secure, private connectivity within the VPC.

- Why Use an API Gateway Private Custom Domain? : 
The Private Custom Domain ensures that all API traffic is securely routed within the VPC using private DNS resolution (via Route 53). This eliminates public exposure of APIs, enhances security, and simplifies integration with other private AWS services like SQS, DynamoDB, and SNS. This architecture is ideal for scenarios requiring strict security and isolation.



# Deployment Instructions

## Prerequisites
- An AWS account with an IAM user or role that has sufficient permissions to make the necessary AWS service calls and manage AWS resources.
- Ensure [**AWS CLI**](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) is installed and configured.
- Install the[**AWS Serverless Application Model (AWS SAM)**](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html) CLI.
- [**Git Installed**](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- Prepare an [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) with [2 subnet](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html) (Recommend)
- Prepate [**ACM certification**](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) for API Gateway custom domain. 
- Gather the following parameters for deployment:
  - **VpcId**: The ID of the VPC where resources will be deployed.
  - **RouteTableId**: The ID of the route table for the DynamoDB Gateway Endpoint.
  - **SubnetIds**: List of Subnet IDs for Lambda function deployment.
  - **CustomDomainName**: Custom domain name for the private API Gateway (e.g., `private.example.com`).
  - **CertificateArn**: ARN of the ACM certificate for the custom domain.
  - **PrivateHostedZoneId**: Hosted zone ID for the private Route53 domain.
  - **SQSQueueName**: Name of the SQS queue (default: `MyCustomQueue`).
  - **DynamoDBTableName**: Name of the DynamoDB table (default: `MyCustomTable`).
  - **SNSTopicName**: Name of the SNS topic (default: `MyCustomTopic`).
  - **SubscriptionEmail**: Email address to subscribe to the SNS topic.

---

## Steps to Deploy

### Step 1: Clone the Repository
1. Create a new directory and navigate to it in a terminal.

> git clone https://github.com/aws-samples/serverless-patterns

2. Change directory to the pattern directory:

> cd apigw-custom-domain-private-serverless-architecture



### Step 2: Deploy with AWS SAM
1. From the project directory, run the following command:

sam deploy --guided



2. During the prompts, provide the following inputs:
- **Stack Name**: Enter a name for your CloudFormation stack (e.g., `private-api-architecture-stack`).
- **AWS Region**: Enter your desired AWS region (e.g., `us-east-1`).
- **VpcId**: Enter your VPC ID.
- **RouteTableId**: Enter your route table ID for DynamoDB Gateway Endpoint.
- **SubnetIds**: Enter a comma-separated list of private subnet IDs for Lambda deployment.
- **CustomDomainName**: Enter your private custom domain name (e.g., `private.example.com`).
- **CertificateArn**: Enter the ARN of your ACM certificate for this domain.
- **PrivateHostedZoneId**: Enter your Route53 private hosted zone ID.
- **SQSQueueName**: Accept default (`MyCustomQueue`) or provide a custom name.
- **DynamoDBTableName**: Accept default (`MyCustomTable`) or provide a custom name.
- **SNSTopicName**: Accept default (`MyCustomTopic`) or provide a custom name.
- **SubscriptionEmail**: Enter a valid email address for SNS topic subscription.

3. Additional prompts:
- Confirm changes before deploy (`Y/n`): `Y`
- Allow SAM CLI IAM role creation (`Y/n`): `Y`
- Disable rollback on failure (`y/N`): `N`
- Save arguments to configuration file (`Y/n`): `Y`
  - Configuration file name (default): `samconfig.toml`
  - Configuration environment (default): `default`

4. Note down the outputs from the SAM deployment process, which include:
- The Private Custom Domain Name URL to test your API.

---

## Testing

To test the private API Gateway, you must first ensure that you are within the subnets of your VPC. This can be achieved by connecting to an **EC2 instance** or using another method to access the private network. The EC2 instance should be launched in that subnets. 

And, once the deployment is complete, you will receive an email at the email address set for SNS notifications with the following content:

**You have chosen to subscribe to the topic: [Your SNS ARN] To confirm this subscription, click or visit the link below (If this was in error no action is necessary):
Confirm subscription**

You need to confirm this subscription to receive SNS notifications in case incorrect values are entered or errors occur later.

### Steps for Testing

1. **Connect to the Subnet**:
   - Launch an EC2 instance in that subnets specified during deployment.
   - Ensure the EC2 instance has a security group allowing outbound HTTPS traffic (port 443).
   - Use **SSH** or **EC2 Instance Connect** to access the instance.

2. **Test the API Gateway**:
   - Once connected to the EC2 instance, use the following `curl` commands to test the API Gateway:

   #### Test DynamoDB Insertion

   > curl -X POST
-H "Content-Type: application/json"
-d '{"Insert": "DynamoDB"}'
https://{PrivateCustomDomainName}/send-message

   #### Test DynamoDB Insertion failure

    > curl -X POST
-H "Content-Type: application/json"
-d '{"Insert": "Dynamoooo"}'
https://{PrivateCustomDomainName}/send-message




---

## Cleanup

To avoid incurring future charges, delete the deployed stack:


> sam delete --stack-name {STACK_NAME}


Replace `{STACK_NAME}` with your CloudFormation stack name (e.g., `private-api-architecture-stack`).









