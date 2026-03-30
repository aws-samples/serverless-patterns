output "function_name" {
  description = "Lambda function name for CLI invocation"
  value       = aws_lambda_function.hello_world.function_name
}

output "function_arn" {
  description = "Lambda function ARN"
  value       = aws_lambda_function.hello_world.arn
}

output "capacity_provider_name" {
  description = "Lambda capacity provider name"
  value       = aws_lambda_capacity_provider.lambda_capacity_provider.name
}

output "capacity_provider_arn" {
  description = "Lambda capacity provider ARN"
  value       = aws_lambda_capacity_provider.lambda_capacity_provider.arn
}