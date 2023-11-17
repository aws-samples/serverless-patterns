/* Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. */

# --- variables.tf ---

# Set AWS Region
variable "region" {
    description = "AWS region to deploy"
    type        = string
    default     = "us-west-1" #Adjust the value per your requirements
}

# Set Environment (dev, test or prod etc.)
variable "environment" {
    description = "Environment"
    type        = string
    default     = "dev" #Adjust the value per your requirements
}

# Set puporse of the functionality
variable "purpose" {
    description = "Purpose of the functionality"
    type        = string
    default     = "Firehose data transformation with Lambda" #Adjust the value per your requirements
}
