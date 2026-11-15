terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.11.0"
    }
  }
}

variable "region" {}
variable "custom_domain_name_prefix" {}
variable "domain_name" {}

# Configure the AWS Provider
provider "aws" {
 profile = "default"
 region  = "${var.region}"
}
 
#Production account
provider "aws" {
 profile = "crossaccount"
 region  = "${var.region}"
 alias   = "crossaccount"
}

data "aws_caller_identity" "current" {
  provider = aws.crossaccount
}