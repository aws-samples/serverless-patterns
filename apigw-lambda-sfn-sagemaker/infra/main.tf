provider "aws" {
  profile = "default"
  region  = "us-east-1"
}

terraform {
  required_version = ">= 1.6.4"
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "5.33.0"
    }
  }
}

# module "sfn_emrserverless" {
#   source     = "./templates"
#   app        = "pattern-sfn-emrserverless"
#   stage_name = "dev"
#   jar_name   = "sample.jar"
# }

