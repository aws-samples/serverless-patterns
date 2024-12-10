variable "table_name" {
  description = "Name of the DynamoDB table"
  type        = string
  default = "test"
}

variable "hash_key" {
  description = "Hash key for the DynamoDB table"
  type        = string
  default     = "UserId"
}

variable "project" {
  description = "Project name"
  type        = string
  default     = "s3-lambda-dynamodb-terraform"
}