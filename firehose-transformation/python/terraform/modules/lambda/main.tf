/* Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. */

# --- modules/lambda/main.tf ---

# Zip the source code
data "archive_file" "lambda_code_in_zip_format" {
    type        = "zip"
    source_dir  = "${path.module}/src/"
    output_path = "${path.module}/src/data_transformation.zip"
}

# Create AWS Lambda - Data Transformation
resource "aws_lambda_function" "data_transformation" {
    filename          = "${path.module}/src/data_transformation.zip"
    function_name     = var.function_name
    role              = aws_iam_role.iam_role_for_lambda.arn
    handler           = var.data_transformation_handler
    runtime           = var.runtime
    timeout           = var.timeout
}

# IAM Role for Lambda 
resource "aws_iam_role" "iam_role_for_lambda" {
    name               = "iam_role_for_lambda"
    assume_role_policy = file("${path.module}/iam_role_for_lambda.json")
}

# IAM Policy for Lambda
resource "aws_iam_policy" "iam_policy_for_lambda" {
    name   = "iam_policy_for_lambda"
    policy = templatefile("${path.module}/iam_policy_for_lambda.tftpl", {data_transformation_lambda_arn = aws_lambda_function.data_transformation.arn})
}

# Attach IAM Role with IAM Policy for Lambda
resource "aws_iam_role_policy_attachment" "attach_iam_role_with_iam_policy" {
    policy_arn = aws_iam_policy.iam_policy_for_lambda.arn
    role       = aws_iam_role.iam_role_for_lambda.name
}

# Permission for Lambda
resource "aws_lambda_permission" "permission_for_lambda" {
    action        = "lambda:InvokeFunction"
    function_name = aws_lambda_function.data_transformation.function_name
    principal     = "firehose.amazonaws.com"
    source_arn    = var.firehose_delivery_stream_arn    
}
