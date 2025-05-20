variable "contructID" {
  description = "Construct ID"
  type        = string
  default     = "ApigwBedrockCognitoCdkStack"
}

variable "region" {
  description = "The AWS region to deploy the resources"
  type        = string
  default     = "us-east-1"
}

variable "rate_limit" {
  description = "Maximum sustained requests per second"
  type        = number
  default     = 1
}

variable "burst_limit" {
  description = "Maximum burst requests per second"
  type        = number
  default     = 2
}

variable "quota_limit" {
  description = "Maximum number of requests allowed in the specified period"
  type        = number
  default     = 25
}

variable "quota_period" {
  description = "Period for the quota (DAY, WEEK, MONTH)"
  type        = string
  default     = "MONTH"
}

variable "stage_name" {
  description = "Stage name for the API Gateway deployment"
  type        = string
  default     = "prod"
}

variable "lambda_runtime" {
  description = "Runtime for the Lambda function"
  type        = string
  default     = "python3.9"
}

variable "auth_handler" {
  description = "The handler for the Lambda function"
  type        = string
  default     = "auth.handler"
}

variable "timeout" {
  description = "Timeout for the Lambda function in seconds"
  type        = number
  default     = 29
}

variable "bedrock_path" {
  description = "Path for bedrock zip"
  type        = string
  default     = "src/bedrock"
}