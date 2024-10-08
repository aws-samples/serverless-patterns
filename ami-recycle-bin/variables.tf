variable "region" {
  type        = string
  default     = "us-east-2"
  description = "AWS region where Terraform will manage the infrastructure"
}

variable "rbin_retention_period_value" {
  type        = number
  default     = 30
  description = "The period value for which the retention rule is to retain resources"
}

variable "rbin_retention_period_unit" {
  type        = string
  default     = "DAYS"
  description = "The unit of time in which the retention period is measured. Currently, only DAYS is supported"
}

variable "resource_tag_key" {
  type        = string
  default     = "Project"
  description = "The tag key"
}

variable "resource_tag_value" {
  type        = string
  default     = "Test-Retention"
  description = "The tag value"
}

variable "cw_retention_period" {
  type        = number
  default     = 14
  description = "Specifies the number of days you want to retain log events in the specified log group"
}

variable "function_name" {
  type        = string
  default     = "ami-recycle-lambda"
  description = "A unique name for your Lambda Function"
}

variable "function_description" {
  type        = string
  default     = "function to automate the expiration of AMI and moving its associated snapshot to Recycle Bin"
  description = "Description of what your Lambda Function does"
}

variable "function_runtime" {
  type        = string
  default     = "python3.12"
  description = "Identifier of the function's runtime"
}

variable "function_timeout" {
  type        = number
  default     = 15
  description = "The amount of time your Lambda Function has to run in seconds"
}

variable "memory_size" {
  type        = number
  default     = 128
  description = "Amount of memory in MB your Lambda Function can use at runtime"
}

variable "dry_run" {
  type        = bool
  default     = true
  description = "If set to true, the script will not delete any resources"
}