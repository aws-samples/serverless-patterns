provider "aws" {
  region = var.aws_region
}

# Data sources
data "aws_caller_identity" "current" {}
data "aws_region" "current" {}

# VPC for Lambda Managed Instances
resource "aws_vpc" "lambda_managed_instances_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name = "lambda-managed-instances-vpc"
  }
}

# Internet Gateway
resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.lambda_managed_instances_vpc.id

  tags = {
    Name = "lambda-managed-instances-igw"
  }
}

# Public subnets for NAT gateways
resource "aws_subnet" "public" {
  count = 2

  vpc_id                  = aws_vpc.lambda_managed_instances_vpc.id
  cidr_block              = "10.0.${count.index + 1}.0/24"
  availability_zone       = data.aws_availability_zones.available.names[count.index]
  map_public_ip_on_launch = true

  tags = {
    Name = "lambda-managed-instances-public-${count.index + 1}"
  }
}

# Private subnets for Lambda Managed Instances
resource "aws_subnet" "private" {
  count = 2

  vpc_id            = aws_vpc.lambda_managed_instances_vpc.id
  cidr_block        = "10.0.${count.index + 10}.0/24"
  availability_zone = data.aws_availability_zones.available.names[count.index]

  tags = {
    Name = "lambda-managed-instances-private-${count.index + 1}"
  }
}

# Data source for availability zones
data "aws_availability_zones" "available" {
  state = "available"
}

# Elastic IPs for NAT gateways
resource "aws_eip" "nat" {
  count = 2

  domain     = "vpc"
  depends_on = [aws_internet_gateway.igw]

  tags = {
    Name = "lambda-managed-instances-nat-eip-${count.index + 1}"
  }
}

# NAT Gateways
resource "aws_nat_gateway" "nat" {
  count = 2

  allocation_id = aws_eip.nat[count.index].id
  subnet_id     = aws_subnet.public[count.index].id

  tags = {
    Name = "lambda-managed-instances-nat-${count.index + 1}"
  }

  depends_on = [aws_internet_gateway.igw]
}

# Route table for public subnets
resource "aws_route_table" "public" {
  vpc_id = aws_vpc.lambda_managed_instances_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }

  tags = {
    Name = "lambda-managed-instances-public-rt"
  }
}

# Route table associations for public subnets
resource "aws_route_table_association" "public" {
  count = 2

  subnet_id      = aws_subnet.public[count.index].id
  route_table_id = aws_route_table.public.id
}

# Route tables for private subnets
resource "aws_route_table" "private" {
  count = 2

  vpc_id = aws_vpc.lambda_managed_instances_vpc.id

  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.nat[count.index].id
  }

  tags = {
    Name = "lambda-managed-instances-private-rt-${count.index + 1}"
  }
}

# Route table associations for private subnets
resource "aws_route_table_association" "private" {
  count = 2

  subnet_id      = aws_subnet.private[count.index].id
  route_table_id = aws_route_table.private[count.index].id
}

# Security Group for Lambda Managed Instances
resource "aws_security_group" "lambda_managed_instances" {
  name_prefix = "lambda-managed-instances-"
  vpc_id      = aws_vpc.lambda_managed_instances_vpc.id

  # Allow all outbound traffic
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "lambda-managed-instances-sg"
  }
}

# IAM role for Lambda function
resource "aws_iam_role" "lambda_role" {
  name = "hello-world-managed-instances-role"

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

# IAM policy attachment for Lambda basic execution
resource "aws_iam_role_policy_attachment" "lambda_basic_execution" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# IAM role for Lambda Capacity Provider Operator
# https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances-operator-role.html
resource "aws_iam_role" "capacity_provider_role" {
  name = "lambda-capacity-provider-role"

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

# IAM policy for Lambda Capacity Provider Operator
resource "aws_iam_role_policy" "capacity_provider_policy" {
  name = "lambda-capacity-provider-policy"
  role = aws_iam_role.capacity_provider_role.id

  policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Effect" : "Allow",
        "Action" : [
          "ec2:RunInstances",
          "ec2:CreateTags",
          "ec2:AttachNetworkInterface"
        ],
        "Resource" : [
          "arn:aws:ec2:*:*:instance/*",
          "arn:aws:ec2:*:*:network-interface/*",
          "arn:aws:ec2:*:*:volume/*"
        ],
        "Condition" : {
          "StringEquals" : {
            "ec2:ManagedResourceOperator" : "scaler.lambda.amazonaws.com"
          }
        }
      },
      {
        "Effect" : "Allow",
        "Action" : [
          "ec2:DescribeAvailabilityZones",
          "ec2:DescribeCapacityReservations",
          "ec2:DescribeInstances",
          "ec2:DescribeInstanceStatus",
          "ec2:DescribeInstanceTypeOfferings",
          "ec2:DescribeInstanceTypes",
          "ec2:DescribeSecurityGroups",
          "ec2:DescribeSubnets"
        ],
        "Resource" : "*"
      },
      {
        "Effect" : "Allow",
        "Action" : [
          "ec2:RunInstances",
          "ec2:CreateNetworkInterface"
        ],
        "Resource" : [
          "arn:aws:ec2:*:*:subnet/*",
          "arn:aws:ec2:*:*:security-group/*"
        ]
      },
      {
        "Effect" : "Allow",
        "Action" : [
          "ec2:RunInstances"
        ],
        "Resource" : [
          "arn:aws:ec2:*:*:image/*"
        ],
        "Condition" : {
          "StringEquals" : {
            "ec2:Owner" : "amazon"
          }
        }
      }
    ]
  })
}

# Create Lambda function package
data "archive_file" "lambda_zip" {
  type        = "zip"
  source_dir  = "${path.module}/lambda"
  output_path = "${path.module}/lambda-function.zip"
}

# Lambda function
resource "aws_lambda_function" "hello_world" {
  filename         = data.archive_file.lambda_zip.output_path
  function_name    = "hello-world-managed-instances-tf"
  role             = aws_iam_role.lambda_role.arn
  handler          = "hello-world.handler"
  runtime          = "nodejs24.x"
  architectures    = ["arm64"]
  source_code_hash = data.archive_file.lambda_zip.output_base64sha256
  memory_size      = 2048
  publish          = true

  description = "Simple Hello World Lambda function on Managed Instances"

  logging_config {
    log_format = "JSON"
  }

  capacity_provider_config {
    lambda_managed_instances_capacity_provider_config {
      capacity_provider_arn = aws_lambda_capacity_provider.lambda_capacity_provider.arn
    }
  }

  depends_on = [
    aws_iam_role_policy_attachment.lambda_basic_execution,
    aws_cloudwatch_log_group.lambda_logs,
    aws_lambda_capacity_provider.lambda_capacity_provider,
  ]
}

# Lambda alias for LATEST_PUBLISHED
resource "aws_lambda_alias" "live" {
  name             = "live"
  description      = "Alias pointing to the latest published version"
  function_name    = aws_lambda_function.hello_world.function_name
  function_version = aws_lambda_function.hello_world.version
}

# CloudWatch Log Group for Lambda function
resource "aws_cloudwatch_log_group" "lambda_logs" {
  name              = "/aws/lambda/hello-world-managed-instances-tf"
  retention_in_days = 14
}

# Lambda Capacity Provider
resource "aws_lambda_capacity_provider" "lambda_capacity_provider" {
  name = "lambda-capacity-provider"

  vpc_config {
    subnet_ids         = aws_subnet.private[*].id
    security_group_ids = [aws_security_group.lambda_managed_instances.id]
  }

  instance_requirements {
    architectures = ["arm64"]
  }

  permissions_config {
    capacity_provider_operator_role_arn = aws_iam_role.capacity_provider_role.arn
  }
}

