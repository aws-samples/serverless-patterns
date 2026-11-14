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

# Flink Kinesis SQL connector, downloaded from Maven Central at apply time.
# The file name must match jar_file in the kinesisanalytics module.
variable "connector_jar_name" {
    description = "File name of the Flink Kinesis SQL connector jar in the application zip"
    type        = string
    default     = "flink-sql-connector-kinesis-1.15.2.jar"
}

variable "connector_jar_url" {
    description = "Maven Central URL of the Flink Kinesis SQL connector jar"
    type        = string
    default     = "https://repo1.maven.org/maven2/org/apache/flink/flink-sql-connector-kinesis/1.15.2/flink-sql-connector-kinesis-1.15.2.jar"
}

variable "connector_jar_sha256" {
    description = "SHA-256 checksum of the Flink Kinesis SQL connector jar"
    type        = string
    default     = "defbbe300be769569218a014d23d6f435bd97ae2e6696abe74fc14705ffa39c6"
}
