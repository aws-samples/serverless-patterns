# CloudFront distribution for HTTP API Gateway
resource "aws_cloudfront_distribution" "http_api_distribution" {
  origin {
    #if domain_name is not empty, domain_name else "${aws_apigatewayv2_api.http_api.id}.execute-api.${var.region}.amazonaws.com"
    domain_name = local.domain_enabled ? var.domain_name : "${aws_apigatewayv2_api.http_api.id}.execute-api.${var.region}.amazonaws.com"
    origin_id   = "http_api_origin"
    custom_origin_config {
      http_port              = "80"
      https_port             = "443"
      origin_protocol_policy = "https-only"
      origin_ssl_protocols   = ["TLSv1.2"]
    }
    custom_header {
      name  = "X-Origin-Verify"
      value = var.cloudfront_api_secret_name
    }
    custom_header {
      name  = "X-Origin-Verify-Region"
      value = var.region
    }    
  }

  enabled = true

  aliases = local.cloudfront_domain_enabled ? [var.cloudfront_domain_name] : []

  default_cache_behavior {
    allowed_methods  = ["GET", "HEAD"]
    cached_methods   = ["GET", "HEAD"]
    target_origin_id = "http_api_origin"

    forwarded_values {
      query_string = false
      headers      = ["Authorization"]

      cookies {
        forward = "none"
      }
    }

    viewer_protocol_policy = "redirect-to-https"
    min_ttl                = var.min_ttl
    default_ttl            = var.default_ttl
    max_ttl                = var.max_ttl

    lambda_function_association {
      event_type   = "origin-request"
      lambda_arn   = aws_lambda_function.http_api_edge_lambda.qualified_arn
      include_body = false
    }

  }

  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }

  # Certificate settings when domain_name is not empty
  dynamic "viewer_certificate" {
    for_each = local.cloudfront_domain_enabled ? [1] : []
    content {
        acm_certificate_arn = local.cloudfront_domain_enabled ? var.cloudfront_certificate_arn : ""
        cloudfront_default_certificate = !local.cloudfront_domain_enabled
        ssl_support_method = "sni-only"
    }
  }

  # Certificate settings when domain_name is empty
  dynamic "viewer_certificate" {
    for_each = !local.cloudfront_domain_enabled ? [1] : []
    content {
        cloudfront_default_certificate = !local.cloudfront_domain_enabled
    }
  }

  web_acl_id = aws_wafv2_web_acl.cloudfront_web_acl.arn
}