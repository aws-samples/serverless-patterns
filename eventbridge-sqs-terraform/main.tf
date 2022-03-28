terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }
  }

  required_version = ">= 0.14.9"
}

provider "aws" {
  profile = "default"
  region  = "us-east-1"
}

data "aws_caller_identity" "current" {}

# Create new SQS Queue
resource "aws_sqs_queue" "MySQSqueue" {
}

# Create a new EventBridge Rule
resource "aws_cloudwatch_event_rule" "MyEventRule" {
  event_pattern = <<PATTERN
{
  "account": ["${data.aws_caller_identity.current.account_id}"],
  "source": ["demo.sqs"]
}
PATTERN
}

# Set the SQS as a target to the EventBridge Rule
resource "aws_cloudwatch_event_target" "MyRuleTarget" {
  rule = aws_cloudwatch_event_rule.MyEventRule.name
  arn  = aws_sqs_queue.MySQSqueue.arn
}

# Allow the EventBridge to send messages to the SQS queue.
resource "aws_sqs_queue_policy" "test" {
  queue_url = aws_sqs_queue.MySQSqueue.id
  policy    = <<POLICY
{
  "Version": "2012-10-17",
  "Id": "sqspolicy",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "events.amazonaws.com"
      },
      "Action": "sqs:SendMessage",
      "Resource": "${aws_sqs_queue.MySQSqueue.arn}",
      "Condition": {
        "ArnEquals": {
          "aws:SourceArn": "${aws_cloudwatch_event_rule.MyEventRule.arn}"
        }
      }
    }
  ]
}
POLICY
}

# Display the SQS queue URL
output "SQS-QUEUE" {
  value       = aws_sqs_queue.MySQSqueue.id
  description = "The SQS Queue URL"
}
