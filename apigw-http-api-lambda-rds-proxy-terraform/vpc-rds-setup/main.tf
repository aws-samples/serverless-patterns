terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.7.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.1.0"
    }
    archive = {
      source  = "hashicorp/archive"
      version = "~> 2.2.0"
    }
  }

  required_version = "~> 1.0"
}

provider "aws" {
  region = var.aws_region
}

data "aws_caller_identity" "current" {}

locals {
  account_id = data.aws_caller_identity.current.account_id
}

resource "random_string" "random" {
  length           = 6
  special          = false
}

################################################################################
# VPC
################################################################################

resource "aws_vpc" "poc_vpc" {
  cidr_block       = var.vpc_cidr
  instance_tenancy = "default"
}

resource "aws_subnet" "public" {
  count = length(var.public_cidr)
  vpc_id = aws_vpc.poc_vpc.id
  cidr_block = element(var.public_cidr,count.index)
  availability_zone = element(var.azs,count.index)
  map_public_ip_on_launch = true
  tags = {
    Name = "public-subnet-${count.index+1}"
  }
}

resource "aws_subnet" "app" {
  count = length(var.app_cidr)
  vpc_id = aws_vpc.poc_vpc.id
  cidr_block = element(var.app_cidr,count.index)
  availability_zone = element(var.azs,count.index)
  map_public_ip_on_launch = true
  tags = {
    Name = "app-subnet-${count.index+1}"
  }
}

resource "aws_subnet" "db" {
  count = length(var.db_cidr)
  vpc_id = aws_vpc.poc_vpc.id
  cidr_block = element(var.db_cidr,count.index)
  availability_zone = element(var.db_azs,count.index)
  map_public_ip_on_launch = true
  tags = {
    Name = "db-subnet-${count.index+1}"
  }
}

resource "aws_internet_gateway" "poc_vpc_igw" {
  vpc_id = aws_vpc.poc_vpc.id

}

resource "aws_eip" "nat_eip" {}

resource "aws_nat_gateway" "poc_nat_gwy" {
  subnet_id     = aws_subnet.public[0].id
  allocation_id = aws_eip.nat_eip.id
  depends_on = [aws_internet_gateway.poc_vpc_igw, aws_eip.nat_eip]
}

resource "aws_route_table" "public_rt" {
  vpc_id = aws_vpc.poc_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.poc_vpc_igw.id
  }
}

resource "aws_route_table" "private_rt" {
  vpc_id = aws_vpc.poc_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.poc_nat_gwy.id
  }
}

resource "aws_route_table_association" "public" {
  count = length(var.public_cidr)
  subnet_id      = element(aws_subnet.public.*.id,count.index)
  route_table_id = aws_route_table.public_rt.id
}

resource "aws_route_table_association" "private" {
  count = length(var.public_cidr)
  subnet_id      = element(aws_subnet.app.*.id,count.index)
  route_table_id = aws_route_table.private_rt.id
}

resource "aws_security_group" "lambda_sg" {
  name        = "lambda-vpc-access"
  description = "associated with lambda function"
  vpc_id      = aws_vpc.poc_vpc.id

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
  }
}

resource "aws_security_group" "ec2" {
  name        = "internet_out"
  description = "Allow outbound to internet"
  vpc_id      = aws_vpc.poc_vpc.id

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
  }

}

resource "aws_security_group" "db_mysql" {
  name        = "allow_mysql"
  description = "Allow mysql inbound traffic"
  vpc_id      = aws_vpc.poc_vpc.id

  ingress {
    description      = "mysql from private subnets"
    from_port        = 3306
    to_port          = 3306
    protocol         = "tcp"
    cidr_blocks      = var.app_cidr
  }
  
    ingress {
    description      = "mysql from lambda sg"
    from_port        = 3306
    to_port          = 3306
    protocol         = "tcp"
    security_groups      = [aws_security_group.lambda_sg.id]
  }
  

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
  }

}

################################################################################
# RDS
################################################################################

resource "aws_db_subnet_group" "default" {
  name       = "db main"
  subnet_ids = [aws_subnet.db[0].id, aws_subnet.db[1].id, aws_subnet.db[2].id]

  tags = {
    Name = "My DB subnet group"
  }
}

resource "random_password" "db_password" {
  length           = 16
  special          = true
  override_special = "()-_=+"
}

resource "aws_rds_cluster" "aurora_mysql" {
  cluster_identifier      = "aurora-cluster-demo"
  engine                  = "aurora-mysql"
  engine_version          = "5.7.mysql_aurora.2.11.2"
  availability_zones      = ["us-east-1a", "us-east-1b", "us-east-1c"]
  db_subnet_group_name    = aws_db_subnet_group.default.id
  database_name           = "mydb"
  master_username         = "admin"
  master_password         = random_password.db_password.result
  backup_retention_period = 5
  preferred_backup_window = "07:00-09:00"
  skip_final_snapshot     = true
  vpc_security_group_ids  = [aws_security_group.db_mysql.id]
}

resource "aws_rds_cluster_instance" "cluster_instance" {
  identifier         = "aurora-cluster-demo-1"
  cluster_identifier = aws_rds_cluster.aurora_mysql.id
  instance_class     = "db.t3.medium"
  db_subnet_group_name    = aws_db_subnet_group.default.id
  engine             = aws_rds_cluster.aurora_mysql.engine
  engine_version     = aws_rds_cluster.aurora_mysql.engine_version
}

resource "aws_instance" "this" {
  ami           = var.ami_id
  instance_type = "t3.micro"
  count = 1
  vpc_security_group_ids = [aws_security_group.lambda_sg.id, aws_security_group.ec2.id]
  subnet_id = aws_subnet.app[0].id
  associate_public_ip_address = false
  depends_on = [aws_rds_cluster_instance.cluster_instance, aws_secretsmanager_secret_version.sversion, aws_secretsmanager_secret_version.sversion1]
  user_data = <<EOF
#!/bin/bash

sudo yum update
sudo yum install mysql -y

mysql -u admin -p'${random_password.db_password.result}' -h '${aws_rds_cluster_instance.cluster_instance.endpoint}' <<MY_QUERY
CREATE USER '${var.username}'@'%' IDENTIFIED BY '${random_password.lambda_password.result}';
CREATE DATABASE IF NOT EXISTS dbname;
GRANT SELECT, INSERT, UPDATE ON dbname.* TO '${var.username}';
FLUSH PRIVILEGES;
MY_QUERY

echo done
EOF
}

resource "random_password" "lambda_password" {
  length           = 16
  special          = true
  override_special = "()-_=+"
}

resource "aws_secretsmanager_secret" "lambda_secret" {
  name = "lambda_secret"
  recovery_window_in_days = 0
}

resource "aws_secretsmanager_secret_version" "sversion" {
  secret_id = aws_secretsmanager_secret.lambda_secret.id
  secret_string = <<EOF
   {
    "username": "lambda",
    "password": "${random_password.lambda_password.result}"
   }
EOF
}

resource "aws_secretsmanager_secret" "aurora-mysql-secret" {
  name = "aurora-mysql-secret"
  recovery_window_in_days = 0
}

resource "aws_secretsmanager_secret_version" "sversion1" {
  secret_id = aws_secretsmanager_secret.aurora-mysql-secret.id
  secret_string = <<EOF
   {
    "username": "admin",
    "password": "${random_password.db_password.result}"
   }
EOF
}

resource "aws_db_proxy" "mysql_proxy" {
  name                   = var.rds_proxy_name
  debug_logging          = true
  engine_family          = "MYSQL"
  idle_client_timeout    = 1800
  require_tls            = true
  role_arn               = aws_iam_role.rds_proxy.arn
  vpc_security_group_ids = [aws_security_group.db_mysql.id]
  vpc_subnet_ids         = [aws_subnet.app[0].id, aws_subnet.app[1].id]

  auth {
    auth_scheme = "SECRETS"
    description = "RDS Proxy with IAM auth for master user"
    iam_auth    = "REQUIRED"
    secret_arn  = aws_secretsmanager_secret.aurora-mysql-secret.arn
  }
  
  auth {
    auth_scheme = "SECRETS"
    description = "RDS Proxy with IAM auth for lambda"
    iam_auth    = "REQUIRED"
    secret_arn  = aws_secretsmanager_secret.lambda_secret.arn
  }
  depends_on = [aws_cloudwatch_log_group.this]
}

resource "aws_db_proxy_default_target_group" "default" {
  db_proxy_name = aws_db_proxy.mysql_proxy.name

  connection_pool_config {
    connection_borrow_timeout    = 120
    max_connections_percent      = 100
    max_idle_connections_percent = 50
  }
}

resource "aws_db_proxy_target" "db_cluster" {
  db_cluster_identifier  = aws_rds_cluster.aurora_mysql.id
  db_proxy_name          = aws_db_proxy.mysql_proxy.name
  target_group_name      = aws_db_proxy_default_target_group.default.name
  depends_on = [aws_rds_cluster.aurora_mysql, aws_db_proxy.mysql_proxy, aws_rds_cluster_instance.cluster_instance]
}

resource "aws_db_proxy_endpoint" "aurora" {
  db_proxy_name          = aws_db_proxy.mysql_proxy.name
  db_proxy_endpoint_name = "lambda-aurora-proxy"
  vpc_subnet_ids         = aws_subnet.app.*.id
  target_role            = "READ_WRITE"
  vpc_security_group_ids = [aws_security_group.db_mysql.id]
}

// coudwatch 

resource "aws_cloudwatch_log_group" "this" {
  name              = "/aws/rds/proxy/${var.rds_proxy_name}"
  retention_in_days = var.log_retention
}
// IAM Role for rds proxy

resource "aws_iam_role" "rds_proxy" {
  name = "RdsProxyRole-${random_string.random.id}"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Sid    = ""
      Principal = {
        Service = "rds.amazonaws.com"
      }
      }
    ]
  })
}

resource "aws_iam_policy" "rds_proxy_iam" {
  name = "RdsProxySecretsManager-${random_string.random.id}"

  policy = <<POLICY
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "secretsmanager:GetSecretValue",
            "Resource": [
                "${aws_secretsmanager_secret.lambda_secret.arn}",
                "${aws_secretsmanager_secret.aurora-mysql-secret.arn}"
            ]
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": "kms:Decrypt",
            "Resource": "arn:aws:kms:${var.aws_region}:${local.account_id}:key/aws/secretsmanager",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "secretsmanager.${var.aws_region}.amazonaws.com"
                }
            }
        }
    ]
}
POLICY
}

resource "aws_iam_role_policy_attachment" "rds_policy" {
  role       = aws_iam_role.rds_proxy.name
  policy_arn = aws_iam_policy.rds_proxy_iam.arn
}
