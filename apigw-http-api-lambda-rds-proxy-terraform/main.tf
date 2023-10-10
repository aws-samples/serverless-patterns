terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.8.0"
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

 required_version = ">= 0.14.9"
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

// get secret info

data "aws_secretsmanager_secret_version" "creds" {
  secret_id = var.secret_name
}

locals {
  lambda_username = jsondecode(
    data.aws_secretsmanager_secret_version.creds.secret_string
  )
}

###############################################################
# Lambda
###############################################################


resource "aws_s3_bucket" "lambda_bucket" {
  bucket_prefix = var.bucket_name
  force_destroy = true
  tags = {
    Name        = "${var.bucket_name}"
  }
}

resource "aws_s3_bucket_acl" "private_bucket" {
  bucket = aws_s3_bucket.lambda_bucket.id
  acl    = "private"
}

resource "null_resource" "my_lambda_buildstep" {
  triggers = {
    app      = "${base64sha256(file("${path.module}/src/app.py"))}"
    requirements = "${base64sha256(file("${path.module}/src/requirements.txt"))}"
    build        = "${base64sha256(file("${path.module}/src/build.sh"))}"
  }

  provisioner "local-exec" {
    command = "${path.module}/src/build.sh"
  }
}

data "archive_file" "lambda_source" {
  type = "zip"

  source_dir  = "${path.module}/src"
  output_path = "${path.module}/src.zip"
  
  depends_on = [null_resource.my_lambda_buildstep]
}

resource "aws_s3_object" "lambda" {
  bucket = aws_s3_bucket.lambda_bucket.id

  key    = "source.zip"
  source = data.archive_file.lambda_source.output_path

  #etag = filemd5(data.archive_file.lambda_source.output_path)
  depends_on = [null_resource.my_lambda_buildstep, data.archive_file.lambda_source]
  
}

//Define lambda function
resource "aws_lambda_function" "rds_proxy_function" {
  function_name = "rds_proxy_function-${random_string.random.id}"

  s3_bucket = aws_s3_bucket.lambda_bucket.id
  s3_key    = aws_s3_object.lambda.key

  runtime = "python3.7"
  handler = "app.lambda_handler"

  source_code_hash = data.archive_file.lambda_source.output_base64sha256
  
  description = "function to access RDS Aurora via RDS proxy endpoint"

  role = aws_iam_role.lambda_exec.arn
  timeout = 60
  
  vpc_config {
    subnet_ids         = var.vpc_subnets
    security_group_ids = [var.security_group]
  }
  
  environment {
    variables = {
      region: var.aws_region,
      rds_endpoint: var.rds_proxy_endpoint,
      port: 3306,
      username: local.lambda_username.username
      database: "dbname"
    }
  }
  
}

resource "aws_cloudwatch_log_group" "rds_proxy_function" {
  name = "/aws/lambda/${aws_lambda_function.rds_proxy_function.function_name}"

  retention_in_days = var.lambda_log_retention
}

resource "aws_iam_role" "lambda_exec" {
  name = "LambdaRdsProxyRole-${random_string.random.id}"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Sid    = ""
      Principal = {
        Service = "lambda.amazonaws.com"
      }
      }
    ]
  })
}

resource "aws_iam_policy" "lambda-exec-role" {
  name = "LambdaRdsProxyPolicy-${random_string.random.id}"

  policy = <<POLICY
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "rds-db:connect"
            ],
            "Resource": "arn:aws:rds-db:${var.aws_region}:${local.account_id}:dbuser:${var.rds_proxy_resourceid}/*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents",
                "ec2:CreateNetworkInterface",
                "ec2:DescribeNetworkInterfaces",
                "ec2:DeleteNetworkInterface",
                "ec2:AssignPrivateIpAddresses",
                "ec2:UnassignPrivateIpAddresses"
            ],
            "Resource": "*"
        }
    ]
}
POLICY
}

resource "aws_iam_role_policy_attachment" "lambda_policy" {
  role       = aws_iam_role.lambda_exec.name
  policy_arn = aws_iam_policy.lambda-exec-role.arn
}

###############################################################
# API Gateway
###############################################################

resource "aws_apigatewayv2_api" "this" {
  name          = "apigw-http-lambda-rds-proxy"
  protocol_type = "HTTP"
}

resource "aws_cloudwatch_log_group" "api_gw" {
  name = "/aws/api_gw/${aws_apigatewayv2_api.this.name}"

  retention_in_days = var.lambda_log_retention
}

resource "aws_apigatewayv2_stage" "lambda" {
  api_id = aws_apigatewayv2_api.this.id

  name        = "$default"
  auto_deploy = true

  access_log_settings {
    destination_arn = aws_cloudwatch_log_group.api_gw.arn

    format = jsonencode({
      requestId               = "$context.requestId"
      sourceIp                = "$context.identity.sourceIp"
      requestTime             = "$context.requestTime"
      protocol                = "$context.protocol"
      httpMethod              = "$context.httpMethod"
      resourcePath            = "$context.resourcePath"
      routeKey                = "$context.routeKey"
      status                  = "$context.status"
      responseLength          = "$context.responseLength"
      integrationErrorMessage = "$context.integrationErrorMessage"
      }
    )
  }
}

resource "aws_apigatewayv2_integration" "lambda" {
  api_id = aws_apigatewayv2_api.this.id

  integration_uri    = aws_lambda_function.rds_proxy_function.invoke_arn
  integration_type   = "AWS_PROXY"
  integration_method = "POST"
}

resource "aws_apigatewayv2_route" "any" {
  api_id = aws_apigatewayv2_api.this.id

  route_key = "$default"
  target    = "integrations/${aws_apigatewayv2_integration.lambda.id}"
}

resource "aws_lambda_permission" "api_gw" {
  statement_id  = "AllowExecutionFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.rds_proxy_function.function_name
  principal     = "apigateway.amazonaws.com"

  source_arn = "${aws_apigatewayv2_api.this.execution_arn}/*/*"
}