terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.57"
    }
  }

  required_version = ">= 0.14.9"
}

provider "aws" {
  profile = "default"
  region  = "us-east-1"
}

# Create a new eventbus for our demo
resource "aws_cloudwatch_event_bus" "custom_event_bus" {
  name = "MyCustomBus"
}

# need to create role and policy for scheduler to put events onto our bus
resource "aws_iam_role" "scheduler_role" {
  name = "delayed-eb-events-SchedulerRole"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = {
      Effect = "Allow"
      Action = "sts:AssumeRole"
      Principal = {
        Service = "scheduler.amazonaws.com"
      }
    }
  })

  inline_policy {
    name = "ScheduleToPutEvents"
    policy = jsonencode({
      Version = "2012-10-17"
      Statement = [
        {
          Effect = "Allow"
          Action = [
            "events:PutEvents",
          ],
          Resource = [aws_cloudwatch_event_bus.custom_event_bus.arn]
        },
      ]
    })
  }
}

# Creating scheduler group 
resource "aws_scheduler_schedule_group" "scheduler_schedule_group" {
  name = "SchedulesForUsers24HoursAfterCreation"
}

data "aws_iam_policy" "lambda_basic_execution_role_policy" {
  name = "AWSLambdaBasicExecutionRole"
}


# Listen to UserCreated and create the schedule
resource "aws_iam_role" "user_created_function_role" {
  name = "delayed-eb-events-UserCreatedFunctionRole"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = {
      Effect = "Allow"
      Action = "sts:AssumeRole"
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }
  })

  managed_policy_arns = [
    data.aws_iam_policy.lambda_basic_execution_role_policy.arn
  ]

  inline_policy {
    name = "CreateSchedule"
    policy = jsonencode({
      Version = "2012-10-17"
      Statement = [
        {
          Effect = "Allow"
          Action = [
            "scheduler:CreateSchedule",
            "iam:PassRole"
          ],
          Resource = ["*"]
        },
      ]
    })
  }
}

data "archive_file" "process_user_created_function_zip_file" {
  type        = "zip"
  source_file = "${path.module}/src/process-user-created/index.mjs"
  output_path = "${path.module}/process_user_created_function_payload.zip"
}

resource "aws_lambda_function" "process_user_created_lambda" {
  filename      = data.archive_file.process_user_created_function_zip_file.output_path
  function_name = "ProcessUserCreatedFunction"
  role          = aws_iam_role.user_created_function_role.arn
  handler       = "index.handler"

  source_code_hash = data.archive_file.process_user_created_function_zip_file.output_base64sha256

  runtime = "nodejs20.x"

  environment {
    variables = {
      SCHEDULE_ROLE_ARN = aws_iam_role.scheduler_role.arn,
      EVENTBUS_ARN      = aws_cloudwatch_event_bus.custom_event_bus.arn
    }
  }
}

# EventBridge rule to listen to UserCreated so we can process it and create schedule
resource "aws_cloudwatch_event_rule" "user_created_rule" {
  name        = "UserCreatedRule"
  description = "Listen to UseCreated events"

  event_pattern = jsonencode({
    source = ["myapp.users"],
    detail-type = [
      "UserCreated"
    ]
  })
  event_bus_name = aws_cloudwatch_event_bus.custom_event_bus.arn
}

resource "aws_cloudwatch_event_target" "user_created_rule_target" {
  rule           = aws_cloudwatch_event_rule.user_created_rule.name
  arn            = aws_lambda_function.process_user_created_lambda.arn
  event_bus_name = aws_cloudwatch_event_bus.custom_event_bus.name
}

resource "aws_lambda_permission" "allow_eventbridge" {
  statement_id  = "AllowExecutionFromEventBridge"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.process_user_created_lambda.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.user_created_rule.arn
}

# Function that listens to schedule directly onto EventBridge and "email a customer" as an example
resource "aws_iam_role" "email_customer_function_role" {
  name = "delayed-eb-events-EmailCustomerFunctionRole"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = {
      Effect = "Allow"
      Action = "sts:AssumeRole"
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }
  })

  managed_policy_arns = [
    data.aws_iam_policy.lambda_basic_execution_role_policy.arn
  ]
}

data "archive_file" "email_customer_function_zip_file" {
  type        = "zip"
  source_file = "${path.module}/src/email-customer/index.mjs"
  output_path = "${path.module}/email_customer_function_payload.zip"
}

resource "aws_lambda_function" "email_customer_lambda" {
  filename      = data.archive_file.email_customer_function_zip_file.output_path
  function_name = "EmailCustomerFunction"
  role          = aws_iam_role.email_customer_function_role.arn
  handler       = "index.handler"

  source_code_hash = data.archive_file.email_customer_function_zip_file.output_base64sha256

  runtime = "nodejs20.x"
}

# Rule to match schedules for users and attach our email customer lambda
resource "aws_cloudwatch_event_rule" "user_created_24hours_ago_rule" {
  name        = "UserCreated24HoursAgoRule"
  description = "Listen to UseCreated events"

  event_pattern = jsonencode({
    source = ["scheduler.notifications"],
    detail-type = [
      "UserCreated24HoursAgo"
    ]
  })
  event_bus_name = aws_cloudwatch_event_bus.custom_event_bus.arn
}

resource "aws_cloudwatch_event_target" "user_created_24hours_ago_rule_target" {
  rule           = aws_cloudwatch_event_rule.user_created_24hours_ago_rule.name
  arn            = aws_lambda_function.email_customer_lambda.arn
  event_bus_name = aws_cloudwatch_event_bus.custom_event_bus.name
}

resource "aws_lambda_permission" "allow_eventbridge_email_customer_lambda" {
  statement_id  = "AllowExecutionFromEventBridge"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.email_customer_lambda.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.user_created_24hours_ago_rule.arn
}

# Outputs
output "custom_event_bus_arn" {
  description = "Custom Event Bus ARN"
  value       = aws_cloudwatch_event_bus.custom_event_bus.arn
}

output "user_created_rule_arn" {
  description = "UserCreatedRule rule ARN"
  value       = aws_cloudwatch_event_rule.user_created_rule.arn
}

output "user_created_24hours_ago_rule_arn" {
  description = "UserCreated24HoursAgoRule rule ARN"
  value       = aws_cloudwatch_event_rule.user_created_24hours_ago_rule.arn
}

output "scheduler_group_name" {
  description = "SchedulesForUsers24HoursAfterCreation scheduler group name"
  value       = aws_scheduler_schedule_group.scheduler_schedule_group.name
}

output "process_user_created_lambda_function_log_group" {
  description = "ProcessUserCreatedFunction CloudWatch Log Group"
  value       = "/aws/lambda/${aws_lambda_function.process_user_created_lambda.function_name}"
}

output "email_customer_lambda_function_log_group" {
  description = "EmailCustomerFunction CloudWatch Log Group"
  value       = "/aws/lambda/${aws_lambda_function.email_customer_lambda.function_name}"
}


