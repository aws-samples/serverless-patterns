# Display the S3 bucket 
output "S3-Bucket" {
  value       = aws_s3_bucket.landing_bucket.id
  description = "The S3 Bucket"
}

output "lambda_function_name" {
  value = aws_lambda_function.first_glue_job_trigger_glue_workflow.function_name
}

output "cloudwatch_log_group" {
  value = aws_cloudwatch_log_group.lambda_demo_loggroup.name
}