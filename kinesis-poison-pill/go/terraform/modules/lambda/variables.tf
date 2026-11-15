/* Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. */

# --- modules/lambda/variables.tf ---

# Lambda Function Name
variable "function_name" {
    description = "function_name"
    type        = string 
    default     = "kinesis_stream"
}

# Lambda Function - Runtime
variable "runtime" {
    description = "runtime"
    type        = string 
    default     = "go1.x"
}

# Lambda - Timeout
variable "timeout" {
    description = "timeout"
    type        = number 
    default     = 120
}

# Lambda Handler
variable "kinesis_error_handler" {
    description = "kinesis_error_handler"
    type        = string 
    default     = "handler"
}

# Do not set any default values for the parameter below
# Firehose Delivery Stream ARN
variable "kinesis_stream_arn" {
    description = "kinesis_stream_arn"
    type        = string 
}

variable "sqs_arn" {
  description = "sqs arn"
    type        = string 
}