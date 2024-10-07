# Secret rotation Lambda function
resource "aws_lambda_function" "secret_rotation_lambda" {
  function_name = var.secret_rotation_function_name
  memory_size   = var.secret_rotation_lambda_memory
  role          = aws_iam_role.secret_rotation_lambda_role.arn
  handler       = "secret_rotation_function.lambda_handler"
  runtime       = var.function_runtime
  filename         = data.archive_file.secret_rotation_lambda_zip.output_path
  source_code_hash = filebase64sha256(data.archive_file.secret_rotation_lambda_zip.output_path)
  #environment variables
  environment {
    variables = {
        "UNIQUE_KEY_LENGTH" = var.unique_key_length
    }
  }  
}

# Zip Lambda code
data "archive_file" "secret_rotation_lambda_zip" {
  type        = "zip"
  source_file = "src/secret_rotation_function.py"
  output_path = "secret_rotation_function.zip"
}

# Lambda permission
resource "aws_lambda_permission" "secret_rotation_lambda_permission" {
  statement_id  = "AllowSecretRotationInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.secret_rotation_lambda.function_name
  principal     = "secretsmanager.amazonaws.com"
  source_arn    = aws_secretsmanager_secret.cf_api_header_secret_store.arn
}

# Lambda role
resource "aws_iam_role" "secret_rotation_lambda_role" {
  name = "secret_rotation_lambda_role"

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
resource "aws_iam_policy" "secret_rotation_lambda_logs_policy" {
  name        = "secret_rotation_lambda_policy"
  path        = "/"
  description = "secret_rotation_lambda_policy"

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

resource "aws_iam_policy" "secret_rotation_lambda_execution_policy" {
  name        = "secret_rotation_lambda_execution_policy"
  path        = "/"
  description = "secret_rotation_lambda_execution_policy"

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

resource "aws_iam_policy" "secret_rotation_secretsmgr_policy" {
  name        = "secret_rotation_secretsmgr_policy"
  path        = "/"
  description = "secret_rotation_secretsmgr_policy"

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "secretsmanager:DescribeSecret",
        "secretsmanager:GetSecretValue",
        "secretsmanager:PutSecretValue",
        "secretsmanager:UpdateSecretVersionStage"
      ],
      "Resource": "${aws_secretsmanager_secret.cf_api_header_secret_store.arn}",
      "Effect": "Allow"
    },
    {
      "Action": [
        "secretsmanager:GetRandomPassword"
      ],
      "Resource": "*",
      "Effect": "Allow"
    }
  ]
}
EOF
}

# Lambda policy attachments
resource "aws_iam_role_policy_attachment" "secret_rotation_lambda_log_policy_attachment" {
  role       = aws_iam_role.secret_rotation_lambda_role.name
  policy_arn = aws_iam_policy.secret_rotation_lambda_logs_policy.arn
}

resource "aws_iam_role_policy_attachment" "secret_rotation_lambda_execution_policy_attachment" {
  role       = aws_iam_role.secret_rotation_lambda_role.name
  policy_arn = aws_iam_policy.secret_rotation_lambda_execution_policy.arn
}

resource "aws_iam_role_policy_attachment" "secret_rotation_secretsmgr_policy_attachment" {
  role       = aws_iam_role.secret_rotation_lambda_role.name
  policy_arn = aws_iam_policy.secret_rotation_secretsmgr_policy.arn
}