# Lambda Authorizer
resource "aws_lambda_function" "http_api_auth_lambda" {
  function_name = var.auth_function_name
  role          = aws_iam_role.http_api_auth_lambda_role.arn
  handler       = "auth_function.lambda_handler"
  runtime       = var.function_runtime
  filename         = data.archive_file.http_api_auth_lambda_zip.output_path
  source_code_hash = filebase64sha256(data.archive_file.http_api_auth_lambda_zip.output_path)
  #environment variables
  environment {
    variables = {
        "SECRET_NAME" = aws_secretsmanager_secret.cf_api_header_secret_store.name
    }
  }
}

# API Gateway
resource "aws_apigatewayv2_authorizer" "http_api_auth_authorizer" {
  api_id                            = aws_apigatewayv2_api.http_api.id
  authorizer_type                   = "REQUEST"
  authorizer_uri                    = aws_lambda_function.http_api_auth_lambda.invoke_arn
  identity_sources                  = ["$request.header.x-origin-verify"]
  name                              = var.auth_function_name
  authorizer_payload_format_version = "2.0"
  authorizer_result_ttl_in_seconds = 0
}

# Zip Lambda code
data "archive_file" "http_api_auth_lambda_zip" {
  type        = "zip"
  source_file = "src/auth_function.py"
  output_path = "auth_function.zip"
}

# Lambda permission
resource "aws_lambda_permission" "http_api_auth_lambda_permission" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.http_api_auth_lambda.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_apigatewayv2_api.http_api.execution_arn}/*/*"
}

# Lambda role
resource "aws_iam_role" "http_api_auth_lambda_role" {
  name = "http_api_auth_lambda_role"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

# Lambda policies
resource "aws_iam_policy" "http_api_auth_lambda_logs_policy" {
  name        = "http_api_auth_lambda_policy"
  path        = "/"
  description = "http_api_auth_lambda_policy"

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*",
      "Effect": "Allow"
    }
  ]
}
EOF
}

resource "aws_iam_policy" "http_api_auth_lambda_execution_policy" {
  name        = "http_api_auth_lambda_execution_policy"
  path        = "/"
  description = "http_api_auth_lambda_execution_policy"

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "lambda:InvokeFunction"
      ],
      "Resource": "*",
      "Effect": "Allow"
    }
  ]
}
EOF
}

resource "aws_iam_policy" "http_api_auth_lambda_secret_policy" {
  name        = "http_api_auth_lambda_secret_policy"
  path        = "/"
  description = "http_api_auth_lambda_secret_policy"

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "secretsmanager:GetSecretValue"
      ],
      "Resource": "${aws_secretsmanager_secret.cf_api_header_secret_store.arn}",
      "Effect": "Allow"
    }
  ]
}
EOF
}

# Lambda Auth policy attachments
resource "aws_iam_role_policy_attachment" "http_api_auth_lambda_log_policy_attachment" {
  role       = aws_iam_role.http_api_auth_lambda_role.name
  policy_arn = aws_iam_policy.http_api_auth_lambda_logs_policy.arn
}

resource "aws_iam_role_policy_attachment" "http_api_auth_lambda_execution_policy_attachment" {
  role       = aws_iam_role.http_api_auth_lambda_role.name
  policy_arn = aws_iam_policy.http_api_auth_lambda_execution_policy.arn
}

resource "aws_iam_role_policy_attachment" "http_api_auth_lambda_secret_policy_attachment" {
  role       = aws_iam_role.http_api_auth_lambda_role.name
  policy_arn = aws_iam_policy.http_api_auth_lambda_secret_policy.arn
}
