/* Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. */

# --- outputs.tf ---


output "lambda_function_name" {
  description = "Name of the Lambda function"
  value       = aws_lambda_function.content_generation.function_name
}

output "api_endpoint" {
  description = "API Gateway endpoint URL"
  value       = "${aws_api_gateway_stage.dev.invoke_url}${aws_api_gateway_resource.generate_content.path}"
}
