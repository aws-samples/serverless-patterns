variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "table_name" {
  description = "DynamoDB table name"
  type        = string
  default     = "source-table"
}

variable "s3_bucket_name" {
  description = "S3 bucket name for data export"
  type        = string
  default     = "glue-zero-etl-bucket"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "dev"
}
