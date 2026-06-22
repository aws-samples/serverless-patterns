# EventBridge ECS Cron Pattern - Terraform Infrastructure
# This file implements a scheduled task execution system using AWS EventBridge and ECS

terraform {
  required_version = ">= 1.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    null = {
      source  = "hashicorp/null"
      version = "~> 3.2"
    }
  }

  # Backend configuration template - uncomment and configure for remote state
  # backend "s3" {
  #   bucket         = "your-terraform-state-bucket"
  #   key            = "eventbridge-ecs-cron/terraform.tfstate"
  #   region         = "us-west-2"
  #   encrypt        = true
  #   dynamodb_table = "terraform-state-lock"
  # }
}

# Variables for configuration
variable "project_name" {
  description = "Name of the project for resource naming and tagging"
  type        = string
  default     = "eventbridge-ecs-cron"
  validation {
    condition     = can(regex("^[a-z0-9][a-z0-9-]*[a-z0-9]$", var.project_name))
    error_message = "Project name must contain only lowercase letters, numbers, and hyphens, and must start and end with alphanumeric characters."
  }
}

variable "environment" {
  description = "Environment name (e.g., dev, staging, prod)"
  type        = string
  default     = "dev"
  validation {
    condition     = contains(["dev", "staging", "prod", "test"], var.environment)
    error_message = "Environment must be one of: dev, staging, prod, test."
  }
}

variable "schedule_expression" {
  description = "Cron expression for EventBridge rule (e.g., 'cron(0 12 * * ? *)')"
  type        = string
  default     = "rate(1 hour)" # Default: run every hour for demo purposes
  validation {
    condition     = can(regex("^(cron|rate)\\(.*\\)$", var.schedule_expression))
    error_message = "Schedule expression must be a valid cron or rate expression format: cron(minute hour day-of-month month day-of-week year) or rate(value unit)."
  }
  validation {
    condition     = can(regex("^cron\\([0-9*,/-]+\\s+[0-9*,/-]+\\s+[0-9*,?/-]+\\s+[0-9*,/-]+\\s+[0-9*,?/-]+\\s+[0-9*,/-]+\\)$", var.schedule_expression)) || can(regex("^rate\\([0-9]+\\s+(minute|minutes|hour|hours|day|days)\\)$", var.schedule_expression))
    error_message = "Invalid cron or rate expression format. Cron format: cron(minute hour day-of-month month day-of-week year). Rate format: rate(value unit) where unit is minute(s), hour(s), or day(s)."
  }
  validation {
    condition     = !can(regex("^cron\\(.*\\s+\\*\\s+.*\\s+\\*\\s+.*\\)$", var.schedule_expression))
    error_message = "Cron expressions cannot have both day-of-month and day-of-week as wildcards (*). Use ? for one of them."
  }
}

variable "task_definition" {
  description = "ECS task definition configuration"
  type = object({
    family                = string
    cpu                   = number
    memory                = number
    container_name        = string
    environment_variables = map(string)
    log_group_name        = string
  })
  default = {
    family                = "eventbridge-ecs-cron-dev-task"
    cpu                   = 256
    memory                = 512
    container_name        = "eventbridge-ecs-cron-dev-container"
    environment_variables = {}
    log_group_name        = "/aws/ecs/eventbridge-ecs-cron-dev-task"
  }
  validation {
    condition = contains([
      256, 512, 1024, 2048, 4096, 8192, 16384
    ], var.task_definition.cpu)
    error_message = "CPU must be one of: 256, 512, 1024, 2048, 4096, 8192, 16384."
  }
  validation {
    condition     = var.task_definition.memory >= 512 && var.task_definition.memory <= 30720
    error_message = "Memory must be between 512 and 30720 MB."
  }
  validation {
    condition     = can(regex("^[a-zA-Z0-9][a-zA-Z0-9_-]*$", var.task_definition.family))
    error_message = "Task family name must start with alphanumeric character and contain only alphanumeric characters, hyphens, and underscores."
  }
  validation {
    condition     = can(regex("^[a-zA-Z0-9][a-zA-Z0-9_-]*$", var.task_definition.container_name))
    error_message = "Container name must start with alphanumeric character and contain only alphanumeric characters, hyphens, and underscores."
  }
  validation {
    condition     = length(var.task_definition.container_name) <= 255
    error_message = "Container name must be 255 characters or less."
  }
  validation {
    condition     = length(var.task_definition.family) <= 255
    error_message = "Task family name must be 255 characters or less."
  }
  validation {
    condition = (
      (var.task_definition.cpu == 256 && var.task_definition.memory >= 512 && var.task_definition.memory <= 2048) ||
      (var.task_definition.cpu == 512 && var.task_definition.memory >= 1024 && var.task_definition.memory <= 4096) ||
      (var.task_definition.cpu == 1024 && var.task_definition.memory >= 2048 && var.task_definition.memory <= 8192) ||
      (var.task_definition.cpu == 2048 && var.task_definition.memory >= 4096 && var.task_definition.memory <= 16384) ||
      (var.task_definition.cpu == 4096 && var.task_definition.memory >= 8192 && var.task_definition.memory <= 30720) ||
      (var.task_definition.cpu >= 8192 && var.task_definition.memory >= 16384 && var.task_definition.memory <= 30720)
    )
    error_message = "Invalid CPU/Memory combination. Valid combinations: 256 CPU (512-2048 MB), 512 CPU (1024-4096 MB), 1024 CPU (2048-8192 MB), 2048 CPU (4096-16384 MB), 4096 CPU (8192-30720 MB), 8192+ CPU (16384-30720 MB)."
  }
}

variable "cluster_config" {
  description = "ECS cluster configuration"
  type = object({
    name               = string
    launch_type        = string
    subnet_ids         = list(string)
    security_group_ids = list(string)
    assign_public_ip   = optional(bool, false)
  })
  default = {
    name               = "eventbridge-ecs-cron-dev-cluster"
    launch_type        = "FARGATE"
    subnet_ids         = []
    security_group_ids = []
    assign_public_ip   = true # Enable public IP to improve connectivity
  }
  validation {
    condition     = contains(["FARGATE", "EC2"], var.cluster_config.launch_type)
    error_message = "Launch type must be either 'FARGATE' or 'EC2'."
  }

  validation {
    condition     = can(regex("^[a-zA-Z0-9][a-zA-Z0-9_-]*$", var.cluster_config.name))
    error_message = "Cluster name must start with alphanumeric character and contain only alphanumeric characters, hyphens, and underscores."
  }
  validation {
    condition     = length(var.cluster_config.name) <= 255
    error_message = "Cluster name must be 255 characters or less."
  }
  validation {
    condition = alltrue([
      for subnet_id in var.cluster_config.subnet_ids : can(regex("^subnet-[0-9a-f]{8,17}$", subnet_id))
    ])
    error_message = "All subnet IDs must be valid AWS subnet IDs (format: subnet-xxxxxxxxx)."
  }
  validation {
    condition = alltrue([
      for sg_id in var.cluster_config.security_group_ids : can(regex("^sg-[0-9a-f]{8,17}$", sg_id))
    ])
    error_message = "All security group IDs must be valid AWS security group IDs (format: sg-xxxxxxxxx)."
  }
}

variable "additional_tags" {
  description = "Additional tags to apply to all resources"
  type        = map(string)
  default     = {}
}

variable "image_tag" {
  description = "Tag applied to the Docker image built from src/ and pushed to the ECR repository created by this module."
  type        = string
  default     = "latest"
  validation {
    condition     = can(regex("^[a-zA-Z0-9_][a-zA-Z0-9._-]{0,127}$", var.image_tag))
    error_message = "Image tag must match the Docker tag format (alphanumerics, underscores, periods, hyphens; up to 128 chars)."
  }
}

# Local values for consistent naming and tagging
locals {
  # Consistent naming convention: {project_name}-{environment}-{resource_type}
  name_prefix = "${var.project_name}-${var.environment}"

  # Common tags applied to all resources
  common_tags = merge({
    Project     = var.project_name
    Environment = var.environment
    ManagedBy   = "Terraform"
    Pattern     = "EventBridge-ECS-Cron"
    CreatedBy   = "Terraform"
    Owner       = "DevOps"
    CostCenter  = var.project_name
  }, var.additional_tags)
}

# Variables for CloudWatch logging configuration
variable "log_retention_days" {
  description = "CloudWatch log retention period in days"
  type        = number
  default     = 14
  validation {
    condition = contains([
      1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, 3653
    ], var.log_retention_days)
    error_message = "Log retention days must be a valid CloudWatch retention period."
  }
}

variable "enable_log_insights" {
  description = "Enable CloudWatch Logs Insights for structured logging"
  type        = bool
  default     = true
}

variable "enable_monitoring" {
  description = "Enable CloudWatch monitoring and alarms"
  type        = bool
  default     = true
}




variable "retry_policy" {
  description = "EventBridge retry policy configuration"
  type = object({
    maximum_retry_attempts       = number
    maximum_event_age_in_seconds = number
  })
  default = {
    maximum_retry_attempts       = 3
    maximum_event_age_in_seconds = 3600 # 1 hour
  }
  validation {
    condition     = var.retry_policy.maximum_retry_attempts >= 0 && var.retry_policy.maximum_retry_attempts <= 185
    error_message = "Maximum retry attempts must be between 0 and 185."
  }
  validation {
    condition     = var.retry_policy.maximum_event_age_in_seconds >= 60 && var.retry_policy.maximum_event_age_in_seconds <= 86400
    error_message = "Maximum event age must be between 60 seconds (1 minute) and 86400 seconds (24 hours)."
  }
}

variable "ecs_task_retry_config" {
  description = "ECS task failure handling configuration"
  type = object({
    enable_circuit_breaker             = bool
    circuit_breaker_rollback           = bool
    deployment_maximum_percent         = number
    deployment_minimum_healthy_percent = number
    enable_execute_command             = bool
  })
  default = {
    enable_circuit_breaker             = true
    circuit_breaker_rollback           = true
    deployment_maximum_percent         = 200
    deployment_minimum_healthy_percent = 100
    enable_execute_command             = false
  }
  validation {
    condition     = var.ecs_task_retry_config.deployment_maximum_percent >= 100 && var.ecs_task_retry_config.deployment_maximum_percent <= 200
    error_message = "Deployment maximum percent must be between 100 and 200."
  }
  validation {
    condition     = var.ecs_task_retry_config.deployment_minimum_healthy_percent >= 0 && var.ecs_task_retry_config.deployment_minimum_healthy_percent <= 100
    error_message = "Deployment minimum healthy percent must be between 0 and 100."
  }
}



# Data source for the AWS account, used to construct image URIs and ARNs
data "aws_caller_identity" "current" {}

# ECR repository that holds the application image built from src/.
# force_delete = true allows `terraform destroy` to remove the repo even if
# it still contains images, which keeps the demo end-to-end self-contained.
resource "aws_ecr_repository" "app" {
  name                 = "${local.name_prefix}-app"
  image_tag_mutability = "MUTABLE"
  force_delete         = true

  image_scanning_configuration {
    scan_on_push = true
  }

  tags = merge(local.common_tags, {
    Name         = "${local.name_prefix}-app"
    ResourceType = "ECR-Repository"
    Purpose      = "Container-Image-Storage"
    Component    = "Compute"
  })
}

# Build the Python application image from src/ and push it to ECR. This runs
# locally (Docker must be installed and running). The image is rebuilt and
# pushed whenever any of the source files or the repo URL change.
resource "null_resource" "docker_build_push" {
  triggers = {
    dockerfile_hash   = filemd5("${path.module}/src/Dockerfile")
    app_hash          = filemd5("${path.module}/src/app.py")
    requirements_hash = filemd5("${path.module}/src/requirements.txt")
    repository_url    = aws_ecr_repository.app.repository_url
    image_tag         = var.image_tag
  }

  provisioner "local-exec" {
    interpreter = ["/bin/sh", "-c"]
    working_dir = "${path.module}/src"
    command     = <<-EOT
      set -euo pipefail
      aws ecr get-login-password --region ${data.aws_region.current.name} \
        | docker login --username AWS --password-stdin ${data.aws_caller_identity.current.account_id}.dkr.ecr.${data.aws_region.current.name}.amazonaws.com
      docker build --platform linux/amd64 -t ${aws_ecr_repository.app.repository_url}:${var.image_tag} .
      docker push ${aws_ecr_repository.app.repository_url}:${var.image_tag}
    EOT
  }

  depends_on = [aws_ecr_repository.app]
}

# Local for the fully-qualified image URI, used by the task definition.
locals {
  container_image = "${aws_ecr_repository.app.repository_url}:${var.image_tag}"
}

# CloudWatch Log Group for ECS tasks
resource "aws_cloudwatch_log_group" "ecs_logs" {
  name              = "/aws/ecs/${local.name_prefix}-task"
  retention_in_days = var.log_retention_days
  tags = merge(local.common_tags, {
    Name         = "${local.name_prefix}-ecs-logs"
    ResourceType = "CloudWatch-LogGroup"
    LogType      = "ECS-Task-Logs"
    Purpose      = "Scheduled-Task-Execution"
    Component    = "Logging"
  })
}

# CloudWatch Log Group for EventBridge events
resource "aws_cloudwatch_log_group" "eventbridge_logs" {
  name              = "/aws/events/${local.name_prefix}-eventbridge"
  retention_in_days = var.log_retention_days
  tags = merge(local.common_tags, {
    Name         = "${local.name_prefix}-eventbridge-logs"
    ResourceType = "CloudWatch-LogGroup"
    LogType      = "EventBridge-Logs"
    Purpose      = "Schedule-Trigger-Events"
    Component    = "Logging"
  })
}

# ECS Cluster
resource "aws_ecs_cluster" "main" {
  name = "${local.name_prefix}-cluster"
  tags = merge(local.common_tags, {
    Name         = "${local.name_prefix}-cluster"
    ResourceType = "ECS-Cluster"
    Purpose      = "Scheduled-Task-Execution"
    Component    = "Compute"
  })

  setting {
    name  = "containerInsights"
    value = "enabled"
  }

  configuration {
    execute_command_configuration {
      logging = "OVERRIDE"
      log_configuration {
        cloud_watch_log_group_name = aws_cloudwatch_log_group.ecs_logs.name
      }
    }
  }
}

# ECS Task Definition
resource "aws_ecs_task_definition" "main" {
  family                   = "${local.name_prefix}-task"
  network_mode             = "awsvpc"
  requires_compatibilities = [var.cluster_config.launch_type]
  cpu                      = var.task_definition.cpu
  memory                   = var.task_definition.memory
  execution_role_arn       = aws_iam_role.ecs_task_execution.arn
  task_role_arn            = aws_iam_role.ecs_task.arn

  container_definitions = jsonencode([
    {
      name  = "${local.name_prefix}-container"
      image = local.container_image

      essential = true

      # Use the Dockerfile's CMD ["python", "app.py"]; no override needed.

      environment = concat([
        for key, value in var.task_definition.environment_variables : {
          name  = key
          value = value
        }
        ], [
        {
          name  = "LOG_LEVEL"
          value = "INFO"
        },
        {
          name  = "LOG_FORMAT"
          value = "json"
        },
        {
          name  = "TASK_FAMILY"
          value = "${local.name_prefix}-task"
        },
        {
          name  = "CLUSTER_NAME"
          value = "${local.name_prefix}-cluster"
        },
        {
          name  = "PROJECT_NAME"
          value = var.project_name
        },
        {
          name  = "ENVIRONMENT"
          value = var.environment
        }
      ])

      logConfiguration = {
        logDriver = "awslogs"
        options = merge({
          "awslogs-group"         = aws_cloudwatch_log_group.ecs_logs.name
          "awslogs-region"        = data.aws_region.current.name
          "awslogs-stream-prefix" = "ecs"
          }, var.enable_log_insights ? {
          "awslogs-create-group" = "true"
          "mode"                 = "non-blocking"
          "max-buffer-size"      = "25m"
        } : {})
      }
    }
  ])

  tags = merge(local.common_tags, {
    Name         = "${local.name_prefix}-task-definition"
    ResourceType = "ECS-TaskDefinition"
    Purpose      = "Scheduled-Task-Execution"
    Component    = "Compute"
  })

  # Ensure the image is built and pushed before the task definition is created
  # so the first scheduled invocation has an image to pull.
  depends_on = [null_resource.docker_build_push]
}

# Data source for current AWS region
data "aws_region" "current" {}

# Data source for default VPC
data "aws_vpc" "default" {
  default = true
}

# Data source for default VPC subnets
data "aws_subnets" "default" {
  filter {
    name   = "vpc-id"
    values = [data.aws_vpc.default.id]
  }
}

# Security Group for ECS tasks
resource "aws_security_group" "ecs_tasks" {
  name_prefix = "${local.name_prefix}-ecs-tasks"
  description = "Security group for ECS tasks in ${local.name_prefix}"
  vpc_id      = data.aws_vpc.default.id

  # Allow HTTPS outbound for pulling container images from ECR, sending logs to
  # CloudWatch, and reaching external HTTPS APIs used by the sample task.
  egress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "Allow HTTPS outbound for ECR, CloudWatch, and external APIs"
  }

  tags = merge(local.common_tags, {
    Name         = "${local.name_prefix}-ecs-tasks-sg"
    ResourceType = "Security-Group"
    Purpose      = "ECS-Task-Networking"
    Component    = "Security"
  })
}

# IAM Role for ECS Task Execution (used by ECS agent)
resource "aws_iam_role" "ecs_task_execution" {
  name = "${local.name_prefix}-task-execution-role"
  tags = merge(local.common_tags, {
    Name         = "${local.name_prefix}-task-execution-role"
    ResourceType = "IAM-Role"
    Purpose      = "ECS-Task-Execution"
    Component    = "Security"
  })

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "ecs-tasks.amazonaws.com"
        }
      }
    ]
  })
}

# IAM Policy for ECS Task Execution Role
resource "aws_iam_role_policy" "ecs_task_execution" {
  name = "${local.name_prefix}-task-execution-policy"
  role = aws_iam_role.ecs_task_execution.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "ecr:GetAuthorizationToken"
        ]
        Resource = "*"
      },
      {
        Effect = "Allow"
        Action = [
          "ecr:BatchCheckLayerAvailability",
          "ecr:GetDownloadUrlForLayer",
          "ecr:BatchGetImage"
        ]
        Resource = aws_ecr_repository.app.arn
      },
      {
        Effect = "Allow"
        Action = [
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ]
        Resource = "${aws_cloudwatch_log_group.ecs_logs.arn}:*"
      }
    ]
  })
}

# IAM Role for ECS Task (used by application code)
resource "aws_iam_role" "ecs_task" {
  name = "${local.name_prefix}-task-role"
  tags = merge(local.common_tags, {
    Name         = "${local.name_prefix}-task-role"
    ResourceType = "IAM-Role"
    Purpose      = "ECS-Task-Application"
    Component    = "Security"
  })

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "ecs-tasks.amazonaws.com"
        }
      }
    ]
  })
}

# IAM Policy for ECS Task Role (minimal permissions for application)
resource "aws_iam_role_policy" "ecs_task" {
  name = "${local.name_prefix}-task-policy"
  role = aws_iam_role.ecs_task.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ]
        Resource = "${aws_cloudwatch_log_group.ecs_logs.arn}:*"
      }
    ]
  })
}

# IAM Role for EventBridge to trigger ECS tasks
resource "aws_iam_role" "eventbridge_ecs" {
  name = "${local.name_prefix}-eventbridge-role"
  tags = merge(local.common_tags, {
    Name         = "${local.name_prefix}-eventbridge-role"
    ResourceType = "IAM-Role"
    Purpose      = "EventBridge-ECS-Trigger"
    Component    = "Security"
  })

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "events.amazonaws.com"
        }
      }
    ]
  })
}

# IAM Policy for EventBridge Role
resource "aws_iam_role_policy" "eventbridge_ecs" {
  name = "${local.name_prefix}-eventbridge-policy"
  role = aws_iam_role.eventbridge_ecs.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "ecs:RunTask"
        ]
        Resource = aws_ecs_task_definition.main.arn
      },
      {
        Effect = "Allow"
        Action = [
          "iam:PassRole"
        ]
        Resource = [
          aws_iam_role.ecs_task_execution.arn,
          aws_iam_role.ecs_task.arn
        ]
      }
    ]
  })
} # EventBridge Rule for scheduled execution
resource "aws_cloudwatch_event_rule" "ecs_schedule" {
  name                = "${local.name_prefix}-schedule"
  description         = "Trigger ECS task on schedule for ${var.project_name} in ${var.environment}"
  schedule_expression = var.schedule_expression
  tags = merge(local.common_tags, {
    Name         = "${local.name_prefix}-schedule"
    ResourceType = "EventBridge-Rule"
    Purpose      = "Scheduled-Task-Trigger"
    Component    = "Scheduling"
  })
}

# EventBridge Target - ECS Task
resource "aws_cloudwatch_event_target" "ecs_target" {
  rule      = aws_cloudwatch_event_rule.ecs_schedule.name
  target_id = "${local.name_prefix}-ecs-target"
  arn       = aws_ecs_cluster.main.arn
  role_arn  = aws_iam_role.eventbridge_ecs.arn

  ecs_target {
    task_count          = 1
    task_definition_arn = aws_ecs_task_definition.main.arn
    launch_type         = var.cluster_config.launch_type
    platform_version    = "LATEST"

    network_configuration {
      subnets          = length(var.cluster_config.subnet_ids) > 0 ? var.cluster_config.subnet_ids : data.aws_subnets.default.ids
      security_groups  = length(var.cluster_config.security_group_ids) > 0 ? var.cluster_config.security_group_ids : [aws_security_group.ecs_tasks.id]
      assign_public_ip = var.cluster_config.assign_public_ip
    }
  }

  retry_policy {
    maximum_retry_attempts       = var.retry_policy.maximum_retry_attempts
    maximum_event_age_in_seconds = var.retry_policy.maximum_event_age_in_seconds
  }
}


# Outputs
output "eventbridge_rule_arn" {
  description = "ARN of the EventBridge rule"
  value       = aws_cloudwatch_event_rule.ecs_schedule.arn
}

output "eventbridge_rule_name" {
  description = "Name of the EventBridge rule"
  value       = aws_cloudwatch_event_rule.ecs_schedule.name
}

output "ecs_cluster_arn" {
  description = "ARN of the ECS cluster"
  value       = aws_ecs_cluster.main.arn
}

output "ecs_task_definition_arn" {
  description = "ARN of the ECS task definition"
  value       = aws_ecs_task_definition.main.arn
}

output "cloudwatch_log_group_name" {
  description = "Name of the CloudWatch log group"
  value       = aws_cloudwatch_log_group.ecs_logs.name
}

output "eventbridge_log_group_name" {
  description = "Name of the EventBridge log group"
  value       = aws_cloudwatch_log_group.eventbridge_logs.name
}

output "ecr_repository_url" {
  description = "URL of the ECR repository that holds the application image"
  value       = aws_ecr_repository.app.repository_url
}

output "container_image" {
  description = "Fully-qualified image URI used by the ECS task definition"
  value       = local.container_image
}



