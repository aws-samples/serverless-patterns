terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.32.0"
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

variable "ses_identity_arn" {
  description = "ARN of the verified SES identity (email or domain) used as the sender (e.g. arn:aws:ses:us-east-1:123456789012:identity/noreply@example.com)"
  type        = string

  validation {
    condition     = can(regex("^arn:aws:ses:[a-z0-9-]+:[0-9]{12}:identity/.+$", var.ses_identity_arn))
    error_message = "Must be a valid SES identity ARN (e.g. arn:aws:ses:us-east-1:123456789012:identity/noreply@example.com)."
  }
}

variable "sender_email" {
  description = "Verified SES sender email address (must match the SES identity)"
  type        = string

  validation {
    condition     = can(regex("^[^@]+@[^@]+\\.[^@]+$", var.sender_email))
    error_message = "Must be a valid email address."
  }
}

variable "schedule_expression" {
  description = "EventBridge Scheduler expression (e.g. rate(1 hour), rate(5 minutes) for testing)"
  type        = string
  default     = "rate(1 hour)"
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
data "aws_region" "current" {}

############################################################
# 1. DYNAMODB TABLE (abandoned cart records)
#
# NOTE: hash_key is deprecated in the AWS provider and will
# be replaced by a key_schema block in a future major
# version. The replacement syntax is not yet available in
# the 5.x provider, so hash_key is used here. The
# deprecation warning can be safely ignored.
############################################################

resource "aws_dynamodb_table" "abandoned_carts" {
  name         = "${var.prefix}-abandoned-carts"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "CustomerId"

  attribute {
    name = "CustomerId"
    type = "S"
  }

  attribute {
    name = "CartAbandoned"
    type = "S"
  }

  # GSI to efficiently query only abandoned carts
  global_secondary_index {
    name            = "CartAbandonedIndex"
    hash_key        = "CartAbandoned"
    projection_type = "ALL"
  }

  tags = {
    Project = "${var.prefix}-abandoned-cart-notifications"
  }

  server_side_encryption {
    enabled = true
  }
}

# ── Seed test data ──

resource "aws_dynamodb_table_item" "test_user_abandoned" {
  table_name = aws_dynamodb_table.abandoned_carts.name
  hash_key   = aws_dynamodb_table.abandoned_carts.hash_key

  item = jsonencode({
    CustomerId = { S = "cust-001" }
    Email      = { S = "recipient@example.com" }
    CustomerName    = { S = "Jane Doe" }
    CartAbandoned   = { S = "true" }
    NotificationSent = { S = "false" }
    CartItems = { L = [
      { M = { ItemName = { S = "Wireless Headphones" }, Price = { N = "79.99" } } },
      { M = { ItemName = { S = "Phone Case" }, Price = { N = "19.99" } } }
    ] }
    CartTotal       = { N = "99.98" }
    CartAbandonedAt = { S = "2025-01-15T08:30:00Z" }
  })
}

resource "aws_dynamodb_table_item" "test_user_active" {
  table_name = aws_dynamodb_table.abandoned_carts.name
  hash_key   = aws_dynamodb_table.abandoned_carts.hash_key

  item = jsonencode({
    CustomerId = { S = "cust-002" }
    Email      = { S = "activecustomer@example.com" }
    CustomerName    = { S = "Active Customer" }
    CartAbandoned   = { S = "false" }
    NotificationSent = { S = "false" }
    CartItems = { L = [
      { M = { ItemName = { S = "Laptop Stand" }, Price = { N = "49.99" } } }
    ] }
    CartTotal       = { N = "49.99" }
    CartAbandonedAt = { S = "N/A" }
  })
}

resource "aws_dynamodb_table_item" "test_user_already_notified" {
  table_name = aws_dynamodb_table.abandoned_carts.name
  hash_key   = aws_dynamodb_table.abandoned_carts.hash_key

  item = jsonencode({
    CustomerId = { S = "cust-003" }
    Email      = { S = "alreadynotified@example.com" }
    CustomerName    = { S = "Already Notified" }
    CartAbandoned   = { S = "true" }
    NotificationSent = { S = "true" }
    CartItems = { L = [
      { M = { ItemName = { S = "USB Cable" }, Price = { N = "12.99" } } }
    ] }
    CartTotal       = { N = "12.99" }
    CartAbandonedAt = { S = "2025-01-14T10:00:00Z" }
  })
}

############################################################
# 2. NOTIFICATION PROCESSOR LAMBDA
############################################################

resource "aws_iam_role" "processor_role" {
  name = "${var.prefix}-notification-processor-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "processor_basic" {
  role       = aws_iam_role.processor_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_iam_role_policy" "processor_dynamodb" {
  name = "${var.prefix}-processor-dynamodb"
  role = aws_iam_role.processor_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Sid    = "DynamoDBReadWrite"
      Effect = "Allow"
      Action = [
        "dynamodb:Scan",
        "dynamodb:Query",
        "dynamodb:GetItem",
        "dynamodb:UpdateItem"
      ]
      Resource = [
        aws_dynamodb_table.abandoned_carts.arn,
        "${aws_dynamodb_table.abandoned_carts.arn}/index/*"
      ]
    }]
  })
}

resource "aws_iam_role_policy" "processor_ses" {
  name = "${var.prefix}-processor-ses"
  role = aws_iam_role.processor_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Sid      = "SendEmail"
      Effect   = "Allow"
      Action   = "ses:SendEmail"
      Resource = var.ses_identity_arn
    }]
  })
}

resource "aws_cloudwatch_log_group" "processor_logs" {
  name              = "/aws/lambda/${var.prefix}-notification-processor"
  retention_in_days = var.log_retention_days
}

data "archive_file" "processor_zip" {
  type        = "zip"
  source_file = "${path.module}/notification_processor.py"
  output_path = "${path.module}/notification_processor.zip"
}

resource "aws_lambda_function" "processor" {
  function_name    = "${var.prefix}-notification-processor"
  role             = aws_iam_role.processor_role.arn
  handler          = "notification_processor.lambda_handler"
  runtime          = "python3.14"
  timeout          = 60
  memory_size      = 256
  filename         = data.archive_file.processor_zip.output_path
  source_code_hash = data.archive_file.processor_zip.output_base64sha256

  environment {
    variables = {
      DYNAMODB_TABLE   = aws_dynamodb_table.abandoned_carts.name
      SES_IDENTITY_ARN = var.ses_identity_arn
      SENDER_EMAIL     = var.sender_email
      PREFIX           = var.prefix
    }
  }

  depends_on = [
    aws_cloudwatch_log_group.processor_logs,
    aws_iam_role_policy_attachment.processor_basic,
    aws_iam_role_policy.processor_dynamodb,
    aws_iam_role_policy.processor_ses,
  ]
}

############################################################
# 3. SQS DEAD-LETTER QUEUE
############################################################

resource "aws_sqs_queue" "scheduler_dlq" {
  name                       = "${var.prefix}-cart-notify-dlq"
  message_retention_seconds  = 1209600 # 14 days
  sqs_managed_sse_enabled    = true
}

############################################################
# 4. EVENTBRIDGE SCHEDULER
############################################################

resource "aws_iam_role" "scheduler_role" {
  name = "${var.prefix}-cart-notify-scheduler-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = { Service = "scheduler.amazonaws.com" }
    }]
  })
}

resource "aws_iam_role_policy" "scheduler_permissions" {
  name = "${var.prefix}-scheduler-permissions"
  role = aws_iam_role.scheduler_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid      = "InvokeLambda"
        Effect   = "Allow"
        Action   = "lambda:InvokeFunction"
        Resource = aws_lambda_function.processor.arn
      },
      {
        Sid      = "SendToDLQ"
        Effect   = "Allow"
        Action   = "sqs:SendMessage"
        Resource = aws_sqs_queue.scheduler_dlq.arn
      }
    ]
  })
}

resource "aws_sqs_queue_policy" "allow_scheduler" {
  queue_url = aws_sqs_queue.scheduler_dlq.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Sid       = "AllowSchedulerSendMessage"
      Effect    = "Allow"
      Principal = { Service = "scheduler.amazonaws.com" }
      Action    = "sqs:SendMessage"
      Resource  = aws_sqs_queue.scheduler_dlq.arn
      Condition = {
        ArnEquals = {
          "aws:SourceArn" = "arn:aws:scheduler:${var.aws_region}:${data.aws_caller_identity.current.account_id}:schedule/default/${var.prefix}-abandoned-cart-notify"
        }
      }
    }]
  })
}

resource "aws_cloudwatch_log_group" "scheduler_logs" {
  name              = "/aws/scheduler/${var.prefix}-abandoned-cart-notify"
  retention_in_days = var.log_retention_days
}

resource "aws_scheduler_schedule" "abandoned_cart_notify" {
  name                = "${var.prefix}-abandoned-cart-notify"
  schedule_expression = var.schedule_expression

  flexible_time_window {
    mode = "OFF"
  }

  target {
    arn      = aws_lambda_function.processor.arn
    role_arn = aws_iam_role.scheduler_role.arn

    input = jsonencode({
      source    = "eventbridge-scheduler"
      taskType  = "abandoned-cart-notification"
      invokedAt = "REPLACED_AT_RUNTIME"
    })

    retry_policy {
      maximum_retry_attempts       = 3
      maximum_event_age_in_seconds = 3600
    }

    dead_letter_config {
      arn = aws_sqs_queue.scheduler_dlq.arn
    }
  }

  depends_on = [aws_cloudwatch_log_group.scheduler_logs]
}

############################################################
# 5. OUTPUTS
############################################################

output "prefix" {
  value = var.prefix
}

output "schedule_name" {
  value = aws_scheduler_schedule.abandoned_cart_notify.name
}

output "schedule_arn" {
  value = aws_scheduler_schedule.abandoned_cart_notify.arn
}

output "lambda_function_name" {
  value = aws_lambda_function.processor.function_name
}

output "dynamodb_table_name" {
  value = aws_dynamodb_table.abandoned_carts.name
}

output "dlq_queue_url" {
  value = aws_sqs_queue.scheduler_dlq.url
}

output "ses_identity_arn" {
  value = var.ses_identity_arn
}

output "sender_email" {
  value = var.sender_email
}