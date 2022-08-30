terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}


variable "region" {}
variable "prefix" {}

# Configure the AWS Provider
provider "aws" {
 profile = "default"
 region  = "${var.region}"
 alias   = "default"
}
 
#cross account
provider "aws" {
 profile = "crossaccount"
 region  = "${var.region}"
 alias   = "crossaccount"
}