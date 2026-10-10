output "rest_api_endpoint" {
  value       = aws_api_gateway_stage.prod.invoke_url
  description = "REST API Gateway Endpoint URL"
}

output "vpc_link_id" {
  value       = aws_apigatewayv2_vpc_link.vpclink.id
  description = "VPC Link V2 ID"
}

output "alb_dns_name" {
  value       = aws_lb.private_alb.dns_name
  description = "Private ALB DNS name"
}

output "ecs_cluster_name" {
  value       = aws_ecs_cluster.main.name
  description = "ECS cluster name"
}

output "ecs_service_name" {
  value       = aws_ecs_service.app.name
  description = "ECS service name"
}
