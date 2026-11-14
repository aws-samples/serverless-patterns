provider "aws" {
  region = "us-east-1"
}

variable "rds_instance_name" {
  description = "Provide name of your existing RDS Instance for which you want to receive event notifications"
}

variable "sns_endpoint" {
  description = "Provide your email address to receive notification from SNS"
}

variable "aws_account_id" {
  description = "Your AWS Account ID"
}

resource "aws_sns_topic" "sns_for_rds_event_subscription" {
  name = "rds-subscription-topic"
}

resource "aws_sns_topic_subscription" "sns_subscription" {
  topic_arn = aws_sns_topic.sns_for_rds_event_subscription.arn
  protocol  = "email"
  endpoint  = var.sns_endpoint
}

resource "aws_sns_topic_policy" "sns_topic_policy" {
  arn    = aws_sns_topic.sns_for_rds_event_subscription.arn
  policy = jsonencode({
    Version   = "2012-10-17"
    Statement = [
      {
        Sid       = "__default_statement_ID"
        Effect    = "Allow"
        Principal = { AWS = var.aws_account_id }
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
        ]
        Resource = aws_sns_topic.sns_for_rds_event_subscription.arn
        Condition = {
          StringEquals = {
            "AWS:SourceOwner" = var.aws_account_id
          }
        }
      },
      {
        Sid       = "TrustRDSToPublishEventsToMyTopic"
        Effect    = "Allow"
        Principal = { Service = "events.rds.amazonaws.com" }
        Action    = "sns:Publish"
        Resource  = aws_sns_topic.sns_for_rds_event_subscription.arn
      },
    ]
  })
}

resource "aws_db_event_subscription" "rds_event_subscription" {
  name           = "RDS-Event-Subscription"
  sns_topic  = aws_sns_topic.sns_for_rds_event_subscription.arn
  source_ids     = [var.rds_instance_name]
  source_type    = "db-instance"
  event_categories = [
    "failure",
    "low storage",
    "availability",
  ]
}

output "sns_topic_name" {
  value       = aws_sns_topic.sns_for_rds_event_subscription.name
  description = "SNS topic name"
}

output "rds_instance_name" {
  value = var.rds_instance_name
}
