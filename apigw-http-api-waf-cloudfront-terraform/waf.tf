resource "aws_wafv2_web_acl" "cloudfront_web_acl" {
  name        = var.waf_webacl_name
  description = var.waf_webacl_name
  scope       = "CLOUDFRONT"

  default_action {
    allow {}
  }

  rule {
    name     = "${var.waf_rule_name}-ratebased"
    priority = 1

    action {
      block {}
    }

    statement {
      rate_based_statement {
        limit              = 100
        aggregate_key_type = "IP"
      }
    }

    visibility_config {
      cloudwatch_metrics_enabled = false
      metric_name                = "${var.waf_rule_name}-ratebased-metric"
      sampled_requests_enabled   = false
    }
  }

  rule {
    name     = "${var.waf_rule_name}-managedcommonrule"
    priority = 2

    override_action {
      none {}
    }

    statement {
      managed_rule_group_statement {
        name        = "AWSManagedRulesCommonRuleSet"
        vendor_name = "AWS"

        rule_action_override {
          action_to_use {
            block {}
          }

          name = "NoUserAgent_HEADER"
        }
      }
    }

    visibility_config {
      cloudwatch_metrics_enabled = false
      metric_name                = "${var.waf_rule_name}-managedcommonrule-metric"
      sampled_requests_enabled   = false
    }
  }

  tags = {
    Name = var.waf_webacl_name
  }

  visibility_config {
    cloudwatch_metrics_enabled = false
    metric_name                = "${var.waf_webacl_name}-metric"
    sampled_requests_enabled   = false
  }
}