variable "aws_region" {
  description = "AWS region for deployment"
  type        = string
  default     = "us-east-1"
}

variable "prefix" {
  description = "Prefix to associate with the resources"
  type        = string
  default     = "s3-lambda-bedrock-tf"
}

provider "aws" {
  region = var.aws_region
}

resource "random_string" "suffix" {
  length  = 8
  special = false
  upper   = false
}

# Data source for current region
data "aws_region" "current" {}

# Data source for current caller identity (account ID)
data "aws_caller_identity" "current" {}

# Create ZIP archive of Lambda function
data "archive_file" "lambda_zip" {
  type        = "zip"
  source_file = "${path.module}/src/app.py"
  output_path = "${path.module}/lambda_function.zip"
}

# S3 bucket for storing images
resource "aws_s3_bucket" "image_bucket" {
  bucket        = "${lower(var.prefix)}-image-analysis-bucket-${random_string.suffix.result}"
  force_destroy = true
}

# Create images folder in S3 bucket
resource "aws_s3_object" "images_folder" {
  bucket = aws_s3_bucket.image_bucket.id
  key    = "images/"
  source = "/dev/null"
}

# S3 bucket versioning
resource "aws_s3_bucket_versioning" "image_bucket_versioning" {
  bucket = aws_s3_bucket.image_bucket.id
  versioning_configuration {
    status = "Enabled"
  }
}

# S3 bucket server side encryption
resource "aws_s3_bucket_server_side_encryption_configuration" "image_bucket_encryption" {
  bucket = aws_s3_bucket.image_bucket.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

# Create CloudWatch Log Group for Lambda
resource "aws_cloudwatch_log_group" "lambda_log_group" {
  name              = "/aws/lambda/${lower(var.prefix)}-image-analysis"
  retention_in_days = 14
  
  lifecycle {
    prevent_destroy = false
  }
}

# IAM Policy for Lambda function
resource "aws_iam_policy" "lambda_policy" {
  name        = "${lower(var.prefix)}-ImageAnalysisPolicy-${random_string.suffix.result}"
  path        = "/"
  description = "IAM policy for Lambda function to access S3, Bedrock Nova Lite, and S3 tagging"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "s3:GetObjectAcl",
          "s3:GetObject",
          "s3:ListAllMyBuckets",
          "s3:ListBucketVersions",
          "s3:GetObjectAttributes",
          "s3:ListBucket",
          "s3:PutObjectTagging",
          "s3:GetObjectTagging"
        ]
        Resource = [
          aws_s3_bucket.image_bucket.arn,
          "${aws_s3_bucket.image_bucket.arn}/*"
        ]
      },
      {
        Effect = "Allow"
        Action = [
          "bedrock:InvokeModel",
          "bedrock:InvokeModelWithResponseStream"
        ]
        Resource = [
          "arn:aws:bedrock:${var.aws_region}::foundation-model/amazon.nova-lite-v1:0"
        ]
      },
      {
        Effect = "Allow"
        Action = [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents",
          "logs:DescribeLogGroups",
          "logs:DescribeLogStreams"
        ]
        Resource = [
          "arn:aws:logs:${var.aws_region}:${data.aws_caller_identity.current.account_id}:log-group:/aws/lambda/${lower(var.prefix)}-image-analysis",
          "arn:aws:logs:${var.aws_region}:${data.aws_caller_identity.current.account_id}:log-group:/aws/lambda/${lower(var.prefix)}-image-analysis:*"
        ]
      }
    ]
  })
}

# IAM role for Lambda function
resource "aws_iam_role" "lambda_role" {
  name = "${lower(var.prefix)}-image-analysis-role-${random_string.suffix.result}"

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

# Attach custom policy to Lambda role
resource "aws_iam_role_policy_attachment" "lambda_policy_attachment" {
  policy_arn = aws_iam_policy.lambda_policy.arn
  role       = aws_iam_role.lambda_role.name
}

# Attach basic execution policy for CloudWatch logs
resource "aws_iam_role_policy_attachment" "lambda_basic_execution" {
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
  role       = aws_iam_role.lambda_role.name
}

# Lambda function
resource "aws_lambda_function" "image_analysis_function" {
  filename         = data.archive_file.lambda_zip.output_path
  function_name    = "${lower(var.prefix)}-image-analysis"
  role            = aws_iam_role.lambda_role.arn
  handler         = "app.lambda_handler"
  source_code_hash = data.archive_file.lambda_zip.output_base64sha256
  runtime         = "python3.13"
  timeout         = 120
  memory_size     = 1024
  description     = "Lambda to analyze images using Amazon Nova Lite and add descriptive tags"

  environment {
    variables = {
      LOG_LEVEL = "INFO"
      AWS_REGION_CUSTOM = var.aws_region
      NOVA_MODEL_ID = "amazon.nova-lite-v1:0"
    }
  }

  depends_on = [
    aws_iam_role_policy_attachment.lambda_policy_attachment,
    aws_iam_role_policy_attachment.lambda_basic_execution,
    aws_cloudwatch_log_group.lambda_log_group
  ]
}

# Lambda permission for S3 to invoke the function
resource "aws_lambda_permission" "s3_invoke" {
  statement_id  = "AllowExecutionFromS3Bucket"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.image_analysis_function.function_name
  principal     = "s3.amazonaws.com"
  source_arn    = aws_s3_bucket.image_bucket.arn
}

# S3 bucket notification for images
resource "aws_s3_bucket_notification" "bucket_notification" {
  bucket = aws_s3_bucket.image_bucket.id

  # Lambda function trigger for JPG images
  lambda_function {
    lambda_function_arn = aws_lambda_function.image_analysis_function.arn
    events              = ["s3:ObjectCreated:Put"]
    filter_prefix       = "images/"
    filter_suffix       = ".jpg"
  }

  # Lambda function trigger for JPEG images
  lambda_function {
    lambda_function_arn = aws_lambda_function.image_analysis_function.arn
    events              = ["s3:ObjectCreated:Put"]
    filter_prefix       = "images/"
    filter_suffix       = ".jpeg"
  }

  # Lambda function trigger for PNG images
  lambda_function {
    lambda_function_arn = aws_lambda_function.image_analysis_function.arn
    events              = ["s3:ObjectCreated:Put"]
    filter_prefix       = "images/"
    filter_suffix       = ".png"
  }

  depends_on = [aws_lambda_permission.s3_invoke]
}

# Outputs
output "lambda_function_arn" {
  description = "The ARN of the Lambda function"
  value       = aws_lambda_function.image_analysis_function.arn
}

output "s3_image_bucket" {
  description = "The S3 bucket for image uploads"
  value       = aws_s3_bucket.image_bucket.id
}

output "cloudwatch_log_group" {
  description = "The CloudWatch Log Group for Lambda function"
  value       = aws_cloudwatch_log_group.lambda_log_group.name
}

output "aws_region" {
  description = "The AWS region used for deployment"
  value       = var.aws_region
}