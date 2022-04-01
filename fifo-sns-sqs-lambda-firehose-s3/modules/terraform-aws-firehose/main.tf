# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

# Variables
variable "stream_name" {}
variable "destination" {}
variable "bucket_arn" {}
variable "buffer_size" { default = null }
variable "buffer_interval" { default = null }
variable "role_name" {}
variable "policy_name" {}
variable "tags" {}

# Resources
resource "aws_kinesis_firehose_delivery_stream" "stream" {
  name        = var.stream_name
  destination = var.destination


  extended_s3_configuration {
    role_arn        = aws_iam_role.firehose_role.arn
    bucket_arn      = var.bucket_arn
    buffer_size     = var.buffer_size != null ? var.buffer_size : 1
    buffer_interval = var.buffer_interval != null ? var.buffer_interval : 60
  }
}

data "aws_iam_policy_document" "firehose_s3_policy" {

  statement {
    effect = "Allow"
    actions = [
      "s3:AbortMultipartUpload",
      "s3:GetBucketLocation",
      "s3:GetObject",
      "s3:ListBucket",
      "s3:ListBucketMultipartUploads",
      "s3:PutObject"
    ]
    resources = [
      "${var.bucket_arn}/*",
      var.bucket_arn
    ]
  }

}

data "aws_iam_policy_document" "firehose_role_policy" {
  statement {
    effect = "Allow"
    actions = [
      "sts:AssumeRole"
    ]
    principals {
      type        = "Service"
      identifiers = ["firehose.amazonaws.com"]
    }
  }
}

resource "aws_iam_policy" "firehose_policy" {
  name   = var.policy_name
  policy = data.aws_iam_policy_document.firehose_s3_policy.json
  tags   = var.tags
}

resource "aws_iam_role" "firehose_role" {
  name               = var.role_name
  tags               = var.tags
  assume_role_policy = data.aws_iam_policy_document.firehose_role_policy.json
}

resource "aws_iam_role_policy_attachment" "firehose_attachement" {
  role       = aws_iam_role.firehose_role.name
  policy_arn = aws_iam_policy.firehose_policy.arn
}


# Outputs
output "aws_firehose_delivery_stream_arn" {
  value = aws_kinesis_firehose_delivery_stream.stream.arn
}

output "aws_firehose_policy_name" {
  value = aws_iam_policy.firehose_policy.name
}

output "aws_firehose_policy_arn" {
  value = aws_iam_policy.firehose_policy.arn
}

output "aws_firehose_role_name" {
  value = aws_iam_role.firehose_role.name
}

output "aws_firehose_role_arn" {
  value = aws_iam_role.firehose_role.arn
}
