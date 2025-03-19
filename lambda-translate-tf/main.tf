provider "aws" {
  region = var.aws_region
}

# Archive the Python source code
data "archive_file" "lambda_zip" {
  type        = "zip"
  source_dir  = "${path.module}/src"
  output_path = "${path.module}/lambda_function.zip"
}

# Create Lambda function
resource "aws_lambda_function" "translate_text" {
  filename         = data.archive_file.lambda_zip.output_path
  function_name    = var.function_name
  role            = aws_iam_role.lambda_role.arn
  handler         = "index.lambda_handler"
  runtime         = "python3.13"
  memory_size     = 128
  timeout         = 10

  source_code_hash = data.archive_file.lambda_zip.output_base64sha256
}
