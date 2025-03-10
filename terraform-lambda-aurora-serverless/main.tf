# VPC and Networking
resource "aws_vpc" "lambda_vpc" {
  cidr_block           = var.vpc_cidr
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name        = "lambda-aurora-vpc"
    Environment = var.environment
  }
}

# Internet Gateway
resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.lambda_vpc.id

  tags = {
    Name        = "main-igw"
    Environment = var.environment
  }
}

# Public Subnet for NAT Gateway
resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.lambda_vpc.id
  cidr_block              = cidrsubnet(var.vpc_cidr, 8, 0)
  availability_zone       = "${var.aws_region}a"
  map_public_ip_on_launch = true

  tags = {
    Name        = "public-subnet"
    Environment = var.environment
  }
}

# Private Subnets for Lambda and Aurora
resource "aws_subnet" "lambda_subnet_1" {
  vpc_id            = aws_vpc.lambda_vpc.id
  cidr_block        = cidrsubnet(var.vpc_cidr, 8, 1)
  availability_zone = "${var.aws_region}a"

  tags = {
    Name        = "lambda-aurora-subnet-1"
    Environment = var.environment
  }
}

resource "aws_subnet" "lambda_subnet_2" {
  vpc_id            = aws_vpc.lambda_vpc.id
  cidr_block        = cidrsubnet(var.vpc_cidr, 8, 2)
  availability_zone = "${var.aws_region}b"

  tags = {
    Name        = "lambda-aurora-subnet-2"
    Environment = var.environment
  }
}

# NAT Gateway
resource "aws_eip" "nat" {
  domain = "vpc"
}

resource "aws_nat_gateway" "main" {
  allocation_id = aws_eip.nat.id
  subnet_id     = aws_subnet.public.id

  tags = {
    Name        = "main-nat"
    Environment = var.environment
  }
}

# Route Tables
resource "aws_route_table" "public" {
  vpc_id = aws_vpc.lambda_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main.id
  }

  tags = {
    Name        = "public-rt"
    Environment = var.environment
  }
}

resource "aws_route_table" "private" {
  vpc_id = aws_vpc.lambda_vpc.id

  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.main.id
  }

  tags = {
    Name        = "private-rt"
    Environment = var.environment
  }
}

# Route Table Associations
resource "aws_route_table_association" "public" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.public.id
}

resource "aws_route_table_association" "private_1" {
  subnet_id      = aws_subnet.lambda_subnet_1.id
  route_table_id = aws_route_table.private.id
}

resource "aws_route_table_association" "private_2" {
  subnet_id      = aws_subnet.lambda_subnet_2.id
  route_table_id = aws_route_table.private.id
}

# Security Groups
resource "aws_security_group" "aurora_sg" {
  name        = "aurora-security-group"
  description = "Security group for Aurora Serverless"
  vpc_id      = aws_vpc.lambda_vpc.id

  ingress {
    from_port   = 3306
    to_port     = 3306
    protocol    = "tcp"
    cidr_blocks = [var.vpc_cidr]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name        = "aurora-sg"
    Environment = var.environment
  }
}

# Secrets Manager Configuration - stores db credentials

resource "aws_secretsmanager_secret" "aurora_secret" {
  name = "aurora-db-credentials"
  tags = {
    Environment = var.environment
  }
}

resource "aws_secretsmanager_secret_version" "aurora_secret_version" {
  secret_id = aws_secretsmanager_secret.aurora_secret.id
  secret_string = jsonencode({
    username = var.db_username
    password = var.db_password
  })
}


# Aurora Configuration
resource "aws_db_subnet_group" "aurora_subnet_group" {
  name       = "aurora-subnet-group"
  subnet_ids = [aws_subnet.lambda_subnet_1.id, aws_subnet.lambda_subnet_2.id]

  tags = {
    Name        = "Aurora subnet group"
    Environment = var.environment
  }
}

resource "aws_rds_cluster" "aurora_cluster" {
  cluster_identifier     = "aurora-serverless-cluster"
  engine                 = "aurora-mysql"
  engine_version         = "8.0.mysql_aurora.3.04.1"
  engine_mode            = "provisioned"
  database_name          = var.database_name
  master_username        = jsondecode(aws_secretsmanager_secret_version.aurora_secret_version.secret_string)["username"]
  master_password        = jsondecode(aws_secretsmanager_secret_version.aurora_secret_version.secret_string)["password"]
  storage_encrypted      = true
  skip_final_snapshot    = true
  db_subnet_group_name   = aws_db_subnet_group.aurora_subnet_group.name
  vpc_security_group_ids = [aws_security_group.aurora_sg.id]

  serverlessv2_scaling_configuration {
    min_capacity = 0.5
    max_capacity = 16.0
  }

  tags = {
    Environment = var.environment
  }
  # Add explicit dependencies
  depends_on = [
    aws_vpc.lambda_vpc,
    aws_subnet.lambda_subnet_1,
    aws_subnet.lambda_subnet_2,
    aws_security_group.aurora_sg
  ]
}

# Create Aurora Instance
resource "aws_rds_cluster_instance" "aurora_instance" {
  cluster_identifier = aws_rds_cluster.aurora_cluster.id
  instance_class    = "db.serverless"
  engine            = aws_rds_cluster.aurora_cluster.engine
  engine_version    = aws_rds_cluster.aurora_cluster.engine_version

  depends_on = [aws_rds_cluster.aurora_cluster]
}

# IAM Configuration
resource "aws_iam_role" "lambda_role" {
  name = "lambda_aurora_role"
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

resource "aws_iam_role_policy" "lambda_policy" {
  name = "lambda_aurora_policy"
  role = aws_iam_role.lambda_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "rds-data:ExecuteStatement",
          "rds-data:BatchExecuteStatement",
          "rds-data:BeginTransaction",
          "rds-data:CommitTransaction",
          "rds-data:RollbackTransaction",
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents",
          "ec2:CreateNetworkInterface",
          "ec2:DescribeNetworkInterfaces",
          "ec2:DeleteNetworkInterface",
          "secretsmanager:GetSecretValue"
        ]
        Resource = "*"
      }
    ]
  })
}

# Lambda Function
data "archive_file" "lambda_zip" {
  type        = "zip"
  source_dir  = "${path.module}/src/function"
  output_path = "${path.module}/function.zip"
}

resource "aws_lambda_function" "aurora_lambda" {
  depends_on = [
    aws_vpc.lambda_vpc,
    aws_subnet.lambda_subnet_1,
    aws_subnet.lambda_subnet_2,
    aws_security_group.aurora_sg,
    aws_rds_cluster.aurora_cluster,
    aws_iam_role.lambda_role
  ]

  function_name    = var.lambda_function_name
  role             = aws_iam_role.lambda_role.arn
  filename         = data.archive_file.lambda_zip.output_path
  source_code_hash = data.archive_file.lambda_zip.output_base64sha256
  handler          = var.lambda_handler
  runtime          = var.lambda_runtime
  timeout          = var.lambda_timeout
  memory_size      = var.lambda_memory_size

  environment {
    variables = {
      DB_ENDPOINT = aws_rds_cluster.aurora_cluster.endpoint
      DB_NAME     = var.database_name
      SECRET_ARN  = aws_secretsmanager_secret.aurora_secret.arn
    }
  }

  vpc_config {
    subnet_ids         = [aws_subnet.lambda_subnet_1.id, aws_subnet.lambda_subnet_2.id]
    security_group_ids = [aws_security_group.aurora_sg.id]
  }

  tags = {
    Environment = var.environment
  }
}
