# TerraformScript Developed by @lpiyumal
# 2 things which requires to be updated by you :
# 1. Region on line 25 and 30
# 2. Your domain name on line 38


terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    time = {
      source  = "hashicorp/time"
      version = "~> 0.9.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.0"
    }
  }
}


provider "aws" {
  region = var.region
}

provider "aws" {
  alias  = "acm_region"
  region = var.region
}


provider "time" {}

provider "random" {}



data "aws_availability_zones" "available" {
  state = "available"
}

data "aws_region" "current" {}

data "aws_caller_identity" "current" {}


resource "time_static" "current" {}


resource "random_string" "suffix" {
  length  = 8
  special = false
  upper   = false
}




data "aws_ami" "amazon_linux_2" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
}

data "aws_vpc_endpoint" "execute_api" {
  id = aws_vpc_endpoint.execute_api.id
  depends_on = [aws_vpc_endpoint.execute_api]
}


resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true
  instance_tenancy     = "default"

  tags = {
    Name = "PrivateApiStack/private-api-tutorial-vpc"
  }
}


resource "aws_subnet" "public_1" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.0.0/18"
  availability_zone       = data.aws_availability_zones.available.names[0]
  map_public_ip_on_launch = true

  tags = {
    Name                = "PrivateApiStack/private-api-tutorial-vpc/PublicSubnet1"
    "aws-cdk:subnet-name" = "Public"
    "aws-cdk:subnet-type" = "Public"
  }
}


resource "aws_subnet" "public_2" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.64.0/18"
  availability_zone       = data.aws_availability_zones.available.names[1]
  map_public_ip_on_launch = true

  tags = {
    Name                = "PrivateApiStack/private-api-tutorial-vpc/PublicSubnet2"
    "aws-cdk:subnet-name" = "Public"
    "aws-cdk:subnet-type" = "Public"
  }
}


resource "aws_subnet" "private_1" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.128.0/18"
  availability_zone       = data.aws_availability_zones.available.names[0]

  tags = {
    Name                = "PrivateApiStack/private-api-tutorial-vpc/PrivateSubnet1"
    "aws-cdk:subnet-name" = "Private"
    "aws-cdk:subnet-type" = "Private"
  }
}


resource "aws_subnet" "private_2" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.192.0/18"
  availability_zone       = data.aws_availability_zones.available.names[1]

  tags = {
    Name                = "PrivateApiStack/private-api-tutorial-vpc/PrivateSubnet2"
    "aws-cdk:subnet-name" = "Private"
    "aws-cdk:subnet-type" = "Private"
  }
}


resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "PrivateApiStack/private-api-tutorial-vpc"
  }
}


resource "aws_eip" "nat_1" {
  domain = "vpc"
  tags = {
    Name = "PrivateApiStack/private-api-tutorial-vpc/PublicSubnet1"
  }
}

resource "aws_eip" "nat_2" {
  domain = "vpc"
  tags = {
    Name = "PrivateApiStack/private-api-tutorial-vpc/PublicSubnet2"
  }
}


resource "aws_nat_gateway" "nat_1" {
  allocation_id = aws_eip.nat_1.id
  subnet_id     = aws_subnet.public_1.id

  tags = {
    Name = "PrivateApiStack/private-api-tutorial-vpc/PublicSubnet1"
  }
}

resource "aws_nat_gateway" "nat_2" {
  allocation_id = aws_eip.nat_2.id
  subnet_id     = aws_subnet.public_2.id

  tags = {
    Name = "PrivateApiStack/private-api-tutorial-vpc/PublicSubnet2"
  }
}


resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main.id
  }

  tags = {
    Name = "Public Route Table"
  }
}

resource "aws_route_table" "private_1" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.nat_1.id
  }

  tags = {
    Name = "Private Route Table 1"
  }
}

resource "aws_route_table" "private_2" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.nat_2.id
  }

  tags = {
    Name = "Private Route Table 2"
  }
}


resource "aws_route_table_association" "public_1" {
  subnet_id      = aws_subnet.public_1.id
  route_table_id = aws_route_table.public.id
}

resource "aws_route_table_association" "public_2" {
  subnet_id      = aws_subnet.public_2.id
  route_table_id = aws_route_table.public.id
}

resource "aws_route_table_association" "private_1" {
  subnet_id      = aws_subnet.private_1.id
  route_table_id = aws_route_table.private_1.id
}

resource "aws_route_table_association" "private_2" {
  subnet_id      = aws_subnet.private_2.id
  route_table_id = aws_route_table.private_2.id
}


resource "aws_security_group" "vpc_endpoint" {
  name_prefix = "private-api-endpoint-${random_string.suffix.result}"
  vpc_id      = aws_vpc.main.id

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = [aws_vpc.main.cidr_block]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "API-Gateway-VPC-Endpoint-SG-${random_string.suffix.result}"
  }
}

resource "aws_security_group" "ec2" {
  name_prefix = "test-ec2-instance-${random_string.suffix.result}"
  vpc_id      = aws_vpc.main.id

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "test-ec2-instance-sg-${random_string.suffix.result}"
  }
}


resource "aws_iam_role" "ec2_role" {
  name = "test-ec2-role-${formatdate("YYYYMMDD-HHmmss", resource.time_static.current.rfc3339)}"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "ec2.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_instance_profile" "ec2_profile" {
  name = "test-ec2-profile-${random_string.suffix.result}"
  role = aws_iam_role.ec2_role.name
}

resource "aws_iam_role_policy_attachment" "ssm_policy" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
  role       = aws_iam_role.ec2_role.name
}

resource "aws_iam_role_policy_attachment" "ssm_policy_full" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonSSMFullAccess"
  role       = aws_iam_role.ec2_role.name
}

resource "aws_iam_role_policy_attachment" "cloudwatch_policy" {
  policy_arn = "arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy"
  role       = aws_iam_role.ec2_role.name
}



resource "aws_route53_zone" "private" {
  name = var.domain_name
  
  vpc {
    vpc_id = aws_vpc.main.id
  }

  tags = {
    Name = "private-api-zone"
  }
}

resource "aws_acm_certificate" "certificate" {
  provider          = aws.acm_region
  domain_name       = var.domain_name
  validation_method = "DNS"

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_route53_record" "cert_validation" {
  for_each = {
    for dvo in aws_acm_certificate.certificate.domain_validation_options : dvo.domain_name => {
      name    = dvo.resource_record_name
      record  = dvo.resource_record_value
      type    = dvo.resource_record_type
    }
  }

  zone_id = aws_route53_zone.private.id
  name    = each.value.name
  type    = each.value.type
  records = [each.value.record]
  ttl     = 60
}

resource "aws_acm_certificate_validation" "certificate" {
  provider                = aws.acm_region
  certificate_arn         = aws_acm_certificate.certificate.arn
  validation_record_fqdns = [for record in aws_route53_record.cert_validation : record.fqdn]
}


resource "aws_vpc_endpoint" "execute_api" {
  vpc_id              = aws_vpc.main.id
  service_name        = "com.amazonaws.${data.aws_region.current.name}.execute-api"
  vpc_endpoint_type   = "Interface"
  private_dns_enabled = true
  subnet_ids          = [aws_subnet.private_1.id, aws_subnet.private_2.id]
  security_group_ids  = [aws_security_group.vpc_endpoint.id]

  tags = {
    Name = "API Gateway VPC Endpoint"
  }
}

resource "aws_iam_role" "lambda_role" {
  name = "private-lambda-role-${random_string.suffix.result}"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_vpc_access" {
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaVPCAccessExecutionRole"
  role       = aws_iam_role.lambda_role.name
}

resource "aws_security_group" "lambda_sg" {
  name_prefix = "lambda-sg-${random_string.suffix.result}"
  vpc_id      = aws_vpc.main.id

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "Lambda-SG-${random_string.suffix.result}"
  }
}


resource "aws_lambda_function" "private_lambda" {
  filename      = "lambda_function.zip"
  function_name = "private-api-lambda-${random_string.suffix.result}"
  role          = aws_iam_role.lambda_role.arn
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.9"

  vpc_config {
    subnet_ids         = [aws_subnet.private_1.id, aws_subnet.private_2.id]
    security_group_ids = [aws_security_group.lambda_sg.id]
  }

  environment {
    variables = {
      ENV = "production"
    }
  }
}

data "archive_file" "lambda_zip" {
  type        = "zip"
  output_path = "lambda_function.zip"
  source {
    content  = <<EOF
import json
import http.client
from datetime import datetime

def get_website_content(host, path="/"):
    conn = http.client.HTTPSConnection(host)
    conn.request("GET", path)
    response = conn.getresponse()
    content = response.read().decode('utf-8')
    conn.close()
    return response.status, content

def lambda_handler(event, context):
    try:
        # Test connections and get content
        aws_status, aws_content = get_website_content("aws.amazon.com")
        
        # Find the title in the content (simple example)
        aws_title = aws_content.split('<title>')[1].split('</title>')[0] if '<title>' in aws_content else 'Title not found'

        test_results = {
            "timestamp": datetime.now().isoformat(),
            "function_name": context.function_name,
            "internet_connectivity_test": {
                "status": "Success",
                "message": "Successfully connected to external website",
                "aws_status_code": aws_status,
                "aws_page_title": aws_title,
                "test_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        }

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps(test_results, indent=2)
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'error': str(e),
                'message': 'Failed to test internet connectivity'
            })
        }
EOF
    filename = "lambda_function.py"
  }
}




resource "aws_vpc_endpoint" "ssm" {
  vpc_id              = aws_vpc.main.id
  service_name        = "com.amazonaws.${data.aws_region.current.name}.ssm"
  vpc_endpoint_type   = "Interface"
  private_dns_enabled = true
  subnet_ids          = [aws_subnet.private_1.id, aws_subnet.private_2.id]
  security_group_ids  = [aws_security_group.vpc_endpoint.id]
}

resource "aws_vpc_endpoint" "ssmmessages" {
  vpc_id              = aws_vpc.main.id
  service_name        = "com.amazonaws.${data.aws_region.current.name}.ssmmessages"
  vpc_endpoint_type   = "Interface"
  private_dns_enabled = true
  subnet_ids          = [aws_subnet.private_1.id, aws_subnet.private_2.id]
  security_group_ids  = [aws_security_group.vpc_endpoint.id]
}

resource "aws_vpc_endpoint" "ec2messages" {
  vpc_id              = aws_vpc.main.id
  service_name        = "com.amazonaws.${data.aws_region.current.name}.ec2messages"
  vpc_endpoint_type   = "Interface"
  private_dns_enabled = true
  subnet_ids          = [aws_subnet.private_1.id, aws_subnet.private_2.id]
  security_group_ids  = [aws_security_group.vpc_endpoint.id]
}



resource "aws_api_gateway_rest_api" "private_api" {
  name = "private-api-tutorial"
  
  endpoint_configuration {
    types            = ["PRIVATE"]
    vpc_endpoint_ids = [aws_vpc_endpoint.execute_api.id]
  }
}

resource "aws_api_gateway_rest_api_policy" "domain_policy" {
  rest_api_id = aws_api_gateway_rest_api.private_api.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = "*"
        Action = "execute-api:Invoke"
        Resource = "${aws_api_gateway_rest_api.private_api.execution_arn}/*"
      },
      {
        Effect = "Deny"
        Principal = "*"
        Action = "execute-api:Invoke"
        Resource = "${aws_api_gateway_rest_api.private_api.execution_arn}/*"
        Condition = {
          StringNotEquals = {
            "aws:SourceVpce": aws_vpc_endpoint.execute_api.id
          }
        }
      }
    ]
  })
}


resource "aws_instance" "test" {
  ami           = data.aws_ami.amazon_linux_2.id
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.private_1.id

  vpc_security_group_ids = [aws_security_group.ec2.id]
  iam_instance_profile   = aws_iam_instance_profile.ec2_profile.name

user_data = <<-EOF
            #!/bin/bash
            # Install and start SSM Agent
            cd /tmp
            sudo yum install -y https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/linux_amd64/amazon-ssm-agent.rpm
            sudo systemctl enable amazon-ssm-agent
            sudo systemctl start amazon-ssm-agent

            # Rest of your existing user data
            yum update -y
            yum install -y curl jq

            # Install AWS CLI
            curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
            yum install -y unzip
            unzip awscliv2.zip
            ./aws/install

            # Create a test script
            cat <<'TEST' > /home/ec2-user/test-api.sh
            #!/bin/bash
            echo "Testing API endpoint: https://${var.domain_name}/lambda"
            curl -v https://${var.domain_name}/lambda
            TEST

            chmod +x /home/ec2-user/test-api.sh
            EOF



  tags = {
    Name = "API-Test-Instance-${random_string.suffix.result}"
  }

  depends_on = [aws_route_table_association.private_1]
}


resource "time_sleep" "wait_for_certificate_validation" {
  depends_on = [aws_acm_certificate_validation.certificate]
  create_duration = "60s"
}

resource "time_sleep" "wait_for_deployment" {
  depends_on = [aws_api_gateway_deployment.api]
  create_duration = "60s"
}

resource "time_sleep" "wait_for_domain" {
  depends_on = [aws_api_gateway_domain_name.api]
  create_duration = "30s"
}

resource "time_sleep" "wait_for_domain_name" {
  depends_on = [
    aws_api_gateway_domain_name.api,
    aws_vpc_endpoint.execute_api,
  ]
  create_duration = "30s"
}


resource "aws_api_gateway_resource" "test" {
  rest_api_id = aws_api_gateway_rest_api.private_api.id
  parent_id   = aws_api_gateway_rest_api.private_api.root_resource_id
  path_part   = "lambda"
}

resource "aws_api_gateway_method" "test" {
  rest_api_id   = aws_api_gateway_rest_api.private_api.id
  resource_id   = aws_api_gateway_resource.test.id
  http_method   = "GET"
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "test" {
  rest_api_id = aws_api_gateway_rest_api.private_api.id
  resource_id = aws_api_gateway_resource.test.id
  http_method = aws_api_gateway_method.test.http_method
  integration_http_method = "POST"
  type        = "AWS_PROXY"
  uri         = aws_lambda_function.private_lambda.invoke_arn

  depends_on = [aws_api_gateway_method.test]
}


resource "aws_lambda_permission" "api_gw" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.private_lambda.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_api_gateway_rest_api.private_api.execution_arn}/*/*"
}

resource "aws_api_gateway_method_response" "test" {
  rest_api_id = aws_api_gateway_rest_api.private_api.id
  resource_id = aws_api_gateway_resource.test.id
  http_method = aws_api_gateway_method.test.http_method
  status_code = "200"

  response_parameters = {
    "method.response.header.Access-Control-Allow-Origin" = true
  }

  response_models = {
    "application/json" = "Empty"
  }

  depends_on = [aws_api_gateway_method.test]
}

resource "aws_api_gateway_integration_response" "test" {
  rest_api_id = aws_api_gateway_rest_api.private_api.id
  resource_id = aws_api_gateway_resource.test.id
  http_method = aws_api_gateway_method.test.http_method
  status_code = aws_api_gateway_method_response.test.status_code

  response_parameters = {
    "method.response.header.Access-Control-Allow-Origin" = "'*'"
  }

  depends_on = [
    aws_api_gateway_integration.test,
    aws_api_gateway_method_response.test
  ]
}


resource "aws_api_gateway_deployment" "api" {
  rest_api_id = aws_api_gateway_rest_api.private_api.id
  
  triggers = {
    redeployment = sha1(jsonencode([
      aws_api_gateway_resource.test.id,
      aws_api_gateway_method.test.id,
      aws_api_gateway_integration.test.id,
      aws_api_gateway_integration_response.test.id,
      aws_api_gateway_method_response.test.id
    ]))
  }

  lifecycle {
    create_before_destroy = true
  }

  depends_on = [
    aws_api_gateway_method.test,
    aws_api_gateway_integration.test,
    aws_api_gateway_integration_response.test,
    aws_api_gateway_method_response.test,
    aws_api_gateway_rest_api_policy.domain_policy
  ]
}


resource "aws_api_gateway_stage" "api" {
  deployment_id = aws_api_gateway_deployment.api.id
  rest_api_id  = aws_api_gateway_rest_api.private_api.id
  stage_name   = "prod"

  depends_on = [
    aws_api_gateway_deployment.api,
    time_sleep.wait_for_deployment
  ]
}

resource "aws_api_gateway_domain_name" "api" {
  domain_name     = var.domain_name
  certificate_arn = aws_acm_certificate.certificate.arn
  security_policy = "TLS_1_2"
  
  endpoint_configuration {
    types = ["PRIVATE"]
  }

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "execute-api:Invoke"
        Effect = "Allow"
        Principal = "*"
        Resource = "*"
      },
      {
        Action = "execute-api:Invoke"
        Effect = "Deny"
        Principal = "*"
        Resource = "*"
        Condition = {
          StringNotEquals = {
            "aws:SourceVpce": aws_vpc_endpoint.execute_api.id
          }
        }
      }
    ]
  })

  depends_on = [
    aws_acm_certificate_validation.certificate,
    time_sleep.wait_for_certificate_validation,
  ]
}

resource "aws_api_gateway_domain_name_access_association" "example" {
  access_association_source      = aws_vpc_endpoint.execute_api.id
  access_association_source_type = "VPCE"
  domain_name_arn               = aws_api_gateway_domain_name.api.arn

  depends_on = [
    aws_api_gateway_domain_name.api,
    aws_vpc_endpoint.execute_api,
    time_sleep.wait_for_domain
  ]
}

resource "aws_api_gateway_base_path_mapping" "api" {
  base_path   = ""
  api_id      = aws_api_gateway_rest_api.private_api.id
  domain_name = aws_api_gateway_domain_name.api.domain_name
  stage_name  = aws_api_gateway_stage.api.stage_name
  domain_name_id = aws_api_gateway_domain_name.api.domain_name_id

  depends_on = [
    aws_api_gateway_stage.api,
    aws_api_gateway_domain_name.api,
    time_sleep.wait_for_domain
  ]

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_route53_record" "api" {
  name    = var.domain_name
  type    = "A"
  zone_id = aws_route53_zone.private.id

  alias {
    name                   = aws_vpc_endpoint.execute_api.dns_entry[0].dns_name
    zone_id                = aws_vpc_endpoint.execute_api.dns_entry[0].hosted_zone_id
    evaluate_target_health = false
  }

  depends_on = [
    aws_api_gateway_domain_name.api,
    aws_vpc_endpoint.execute_api,
    aws_api_gateway_domain_name_access_association.example,
    time_sleep.wait_for_domain
  ]
}
