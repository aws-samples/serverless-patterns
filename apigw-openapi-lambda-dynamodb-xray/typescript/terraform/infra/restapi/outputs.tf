# This code declars outputs from terraform deployment of REST API.  
# © 2023 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.  
# This AWS Content is provided subject to the terms of the AWS Customer Agreement available at  
# http://aws.amazon.com/agreement or other written agreement between Customer and either
# Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.

output "apigateway_restapi_api_id" {
  description = "The API identifier"
  value       = aws_api_gateway_rest_api.this.id
}

output "apigateway_restapi_api_arn" {
  description = "The ARN of the API"
  value       = aws_api_gateway_rest_api.this.arn
}

output "apigateway_restapi_execution_arn" {
  description = "The ARN prefix to be used in an aws_lambda_permission's source_arn attribute"
  value       = aws_api_gateway_rest_api.this.execution_arn
}

output "apigateway_restapi_stage_name" {
  description = "The API Gateway stage name"
  value       = aws_api_gateway_stage.this.stage_name
}

output "apigateway_restapi_invoke_url" {
  description = "The API Gateway invocation url pointing to the stage"
  value       = aws_api_gateway_stage.this.invoke_url
}
