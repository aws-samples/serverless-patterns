/* Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. */

# --- modules/s3/outputs.tf ---

# S3 Bucket id
output "bucket_id" {
    value       = aws_s3_bucket.kinesis_analytics_flink_application_bucket.id
    description = "Output of s3 bucket id"
}

# S3 Bucket arn
output "bucket_arn" {
    value       = aws_s3_bucket.kinesis_analytics_flink_application_bucket.arn
    description = "Output of s3 bucket arn"
}

# S3 Object Key
output "file_key" {
    value       = aws_s3_object.kinesis_analytics_flink_application.key
    description = "Kinesis Flink Application - Object Key"
}
