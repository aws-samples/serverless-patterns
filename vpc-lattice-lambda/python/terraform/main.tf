# Provider Configuration
provider "aws" {
  region = "us-east-1" # Change this to your desired region
}

# Variables
variable "vpc_cidr" {
  default = "10.0.0.0/16"
}

variable "subnet_cidr" {
  default = "10.0.7.0/24"
}

# VPC Resources
resource "aws_vpc" "vpc_lattice_vpc" {
  cidr_block           = var.vpc_cidr
  enable_dns_support   = true
  enable_dns_hostnames = true
  instance_tenancy     = "default"
}

resource "aws_subnet" "vpc_subnet" {
  vpc_id                  = aws_vpc.vpc_lattice_vpc.id
  cidr_block             = var.subnet_cidr
  availability_zone      = "${data.aws_region.current.name}b"
  map_public_ip_on_launch = false

  tags = {
    Name = "Private-new-availability"
  }
}

# Security Group
resource "aws_security_group" "vpc_lattice_sg" {
  name        = "VPCLatticeServiceNetworkSecurityGroup"
  description = "Security group for VPC LatticeService"
  vpc_id      = aws_vpc.vpc_lattice_vpc.id

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["10.0.0.0/16"]
  }

  egress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# VPC Lattice Resources
resource "aws_vpclattice_service_network" "vl_service_network" {
  name      = "vl-test-service-network"
  auth_type = "NONE"
}

resource "aws_vpclattice_service" "vl_service" {
  name      = "vl-test-service"
  auth_type = "NONE"
}

# IAM Role for Lambda Functions
resource "aws_iam_role" "lambda_role" {
  name = "vpc_lattice_lambda_role"

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

# Attach basic Lambda execution policy
resource "aws_iam_role_policy_attachment" "lambda_basic" {
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
  role       = aws_iam_role.lambda_role.name
}

# Attach VPC access policy for Lambda
resource "aws_iam_role_policy_attachment" "lambda_vpc" {
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaVPCAccessExecutionRole"
  role       = aws_iam_role.lambda_role.name
}

# Lambda Functions
resource "aws_lambda_function" "vl_function_primary" {
  filename         = "primary.zip"
  function_name    = "vl-function-primary"
  role            = aws_iam_role.lambda_role.arn
  handler         = "app.lambda_handler"
  runtime         = "python3.14"
  architectures   = ["x86_64"]
  source_code_hash = filebase64sha256("primary.zip")
}

resource "aws_lambda_function" "vl_function_secondary" {
  filename         = "secondary.zip"
  function_name    = "vl-function-secondary"
  role            = aws_iam_role.lambda_role.arn
  handler         = "app.lambda_handler"
  runtime         = "python3.14"
  architectures   = ["x86_64"]
  source_code_hash = filebase64sha256("secondary.zip")
}

resource "aws_lambda_function" "demo_lambda" {
  filename         = "demolambda.zip"
  function_name    = "demo-lambda"
  role            = aws_iam_role.lambda_role.arn
  handler         = "app.lambda_handler"
  runtime         = "python3.14"
  architectures   = ["x86_64"]
  source_code_hash = filebase64sha256("demolambda.zip")

  vpc_config {
    subnet_ids         = [aws_subnet.vpc_subnet.id]
    security_group_ids = [aws_security_group.vpc_lattice_sg.id]
  }

  environment {
    variables = {
      URL = aws_vpclattice_service.vl_service.dns_entry[0].domain_name
    }
  }
}

# VPC Lattice Target Groups
resource "aws_vpclattice_target_group" "primary_tg" {
  name = "vl-primary-target-group"
  type = "LAMBDA"
  
  config {
    lambda_event_structure_version = "V2"
  }
}

resource "aws_vpclattice_target_group_attachment" "primary_tg_attachment" {
  target_group_identifier = aws_vpclattice_target_group.primary_tg.id
  target {
    id = aws_lambda_function.vl_function_primary.arn
  }
}

resource "aws_vpclattice_target_group" "secondary_tg" {
  name = "vl-secondary-target-group"
  type = "LAMBDA"
  
  config {
    lambda_event_structure_version = "V2"
  }
}

resource "aws_vpclattice_target_group_attachment" "secondary_tg_attachment" {
  target_group_identifier = aws_vpclattice_target_group.secondary_tg.id
  target {
    id = aws_lambda_function.vl_function_secondary.arn
  }
}

# VPC Lattice Listener
resource "aws_vpclattice_listener" "vl_listener" {
  name                = "vl-service-listener"
  protocol            = "HTTPS"
  port               = 443
  service_identifier = aws_vpclattice_service.vl_service.id

  default_action {
    forward {
      target_groups {
        target_group_identifier = aws_vpclattice_target_group.primary_tg.id
        weight                 = 60
      }
      target_groups {
        target_group_identifier = aws_vpclattice_target_group.secondary_tg.id
        weight                 = 40
      }
    }
  }
}

# VPC Lattice Associations
resource "aws_vpclattice_service_network_service_association" "service_association" {
  service_identifier         = aws_vpclattice_service.vl_service.id
  service_network_identifier = aws_vpclattice_service_network.vl_service_network.id
}

resource "aws_vpclattice_service_network_vpc_association" "vpc_association" {
  vpc_identifier            = aws_vpc.vpc_lattice_vpc.id
  service_network_identifier = aws_vpclattice_service_network.vl_service_network.id
  security_group_ids        = [aws_security_group.vpc_lattice_sg.id]
}

# Outputs
output "vl_function_primary_arn" {
  value = aws_lambda_function.vl_function_primary.arn
}

output "vl_function_secondary_arn" {
  value = aws_lambda_function.vl_function_secondary.arn
}

output "vl_service_network_id" {
  value = aws_vpclattice_service_network.vl_service_network.id
}

output "vl_service_id" {
  value = aws_vpclattice_service.vl_service.id
}

output "vl_service_dns" {
  value = aws_vpclattice_service.vl_service.dns_entry[0].domain_name
}

# Data source for current region
data "aws_region" "current" {}
