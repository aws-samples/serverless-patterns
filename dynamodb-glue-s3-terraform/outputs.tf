output "dynamodb_table_name" {
  description = "Name of the DynamoDB table"
  value       = aws_dynamodb_table.source_table.name
}

output "s3_bucket_name" {
  description = "Name of the S3 bucket"
  value       = aws_s3_bucket.data_bucket.bucket
}

output "glue_job_name" {
  description = "Name of the Glue job"
  value       = aws_glue_job.zero_etl_job.name
}

output "glue_database_name" {
  description = "Name of the Glue database"
  value       = aws_glue_catalog_database.zero_etl_database.name
}

output "iam_role_arn" {
  description = "ARN of the IAM role for Glue"
  value       = aws_iam_role.glue_zero_etl_role.arn
}
