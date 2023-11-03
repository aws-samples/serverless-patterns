/* Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. */

# --- modules/firehose/variables.tf ---

# Kinesis Firehose Delivery Stream  - Name
variable "kinesis_firehose_name" {
    description = "kinesis_firehose_name"
    type        = string 
    default     = "kinesis_source_delivery_stream"
}

# Kinesis Firehose Delivery Stream - Destination
variable "kinesis_firehose_destination" {
    description = "kinesis_firehose_destination"
    type        = string 
    default     = "extended_s3"
}

# Kinesis Firehose Delivery Stream - Processing Type
variable "kinesis_firehose_processing_type" {
    description = "kinesis_firehose_processing_type"
    type        = string 
    default     = "Lambda"
}

# Kinesis Firehose Delivery Stream  - buffer_interval
variable "buffer_interval" {
    description = "buffer_interval"
    type        = number 
    default     = 60
}

# Kinesis Data Streams - buffer_size
variable "buffer_size" {
    description = "buffer_size"
    type        = number
    default     = 128 
}

# Kinesis Firehose Delivery Stream  - compression_format
variable "compression_format" {
    description = "compression_format"
    type        = string
    default     = "GZIP" 
}

# Kinesis Firehose Delivery Stream - timeout
variable "timeout" {
    description = "timeout"
    type        = number 
    default     = 120
}


# Do not set any default values for these parameters below
# S3 destination bucket ARN
variable "s3_destination_bucket_arn" {
    description = "s3_destination_bucket_arn"
    type        = string 
}

# Data Transformation - Lambda ARN
variable "data_transformation_lambda_arn" {
    description = "data_transformation_lambda_arn"
    type        = string 
}