# This code declars outputs from terraform deployment to be used in other parts of the app.  
# © 2023 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.  
# This AWS Content is provided subject to the terms of the AWS Customer Agreement available at  
# http://aws.amazon.com/agreement or other written agreement between Customer and either
# Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.

output "restapi_url" {
  description = "The API Gateway invocation url pointing to the stage"
  value       = module.openapi_demo_rest_api.apigateway_restapi_invoke_url
}
