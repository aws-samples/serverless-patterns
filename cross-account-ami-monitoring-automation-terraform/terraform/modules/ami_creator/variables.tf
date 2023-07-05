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

variable "ami_share_function_name" {
  description = "AWS Lambda function name of AMI share function"
  default     = "ami-share-function"
  type        = string
}

variable "account_email_mapping" {
  description = "Account id and email id mapping of AWS Account's"
  type = list(object({
    account = string
    email   = string
  }))
}

variable "ssm_prefix" {
  type        = string
  description = "Prefix for SSM parameter store"
  default     = "/cross-account-ami"
}
variable "consumer" {
  type        = bool
  description = "Enable AMI Consumption in the creator account"
  default     = false
}

