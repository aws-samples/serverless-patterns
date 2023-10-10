# Input variable definitions

variable "aws_region" {
  description = "AWS region for all resources."
  type    = string
  default = "us-east-1"
}

variable "s3_bucket_prefix" {
  description = "S3 bucket prefix for lambda code"
  type = string
  default = "apigw-http-api-lambda"
  
}

variable "lambda_name" {
  description = "name of lambda function"
  type = string
  default = "test_apigw_integration"
}

variable "lambda_log_retention" {
  description = "lambda log retention in days"
  type = number
  default = 7
}

variable "apigw_log_retention" {
  description = "api gwy log retention in days"
  type = number
  default = 7
}
