# Outputs for Lambda Managed Instances Terraform implementation

output "function_name" {
  description = "Lambda function name for CLI invocation"
  value       = aws_lambda_function.hello_world_function.function_name
}

output "function_arn" {
  description = "Lambda function ARN"
  value       = aws_lambda_function.hello_world_function.arn
}

output "log_group_name" {
  description = "CloudWatch Log Group name"
  value       = aws_cloudwatch_log_group.demo_log_group.name
}

output "capacity_provider_arn" {
  description = "Lambda Capacity Provider ARN"
  value       = aws_lambda_capacity_provider.lambda_capacity_provider.arn
}

output "capacity_provider_name" {
  description = "Lambda Capacity Provider name"
  value       = aws_lambda_capacity_provider.lambda_capacity_provider.name
}

output "vpc_id" {
  description = "VPC ID for Lambda Managed Instances"
  value       = aws_vpc.lambda_managed_instances_vpc.id
}

output "private_subnet_ids" {
  description = "Private subnet IDs"
  value       = [aws_subnet.private_subnet_1.id, aws_subnet.private_subnet_2.id, aws_subnet.private_subnet_3.id]
}

output "public_subnet_ids" {
  description = "Public subnet IDs"
  value       = [aws_subnet.public_subnet_1.id, aws_subnet.public_subnet_2.id, aws_subnet.public_subnet_3.id]
}

output "security_group_id" {
  description = "Security Group ID"
  value       = aws_security_group.lambda_security_group.id
}

output "default_security_group_id" {
  description = "Default Security Group ID (restricted)"
  value       = aws_default_security_group.default.id
}

output "capacity_provider_association" {
  description = "Confirmation that Lambda function is associated with capacity provider"
  value       = "Function ${aws_lambda_function.hello_world_function.function_name} is configured to use capacity provider ${aws_lambda_capacity_provider.lambda_capacity_provider.name}"
}

output "function_alias" {
  description = "Lambda function alias for invocation"
  value       = "${aws_lambda_function.hello_world_function.function_name}:${aws_lambda_alias.hello_world_alias.name}"
}

output "manual_association_command" {
  description = "Manual command to associate Lambda function with capacity provider"
  value = "aws lambda put-capacity-provider-function --capacity-provider-arn ${aws_lambda_capacity_provider.lambda_capacity_provider.arn} --function-name ${aws_lambda_function.hello_world_function.function_name}"
}

output "nat_gateway_ids" {
  description = "NAT Gateway IDs"
  value       = [aws_nat_gateway.nat_gateway_1.id, aws_nat_gateway.nat_gateway_2.id, aws_nat_gateway.nat_gateway_3.id]
}

output "elastic_ip_addresses" {
  description = "Elastic IP addresses for NAT Gateways"
  value       = [aws_eip.nat_eip_1.public_ip, aws_eip.nat_eip_2.public_ip, aws_eip.nat_eip_3.public_ip]
}