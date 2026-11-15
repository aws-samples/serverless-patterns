# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

# Variables
variable "topic_name" {}
variable "queue_arn" {}
variable "tags" {}

# Resources
data "aws_caller_identity" "current" {}

resource "aws_sns_topic" "topic" {
  name         = var.topic_name
  display_name = split(".", var.topic_name)[0]
  fifo_topic   = true
  tags         = var.tags
}

data "aws_iam_policy_document" "policy" {
  statement {
    effect = "Allow"
    actions = [
      "SNS:GetTopicAttributes",
      "SNS:SetTopicAttributes",
      "SNS:AddPermission",
      "SNS:RemovePermission",
      "SNS:DeleteTopic",
      "SNS:Subscribe",
      "SNS:ListSubscriptionsByTopic",
      "SNS:Publish"
    ]

    condition {
      test     = "StringEquals"
      variable = "AWS:SourceOwner"

      values = [
        data.aws_caller_identity.current.account_id
      ]
    }

    principals {
      type        = "AWS"
      identifiers = ["*"]
    }

    resources = [
      aws_sns_topic.topic.arn
    ]
  }
}

resource "aws_sns_topic_policy" "policy" {
  arn    = aws_sns_topic.topic.arn
  policy = data.aws_iam_policy_document.policy.json
}

resource "aws_sns_topic_subscription" "sqs_to_sns_subscription" {
  topic_arn = aws_sns_topic.topic.arn
  protocol  = "sqs"
  endpoint  = var.queue_arn
}

# Outputs
output "aws_sns_topic_name" {
  value = aws_sns_topic.topic.name
}

output "aws_sns_topic_arn" {
  value = aws_sns_topic.topic.arn
}
