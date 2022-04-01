# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

# Variable
variable "bucket_name" {}
variable "tags" {}

# Resources
resource "aws_s3_bucket" "bucket" {
  bucket        = var.bucket_name
  tags          = var.tags
  force_destroy = true

}

resource "aws_s3_bucket_acl" "acl" {
  bucket = aws_s3_bucket.bucket.id
  acl    = "private"
}

resource "aws_s3_bucket_public_access_block" "access" {
  bucket                  = aws_s3_bucket.bucket.id
  block_public_acls       = true
  block_public_policy     = true
  restrict_public_buckets = true
  ignore_public_acls      = true
}

# Outputs
output "aws_s3_bucket_arn" {
  value = aws_s3_bucket.bucket.arn
}
