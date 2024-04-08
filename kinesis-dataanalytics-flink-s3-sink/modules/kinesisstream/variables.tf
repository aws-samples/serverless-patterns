/* Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. */

# --- modules/kinesisstream/variables.tf ---

# Name of the Kinesis streams
variable "name" {
    description = "name"
    type        = string 
    default     = "demo_stream"
}

# Kinesis streams - Retention Period
variable "retention_period" {
    description = "retention_period"
    type        = number 
    default     = 24
}

