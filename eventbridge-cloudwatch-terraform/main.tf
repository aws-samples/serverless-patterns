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

# Create a Log Group for Eventbridge to push logs to
resource "aws_cloudwatch_log_group" "MyLogGroup" {
  name_prefix = "/aws/events/terraform"
}

# Create a Log Policy to allow Cloudwatch to Create log streams and put logs
resource "aws_cloudwatch_log_resource_policy" "MyCloudWatchLogPolicy" {
  policy_name     = "Terraform-CloudWatchLogPolicy-${data.aws_caller_identity.current.account_id}"
  policy_document = <<POLICY
{
  "Version": "2012-10-17",
  "Id": "CWLogsPolicy",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": [ 
          "events.amazonaws.com",
          "delivery.logs.amazonaws.com"
          ]
      },
      "Action": [
        "logs:CreateLogStream",
        "logs:PutLogEvents"
        ],
      "Resource": "${aws_cloudwatch_log_group.MyLogGroup.arn}",
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

#Create a new Event Rule
resource "aws_cloudwatch_event_rule" "MyEventRule" {
  event_pattern = <<PATTERN
{
  "account": ["${data.aws_caller_identity.current.account_id}"],
  "source": ["demo.logs"]
}
PATTERN
}

#Set the log group as a target for the Eventbridge rule
resource "aws_cloudwatch_event_target" "MyRuleTarget" {
  rule = aws_cloudwatch_event_rule.MyEventRule.name
  arn  = aws_cloudwatch_log_group.MyLogGroup.arn
}

#output the CloudWatch Log Stream Name
output "CW-Logs-Stream-Name" {
  value       = aws_cloudwatch_log_group.MyLogGroup.id
  description = "The CloudWatch Log Group Name"
}