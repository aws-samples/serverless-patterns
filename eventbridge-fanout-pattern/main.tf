terraform {
  required_version = ">= 1.5"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

############################################################
# Variables
############################################################

variable "aws_region" {
  description = "AWS region for resources (e.g. us-east-1, us-west-2)"
  type        = string

  validation {
    condition     = can(regex("^[a-z]{2}-[a-z]+-[0-9]+$", var.aws_region))
    error_message = "Must be a valid AWS region (e.g. us-east-1, eu-west-2)."
  }
}

variable "prefix" {
  description = "Unique prefix for all resource names"
  type        = string

  validation {
    condition     = can(regex("^[a-z0-9][a-z0-9\\-]{1,20}$", var.prefix))
    error_message = "Prefix must be 2-21 lowercase alphanumeric characters or hyphens."
  }
}

variable "log_retention_days" {
  description = "CloudWatch log retention in days (0 = never expire)"
  type        = number
  default     = 14
}

############################################################
# Data Sources
############################################################

data "aws_caller_identity" "current" {}

############################################################
# 1. CUSTOM EVENT BUS (the fan-out hub)
############################################################

resource "aws_cloudwatch_event_bus" "scheduled_bus" {
  name = "${var.prefix}-scheduled-bus"
}

############################################################
# 2. TARGETS — Lambda (Python), SNS, SQS
############################################################

# --- Lambda ---

resource "aws_iam_role" "lambda_role" {
  name = "${var.prefix}-processor-lambda-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_basic" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# Create log group BEFORE the Lambda so Terraform owns it
resource "aws_cloudwatch_log_group" "processor_logs" {
  name              = "/aws/lambda/${var.prefix}-scheduled-processor"
  retention_in_days = var.log_retention_days
}

resource "aws_lambda_function" "processor" {
  function_name    = "${var.prefix}-scheduled-processor"
  role             = aws_iam_role.lambda_role.arn
  handler          = "processor.lambda_handler"
  runtime          = "python3.14"
  timeout          = 30
  memory_size      = 128
  filename         = "processor.zip"

  environment {
    variables = {
      PREFIX    = var.prefix
      ENV       = "production"
      LOG_LEVEL = "INFO"
    }
  }

  depends_on = [
    aws_cloudwatch_log_group.processor_logs,
    aws_iam_role_policy_attachment.lambda_basic,
  ]
}

# --- SNS ---

resource "aws_sns_topic" "alerts" {
  name = "${var.prefix}-scheduled-alerts"
}

# --- SQS ---

resource "aws_sqs_queue" "archive" {
  name = "${var.prefix}-scheduled-archive"
}

############################################################
# 3. EVENT RULES (fan-out from bus to targets)
############################################################

locals {
  event_pattern = jsonencode({
    source      = ["${var.prefix}.scheduler.fan-out"]
    detail-type = ["ScheduledTask"]
  })
}

# --- Rule #1 → Lambda ---

resource "aws_cloudwatch_event_rule" "process_rule" {
  name           = "${var.prefix}-process-scheduled-event"
  event_bus_name = aws_cloudwatch_event_bus.scheduled_bus.name
  event_pattern  = local.event_pattern
}

resource "aws_cloudwatch_event_target" "lambda_target" {
  rule           = aws_cloudwatch_event_rule.process_rule.name
  event_bus_name = aws_cloudwatch_event_bus.scheduled_bus.name
  target_id      = "${var.prefix}-send-to-lambda"
  arn            = aws_lambda_function.processor.arn
}

resource "aws_lambda_permission" "allow_eventbridge" {
  statement_id  = "AllowEventBridgeInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.processor.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.process_rule.arn
}

# --- Rule #2 → SNS ---

resource "aws_cloudwatch_event_rule" "notify_rule" {
  name           = "${var.prefix}-notify-scheduled-event"
  event_bus_name = aws_cloudwatch_event_bus.scheduled_bus.name
  event_pattern  = local.event_pattern
}

resource "aws_cloudwatch_event_target" "sns_target" {
  rule           = aws_cloudwatch_event_rule.notify_rule.name
  event_bus_name = aws_cloudwatch_event_bus.scheduled_bus.name
  target_id      = "${var.prefix}-send-to-sns"
  arn            = aws_sns_topic.alerts.arn
}

resource "aws_sns_topic_policy" "allow_eventbridge" {
  arn = aws_sns_topic.alerts.arn

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Sid       = "AllowEventBridgePublish"
      Effect    = "Allow"
      Principal = { Service = "events.amazonaws.com" }
      Action    = "sns:Publish"
      Resource  = aws_sns_topic.alerts.arn
      Condition = {
        ArnEquals = {
          "aws:SourceArn" = aws_cloudwatch_event_rule.notify_rule.arn
        }
      }
    }]
  })
}

# --- Rule #3 → SQS ---

resource "aws_cloudwatch_event_rule" "archive_rule" {
  name           = "${var.prefix}-archive-scheduled-event"
  event_bus_name = aws_cloudwatch_event_bus.scheduled_bus.name
  event_pattern  = local.event_pattern
}

resource "aws_cloudwatch_event_target" "sqs_target" {
  rule           = aws_cloudwatch_event_rule.archive_rule.name
  event_bus_name = aws_cloudwatch_event_bus.scheduled_bus.name
  target_id      = "${var.prefix}-send-to-sqs"
  arn            = aws_sqs_queue.archive.arn
}

resource "aws_sqs_queue_policy" "allow_eventbridge" {
  queue_url = aws_sqs_queue.archive.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Sid       = "AllowEventBridgeSend"
      Effect    = "Allow"
      Principal = { Service = "events.amazonaws.com" }
      Action    = "sqs:SendMessage"
      Resource  = aws_sqs_queue.archive.arn
      Condition = {
        ArnEquals = {
          "aws:SourceArn" = aws_cloudwatch_event_rule.archive_rule.arn
        }
      }
    }]
  })
}

############################################################
# 4. SCHEDULER → EVENT BUS (the single schedule)
############################################################

resource "aws_iam_role" "scheduler_role" {
  name = "${var.prefix}-scheduler-eventbridge-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = { Service = "scheduler.amazonaws.com" }
    }]
  })
}

resource "aws_iam_role_policy" "scheduler_put_events" {
  name = "${var.prefix}-put-events-policy"
  role = aws_iam_role.scheduler_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect   = "Allow"
      Action   = "events:PutEvents"
      Resource = aws_cloudwatch_event_bus.scheduled_bus.arn
    }]
  })
}

# Log group for scheduler (delivery logs)
resource "aws_cloudwatch_log_group" "scheduler_logs" {
  name              = "/aws/scheduler/${var.prefix}-fan-out"
  retention_in_days = var.log_retention_days
}

resource "aws_scheduler_schedule" "fan_out" {
  name                = "${var.prefix}-fan-out"
  schedule_expression = "rate(5 minutes)"

  flexible_time_window {
    mode = "OFF"
  }

  target {
    arn      = aws_cloudwatch_event_bus.scheduled_bus.arn
    role_arn = aws_iam_role.scheduler_role.arn

    eventbridge_parameters {
      source      = "${var.prefix}.scheduler.fan-out"
      detail_type = "ScheduledTask"
    }

    input = jsonencode({
      taskId  = "5-minute-job"
      prefix  = var.prefix
      message = "Triggered by EventBridge Scheduler"
    })
  }

  depends_on = [aws_cloudwatch_log_group.scheduler_logs]
}

############################################################
# 5. OUTPUTS
############################################################

output "prefix" {
  value = var.prefix
}

output "event_bus_name" {
  value = aws_cloudwatch_event_bus.scheduled_bus.name
}

output "event_bus_arn" {
  value = aws_cloudwatch_event_bus.scheduled_bus.arn
}

output "schedule_name" {
  value = aws_scheduler_schedule.fan_out.name
}

output "schedule_arn" {
  value = aws_scheduler_schedule.fan_out.arn
}

output "lambda_function_name" {
  value = aws_lambda_function.processor.function_name
}

output "sns_topic_arn" {
  value = aws_sns_topic.alerts.arn
}

output "sqs_queue_url" {
  value = aws_sqs_queue.archive.url
}