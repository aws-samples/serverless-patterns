terraform {
  required_version = ">= 1.0.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.20.1"
    }
  }
}

provider "aws" {
  alias   = "ami-creation-account"
  region  = "us-west-2"
  profile = "creation"
}

provider "aws" {
  alias   = "ami-consumer-account_1"
  region  = "us-west-2"
  profile = "consumer"
}