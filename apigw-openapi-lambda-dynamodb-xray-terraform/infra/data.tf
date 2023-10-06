# This code declars aws_caller_identity data source that helps retrieve AccountId.  
# © 2023 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.  
# This AWS Content is provided subject to the terms of the AWS Customer Agreement available at  
# http://aws.amazon.com/agreement or other written agreement between Customer and either
# Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.

data "aws_caller_identity" "current" {}

data "aws_canonical_user_id" "current" {}

data "template_file" "open_api_spec" {
  template = file("openapi-spec.yaml")
  vars = {
    openapi_demo_lambda_uri = module.openapi_demo_lambda_function.lambda_function_invoke_arn
  }
}