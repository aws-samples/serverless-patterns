terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

locals {
   name_prefix = var.environment
}

# S3 bucket for data storage
resource "aws_s3_bucket" "data_bucket" {
  bucket = "${local.name_prefix}-${var.s3_bucket_name}"
  force_destroy = true
}

resource "aws_s3_bucket_public_access_block" "data_bucket_pab" {
  bucket = aws_s3_bucket.data_bucket.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

# Upload the script file to S3
resource "aws_s3_object" "file_upload" {
  bucket = aws_s3_bucket.data_bucket.id
  key    = "scripts/glue-zero-etl-script.py"
  source = "glue-zero-etl-script.py"
}

# DynamoDB source table
resource "aws_dynamodb_table" "source_table" {
  name             = "${var.table_name}"
  billing_mode     = "PAY_PER_REQUEST"
  hash_key         = "id"
  stream_enabled   = true
  stream_view_type = "NEW_AND_OLD_IMAGES"

  attribute {
    name = "id"
    type = "S"
  }

  point_in_time_recovery {
    enabled = true
  }
}

# IAM role for Glue Zero-ETL
resource "aws_iam_role" "glue_zero_etl_role" {
  name = "${local.name_prefix}-glue-zero-etl-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "glue.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_role_policy" "glue_zero_etl_policy" {
  name = "${local.name_prefix}-glue-zero-etl-policy"
  role = aws_iam_role.glue_zero_etl_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "dynamodb:DescribeTable",
          "dynamodb:GetRecords",
          "dynamodb:ListStreams",
          "dynamodb:ExportTableToPointInTime",
          "dynamodb:Scan",
          "dynamodb:Query"
        ]
        Resource = [
          aws_dynamodb_table.source_table.arn,
          "${aws_dynamodb_table.source_table.arn}/stream/*"
        ]
      },
      {
        Effect = "Allow"
        Action = [
          "s3:GetObject",
          "s3:PutObject",
          "s3:DeleteObject",
          "s3:ListBucket"
        ]
        Resource = [
          aws_s3_bucket.data_bucket.arn,
          "${aws_s3_bucket.data_bucket.arn}/*"
        ]
      },
      {
        Effect = "Allow"
        Action = [
          "glue:*",
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ]
        Resource = "*"
      }
    ]
  })
}

# Glue Catalog Database
resource "aws_glue_catalog_database" "zero_etl_database" {
  name = "${local.name_prefix}_zero_etl_database"
}

# Glue Job for Zero-ETL
resource "aws_glue_job" "zero_etl_job" {
  name         = "${local.name_prefix}-dynamodb-to-s3-zero-etl"
  role_arn     = aws_iam_role.glue_zero_etl_role.arn
  glue_version = "4.0"

  command {
    script_location = "s3://${aws_s3_bucket.data_bucket.bucket}/scripts/glue-zero-etl-script.py"
    python_version  = "3"
  }

  default_arguments = {
    "--job-language"                     = "python"
    "--job-bookmark-option"              = "job-bookmark-enable"
    "--enable-continuous-cloudwatch-log" = "true"
    "--source-table"                     = aws_dynamodb_table.source_table.name
    "--target-bucket"                    = aws_s3_bucket.data_bucket.bucket
    "--database-name"                    = aws_glue_catalog_database.zero_etl_database.name
  }

  max_retries = 1
  timeout     = 30
}
