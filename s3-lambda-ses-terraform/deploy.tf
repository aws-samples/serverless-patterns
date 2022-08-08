provider "aws" {
  region = var.aws_region
}

resource "random_id" "rng" {
  keepers = {
    first = "${timestamp()}"
  }     
  byte_length = 8
}

# Creating Lambda IAM resource
resource "aws_iam_role" "lambda_iam" {
  name = "${var.lambda_role_name}-${random_id.rng.hex}"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF
}

resource "aws_iam_role_policy" "Lambda_SES_S3" {
  name = "${var.lambda_iam_policy_name}-${random_id.rng.hex}"
  role = aws_iam_role.lambda_iam.id

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents",
        "s3:*",
        "ses:*"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
EOF
}

data "archive_file" "zip" {
  type        = "zip"
  source_file = "src/emailSender.py"
  output_path = "src/emailSender.zip"
}

resource "aws_s3_bucket" "newbucket" {
    bucket = var.bucket_name
    force_destroy = true
    acl = var.acl_value   
}

resource "aws_lambda_layer_version" "lambda_layer" {
  filename   = "src/urlshortner.zip"
  layer_name = "pyshortner"
  compatible_runtimes = ["python3.9"]
}

# Creating Lambda resource
resource "aws_lambda_function" "test_lambda" {
  function_name    = "${var.function_name}-${random_id.rng.hex}"
  role             = aws_iam_role.lambda_iam.arn
  handler          = "emailSender.lambda_handler"
  runtime          = "python3.9"
  timeout          = var.timeout
  filename         = "${data.archive_file.zip.output_path}"
  source_code_hash = "${data.archive_file.zip.output_base64sha256}"
  layers = [aws_lambda_layer_version.lambda_layer.arn]
  environment {
    variables = {
      env            = var.environment
      SENDER_EMAIL   = var.sender_email
      RECEIVER_EMAIL = var.receiver_email
    }
  }
}

# Adding S3 bucket as trigger to lambda and giving the permissions
resource "aws_s3_bucket_notification" "aws-lambda-trigger" {
  bucket = aws_s3_bucket.newbucket.id
  lambda_function {
    lambda_function_arn = aws_lambda_function.test_lambda.arn
    events              = ["s3:ObjectCreated:*"]
    filter_prefix       =  var.prefix
    filter_suffix       =  var.suffix
  }
}

resource "aws_lambda_permission" "test" {
  statement_id  = "AllowS3Invoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.test_lambda.function_name
  principal     = "s3.amazonaws.com"
  source_arn    = "arn:aws:s3:::${aws_s3_bucket.newbucket.id}"
}