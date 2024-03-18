/* Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. */

# --- modules/lambda/variables.tf ---

# Lambda Function Name
variable "function_name" {
    description = "function_name"
    type        = string 
    default     = "data_transformation"
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

# Lambda Handler
variable "data_transformation_handler" {
    description = "data_transformation_handler"
    type        = string 
    default     = "data_transformation.data_transformation_handler"
}

# Do not set any default values for the parameter below
# Firehose Delivery Stream ARN
variable "firehose_delivery_stream_arn" {
    description = "firehose_delivery_stream_arn"
    type        = string 
}
