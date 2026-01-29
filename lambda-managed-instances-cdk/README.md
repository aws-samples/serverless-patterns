# Hello World on AWS Lambda Managed Instances

This pattern demonstrates how to deploy a simple Hello World Lambda function running on Lambda Managed Instances using AWS CDK. Lambda Managed Instances provide predictable performance and reduced cold starts for your Lambda functions.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-managed-instances-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

**Note**: Lambda Managed Instances provision EC2 instances that are **NOT eligible for the AWS Free Tier**. These instances will incur charges immediately upon deployment, regardless of your Free Tier status.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) (latest available version) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html) (version 2.232.0 or later) installed and configured
* [Node.js](https://nodejs.org/) (version 24.x or later)

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd lambda-managed-instances-cdk
    ```
1. Install the project dependencies:
    ```
    npm install
    ```
1. Deploy the CDK stack:
    ```
    cdk deploy
    ```
    Note: This stack will deploy to your default AWS region. Please refer to the [AWS capabilities explorer](https://builder.aws.com/build/capabilities/explore) for feature availability in your desired region.

1. Note the outputs from the CDK deployment process. These contain the resource names and/or ARNs which are used for testing.

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
- Uses AWS Lambda PowerTools for efficient event logging
- Demonstrates minimal Lambda function structure using the Handler type

### Amazon CloudWatch Log Group
The pattern includes a dedicated CloudWatch log group with:
- **Custom log group name**: `/demo/lambda/hello-world-managed-instances-cdk`
- **Retention period**: 2 weeks (14 days) to manage storage costs
- **Automatic cleanup**: Configured with `RemovalPolicy.DESTROY` to be deleted when the stack is destroyed
- **Direct integration**: The Lambda function is configured to use this specific log group

## Testing

After deployment, you can test the Lambda function using AWS CLI or AWS Console.

### AWS CLI Testing

1. **Basic function invocation**:
   ```bash
   aws lambda invoke \
     --function-name hello-world-managed-instances-cdk \
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
     --function-name hello-world-managed-instances-cdk \
     --payload file:///dev/stdin \
     --cli-binary-format raw-in-base64-out \
     custom-response.json
   ```

4. **View CloudWatch logs**:
   ```bash
   aws logs filter-log-events \
     --log-group-name /demo/lambda/hello-world-managed-instances-cdk \
     --start-time $(date -d '5 minutes ago' +%s)000
   ```

### AWS Console Testing

1. Navigate to the Lambda service in the AWS Console
2. Find the function named `hello-world-managed-instances-cdk`
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

The stack outputs include the log group name for easy reference when setting up monitoring dashboards or log analysis tools.

## Inspecting Lambda Managed Instances Infrastructure

Lambda Managed Instances provision EC2 instances behind the scenes to provide predictable performance. You can inspect this infrastructure using AWS CLI commands:

### View Capacity Provider Details

```bash
aws lambda get-capacity-provider --capacity-provider-name lambda-capacity-provider-cdk
```

This shows:
- Capacity provider ARN and state
- VPC configuration (subnets and security groups)
- Instance requirements (architecture, scaling mode)
- IAM roles and permissions

### List Associated EC2 Instances

```bash
aws ec2 describe-instances \
  --filters "Name=tag:aws:lambda:capacity-provider,Values=arn:aws:lambda:*:capacity-provider:lambda-capacity-provider-cdk" \
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

## Regional Availability

This stack will deploy to your default AWS region. Before deploying, please verify that Lambda Managed Instances feature is available in your target region by using the [AWS capabilities explorer](https://builder.aws.com/build/capabilities/explore) or consulting the official [Lambda Managed Instances documentation](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances.html).

## Cleanup
 
1. Delete the stack
    ```bash
    cdk destroy
    ```
1. Confirm the stack has been deleted by checking the AWS CloudFormation console or running:
    ```bash
    aws cloudformation describe-stacks --stack-name lambda-managed-instances-cdk
    ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0