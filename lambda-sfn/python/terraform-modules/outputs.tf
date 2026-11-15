# Lambda Function
output "lambda_function_arn" {
  description = "The ARN of the Lambda Function"
  value       = module.lambda_function.lambda_function_arn
}

output "lambda_function_arn_static" {
  description = "The static ARN of the Lambda Function. Use this to avoid cycle errors between resources (e.g., Step Functions)"
  value       = module.lambda_function.lambda_function_arn_static
}

output "lambda_function_invoke_arn" {
  description = "The Invoke ARN of the Lambda Function"
  value       = module.lambda_function.lambda_function_invoke_arn
}

output "lambda_function_name" {
  description = "The name of the Lambda Function"
  value       = module.lambda_function.lambda_function_name
}

output "lambda_function_qualified_arn" {
  description = "The ARN identifying your Lambda Function Version"
  value       = module.lambda_function.lambda_function_qualified_arn
}

output "lambda_function_version" {
  description = "Latest published version of Lambda Function"
  value       = module.lambda_function.lambda_function_version
}

# IAM Role of Lambda Function
output "lambda_role_arn" {
  description = "The ARN of the IAM role created for the Lambda Function"
  value       = module.lambda_function.lambda_role_arn
}

# State Machine
output "state_machine_id" {
  description = "The ARN of the State Machine"
  value       = module.step_function.state_machine_id
}

output "state_machine_arn" {
  description = "The ARN of the State Machine"
  value       = module.step_function.state_machine_arn
}

# IAM Role
output "step_function_role_arn" {
  description = "The ARN of the IAM role created for the State Machine"
  value       = module.step_function.role_arn
}

output "step_function_role_name" {
  description = "The name of the IAM role created for the State Machine"
  value       = module.step_function.role_name
}
