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

# Create new SNS topic
resource "aws_sns_topic" "MySNSTopic" {
}

# Create SNS topic policy to allow Eventbridge to publish to the SNS topic
resource "aws_sns_topic_policy" "default" {
  arn    = aws_sns_topic.MySNSTopic.arn
  policy = <<POLICY
{
  "Version": "2008-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "events.amazonaws.com"
      },
      "Action": "sns:Publish",
      "Resource": "${aws_sns_topic.MySNSTopic.arn}",
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

# Create a new event bridge Rule
resource "aws_cloudwatch_event_rule" "MyEventRule" {
  event_pattern = <<PATTERN
{
  "account": ["${data.aws_caller_identity.current.account_id}"],
  "source": ["demo.sns"]
}
PATTERN
}

# Set the SNS topic as a target to the EventBridge rule.
resource "aws_cloudwatch_event_target" "MyRuleTarget" {
  rule = aws_cloudwatch_event_rule.MyEventRule.name
  arn  = aws_sns_topic.MySNSTopic.arn
}

# display the Name and ARN of the SNS topic
output "SNS-Topic" {
  value       = aws_sns_topic.MySNSTopic.name
  description = "The SNS Topic Name"
}

output "SNS-Topic-ARN" {
  value       = aws_sns_topic.MySNSTopic.arn
  description = "The SNS Topic ARN"
}
