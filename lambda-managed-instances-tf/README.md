# Hello World on AWS Lambda Managed Instances (Terraform)

This pattern demonstrates how to deploy a simple Hello World Lambda function running on AWS Lambda Managed Instances using Terraform. AWS Lambda Managed Instances enables you to run Lambda functions on EC2 instances while maintaining Lambda's operational simplicity. It fully manages infrastructure tasks including instance lifecycle, OS and runtime patching, routing, load balancing, and auto scaling.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-managed-instances-tf

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

**Note**: AWS Lambda Managed Instances provision EC2 instances that are **NOT eligible for the AWS Free Tier**. These instances will incur charges immediately upon deployment, regardless of your Free Tier status.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) (latest available version) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli) (version 1.0 or later) installed
* [Node.js](https://nodejs.org/) (version 18.x or later) for Lambda function dependencies

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd lambda-managed-instances-tf
    ```

### Manual Deployment

1. Install Lambda function dependencies:
    ```
    cd lambda && npm install && cd ..
    ```
1. Initialize Terraform:
    ```
    terraform init
    ```
1. Plan the deployment:
    ```
    terraform plan
    ```
1. Deploy the infrastructure:
    ```
    terraform apply
    ```
    Note: This stack will deploy to your default AWS region. You can specify a different region by setting the `aws_region` variable.

### Automated deployment

1. Use the automated deployment script:
    ```
    ./deploy.sh [aws-region]
    ```

1. Note the outputs from the Terraform deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern creates a capacity provider with VPC and security group configuration, then deploys a Node.js Lambda function (ARM64 architecture) that is associated with the capacity provider to run on managed EC2 instances. The Terraform configuration provisions a complete VPC infrastructure with public and private subnets across multiple availability zones, NAT gateways for outbound connectivity, and all necessary IAM roles and permissions.

## Testing

After deployment, you can test the Lambda function using AWS CLI or AWS Console.

### AWS CLI Testing

1. **Basic function invocation**:
   ```bash
   aws lambda invoke \
     --function-name hello-world-managed-instances-tf \
     --payload file://events/hello-world.json \
     --cli-binary-format raw-in-base64-out \
     response.json
   ```

2. **View the response**:
   ```bash
   cat response.json
   ```

3. **Custom name invocation**:
   ```bash
   echo '{"name":"Lambda Managed Instances"}' | aws lambda invoke \
     --function-name hello-world-managed-instances-tf \
     --payload file:///dev/stdin \
     --cli-binary-format raw-in-base64-out \
     custom-response.json
   ```

4. **View CloudWatch logs**:
   ```bash
   aws logs filter-log-events \
     --log-group-name /aws/lambda/hello-world-managed-instances-tf \
     --start-time $(date -d '5 minutes ago' +%s)000
   ```

### AWS Console Testing

1. Navigate to the Lambda service in the AWS Console
2. Find the function named `hello-world-managed-instances-tf`
3. Create a test event using the payload from `events/hello-world.json` or create a custom payload:
   ```json
   {
     "name": "Your Custom Name"
   }
   ```
4. Execute the test and observe the results in the execution logs

### Expected Response

The function returns a JSON response with the following structure:

```json
{
  "response": "Hello AWS Lambda on Managed Instances"
}
```

### Monitoring and Observability

Monitor the function execution through:
- **CloudWatch Logs**: Detailed execution logs with event and response data
- **Lambda Metrics**: Function performance and invocation statistics
- **CloudWatch Metrics**: Custom metrics and alarms for monitoring

## Inspecting AWS Lambda Managed Instances Infrastructure

AWS Lambda Managed Instances provision EC2 instances behind the scenes to run your Lambda functions. You can inspect this infrastructure using AWS CLI commands:

### View Capacity Provider Details

```bash
aws lambda get-capacity-provider --capacity-provider-name lambda-capacity-provider
```

This shows:
- Capacity provider ARN and state
- VPC configuration (subnets and security groups)
- Instance requirements (architecture, scaling mode)
- IAM roles and permissions

### List Associated EC2 Instances

```bash
aws ec2 describe-instances \
  --filters "Name=tag:aws:lambda:capacity-provider,Values=arn:aws:lambda:*:capacity-provider:lambda-capacity-provider" \
  --query 'Reservations[*].Instances[*].[InstanceId,InstanceType,State.Name,LaunchTime,SubnetId,PrivateIpAddress]' \
  --output table
```

This displays:
- Instance IDs and types
- Current state (running, pending, terminated)
- Launch times and subnet distribution
- Private IP addresses within the VPC

**Note**: For a complete list of supported EC2 instance types for AWS Lambda Managed Instances and their pricing, see the [AWS Lambda Pricing page](https://aws.amazon.com/lambda/pricing/).

### Understanding Instance Behavior

**Auto-scaling**: Instances are automatically created and terminated based on function demand
- **Scale-up**: New instances launch when function invocation increases
- **Scale-down**: Unused instances terminate after periods of low activity
- **Multi-AZ**: Instances are distributed across availability zones for high availability

**Instance Lifecycle**:
- Instances typically launch within 1-2 minutes of stack deployment
- They remain running to provide immediate function execution
- AWS manages all instance lifecycle operations automatically

### Automated Testing

The included test script (`./test-lambda.sh`) automatically inspects both the capacity provider and EC2 instances, providing a comprehensive view of the managed instances infrastructure.

## Regional Availability

This stack will deploy to your default AWS region or the region specified in the `aws_region` variable. Before deploying, please verify that AWS Lambda Managed Instances feature is available in your target region by using the [AWS capabilities explorer](https://builder.aws.com/build/capabilities/explore) or consulting the official [AWS Lambda Managed Instances documentation](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances.html).

## Customization

You can customize the deployment by modifying the variables in `variables.tf` or by passing variables during deployment:

```bash
terraform apply -var="aws_region=us-east-1"
```

## Cleanup
 
1. Delete the infrastructure:
    ```bash
    terraform destroy
    ```
    
    **Alternative**: Use the automated cleanup script:
    ```bash
    ./cleanup.sh [aws-region]
    ```

1. Confirm the resources have been deleted by checking the AWS Console.

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0