variable "aws_region" {
  description = "AWS Region to deploy to. It must offer AWS Lambda Web Functions, Amazon Bedrock AgentCore Runtime and the model in model_id."
  type        = string
  default     = "us-east-1"
}

variable "model_id" {
  description = <<-EOT
    Amazon Bedrock inference profile ID that the agent calls. Leave empty to use Claude Sonnet 5.5
    through the cross-Region inference profile for the geography of aws_region: us. in US Regions,
    eu. in Europe and global. anywhere else.
  EOT
  type        = string
  default     = ""
}

variable "rate_limit" {
  description = "Requests per second that the Web Function endpoint accepts before it returns HTTP 429. Up to 1,000 it must be a multiple of 100. The endpoint is public, so this caps how fast anyone can spend model tokens in your account."
  type        = number
  default     = 100

  validation {
    condition     = var.rate_limit >= 100 && (var.rate_limit <= 1000 ? var.rate_limit % 100 == 0 : var.rate_limit % 1000 == 0 && var.rate_limit <= 10000)
    error_message = "rate_limit must be 100 to 1,000 in steps of 100, or 2,000 to 10,000 in steps of 1,000."
  }
}

variable "max_environments" {
  description = "Maximum number of Web Function execution environments. Each one serves many concurrent requests."
  type        = number
  default     = 2

  validation {
    condition     = var.max_environments >= 2 && var.max_environments <= 10000
    error_message = "max_environments must be between 2 and 10,000."
  }
}

variable "log_retention_days" {
  description = "Number of days to keep the Web Function and agent logs in Amazon CloudWatch Logs."
  type        = number
  default     = 7
}
