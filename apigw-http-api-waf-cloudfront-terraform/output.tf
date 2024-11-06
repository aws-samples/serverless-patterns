# api gateway endpoint output
output "api_gateway_endpoint" {
  value = aws_apigatewayv2_api.http_api.api_endpoint
}

# cloudfront distribution output
output "cloudfront_distribution_id" {
  value = aws_cloudfront_distribution.http_api_distribution.domain_name
}

# cloudfront domain name
output "cloudfront_domain_name" {
  value = var.cloudfront_domain_name
}

# domain name
output "domain_name" {
  value = var.domain_name
}