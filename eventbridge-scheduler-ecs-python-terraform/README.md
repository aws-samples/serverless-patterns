# EventBridge to ECS Cron Pattern

This pattern demonstrates how to use Amazon EventBridge to schedule and trigger Amazon ECS tasks on a cron schedule using Terraform. The pattern provides a serverless, cost-effective solution for running scheduled containerized workloads.

**What the sample job does:**
- Fetches data from a public API (JSONPlaceholder)
- Processes the data (calculates statistics)
- Logs structured output to CloudWatch
- Demonstrates a typical batch processing workflow

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli) (>= 1.0) installed
* [Docker](https://docs.docker.com/get-docker/) installed (optional, for building custom container images)

## Deployment Instructions

This pattern is designed to work out-of-the-box with sensible defaults. You can deploy immediately or customize as needed.

### Quick Start (Minimal Configuration)

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd eventbridge-ecs-cron
   ```

2. **Deploy with defaults**
   ```bash
   terraform init
   terraform apply
   ```

   This will create:
   - EventBridge rule that triggers every hour
   - ECS cluster with Fargate tasks
   - All necessary IAM roles and policies
   - CloudWatch logging and monitoring
   - Auto-discovered networking (default VPC)

### Custom Configuration

For production use, create a `terraform.tfvars` file:

```hcl
# Basic configuration
project_name = "my-batch-job"
environment = "prod"
schedule_expression = "cron(0 2 * * ? *)"  # Daily at 2 AM UTC

# Container configuration
task_definition = {
  container_image = "123456789012.dkr.ecr.us-west-2.amazonaws.com/my-app:latest"
  cpu = 512
  memory = 1024
  environment_variables = {
    DATABASE_URL = "postgresql://user:pass@host:5432/db"
    LOG_LEVEL = "info"
  }
}

# Monitoring
enable_monitoring = true
```

Then deploy:
```bash
terraform init
terraform plan
terraform apply
```

## Architecture

![Architecture Diagram](architecture.png)

1. **EventBridge Rule** triggers on the specified cron schedule
2. **ECS Task** is launched in the specified cluster
3. **CloudWatch Logs** captures task execution logs
4. **CloudWatch Metrics** track task execution statistics

## How it works

1. **EventBridge Rule** is configured with a cron or rate expression to trigger on schedule
2. **ECS Task** is launched in a Fargate cluster when the rule triggers
3. **Container** executes your application code with specified environment variables
4. **CloudWatch Logs** captures all task execution logs for monitoring and debugging
5. **CloudWatch Metrics** track task execution statistics for operational visibility

## Testing

After deployment, you can test the pattern:

1. **Check EventBridge rule**:
   ```bash
   aws events list-rules --name-prefix eventbridge-ecs-cron-dev
   ```

2. **Manually trigger the rule** (for testing):
   ```bash
   aws events put-events --entries Source=manual.test,DetailType="Manual Test",Detail="{}"
   ```

3. **Monitor ECS tasks**:
   ```bash
   aws ecs list-tasks --cluster eventbridge-ecs-cron-dev-cluster
   ```

4. **View logs**:
   ```bash
   aws logs describe-log-streams --log-group-name /aws/ecs/eventbridge-ecs-cron-dev-task
   ```

## AWS services used

- [Amazon EventBridge](https://aws.amazon.com/eventbridge/) - Event bus service for application integration
- [Amazon ECS](https://aws.amazon.com/ecs/) - Container orchestration service
- [AWS Fargate](https://aws.amazon.com/fargate/) - Serverless compute for containers
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) - Monitoring and logging service
- [AWS IAM](https://aws.amazon.com/iam/) - Identity and access management

## Key Features

- **Zero Configuration Deployment**: Works out-of-the-box with sensible defaults
- **Auto-Discovery**: Automatically discovers default VPC and creates necessary security groups
- **Comprehensive Monitoring**: Built-in CloudWatch metrics and logging
- **Error Handling**: EventBridge retry policies for failed executions
- **Cost Optimized**: Uses Fargate with minimal resource allocation
- **Production Ready**: Includes security best practices and monitoring
- **Flexible Scheduling**: Supports both cron expressions and rate expressions
- **Infrastructure as Code**: Complete Terraform configuration

## Configuration Options

### Schedule Expressions

EventBridge supports both cron and rate expressions:

```hcl
# Cron expressions (6 fields: minute hour day-of-month month day-of-week year)
schedule_expression = "cron(0 9 * * ? *)"        # Daily at 9 AM UTC
schedule_expression = "cron(0 */6 * * ? *)"       # Every 6 hours
schedule_expression = "cron(0 9 ? * MON-FRI *)"   # Weekdays at 9 AM UTC

# Rate expressions
schedule_expression = "rate(1 hour)"               # Every hour
schedule_expression = "rate(30 minutes)"           # Every 30 minutes
schedule_expression = "rate(1 day)"                # Daily
```

### Container Configuration

```hcl
task_definition = {
  # Resource allocation
  cpu    = 256    # 256, 512, 1024, 2048, 4096, 8192, 16384
  memory = 512    # Must be compatible with CPU selection
  
  # Container image
  container_image = "your-app:latest"
  
  # Environment variables
  environment_variables = {
    DATABASE_URL = "postgresql://..."
    API_KEY      = "your-api-key"
    LOG_LEVEL    = "info"
  }
}
```

### Monitoring Configuration

```hcl
# Enable/disable monitoring
enable_monitoring = true

# Log retention
log_retention_days = 14  # 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, etc.
```

## Useful commands

- `terraform init` - Initialize Terraform working directory
- `terraform plan` - Preview changes before applying
- `terraform apply` - Create or update infrastructure
- `terraform destroy` - Remove all created resources
- `aws events list-rules` - List EventBridge rules
- `aws ecs list-clusters` - List ECS clusters
- `aws ecs list-tasks --cluster <cluster-name>` - List running tasks
- `aws logs describe-log-groups` - List CloudWatch log groups

## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| Task fails to start | IAM permissions, image not found | Check task execution role permissions, verify container image exists |
| EventBridge rule not triggering | Invalid cron expression, disabled rule | Validate cron syntax, ensure rule is enabled |
| Network connectivity issues | VPC configuration, security groups | Check subnet internet access, verify security group rules |
| Container exits immediately | Application error, missing environment variables | Review CloudWatch logs, check environment configuration |

## Security

This pattern implements security best practices:

- **Least Privilege IAM**: Each service has minimal required permissions
- **Network Isolation**: Tasks run in VPC with controlled network access
- **Encryption**: CloudWatch logs and SQS messages are encrypted at rest
- **No Hardcoded Secrets**: Use AWS Systems Manager Parameter Store or Secrets Manager for sensitive data

## Cost Optimization

- **Right-sizing**: Start with minimal CPU/memory and scale based on actual usage
- **Log Retention**: Configure appropriate log retention periods (default: 14 days)
- **Fargate Spot**: Consider using Spot pricing for non-critical workloads
- **Resource Tagging**: All resources are tagged for cost tracking and management

## Cleanup

To remove all resources and avoid ongoing charges:

```bash
terraform destroy
```

Confirm the destruction by typing `yes` when prompted.

## Additional Resources

- [Amazon EventBridge User Guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/)
- [Amazon ECS Developer Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/)
- [AWS Fargate User Guide](https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html)
- [EventBridge Cron Expressions](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule-schedule.html)
- [Terraform AWS Provider Documentation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)

---

Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0