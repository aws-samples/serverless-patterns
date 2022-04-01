# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

# Variables
variable "queue_name" {}
variable "topic_arn" {}
variable "tags" {}

# Resources
resource "aws_sqs_queue" "queue" {
  name       = var.queue_name
  fifo_queue = true
  tags       = var.tags
}

data "aws_caller_identity" "current" {}

data "aws_iam_policy_document" "policy" {

  statement {
    effect = "Allow"
    actions = [
      "sqs:*"
    ]

    principals {
      type = "AWS"
      identifiers = [
        data.aws_caller_identity.current.account_id
      ]
    }

    resources = [
      aws_sqs_queue.queue.arn
    ]
  }

  statement {
    effect = "Allow"
    actions = [
      "sqs:SendMessage"
    ]

    principals {
      type        = "AWS"
      identifiers = ["*"]
    }

    condition {
      test     = "ArnEquals"
      variable = "aws:SourceArn"

      values = [
        var.topic_arn
      ]
    }

    resources = [
      aws_sqs_queue.queue.arn
    ]
  }

}

resource "aws_sqs_queue_policy" "policy" {
  queue_url = aws_sqs_queue.queue.id
  policy    = data.aws_iam_policy_document.policy.json
}


# Outputs
output "aws_sqs_queue_name" {
  value = aws_sqs_queue.queue.name
}

output "aws_sqs_queue_arn" {
  value = aws_sqs_queue.queue.arn
}
