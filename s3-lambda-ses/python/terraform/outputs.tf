# Output value definitions

output "lambda_arn" {
  description = "Lambda"
  value = aws_lambda_function.test_lambda.arn
}

output "s3_bucket" {
    description = "S3_bucket"
    value = aws_s3_bucket.newbucket.id
}