#aws provider
provider "aws" {
  region = var.region
}

#get current caller identity
data "aws_caller_identity" "current" {}

#local variables
locals {
  account_id = data.aws_caller_identity.current.account_id
  cloudfront_domain_enabled = (var.cloudfront_domain_name != "")
  domain_enabled = (var.domain_name != "")
}