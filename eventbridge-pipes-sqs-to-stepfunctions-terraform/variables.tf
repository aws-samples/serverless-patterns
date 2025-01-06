/* Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. */

# --- variables.tf ---

# Set AWS Region
variable "region" {
    description = "AWS region to deploy"
    type        = string
    default     = "us-west-2" #Adjust the value per your requirements
}

# Set Environment (dev, test or prod etc.)
variable "environment" {
    description = "Environment"
    type        = string
    default     = "dev" #Adjust the value per your requirements
}

# Set purpose of the functionality
variable "purpose" {
    description = "Purpose of the functionality"
    type        = string
    default     = "Amazon EventBridge Pipes: SQS to Step Functions with Filtering and Transformation (Terraform)" #Adjust the value per your requirements
}
