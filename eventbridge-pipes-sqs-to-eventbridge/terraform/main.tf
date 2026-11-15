terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
provider "aws" {}

# Create EventBus Target
resource "aws_cloudwatch_event_bus" "target" {
  name = "demo_bus"
}

# Create SQS Source
resource "aws_sqs_queue" "source" {
  name = "demo_queue"
}

# Create EventBridge Pipe
resource "aws_pipes_pipe" "demo_pipe" {
  name     = "demo_pipe"
  role_arn = aws_iam_role.demo_role.arn
  source   = aws_sqs_queue.source.arn
  target   = aws_cloudwatch_event_bus.target.arn
  source_parameters {
    sqs_queue_parameters {
      batch_size = 1
      maximum_batching_window_in_seconds = 2
    }
  filter_criteria {
      filter {
        pattern = jsonencode({
          "body":{"type":["NEW"]}
        })
      }
    }
  }
  target_parameters {
    eventbridge_event_bus_parameters {
      source = "myapp.demo"
    }
  }
}

# Create IAM role for EventBridge Pipe
resource "aws_iam_role" "demo_role" {
  name = "demo_role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Sid    = ""
        Principal = {
          Service = "pipes.amazonaws.com"
        }
      },
    ]
  })
}

# Create an IAM policy for EventBridge Pipe
resource "aws_iam_policy" "demo_policy" {
  name = "demo_policy"
  policy = jsonencode({
    "Version": "2012-10-17",
    "Statement": [
        {   "Sid": "SourcePermissions",
            "Effect": "Allow",
            "Action": [
                "sqs:ReceiveMessage",
                "sqs:DeleteMessage",
                "sqs:GetQueueAttributes"
            ],
            "Resource": [
                aws_sqs_queue.source.arn
            ]
        },
        {   "Sid": "TargetPermissions"
            "Effect": "Allow",
            "Action": [
                "events:PutEvents"
            ],
            "Resource": [
                aws_cloudwatch_event_bus.target.arn
            ]
        }
    ]
})

# Attach the IAM policy to the IAM role
}
resource "aws_iam_role_policy_attachment" "demo-attach" {
  role       = aws_iam_role.demo_role.name
  policy_arn = aws_iam_policy.demo_policy.arn
}

output "SQS_url" {
  value       = aws_sqs_queue.source.url
  description = "The URL of the SQS queue."
}

output "Pipes_arn" {
  value       = aws_pipes_pipe.demo_pipe.arn
  description = "The ARN of the Pipe."
}

