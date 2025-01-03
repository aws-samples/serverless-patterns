variable "bucket_name" {
  description = "Name of the S3 bucket for website hosting"
  type        = string
  default     = "json-store"
}

variable "table_name" {
  type        = string
  description = "Name of the DynamoDB table"
}

variable "project" {
  description = "Project name"
  type        = string
  default     = "s3-lambda-dynamodb-terraform"
}