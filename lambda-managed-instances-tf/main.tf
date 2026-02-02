# Lambda Hello World on Lambda Managed Instances - Terraform Implementation

terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.25"
    }
    archive = {
      source  = "hashicorp/archive"
      version = "~> 2.4"
    }
    null = {
      source  = "hashicorp/null"
      version = "~> 3.2"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# Local variables
locals {
  function_name = "hello-world-managed-instances-tf"
  log_group_name = "/demo/lambda/${local.function_name}"
}

# Data source to get current AWS account and region
data "aws_caller_identity" "current" {}
data "aws_region" "current" {}

# Create ZIP archive of Lambda function
data "archive_file" "lambda_zip" {
  type        = "zip"
  source_dir  = "${path.module}/lambda"
  output_path = "${path.module}/lambda-function.zip"
}

# CloudWatch Log Group
resource "aws_cloudwatch_log_group" "demo_log_group" {
  name              = local.log_group_name
  retention_in_days = 14
  
  tags = {
    Name        = "DemoLogGroup"
    Environment = "demo"
  }
}

# IAM role for Lambda function
resource "aws_iam_role" "lambda_role" {
  name = "${local.function_name}-role"

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

  tags = {
    Name        = "${local.function_name}-role"
    Environment = "demo"
  }
}

# IAM policy attachment for basic Lambda execution
resource "aws_iam_role_policy_attachment" "lambda_basic_execution" {
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
  role       = aws_iam_role.lambda_role.name
}

# VPC for Lambda Managed Instances
resource "aws_vpc" "lambda_managed_instances_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name        = "LambdaManagedInstancesVPC"
    Environment = "demo"
  }
}

# Internet Gateway
resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.lambda_managed_instances_vpc.id

  tags = {
    Name        = "LambdaManagedInstancesIGW"
    Environment = "demo"
  }
}

# Public subnets (matching CDK CIDR blocks)
resource "aws_subnet" "public_subnet_1" {
  vpc_id                  = aws_vpc.lambda_managed_instances_vpc.id
  cidr_block              = "10.0.0.0/19"
  availability_zone       = data.aws_availability_zones.available.names[0]
  map_public_ip_on_launch = true

  tags = {
    Name                = "LambdaManagedInstancesPublicSubnet1"
    Environment         = "demo"
    "aws-cdk:subnet-name" = "Public"
    "aws-cdk:subnet-type" = "Public"
  }
}

resource "aws_subnet" "public_subnet_2" {
  vpc_id                  = aws_vpc.lambda_managed_instances_vpc.id
  cidr_block              = "10.0.32.0/19"
  availability_zone       = data.aws_availability_zones.available.names[1]
  map_public_ip_on_launch = true

  tags = {
    Name                = "LambdaManagedInstancesPublicSubnet2"
    Environment         = "demo"
    "aws-cdk:subnet-name" = "Public"
    "aws-cdk:subnet-type" = "Public"
  }
}

resource "aws_subnet" "public_subnet_3" {
  vpc_id                  = aws_vpc.lambda_managed_instances_vpc.id
  cidr_block              = "10.0.64.0/19"
  availability_zone       = data.aws_availability_zones.available.names[2]
  map_public_ip_on_launch = true

  tags = {
    Name                = "LambdaManagedInstancesPublicSubnet3"
    Environment         = "demo"
    "aws-cdk:subnet-name" = "Public"
    "aws-cdk:subnet-type" = "Public"
  }
}

# Private subnets (matching CDK CIDR blocks)
resource "aws_subnet" "private_subnet_1" {
  vpc_id            = aws_vpc.lambda_managed_instances_vpc.id
  cidr_block        = "10.0.96.0/19"
  availability_zone = data.aws_availability_zones.available.names[0]

  tags = {
    Name                = "LambdaManagedInstancesPrivateSubnet1"
    Environment         = "demo"
    "aws-cdk:subnet-name" = "Private"
    "aws-cdk:subnet-type" = "Private"
  }
}

resource "aws_subnet" "private_subnet_2" {
  vpc_id            = aws_vpc.lambda_managed_instances_vpc.id
  cidr_block        = "10.0.128.0/19"
  availability_zone = data.aws_availability_zones.available.names[1]

  tags = {
    Name                = "LambdaManagedInstancesPrivateSubnet2"
    Environment         = "demo"
    "aws-cdk:subnet-name" = "Private"
    "aws-cdk:subnet-type" = "Private"
  }
}

resource "aws_subnet" "private_subnet_3" {
  vpc_id            = aws_vpc.lambda_managed_instances_vpc.id
  cidr_block        = "10.0.160.0/19"
  availability_zone = data.aws_availability_zones.available.names[2]

  tags = {
    Name                = "LambdaManagedInstancesPrivateSubnet3"
    Environment         = "demo"
    "aws-cdk:subnet-name" = "Private"
    "aws-cdk:subnet-type" = "Private"
  }
}

# Data source for availability zones
data "aws_availability_zones" "available" {
  state = "available"
}

# Elastic IPs for NAT Gateways
resource "aws_eip" "nat_eip_1" {
  domain = "vpc"
  depends_on = [aws_internet_gateway.igw]

  tags = {
    Name        = "LambdaManagedInstancesNATEIP1"
    Environment = "demo"
  }
}

resource "aws_eip" "nat_eip_2" {
  domain = "vpc"
  depends_on = [aws_internet_gateway.igw]

  tags = {
    Name        = "LambdaManagedInstancesNATEIP2"
    Environment = "demo"
  }
}

resource "aws_eip" "nat_eip_3" {
  domain = "vpc"
  depends_on = [aws_internet_gateway.igw]

  tags = {
    Name        = "LambdaManagedInstancesNATEIP3"
    Environment = "demo"
  }
}

# NAT Gateways
resource "aws_nat_gateway" "nat_gateway_1" {
  allocation_id = aws_eip.nat_eip_1.id
  subnet_id     = aws_subnet.public_subnet_1.id

  tags = {
    Name        = "LambdaManagedInstancesNATGateway1"
    Environment = "demo"
  }

  depends_on = [aws_internet_gateway.igw]
}

resource "aws_nat_gateway" "nat_gateway_2" {
  allocation_id = aws_eip.nat_eip_2.id
  subnet_id     = aws_subnet.public_subnet_2.id

  tags = {
    Name        = "LambdaManagedInstancesNATGateway2"
    Environment = "demo"
  }

  depends_on = [aws_internet_gateway.igw]
}

resource "aws_nat_gateway" "nat_gateway_3" {
  allocation_id = aws_eip.nat_eip_3.id
  subnet_id     = aws_subnet.public_subnet_3.id

  tags = {
    Name        = "LambdaManagedInstancesNATGateway3"
    Environment = "demo"
  }

  depends_on = [aws_internet_gateway.igw]
}

# Route table for public subnets
resource "aws_route_table" "public_route_table_1" {
  vpc_id = aws_vpc.lambda_managed_instances_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }

  tags = {
    Name        = "LambdaManagedInstancesPublicRouteTable1"
    Environment = "demo"
  }
}

resource "aws_route_table" "public_route_table_2" {
  vpc_id = aws_vpc.lambda_managed_instances_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }

  tags = {
    Name        = "LambdaManagedInstancesPublicRouteTable2"
    Environment = "demo"
  }
}

resource "aws_route_table" "public_route_table_3" {
  vpc_id = aws_vpc.lambda_managed_instances_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }

  tags = {
    Name        = "LambdaManagedInstancesPublicRouteTable3"
    Environment = "demo"
  }
}

# Route table associations for public subnets
resource "aws_route_table_association" "public_subnet_1_association" {
  subnet_id      = aws_subnet.public_subnet_1.id
  route_table_id = aws_route_table.public_route_table_1.id
}

resource "aws_route_table_association" "public_subnet_2_association" {
  subnet_id      = aws_subnet.public_subnet_2.id
  route_table_id = aws_route_table.public_route_table_2.id
}

resource "aws_route_table_association" "public_subnet_3_association" {
  subnet_id      = aws_subnet.public_subnet_3.id
  route_table_id = aws_route_table.public_route_table_3.id
}

# Route tables for private subnets
resource "aws_route_table" "private_route_table_1" {
  vpc_id = aws_vpc.lambda_managed_instances_vpc.id

  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.nat_gateway_1.id
  }

  tags = {
    Name        = "LambdaManagedInstancesPrivateRouteTable1"
    Environment = "demo"
  }
}

resource "aws_route_table" "private_route_table_2" {
  vpc_id = aws_vpc.lambda_managed_instances_vpc.id

  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.nat_gateway_2.id
  }

  tags = {
    Name        = "LambdaManagedInstancesPrivateRouteTable2"
    Environment = "demo"
  }
}

resource "aws_route_table" "private_route_table_3" {
  vpc_id = aws_vpc.lambda_managed_instances_vpc.id

  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.nat_gateway_3.id
  }

  tags = {
    Name        = "LambdaManagedInstancesPrivateRouteTable3"
    Environment = "demo"
  }
}

# Route table associations for private subnets
resource "aws_route_table_association" "private_subnet_1_association" {
  subnet_id      = aws_subnet.private_subnet_1.id
  route_table_id = aws_route_table.private_route_table_1.id
}

resource "aws_route_table_association" "private_subnet_2_association" {
  subnet_id      = aws_subnet.private_subnet_2.id
  route_table_id = aws_route_table.private_route_table_2.id
}

resource "aws_route_table_association" "private_subnet_3_association" {
  subnet_id      = aws_subnet.private_subnet_3.id
  route_table_id = aws_route_table.private_route_table_3.id
}

# Security Group for Lambda Managed Instances
resource "aws_security_group" "lambda_security_group" {
  name_prefix = "${local.function_name}-sg"
  vpc_id      = aws_vpc.lambda_managed_instances_vpc.id

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
    description = "Allow all outbound traffic by default"
  }

  tags = {
    Name        = "LambdaManagedInstancesSecurityGroup"
    Environment = "demo"
  }
}

# Restrict default security group (matching CDK behavior)
resource "aws_default_security_group" "default" {
  vpc_id = aws_vpc.lambda_managed_instances_vpc.id

  # Remove all ingress and egress rules
  ingress = []
  egress  = []

  tags = {
    Name        = "LambdaManagedInstancesDefaultSecurityGroup"
    Environment = "demo"
  }
}

# Lambda function
resource "aws_lambda_function" "hello_world_function" {
  filename         = data.archive_file.lambda_zip.output_path
  function_name    = local.function_name
  role            = aws_iam_role.lambda_role.arn
  handler         = "hello-world.lambda_handler"
  source_code_hash = data.archive_file.lambda_zip.output_base64sha256
  runtime         = "python3.13"
  architectures   = ["arm64"]
  description     = "Simple Hello World Lambda function on Managed Instances"
  memory_size     = 2048
  publish         = true

  logging_config {
    log_format = "JSON"
    log_group  = aws_cloudwatch_log_group.demo_log_group.name
  }

  # Lambda Managed Instances configuration
  capacity_provider_config {
    lambda_managed_instances_capacity_provider_config {
      capacity_provider_arn = aws_lambda_capacity_provider.lambda_capacity_provider.arn
    }
  }

  # Force recreation when capacity provider changes
  lifecycle {
    replace_triggered_by = [
      aws_lambda_capacity_provider.lambda_capacity_provider
    ]
  }

  depends_on = [
    aws_iam_role_policy_attachment.lambda_basic_execution,
    aws_cloudwatch_log_group.demo_log_group,
    aws_lambda_capacity_provider.lambda_capacity_provider,
  ]

  tags = {
    Name        = local.function_name
    Environment = "demo"
  }
}

# Lambda alias for managed instances (required for invocation)
resource "aws_lambda_alias" "hello_world_alias" {
  name             = "live"
  description      = "Alias for Lambda Managed Instances function"
  function_name    = aws_lambda_function.hello_world_function.function_name
  function_version = aws_lambda_function.hello_world_function.version
}

# IAM role for Lambda Capacity Provider
resource "aws_iam_role" "capacity_provider_role" {
  name = "${local.function_name}-capacity-provider-role"

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

  tags = {
    Name        = "${local.function_name}-capacity-provider-role"
    Environment = "demo"
  }
}

# Attach AWS managed policy for Lambda Managed EC2 Resource Operator
resource "aws_iam_role_policy_attachment" "capacity_provider_managed_policy" {
  policy_arn = "arn:aws:iam::aws:policy/AWSLambdaManagedEC2ResourceOperator"
  role       = aws_iam_role.capacity_provider_role.name
}

# Lambda Capacity Provider for Managed Instances
resource "aws_lambda_capacity_provider" "lambda_capacity_provider" {
  name = "lambda-capacity-provider-tf"
  
  vpc_config {
    subnet_ids         = [aws_subnet.private_subnet_1.id, aws_subnet.private_subnet_2.id, aws_subnet.private_subnet_3.id]
    security_group_ids = [aws_security_group.lambda_security_group.id]
  }

  instance_requirements {
    architectures = ["arm64"]
  }

  permissions_config {
    capacity_provider_operator_role_arn = aws_iam_role.capacity_provider_role.arn
  }

  tags = {
    Name        = "lambda-capacity-provider-tf"
    Environment = "demo"
  }
}

# Function association with capacity provider is configured in the Lambda function resource above