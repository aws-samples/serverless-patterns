output "lambda_function_name" {
  description = "Lambda Function Name"
  value       = aws_lambda_function.translate_text.function_name
}

output "lambda_function_arn" {
  description = "Lambda Function ARN"
  value       = aws_lambda_function.translate_text.arn
}