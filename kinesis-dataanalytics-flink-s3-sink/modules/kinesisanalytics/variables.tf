/* Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. */

# --- modules/kinesisanalytics/variables.tf ---

# Kinesis Analytics Application - Name
variable "kinesis_analytics_application" {
    description = "name"
    type        = string 
    default     = "kinesis_analytics_demo_application"
}

# Kinesis Analytics Application - Runtime
variable "kinesis_analytics_application_runtime" {
    description = "runtime_environment"
    type        = string 
    default     = "FLINK-1_15"
}

# Kinesis Analytics Application - Code Content Type
variable "code_content_type" {
    description = "code_content_type"
    type        = string 
    default     = "ZIPFILE"
}

# Kinesis Analytics Application - Consumer Property Group
variable "consumer_property_group" {
    description = "consumer_property_group"
    type        = string 
    default     = "consumer.config.0"
}

# Kinesis Analytics Application - Scan Initial Position
variable "scan_stream_initpos" {
    description = "scan_stream_initpos"
    type        = string 
    default     = "LATEST"
}

# Kinesis Analytics Application - Application Runtime Options
variable "application_runtime_options" {
    description = "application_runtime_options"
    type        = string 
    default     = "kinesis.analytics.flink.run.options"
}

# Kinesis Analytics Application - Sink Config
variable "sink_config" {
    description = "sink_config"
    type        = string 
    default     = "sink.config.0"
}

# Kinesis Analytics Application - Python Code File Name
variable "python_code_file" {
    description = "python_code_file"
    type        = string 
    default     = "streaming-file-sink.py"
}

# Kinesis Analytics Application - Jar File
variable "jar_file" {
    description = "jar_file"
    type        = string 
    default     = "flink-sql-connector-kinesis-1.15.2.jar"
}

# Kinesis Analytics Application - Auto Scaling Enabled
variable "auto_scaling_enabled" {
    description = "auto_scaling_enabled"
    type        = bool 
    default     = "true"
}

# Kinesis Analytics Application - Parallelism Configuration Type
variable "parallelism_configuration_type" {
    description = "parallelism_configuration_type"
    type        = string 
    default     = "CUSTOM"
}

# Kinesis Analytics Application - Parallelism
variable "parallelism" {
    description = "parallelism"
    type        = number 
    default     = 1
}

# Kinesis Analytics Application - Parallelism Per KPU
variable "parallelism_per_kpu" {
    description = "parallelism_per_kpu"
    type        = number 
    default     = 1
}

# Kinesis Analytics Application - Checkpoint Configuration Type
variable "checkpoint_configuration_type" {
    description = "checkpoint_configuration_type"
    type        = string
    default     = "DEFAULT"
}

# Kinesis Analytics Application - Log level
variable "log_level" {
    description = "log_level"
    type        = string
    default     = "INFO"
}

# Kinesis Analytics Application - Metrics level
variable "metrics_level" {
    description = "metrics_level"
    type        = string
    default     = "APPLICATION"
}

# Kinesis Analytics Application - Checkpoint Configuration Type
variable "monitoring_configuration_type" {
    description = "monitoring_configuration_type"
    type        = string
    default     = "DEFAULT"
}

# Kinesis Analytics Application - Log Stream
variable "log_stream" {
    description = "log_stream"
    type        = string
    default     = "kinesis_analytics_demo_application_log_stream"
}

# Do not set any default values for these parameters below
# S3 bucket ARN
variable "bucket_arn" {
    description = "bucket_arn"
    type        = string 
}

# S3 bucket Name
variable "bucket_name" {
    description = "bucket_name"
    type        = string 
}

# S3 Object file_key
variable "file_key" {
    description = "file_key"
    type        = string 
}

# Kinesis Stream name
variable "stream_name" {
    description = "stream_name"
    type        = string 
}

# AWS Region
variable "region" {
    description = "region"
    type        = string 
}


