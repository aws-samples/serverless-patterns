# AWS Lambda Hello World on AWS Lambda Managed Instances (Terraform)

This pattern demonstrates how to deploy a simple Hello World Lambda function running on Lambda Managed Instances using Terraform. Lambda Managed Instances provide predictable performance and reduced cold starts for your Lambda functions.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-managed-instances-tf

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

**Note**: Lambda Managed Instances provision EC2 instances that are **NOT eligible for the AWS Free Tier**. These instances will incur charges immediately upon deployment, regardless of your Free Tier status.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) (latest available version) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform](https://www.terraform.io/downloads.html) (version 1.0 or later) installed and configured
* [Python](https://www.python.org/) (version 3.13 or later) for the Lambda function runtime

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd lambda-managed-instances-tf
    ```
1. Initialize Terraform:
    ```
    terraform init
    ```
1. Review the Terraform plan:
    ```
    terraform plan
    ```
1. Deploy the Terraform stack:
    ```
    terraform apply
    ```
    Note: This stack will deploy to your default AWS region (us-east-1). You can change the region by modifying the `aws_region` variable in `variables.tf` or by passing `-var="aws_region=your-region"` to the terraform commands.
1. Note the outputs from the Terraform deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern demonstrates the deployment of a simple Lambda function on Lambda Managed Instances:

### Lambda Managed Instances

[Lambda Managed Instances](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances.html) provide:
- Predictable performance with pre-warmed execution environments
- Reduced cold start latency
- Consistent execution characteristics
- Better resource utilization for frequently invoked functions

The underlying EC2 infrastructure can be inspected using AWS CLI commands to understand how managed instances work (see "Inspecting Lambda Managed Instances Infrastructure" section below).

### Hello World Function

The Lambda function is a simple Hello World implementation that:
- Accepts an event with a name parameter
- Returns a JSON response with a greeting message
- Uses Python's standard logging library for event logging
- Demonstrates minimal Lambda function structure using Python type hints

### CloudWatch Log Group

The pattern includes a dedicated CloudWatch log group with:
- **Custom log group name**: `/demo/lambda/hello-world-managed-instances-tf`
- **Retention period**: 2 weeks (14 days) to manage storage costs
- **Automatic cleanup**: Resources are destroyed when `terraform destroy` is run
- **Direct integration**: The Lambda function is configured to use this specific log group

### VPC Configuration

The Terraform implementation creates a complete VPC setup including:
- **VPC**: Custom VPC with DNS support (10.0.0.0/16 CIDR)
- **Subnets**: 3 public and 3 private subnets across 3 availability zones for high availability
  - Public subnets: 10.0.0.0/19, 10.0.32.0/19, 10.0.64.0/19
  - Private subnets: 10.0.96.0/19, 10.0.128.0/19, 10.0.160.0/19
- **NAT Gateways**: 3 NAT Gateways (one per AZ) for outbound internet access from private subnets
- **Security Groups**: Configured for Lambda function access with restricted default security group
- **Route Tables**: Separate route tables for each subnet with proper routing configuration

## Testing

After deployment, you can test the Lambda function using AWS CLI or AWS Console.

### AWS CLI Testing

1. **Basic function invocation**:
   ```bash
   aws lambda invoke \
     --function-name hello-world-managed-instances-tf:live \
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
     --function-name hello-world-managed-instances-tf:live \
     --payload file:///dev/stdin \
     --cli-binary-format raw-in-base64-out \
     custom-response.json
   ```

4. **View CloudWatch logs**:
   ```bash
   aws logs filter-log-events \
     --log-group-name /demo/lambda/hello-world-managed-instances-tf \
     --start-time $(date -d '5 minutes ago' +%s)000
   ```

5. **View Terraform outputs**:
   ```bash
   terraform output
   ```

   **Available outputs:**
   - `function_name` - Lambda function name for CLI invocation
   - `function_arn` - Lambda function ARN
   - `function_alias` - Lambda function alias for invocation (function:live)
   - `log_group_name` - CloudWatch Log Group name
   - `capacity_provider_arn` - Lambda Capacity Provider ARN
   - `capacity_provider_name` - Lambda Capacity Provider name
   - `vpc_id` - VPC ID for Lambda Managed Instances
   - `private_subnet_ids` - Private subnet IDs (3 subnets across AZs)
   - `public_subnet_ids` - Public subnet IDs (3 subnets across AZs)
   - `security_group_id` - Lambda Security Group ID
   - `default_security_group_id` - Default Security Group ID (restricted)
   - `nat_gateway_ids` - NAT Gateway IDs (3 gateways)
   - `elastic_ip_addresses` - Elastic IP addresses for NAT Gateways

### Automated Testing Script

Use the included test script for comprehensive testing:

```bash
./test-lambda.sh [aws-profile]
```

This script performs:
- Function invocation with sample events
- CloudWatch logs inspection
- Capacity provider details retrieval
- EC2 instances inspection for managed instances

**Using Terraform outputs in the test script:**
```bash
# Get function name from Terraform output
FUNCTION_NAME=$(terraform output -raw function_name)

# Invoke function using output
aws lambda invoke \
  --function-name "$FUNCTION_NAME" \
  --payload file://events/hello-world.json \
  response.json

# View logs using output
aws logs filter-log-events \
  --log-group-name $(terraform output -raw log_group_name) \
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
- **CloudWatch Logs**: Detailed execution logs with event and response data in the dedicated log group
- **Lambda Metrics**: Function performance and invocation statistics
- **CloudWatch Metrics**: Custom metrics and alarms for monitoring

The Terraform outputs include all resource identifiers for easy reference when setting up monitoring dashboards or log analysis tools:

```bash
# Monitor function execution
aws logs filter-log-events \
  --log-group-name $(terraform output -raw log_group_name) \
  --start-time $(date -d '1 hour ago' +%s)000

# Check VPC and networking
aws ec2 describe-vpc --vpc-ids $(terraform output -raw vpc_id)
aws ec2 describe-subnets --subnet-ids $(terraform output -json private_subnet_ids | jq -r '.[]')
aws ec2 describe-nat-gateways --nat-gateway-ids $(terraform output -json nat_gateway_ids | jq -r '.[]')

# Inspect capacity provider
aws lambda get-capacity-provider --capacity-provider-name $(terraform output -raw capacity_provider_name)
```

## Inspecting Lambda Managed Instances Infrastructure

Lambda Managed Instances provision EC2 instances behind the scenes to provide predictable performance. You can inspect this infrastructure using AWS CLI commands:

### View Capacity Provider Details

```bash
# Using Terraform output
aws lambda get-capacity-provider --capacity-provider-name $(terraform output -raw capacity_provider_name)
```

This shows:
- Capacity provider ARN and state
- VPC configuration (subnets and security groups)
- Instance requirements (architecture, scaling mode)
- IAM roles and permissions

### List Associated EC2 Instances

```bash
# Using Terraform output for capacity provider ARN
CAPACITY_PROVIDER_ARN=$(terraform output -raw capacity_provider_arn)
aws ec2 describe-instances \
  --filters "Name=tag:aws:lambda:capacity-provider,Values=$CAPACITY_PROVIDER_ARN" \
  --query 'Reservations[*].Instances[*].[InstanceId,InstanceType,State.Name,LaunchTime,SubnetId,PrivateIpAddress]' \
  --output table
```

This displays:
- Instance IDs and types
- Current state (running, pending, terminated)
- Launch times and subnet distribution
- Private IP addresses within the VPC

**Note**: For a complete list of supported EC2 instance types for Lambda Managed Instances and their pricing, see the [AWS Lambda Pricing page](https://aws.amazon.com/lambda/pricing/).

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

## Terraform Configuration

### Variables

The following variables can be customized in `variables.tf` or passed via command line:

- `aws_region`: AWS region for deployment (default: us-east-1)
- `environment`: Environment name for tagging (default: demo)
- `project_name`: Project name for resource naming (default: lambda-managed-instances)

### Outputs

The Terraform configuration provides the following outputs:

- `function_name`: Lambda function name
- `function_arn`: Lambda function ARN
- `function_alias`: Lambda function alias (function:live)
- `log_group_name`: CloudWatch log group name
- `capacity_provider_arn`: Lambda capacity provider ARN
- `capacity_provider_name`: Lambda capacity provider name
- `vpc_id`: VPC ID
- `private_subnet_ids`: Private subnet IDs (array of 3)
- `public_subnet_ids`: Public subnet IDs (array of 3)
- `security_group_id`: Lambda security group ID
- `default_security_group_id`: Default security group ID (restricted)
- `nat_gateway_ids`: NAT Gateway IDs (array of 3)
- `elastic_ip_addresses`: Elastic IP addresses (array of 3)

### Using Outputs in Scripts

```bash
# Get all outputs
terraform output

# Get specific output values
FUNCTION_NAME=$(terraform output -raw function_name)
VPC_ID=$(terraform output -raw vpc_id)
CAPACITY_PROVIDER_ARN=$(terraform output -raw capacity_provider_arn)

# Use in AWS CLI commands
aws lambda invoke --function-name "$FUNCTION_NAME" --payload '{}' response.json
aws ec2 describe-vpc --vpc-ids "$VPC_ID"

# Use function alias for managed instances
FUNCTION_ALIAS=$(terraform output -raw function_alias)
aws lambda invoke --function-name "$FUNCTION_ALIAS" --payload '{}' response.json

# Get capacity provider association status
terraform output capacity_provider_association

# Get manual association command if needed
terraform output manual_association_command
```

## Regional Availability

This stack will deploy to your configured AWS region (default: us-east-1). Before deploying, please verify that Lambda Managed Instances feature is available in your target region by using the [AWS capabilities explorer](https://builder.aws.com/build/capabilities/explore) or consulting the official [Lambda Managed Instances documentation](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances.html).

## Cleanup

1. Delete the Terraform stack:
    ```bash
    terraform destroy
    ```
1. Confirm all resources have been deleted by checking the AWS Console or running:
    ```bash
    terraform show
    ```

## File Structure

```
lambda-managed-instances-tf/
├── main.tf                      # Main Terraform configuration
├── variables.tf                 # Input variables
├── outputs.tf                   # Output values
├── README.md                    # This file
├── test-lambda.sh              # Testing script
├── .gitignore                  # Terraform-specific gitignore
├── terraform.tfvars.example    # Example variables file
├── example-pattern.json        # Pattern metadata
├── lambda/
│   └── hello-world.py          # Lambda function code
└── events/
    └── hello-world.json        # Test event payload
```

----
Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0