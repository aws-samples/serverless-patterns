# Lambda returning mock response
resource "aws_lambda_function" "http_api_lambda" {
  function_name = var.function_name
  role          = aws_iam_role.http_api_lambda_role.arn
  handler       = "lambda_function.lambda_handler"
  runtime       = var.function_runtime
  filename         = data.archive_file.http_api_lambda_zip.output_path
  source_code_hash = filebase64sha256(data.archive_file.http_api_lambda_zip.output_path)
}

# Zip Lambda code
data "archive_file" "http_api_lambda_zip" {
  type        = "zip"
  source_file = "src/lambda_function.py"
  output_path = "lambda_function.zip"
}

# Lambda permission
resource "aws_lambda_permission" "http_api_lambda_permission" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.http_api_lambda.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_apigatewayv2_api.http_api.execution_arn}/*/*"
}

# Lambda role
resource "aws_iam_role" "http_api_lambda_role" {
  name = "http_api_lambda_role"

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
resource "aws_iam_policy" "http_api_lambda_logs_policy" {
  name        = "http_api_lambda_policy"
  path        = "/"
  description = "http_api_lambda_policy"

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

resource "aws_iam_policy" "http_api_lambda_execution_policy" {
  name        = "http_api_lambda_execution_policy"
  path        = "/"
  description = "http_api_lambda_execution_policy"

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

# Lambda policy attachments
resource "aws_iam_role_policy_attachment" "http_api_lambda_log_policy_attachment" {
  role       = aws_iam_role.http_api_lambda_role.name
  policy_arn = aws_iam_policy.http_api_lambda_logs_policy.arn
}

resource "aws_iam_role_policy_attachment" "http_api_lambda_execution_policy_attachment" {
  role       = aws_iam_role.http_api_lambda_role.name
  policy_arn = aws_iam_policy.http_api_lambda_execution_policy.arn
}
