resource "aws_acm_certificate" "cert" {
  domain_name       = "${var.custom_domain_name_prefix}.${var.domain_name}"
  validation_method = "DNS"
}

data "aws_route53_zone" "r53" {
  name         = "${var.domain_name}"
  private_zone = false
}

resource "aws_route53_record" "cert_record" {
  for_each = {
    for dvo in aws_acm_certificate.cert.domain_validation_options : dvo.domain_name => {
      name   = dvo.resource_record_name
      record = dvo.resource_record_value
      type   = dvo.resource_record_type
    }
  }

  allow_overwrite = true
  name            = each.value.name
  records         = [each.value.record]
  ttl             = 60
  type            = each.value.type
  zone_id         = data.aws_route53_zone.r53.zone_id
}

resource "aws_acm_certificate_validation" "validation" {
  certificate_arn         = aws_acm_certificate.cert.arn
  validation_record_fqdns = [for record in aws_route53_record.cert_record : record.fqdn]
}

resource "aws_route53_record" "record" {
  zone_id = data.aws_route53_zone.r53.zone_id
  name    = "${var.custom_domain_name_prefix}"
  type    = "CNAME"
  ttl     = "300"
  records = [aws_lb.public_alb.dns_name]
}