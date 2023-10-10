provider "aws" {
  region = "us-east-1"  # Set your desired AWS region here
}

variable "SNSEndpoint" {
  description = "Provide your email address to receive notification from SNS"
}

data "aws_caller_identity" "current" {}

resource "aws_cloudwatch_event_rule" "event_rule" {
  name        = "detect-secret-key-changes"
  description = "A CloudWatch Event Rule that detects changes to Secret Manager secret keys and publishes change events to an SNS topic for notification."
  event_pattern = jsonencode({
    detail_type: ["AWS API Call via CloudTrail"],
    detail: {
      eventSource: ["secretsmanager.amazonaws.com"],
      eventName: ["CreateSecret", "UpdateSecret", "GetSecretValue", "PutSecretValue"],
    },
  })
  is_enabled = true
}

resource "aws_sns_topic" "sns_topic" {
  name = "event-rule-action"
}

resource "aws_sns_topic_policy" "sns_topic_policy" {
  arn = aws_sns_topic.sns_topic.arn

  policy = jsonencode({
    Version = "2012-10-17",
    Id      = "__default_policy_ID",
    Statement = [
      {
        Sid       = "__default_statement_ID",
        Effect    = "Allow",
        Principal = "*",
        Action    = [
          "SNS:GetTopicAttributes",
          "SNS:SetTopicAttributes",
          "SNS:AddPermission",
          "SNS:RemovePermission",
          "SNS:DeleteTopic",
          "SNS:Subscribe",
          "SNS:ListSubscriptionsByTopic",
          "SNS:Publish",
          "SNS:Receive",
        ],
        Resource  = aws_sns_topic.sns_topic.arn,
        Condition = {
          StringEquals = {
            "AWS:SourceOwner" = data.aws_caller_identity.current.account_id,
          },
        },
      },
      {
        Sid       = "TrustCWEToPublishEventsToMyTopic",
        Effect    = "Allow",
        Principal = {
          Service = "events.amazonaws.com",
        },
        Action    = "sns:Publish",
        Resource  = aws_sns_topic.sns_topic.arn,
      },
    ],
  })
}

resource "aws_sns_topic_subscription" "sns_topic_subscription" {
  topic_arn = aws_sns_topic.sns_topic.arn
  protocol  = "email"
  endpoint  = var.SNSEndpoint
}

output "MySnsTopicName" {
  description = "SNS topic name"
  value       = aws_sns_topic.sns_topic.name
}

output "MySnsTopicArn" {
  description = "SNS topic ARN"
  value       = aws_sns_topic.sns_topic.arn
}
