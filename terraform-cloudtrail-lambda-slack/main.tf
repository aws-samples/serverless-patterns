terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "us-east-1"
}


variable "function_names" {
  type = list(string)
  description = "Enter the function ARNS to monitor in the form of a list"
}

variable "slack" {
  type = string
  description = "Enter your slack channel url"
}


variable "bucket_name" {
  type = string
  description = "Enter a unique S3 bucketname"
}