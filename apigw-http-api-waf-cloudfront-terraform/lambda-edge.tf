# Lambda Edge
resource "aws_lambda_function" "http_api_edge_lambda" {
  function_name = var.edge_function_name
  role          = aws_iam_role.http_api_edge_lambda_role.arn
  handler       = "edge_function.lambda_handler"
  runtime       = var.function_runtime
  filename         = data.archive_file.http_api_edge_lambda_zip.output_path
  source_code_hash = filebase64sha256(data.archive_file.http_api_edge_lambda_zip.output_path)
  publish = true
}

# Zip Lambda code
data "archive_file" "http_api_edge_lambda_zip" {
  type        = "zip"
  source_file = "src/edge_function.py"
  output_path = "edge_function.zip"
}

# Lambda permission
resource "aws_lambda_permission" "http_api_edge_lambda_permission" {
  statement_id  = "AllowCloudFrontEdgeInvoke"
  action        = "lambda:InvokeFunction"
  function_name = var.edge_function_name
  principal     = "cloudfront.amazonaws.com"
  source_arn    = aws_cloudfront_distribution.http_api_distribution.arn
}

# Lambda role
resource "aws_iam_role" "http_api_edge_lambda_role" {
  name = "http_api_edge_lambda_role"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": [
            "lambda.amazonaws.com",
            "edgelambda.amazonaws.com"
        ]
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

# Lambda policies
resource "aws_iam_policy" "http_api_edge_lambda_logs_policy" {
  name        = "http_api_edge_lambda_policy"
  path        = "/"
  description = "http_api_edge_lambda_policy"

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

resource "aws_iam_policy" "http_api_edge_lambda_execution_policy" {
  name        = "http_api_edge_lambda_execution_policy"
  path        = "/"
  description = "http_api_edge_lambda_execution_policy"

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

resource "aws_iam_policy" "http_api_edge_lambda_secret_policy" {
  name        = "http_api_edge_lambda_secret_policy"
  path        = "/"
  description = "http_api_edge_lambda_secret_policy"

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
resource "aws_iam_role_policy_attachment" "http_api_edge_lambda_log_policy_attachment" {
  role       = aws_iam_role.http_api_edge_lambda_role.name
  policy_arn = aws_iam_policy.http_api_edge_lambda_logs_policy.arn
}

resource "aws_iam_role_policy_attachment" "http_api_edge_lambda_execution_policy_attachment" {
  role       = aws_iam_role.http_api_edge_lambda_role.name
  policy_arn = aws_iam_policy.http_api_edge_lambda_execution_policy.arn
}

resource "aws_iam_role_policy_attachment" "http_api_edge_lambda_secret_policy_attachment" {
  role       = aws_iam_role.http_api_edge_lambda_role.name
  policy_arn = aws_iam_policy.http_api_edge_lambda_secret_policy.arn
}
