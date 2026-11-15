####################################################
# Variables with Defaults
####################################################
variable "env" {
  type        = string
  description = "Name of the environment this infrastructure is for"
  default     = "testing"
}

variable "organization" {
  type        = string
  description = "Name of the organization this infrastructure is for"
  default     = "serverlessland"
}

variable "timeout" {
  type        = number
  description = "Timeout for Lambda Task"
  default     = 900
}

variable "memory_size" {
  type        = number
  description = "Memory for Lambda Task"
  default     = 512
}

variable "logging_level" {
  type        = string
  description = "Level of logging required for this Lambda function"
  default     = "INFO"

  validation {
    condition     = contains(["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], var.logging_level)
    error_message = "Valid values for logging_level are (DEBUG, INFO, WARNING, ERROR, CRITICAL)"
  }
}

variable "bedrock_foundation_model" {
  type        = string
  description = "Bedrock Foundation Model"
  default     = "anthropic.claude-v2"
}

####################################################
# Variables without Defaults
####################################################
variable "aws_vpc_id" {
  type        = string
  description = "VPC ID for Lambda Task"
}

variable "aws_subnets" {
  type        = set(any)
  description = "A list of subnets inside the VPC"
}