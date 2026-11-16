#aws provider
provider "aws" {
  region = var.region
}

#aws provider for resources dependent on us-east-1 region
#Lambda@Edge function must be deployed in us-east-1 region
#AWS WAF is available globally for CloudFront distributions, but you must use us-east-1
#to create your web ACL and any resources used in the web ACL, such as rule groups, IP sets, and regex pattern sets
provider "aws" {
  alias  = "cloudfront"
  region = "us-east-1"
}

#get current caller identity
data "aws_caller_identity" "current" {}

#local variables
locals {
  account_id = data.aws_caller_identity.current.account_id
  cloudfront_domain_enabled = (var.cloudfront_domain_name != "")
  domain_enabled = (var.domain_name != "")
}