# Scheduled Amazon ECS Task Execution Using Amazon EventBridge and Terraform

This pattern demonstrates how to use Amazon EventBridge to schedule and trigger Amazon ECS Fargate tasks on a cron or rate schedule using Terraform. It provides a serverless, cost-effective solution for running scheduled containerized workloads.

The pattern ships a small Python application in `src/` that demonstrates a real scheduled job: it fetches sample data from a public API ([JSONPlaceholder](https://jsonplaceholder.typicode.com/)), processes it, and writes structured JSON logs to Amazon CloudWatch Logs. During `terraform apply`, Terraform creates an Amazon ECR repository, builds the Python image locally with Docker, pushes it to ECR, and wires it into the ECS task definition.

**What the sample job does:**
- Fetches sample posts from JSONPlaceholder
- Computes basic statistics (total posts, average title length, average word count, longest/shortest post)
- Emits structured JSON log lines to CloudWatch Logs

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage. Please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli) (>= 1.0) installed
* [Git](https://git-scm.com/downloads) installed
* [Docker](https://docs.docker.com/get-docker/) installed and **running locally**. Terraform builds the container image and pushes it to Amazon ECR during `terraform apply`. Verify Docker is running with:
  ```bash
  docker info
  ```

## Deployment Instructions

This pattern is designed to work out-of-the-box with sensible defaults. You can deploy immediately or customize as needed.

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/aws-samples/serverless-patterns
   cd serverless-patterns/eventbridge-scheduler-ecs-python-terraform
   ```

2. **Ensure Docker is running**
   ```bash
   docker info
   ```
   If this command fails, start Docker Desktop (macOS/Windows) or the Docker daemon (`sudo systemctl start docker` on Linux) before continuing.

3. **Deploy** (Terraform handles ECR creation, Docker build, and push automatically)
   ```bash
   terraform init
   terraform apply
   ```
   Type `yes` when prompted.

   This will create:
   - An Amazon ECR repository, then build the Python image from `src/` and push it
   - An Amazon ECS Fargate cluster and task definition that uses that image
   - An Amazon EventBridge rule that triggers on the configured schedule (default: `rate(1 hour)`)
   - IAM roles for ECS task execution, the task itself, and EventBridge → ECS, scoped to least privilege
   - An Amazon CloudWatch log group for ECS task logs (14-day retention by default)
   - A second Amazon CloudWatch log group for EventBridge events
   - A security group allowing HTTPS (TCP 443) outbound for image pulls, CloudWatch, and the JSONPlaceholder API
   - Auto-discovered networking using the default VPC and its subnets

### Custom Configuration

For production use, create a `terraform.tfvars` file:

```hcl
# Basic configuration
project_name        = "my-batch-job"
environment         = "prod"
schedule_expression = "cron(0 2 * * ? *)" # Daily at 2 AM UTC

# Container configuration
task_definition = {
  family   = "my-batch-job-prod-task"
  cpu      = 512
  memory   = 1024
  container_name = "my-batch-job-prod-container"
  environment_variables = {
    LOG_LEVEL = "info"
  }
  log_group_name = "/aws/ecs/my-batch-job-prod-task"
}

# Optional: tag the image something other than "latest"
image_tag = "v1.0.0"
```

Then deploy:
```bash
terraform init
terraform plan
terraform apply
```

To run a different workload, modify `src/app.py` (and `src/Dockerfile`/`src/requirements.txt` if needed) before running `terraform apply` — Terraform will rebuild and push the image automatically because the source file hashes are tracked in the build resource's `triggers`.

## Architecture

![Architecture Diagram](architecture.png)

1. **Amazon EventBridge rule** triggers on the configured schedule (default: `rate(1 hour)`)
2. **Amazon EventBridge** assumes the EventBridge IAM role and calls `ecs:RunTask` against the ECS cluster
3. **Amazon ECS Fargate task** is launched in the default VPC and pulls the Python image from Amazon ECR
4. **Python app** fetches data from JSONPlaceholder, processes it, and emits JSON log lines
5. **Amazon CloudWatch Logs** captures the structured JSON output for monitoring and debugging

## How it works

1. **EventBridge rule** is configured with a cron or rate expression to trigger on schedule
2. **ECS task** is launched in the Fargate cluster when the rule fires
3. **Container** runs the configured image (the Dockerfile's `CMD ["python", "app.py"]` by default) with the supplied environment variables
4. **CloudWatch Logs** captures all task execution output for monitoring and debugging

## Testing

After deployment, the ECS task is triggered automatically by EventBridge based on the configured schedule. With the default `rate(1 hour)`, the first task will run within the next hour. You can either wait for the schedule or trigger a run manually as described in step 4.

1. **Confirm the EventBridge rule and its schedule**:
   ```bash
   aws events list-rules --name-prefix eventbridge-ecs-cron-dev
   ```
   The `ScheduleExpression` in the output tells you when the next trigger will occur.

2. **Wait for the scheduled trigger**, then check stopped tasks (Fargate one-shot tasks complete and stop):
   ```bash
   aws ecs list-tasks \
     --cluster eventbridge-ecs-cron-dev-cluster \
     --desired-status STOPPED
   ```
   If the list is empty, the schedule has not triggered yet. Either wait for the next interval or run a task manually as described in step 4.

3. **View the task logs in CloudWatch**:
   ```bash
   aws logs tail /aws/ecs/eventbridge-ecs-cron-dev-task --since 1h
   ```
   You should see structured JSON output like:
   ```json
   {"timestamp":"...","level":"INFO","message":"=== Starting Data Processing Job ===",...}
   {"timestamp":"...","level":"INFO","message":"Fetching sample data from API",...}
   {"timestamp":"...","level":"INFO","message":"Successfully fetched 100 posts from API",...}
   {"timestamp":"...","level":"INFO","message":"Report generated successfully",...}
   {"timestamp":"...","level":"INFO","message":"=== Job Completed Successfully ===","duration_seconds":...,"posts_processed":100}
   ```

4. **Trigger a run manually** (without waiting for the schedule):
   ```bash
   # Look up the default VPC subnet and the security group created by Terraform
   SUBNET_ID=$(aws ec2 describe-subnets \
     --filters "Name=vpc-id,Values=$(aws ec2 describe-vpcs --filters Name=is-default,Values=true --query 'Vpcs[0].VpcId' --output text)" \
     --query 'Subnets[0].SubnetId' --output text)
   SG_ID=$(aws ec2 describe-security-groups \
     --filters "Name=group-name,Values=eventbridge-ecs-cron-dev-ecs-tasks*" \
     --query 'SecurityGroups[0].GroupId' --output text)

   aws ecs run-task \
     --cluster eventbridge-ecs-cron-dev-cluster \
     --task-definition eventbridge-ecs-cron-dev-task \
     --launch-type FARGATE \
     --network-configuration "awsvpcConfiguration={subnets=[$SUBNET_ID],securityGroups=[$SG_ID],assignPublicIp=ENABLED}"
   ```

## AWS services used

- [Amazon EventBridge](https://aws.amazon.com/eventbridge/) - Event bus service for scheduling
- [Amazon ECS](https://aws.amazon.com/ecs/) - Container orchestration service
- [AWS Fargate](https://aws.amazon.com/fargate/) - Serverless compute for containers
- [Amazon ECR](https://aws.amazon.com/ecr/) - Container image registry
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) - Monitoring and logging service
- [AWS IAM](https://aws.amazon.com/iam/) - Identity and access management

## Configuration Options

### Schedule Expressions

EventBridge supports both cron and rate expressions:

```hcl
# Cron expressions (6 fields: minute hour day-of-month month day-of-week year)
schedule_expression = "cron(0 9 * * ? *)"       # Daily at 9 AM UTC
schedule_expression = "cron(0 */6 * * ? *)"     # Every 6 hours
schedule_expression = "cron(0 9 ? * MON-FRI *)" # Weekdays at 9 AM UTC

# Rate expressions
schedule_expression = "rate(1 hour)"            # Every hour (default)
schedule_expression = "rate(30 minutes)"        # Every 30 minutes
schedule_expression = "rate(1 day)"             # Daily
```

### Container Configuration

```hcl
task_definition = {
  family                = "eventbridge-ecs-cron-dev-task"
  cpu                   = 256                                    # 256, 512, 1024, 2048, 4096, 8192, 16384
  memory                = 512                                    # Must be a valid combination with cpu
  container_name        = "eventbridge-ecs-cron-dev-container"
  environment_variables = {
    LOG_LEVEL = "info"
  }
  log_group_name = "/aws/ecs/eventbridge-ecs-cron-dev-task"
}

# Tag applied to the image built from src/ and pushed to ECR
image_tag = "latest"
```

The container image is built automatically from `src/` and pushed to the ECR repository managed by Terraform. To customize the application, modify `src/app.py` (and `src/Dockerfile` / `src/requirements.txt` if needed) and re-run `terraform apply` — Terraform tracks file hashes in the build resource's `triggers`, so changes will trigger a rebuild and push.

### Logging Configuration

```hcl
log_retention_days = 14 # 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, etc.
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
| `terraform apply` fails at the Docker build step | Docker not running | Run `docker info` to verify Docker is running. Start Docker Desktop or the daemon first |
| Task fails to start with `CannotPullContainerError` | Subnet has no path to ECR, or image not yet pushed | Confirm `terraform apply` completed without errors and that the subnet has a NAT/Internet Gateway route or `cluster_config.assign_public_ip = true` |
| Task fails to start with image platform mismatch | Image built for the wrong CPU architecture | The build uses `--platform linux/amd64` by default for Fargate compatibility; confirm you did not override this in `src/Dockerfile` |
| EventBridge rule not triggering | Invalid cron expression or rule disabled | Validate cron syntax against the EventBridge docs and confirm the rule is enabled in the console |
| No tasks appear after the schedule fires | Network or IAM issue | Check the EventBridge log group `/aws/events/<project>-<env>-eventbridge` and the ECS log group |
| Network connectivity issues | VPC config or security groups | Confirm the subnet has internet access and the security group allows outbound HTTPS (TCP 443) |
| Container exits immediately | Application error or missing env vars | Review CloudWatch logs and check the container's command/environment configuration |

## Security

This pattern implements security best practices:

- **Least privilege IAM**: The task execution role grants only `ecr:GetAuthorizationToken` (cluster-wide), repository-scoped `ecr:BatchCheckLayerAvailability` / `ecr:GetDownloadUrlForLayer` / `ecr:BatchGetImage` on the project's ECR repo, and CloudWatch Logs writes scoped to the task log group. The task role grants only CloudWatch Logs writes. The EventBridge role grants only `ecs:RunTask` on the project's task definition and `iam:PassRole` on the two task roles.
- **Network isolation**: Tasks run inside a VPC behind a security group that only allows HTTPS (TCP 443) outbound.
- **Encryption**: Amazon CloudWatch Logs is encrypted at rest by default. Image scan-on-push is enabled on the ECR repository.
- **No hardcoded secrets**: Use AWS Systems Manager Parameter Store or AWS Secrets Manager for sensitive data, and reference them as `secrets` on the container definition.

## Cost Optimization

- **Right-sizing**: Start with minimal CPU/memory and scale based on actual usage
- **Log retention**: Configure appropriate log retention periods (default: 14 days)
- **Fargate Spot**: Consider using Spot pricing for non-critical workloads
- **Resource tagging**: All resources are tagged for cost tracking and management

## Cleanup

To remove all resources and avoid ongoing charges:

```bash
terraform destroy
```

Confirm the destruction by typing `yes` when prompted. The ECR repository is created with `force_delete = true`, so the destroy will remove it even if it still contains the pushed image.

## Additional Resources

- [Amazon EventBridge User Guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/)
- [Amazon ECS Developer Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/)
- [AWS Fargate User Guide](https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html)
- [EventBridge Cron Expressions](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule-schedule.html)
- [Terraform AWS Provider Documentation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)

---

Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
