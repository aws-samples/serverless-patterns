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

# Source SQS
resource "aws_sqs_queue" "source_queue" {
  name = "eb-pipes-sqs-sf-SourceQueue"
  redrive_policy = jsonencode({
    deadLetterTargetArn = aws_sqs_queue.source_queue_dlq.arn
    maxReceiveCount     = 5
  })
}

# DLQ for source
resource "aws_sqs_queue" "source_queue_dlq" {
  name = "eb-pipes-sqs-sf-SourceQueueDLQ"
}

#Log Group for StepFunction
resource "aws_cloudwatch_log_group" "target_state_machine_log_group" {
  name              = "sqs-pipes-sf/StateMachine"
  retention_in_days = 7
}

#Execution Role for StepFunction
resource "aws_iam_role" "target_state_machine_role" {
  name = "eb-pipes-sqs-sf-TargetStateMachineRole"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = {
      Effect = "Allow"
      Action = "sts:AssumeRole"
      Principal = {
        Service = "states.amazonaws.com"
      }
    }
  })

  inline_policy {
    name = "CloudWatchLogs"
    policy = jsonencode({
      Version = "2012-10-17"
      Statement = [
        {
          Effect = "Allow"
          Action = [
            "logs:CreateLogDelivery",
            "logs:GetLogDelivery",
            "logs:UpdateLogDelivery",
            "logs:DeleteLogDelivery",
            "logs:ListLogDeliveries",
            "logs:PutResourcePolicy",
            "logs:DescribeResourcePolicies",
            "logs:DescribeLogGroups",
          ],
          Resource = ["*"]
        },
      ]
    })
  }
}

# Target Step Function State Machine
resource "aws_sfn_state_machine" "target_state_machine" {
  name       = "eb-pipes-sqs-sf-TargetStateMachine"
  role_arn   = aws_iam_role.target_state_machine_role.arn
  type       = "EXPRESS"
  definition = templatefile("workflow/sqs-pipes-sfn.asl.json", {})
  logging_configuration {
    log_destination        = "${aws_cloudwatch_log_group.target_state_machine_log_group.arn}:*"
    include_execution_data = true
    level                  = "ALL"
  }
}


# Role for EventBridge Pipes to read from SQS and launch SFN
resource "aws_iam_role" "event_bridge_pipes_role" {
  name = "eb-pipes-sqs-sf-EventBridgePipesRole"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = {
      Effect = "Allow"
      Action = "sts:AssumeRole"
      Principal = {
        Service = "pipes.amazonaws.com"
      }
    }
  })

  inline_policy {
    name = "CloudWatchLogs"
    policy = jsonencode({
      Version = "2012-10-17"
      Statement = [
        {
          Effect = "Allow"
          Action = [
            "logs:CreateLogGroup",
            "logs:CreateLogStream",
            "logs:PutLogEvents"
          ],
          Resource = ["*"]
        },
      ]
    })
  }
  inline_policy {
    name = "ReadSQS"
    policy = jsonencode({
      Version = "2012-10-17"
      Statement = [
        {
          Effect = "Allow"
          Action = [
            "sqs:ReceiveMessage",
            "sqs:DeleteMessage",
            "sqs:GetQueueAttributes"
          ],
          Resource = [aws_sqs_queue.source_queue.arn, ]
        },
      ]
    })
  }
  inline_policy {
    name = "ExecuteSFN"
    policy = jsonencode({
      Version = "2012-10-17"
      Statement = [
        {
          Effect = "Allow"
          Action = [
            "states:StartExecution"
          ],
          Resource = [aws_sfn_state_machine.target_state_machine.arn, ]
        },
      ]
    })
  }
}

# EventBridge Pipes
resource "aws_pipes_pipe" "sqs_to_sfn" {
  name     = "SqsToSfnPipe"
  role_arn = aws_iam_role.event_bridge_pipes_role.arn
  source   = aws_sqs_queue.source_queue.arn
  source_parameters {
    sqs_queue_parameters {
      batch_size = 1
    }
  }
  target = aws_sfn_state_machine.target_state_machine.arn
  target_parameters {
    step_function_state_machine_parameters {
      invocation_type = "FIRE_AND_FORGET"
    }
  }
}

# Outputs
output "source_queue_url" {
  description = "Source SQS Queue URL"
  value       = aws_sqs_queue.source_queue.id
}
output "sfn_log_group_arn" {
  description = "StepFunctions LogGroup ARN"
  value       = aws_cloudwatch_log_group.target_state_machine_log_group.arn
}