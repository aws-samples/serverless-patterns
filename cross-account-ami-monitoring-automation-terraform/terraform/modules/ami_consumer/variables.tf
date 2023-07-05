variable "iam_policy_arn" {
  description = "Additional IAM Policy to be attached to role"
  type        = list(string)
  default     = []
}

variable "lambda_runtime" {
  type        = string
  default     = "python3.9"
  description = "AWS Lambda function execution runtime"
}

variable "lambda_timeout" {
  type        = number
  default     = 300
  description = "AWS Lambda function execution timeout"
}


variable "lambda_memory_size" {
  type        = number
  default     = 128
  description = "AWS Lambda function memory size"
}


variable "ami_usage_function_name" {
  description = "AWS Lambda function name of AMI register function"
  default     = "ami-usage-function"
  type        = string
}

variable "configuration_inputs" {
  type = object({
    ami_share_ddb_table      = string
    external_assume_role_arn = string
  })
  description = "Configuration inputs required from AMI creator account"
}

variable "ami_creator_account" {
  description = "If AMI is getting consumed in the same AWS account as AMI creator account"
  type        = bool
  default     = false
}