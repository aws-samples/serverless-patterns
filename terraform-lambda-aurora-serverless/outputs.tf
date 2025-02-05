output "lambda_function_arn" {
  description = "ARN of the Lambda function"
  value       = aws_lambda_function.aurora_lambda.arn
}

output "lambda_function_name" {
  description = "Name of the Lambda function"
  value       = aws_lambda_function.aurora_lambda.function_name
}

output "aurora_cluster_endpoint" {
  description = "Aurora cluster endpoint"
  value       = aws_rds_cluster.aurora_cluster.endpoint
}

output "aurora_cluster_arn" {
  description = "Aurora cluster ARN"
  value       = aws_rds_cluster.aurora_cluster.arn
}

output "vpc_id" {
  description = "ID of the VPC"
  value       = aws_vpc.lambda_vpc.id
}

output "subnet_ids" {
  description = "IDs of the subnets"
  value       = [aws_subnet.lambda_subnet_1.id, aws_subnet.lambda_subnet_2.id]
}