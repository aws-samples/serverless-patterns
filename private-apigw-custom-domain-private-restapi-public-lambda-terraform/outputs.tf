output "network_infrastructure" {
  description = "Network Infrastructure Details"
  value = {
    vpc_id                = aws_vpc.main.id
    public_subnet_1_id    = aws_subnet.public_1.id
    public_subnet_2_id    = aws_subnet.public_2.id
    private_subnet_1_id   = aws_subnet.private_1.id
    private_subnet_2_id   = aws_subnet.private_2.id
    internet_gateway_id   = aws_internet_gateway.main.id
    nat_gateway_1_id      = aws_nat_gateway.nat_1.id
    nat_gateway_2_id      = aws_nat_gateway.nat_2.id
    route_tables = {
      public     = aws_route_table.public.id
      private_1  = aws_route_table.private_1.id
      private_2  = aws_route_table.private_2.id
    }
  }
}

output "security" {
  description = "Security Configuration Details"
  value = {
    vpc_endpoint_sg_id = aws_security_group.vpc_endpoint.id
    ec2_sg_id         = aws_security_group.ec2.id
    ec2_role_arn      = aws_iam_role.ec2_role.arn
    ec2_profile_name  = aws_iam_instance_profile.ec2_profile.name
  }
}

output "dns_and_certificates" {
  description = "DNS and Certificate Details"
  value = {
    hosted_zone_id     = aws_route53_zone.private.id
    certificate_arn    = aws_acm_certificate.certificate.arn
    certificate_status = aws_acm_certificate.certificate.status
  }
}

output "vpc_endpoint_details" {
  description = "VPC Endpoint Details"
  value = {
    id         = aws_vpc_endpoint.execute_api.id
    arn        = aws_vpc_endpoint.execute_api.arn
    dns_entry  = aws_vpc_endpoint.execute_api.dns_entry
  }
}

output "api_gateway_configuration" {
  description = "API Gateway Configuration Details"
  value = {
    rest_api_id     = aws_api_gateway_rest_api.private_api.id
    deployment_id   = aws_api_gateway_deployment.api.id
    stage_name      = aws_api_gateway_stage.api.stage_name
    domain_name     = aws_api_gateway_domain_name.api.domain_name
    endpoint_url    = "https://${var.domain_name}/lambda"
  }
}

output "ec2_instance" {
  description = "EC2 Instance Details"
  value = {
    id         = aws_instance.test.id
    public_ip  = aws_instance.test.public_ip
    private_ip = aws_instance.test.private_ip
  }
}

output "ssm_endpoints" {
  description = "SSM VPC Endpoints"
  value = {
    ssm          = aws_vpc_endpoint.ssm.id
    ssmmessages  = aws_vpc_endpoint.ssmmessages.id
    ec2messages  = aws_vpc_endpoint.ec2messages.id
  }
}
