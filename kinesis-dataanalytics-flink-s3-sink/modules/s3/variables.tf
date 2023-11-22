/* Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. */

# --- modules/s3/variables.tf ---

# Name of the zip (application) file
variable "name" {
    description = "name"
    type        = string 
    default     = "sample_application.zip"
}

# S3 Object Key
variable "key" {
    description = "key"
    type        = string 
    default     = "sample_application.zip"
}

# Path to store the zip (application) file
variable "path" {
    description = "path"
    type        = string 
    default     = "tmp"
}

# S3 Bucket Name - Prefix
variable "s3_bucket_name_prefix" {
    description = "s3_bucket_name_prefix"
    type        = string 
    default     = "kinesis-analytics-landing-zone"
}

# S3 Object - file compression type
variable "compression_type" {
    description = "compression_type"
    type        = string 
    default     = "zip"
}
