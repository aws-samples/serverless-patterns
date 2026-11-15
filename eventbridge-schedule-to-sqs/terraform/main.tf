terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.22"
    }
  }
  required_version = ">= 0.14.9"
}

provider "aws" {
  profile = "default"
  region  = "us-east-1"
}

data "aws_caller_identity" "current" {}

# Create new IAM Policy and Role for EventBridge Scheduler
resource "aws_iam_policy" "sqs_access_policy" {
  name        = "sqs-access-policy"
  description = "Policy for EventBridge Scheduler to send messages to SQS"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "sqs:ReceiveMessage",
          "sqs:DeleteMessage",
          "sqs:SendMessage",
          "sqs:GetQueueAttributes",
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ],
        Effect   = "Allow"
        Resource = "${aws_sqs_queue.my_sqs_queue.arn}"
      }
    ]
  })
}

resource "aws_iam_role" "eventbridge_scheduler_iam_role" {
  name_prefix         = "eb-scheduler-role-"
  managed_policy_arns = [aws_iam_policy.sqs_access_policy.arn]
  path = "/"
  assume_role_policy  = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "scheduler.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
EOF
}

# Create new SQS Queue
resource "aws_sqs_queue" "my_sqs_queue" {
    name = "my-sqs-queue"
}

# Create new Eventbridge Scheduler
resource "aws_scheduler_schedule" "my_scheduler" {
  name = "my-scheduler"

  flexible_time_window {
    mode = "OFF"
  }

  schedule_expression = "rate(1 minutes)"

  target {
    arn      = "arn:aws:scheduler:::aws-sdk:sqs:sendMessage"
    role_arn = aws_iam_role.eventbridge_scheduler_iam_role.arn

    input = jsonencode({
      MessageBody = "Hello, ServerlessLand!"
      QueueUrl    = aws_sqs_queue.my_sqs_queue.url
    })
  }
}

output "EventBridgeSchedulerArn" {
  value       = aws_scheduler_schedule.my_scheduler.arn
  description = "EventBridge my-scheduler ARN"
}

output "SQSQueueArn" {
      value       = aws_sqs_queue.my_sqs_queue.arn
  description = "SQS Queue my-sqs-queue ARN"
}

