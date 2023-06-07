terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}


variable "region" {}
variable "topicName" {}
variable "lambdaName" {}
variable "lambdaRegion" {}
variable "lambdaAccountId" {}


# Configure the AWS Provider
provider "aws" {
 profile = "default"
 region  = "${var.region}"
 alias   = "default"
}
 
#cross account for lambda
provider "aws" {
 profile = "shivMain"
 region  = "${var.lambdaRegion}"
 alias   = "crossaccount"
}

#cross account for sns sub
provider "aws" {
 profile = "shivMain"
 region  = "${var.region}"
 alias   = "snssub"
}

data "aws_caller_identity" "current" {}
