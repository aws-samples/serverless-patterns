# create api gateway custom domain
resource "aws_apigatewayv2_domain_name" "http_api_domain_name" {
  count = local.domain_enabled ? 1 : 0
  domain_name = var.domain_name

  domain_name_configuration {
    certificate_arn = var.certificate_arn
    endpoint_type   = "REGIONAL"
    security_policy = "TLS_1_2"
  }
}

# create api gateway mapping
resource "aws_apigatewayv2_api_mapping" "http_api_mapping" {
  count = local.domain_enabled ? 1 : 0
  api_id      = aws_apigatewayv2_api.http_api.id
  domain_name = aws_apigatewayv2_domain_name.http_api_domain_name[0].id
  stage       = aws_apigatewayv2_stage.http_api_stage.id
}

# create route53 record for api gateway custom domain
resource "aws_route53_record" "http_api_route53_record" {
  count = local.domain_enabled ? 1 : 0
  name    = aws_apigatewayv2_domain_name.http_api_domain_name[0].domain_name
  type    = "A"
  zone_id = var.zone_id

  alias {
    name                   = aws_apigatewayv2_domain_name.http_api_domain_name[0].domain_name_configuration[0].target_domain_name
    zone_id                = aws_apigatewayv2_domain_name.http_api_domain_name[0].domain_name_configuration[0].hosted_zone_id
    evaluate_target_health = false
  }
}

# create route53 record for cloudfront custom domain
resource "aws_route53_record" "cloudfront_route53_record" {
  count = local.cloudfront_domain_enabled ? 1 : 0
  name    = var.cloudfront_domain_name
  type    = "A"
  zone_id = var.zone_id

  alias {
    name = "${aws_cloudfront_distribution.http_api_distribution.domain_name}"
    zone_id = "${aws_cloudfront_distribution.http_api_distribution.hosted_zone_id}"
    evaluate_target_health = false
  }
}
