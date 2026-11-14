# Output value definitions

output "vpc_id" {
  description = "the vpc id"
  value = aws_vpc.poc_vpc.id
}

output "lambda_sg" {
  description = "security group to be assigned to lambda function"
  value = aws_security_group.lambda_sg.id
}

output "lambda_subnet_1" {
  description = "private subnet id for lambda function"
  value = aws_subnet.app[0].id
}

output "lambda_subnet_2" {
  description = "private subnet id for lambda function"
  value = aws_subnet.app[1].id
}

output "rds_proxy_arn" {
  description = "the arn of the RDS proxy, includes the rds proxy resource id, prx-<hash>"
  value = aws_db_proxy.mysql_proxy.arn
}

output "rds_proxy_endpoint" {
  description = "the name of the endpoint for the RDS proxy"
  value = aws_db_proxy_endpoint.aurora.endpoint
}

output "lambda_secret" {
  description = "the name of the Secrets Manager secret that stores the database user credentials"
  value = aws_secretsmanager_secret.lambda_secret.name
}

output "rds_proxy_log" {
  description = "CloudWatch log group name for RDS Proxy logs"
  value = aws_cloudwatch_log_group.this.id
}
