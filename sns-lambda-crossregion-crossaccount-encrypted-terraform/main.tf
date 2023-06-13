terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.22"
    }
  }

  required_version = ">= 0.14.9"
}

variable "sns_region" {}
variable "lambda_region" {}
variable "snsAccountId" {}
variable "lambdaAccountId" {}
variable "kmsAlias" {}

# Configure the AWS Provider
provider "aws" {
 profile = "default"
 region  = "${var.sns_region}"
 alias   = "default"
}
 
#cross account
provider "aws" {
 profile = "burner"
 region  = "${var.lambda_region}"
 alias   = "crossaccount"
}

#subscription cross account
provider "aws" {
 profile = "burner"
 region  = "${var.sns_region}"
 alias   = "snscrossaccount"
}
