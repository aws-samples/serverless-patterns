/* Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. */

# --- modules/lambda/variables.tf ---

# Lambda Function Name - with filter
variable "esm_lambda_with_filter_function_name" {
    description = "esm_lambda_with_filter_function_name"
    type        = string 
    default     = "esm_lambda_with_filter"
}

# Lambda Function Name - with no filter
variable "esm_lambda_with_no_filter_function_name" {
    description = "esm_lambda_with_no_filter_function_name"
    type        = string 
    default     = "esm_lambda_with_no_filter"
}

# Lambda Function - Runtime
variable "runtime" {
    description = "runtime"
    type        = string 
    default     = "python3.9"
}

# Lambda - Timeout
variable "timeout" {
    description = "timeout"
    type        = number 
    default     = 120
}

# Lambda Handler - with no filter
variable "esm_lambda_with_no_filter_handler" {
    description = "esm_lambda_with_no_filter_handler"
    type        = string 
    default     = "esm_lambda_with_no_filter.esm_lambda_with_no_filter_handler"
}

# Lambda Handler - with filter
variable "esm_lambda_with_filter_handler" {
    description = "esm_lambda_with_filter_handler"
    type        = string 
    default     = "esm_lambda_with_filter.esm_lambda_with_filter_handler"
}

# Do not set any default values for the parameter below
# Kinesis Data Streams ARN
variable "stream_arn" {
    description = "stream_arn"
    type        = string 
}
