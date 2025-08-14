terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }
  }

  required_version = ">= 0.14.9"
}

# Fetching current Account ID, AWS region and AZs
data "aws_caller_identity" "current" {}
data "aws_region" "current" {}
data "aws_availability_zones" "available" {}

#################################################################
# Outputs
#################################################################
output "APIGatewayUrl" {
  value = "${aws_apigatewayv2_api.MyApp-APIGatewayHTTP.api_endpoint}"
  description = "API Gateway URL to access the GET endpoint"
}

output "MyFargateServiceLoadBalancer" {
  value       = "${aws_alb.MyApp-ALB.dns_name}"
}

output "MyFargateServiceServiceURL" {
  value       = "http://${aws_alb.MyApp-ALB.dns_name}"
}

