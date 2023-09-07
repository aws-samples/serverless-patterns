/* Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. */

# --- modules/s3/main.tf ---

# Random number generator
resource "random_id" "random_generator" {
    byte_length = 8
}

# Create the Amazon S3 Destination Bucket for Kinesis Data Streams
resource "aws_s3_bucket" "s3_destination_bucket" {
    bucket        = "s3-destination-bucket-${random_id.random_generator.hex}"
    force_destroy = true
}

# S3 Destination Bucket - block public access
resource "aws_s3_bucket_public_access_block" "s3_destination_bucket_acl" {
    bucket                  = aws_s3_bucket.s3_destination_bucket.id
    block_public_acls       = true
    block_public_policy     = true
    ignore_public_acls      = true
    restrict_public_buckets = true
}