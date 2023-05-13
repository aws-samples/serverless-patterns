terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.41.0"
    }
  }
}

provider "aws" {

}

data "aws_caller_identity" "current" {}


resource "aws_lambda_function" "eventbridge_function" {
  function_name = "EventBridgeScheduleTargetJava"
  filename      = "${path.module}/target/EventBridgeFunction-1.0.jar"
  handler       = "com.example.EventBridgeFunction::handleRequest"
  role          = aws_iam_role.iam_for_lambda.arn
  runtime       = "java11"
  memory_size   = 512
  timeout       = 30
}

resource "aws_iam_role" "scheduler_role" {
  name = "EventBridgeSchedulerRole"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "scheduler.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_role_policy" "eventbridge_invoke_policy" {
  name = "EventBridgeInvokeLambdaPolicy"
  role = aws_iam_role.scheduler_role.id
  policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Sid" : "AllowEventBridgeToInvokeLambda",
        "Action" : [
          "lambda:InvokeFunction"
        ],
        "Effect" : "Allow",
        "Resource" : aws_lambda_function.eventbridge_function.arn
      }
    ]
  })
}

resource "aws_iam_role" "iam_for_lambda" {
  name = "ScheduleTargetExecutionRole"
  assume_role_policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Action" : "sts:AssumeRole",
        "Principal" : {
          "Service" : "lambda.amazonaws.com"
        },
        "Effect" : "Allow",
        "Sid" : ""
      }
    ]
  })
}

resource "aws_iam_role_policy" "lambda_logs_policy" {
  name = "PublishLogsPolicy"
  role = aws_iam_role.iam_for_lambda.id
  policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Sid" : "AllowLambdaFunctionToCreateLogs",
        "Action" : [
          "logs:*"
        ],
        "Effect" : "Allow",
        "Resource" : [
          "arn:aws:logs:*:${data.aws_caller_identity.current.account_id}:log-group:/aws/lambda/${aws_lambda_function.eventbridge_function.function_name}:*"
        ]
      }
    ]
  })
}

resource "aws_scheduler_schedule" "invoke_lambda_schedule" {
  name = "InvokeLambdaSchedule"
  flexible_time_window {
    mode = "OFF"
  }
  schedule_expression = "rate(5 minute)"
  target {
    arn      = aws_lambda_function.eventbridge_function.arn
    role_arn = aws_iam_role.scheduler_role.arn
    input    = "{\"input\": \"This message was sent using EventBridge Scheduler!\"}"
  }
}

output "ScheduleTargetFunction" {
  value       = aws_lambda_function.eventbridge_function.arn
  description = "The ARN of the Lambda function being invoked from EventBridge Scheduler"
}

output "ScheduleName" {
  value       = aws_scheduler_schedule.invoke_lambda_schedule.name
  description = "Name of the EventBridge Schedule"
}
