terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
provider "aws" {
  profile = "default"
  region  = "us-east-1"
}


# Create DynamoDB table
resource "aws_dynamodb_table" "source" {
  name           = "demo_table"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "Id"

  attribute {
    name = "Id"
    type = "S"
  }

  stream_enabled   = true
  stream_view_type = "NEW_AND_OLD_IMAGES"
}

# Create SQS queue
resource "aws_sqs_queue" "target" {
  name = "demo_queue"
}

# Create EventBridge Pipe
resource "aws_pipes_pipe" "demo_pipe" {
  name     = "demo_pipe"
  role_arn = aws_iam_role.demo_role.arn
  source   = aws_dynamodb_table.source.stream_arn
  target   = aws_sqs_queue.target.arn
  source_parameters {
    dynamodb_stream_parameters {
      starting_position = "TRIM_HORIZON"
      batch_size = 1
    }
  }
}
# Create IAM role for EventBridge Pipe
resource "aws_iam_role" "demo_role" {
  name = "demo-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Sid    = "PipesPermissions"
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
        {
            "Sid": "dynamodbPermissions",
            "Effect": "Allow",
            "Action": [
                "dynamodb:DescribeStream",
                "dynamodb:GetRecords",
                "dynamodb:GetShardIterator",
                "dynamodb:ListStreams"
            ],
            "Resource": [
                aws_dynamodb_table.source.stream_arn
            ]
        },
        {
            "Sid": "sqsPermissions",
            "Effect": "Allow",
            "Action": [
                "sqs:SendMessage"
            ],
            "Resource": [
                aws_sqs_queue.target.arn
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

output "SQS_arn" {
  value       = aws_sqs_queue.target.id
  description = "The ARN of the SQS queue URL."
}

output "DynamoDB_arn" {
  value       = aws_dynamodb_table.source.arn
  description = "The ARN of the DynamoDB table."
}
