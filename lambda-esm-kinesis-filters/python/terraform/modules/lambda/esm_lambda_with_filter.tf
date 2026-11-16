/* Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. */

# --- modules/lambda/esm_lambda_with_filter.tf ---

# Zip the source code
data "archive_file" "esm_lambda_with_filter_in_zip_format" {
    type        = "zip"
    source_dir  = "${path.module}/src/with_filter"
    output_path = "${path.module}/tmp/esm_lambda_with_filter.zip"
}

# Create AWS Lambda - Event Source Mapping (ESM) with filter
resource "aws_lambda_function" "esm_lambda_with_filter" {
    filename          = "${path.module}/tmp/esm_lambda_with_filter.zip"
    function_name     = var.esm_lambda_with_filter_function_name
    role              = aws_iam_role.iam_role_for_esm_lambda_with_filter.arn
    handler           = var.esm_lambda_with_filter_handler
    runtime           = var.runtime
    timeout           = var.timeout

    provisioner "local-exec" {
        environment = {
            file_path = "${path.module}/tmp/esm_lambda_with_filter.zip" //Change this location per your application needs
        }
        
        command = "rm -f $file_path"
        when    = destroy
    }
}


# Random number generator
resource "random_id" "random_generator_with_filter" {
    byte_length = 8
}

# IAM Role for Lambda 
resource "aws_iam_role" "iam_role_for_esm_lambda_with_filter" {
    name               = "iam_role_for_esm_lambda_with_filter_${random_id.random_generator_with_filter.hex}"
    assume_role_policy = file("${path.module}/iam_role_for_lambda.json")
    force_detach_policies = true
}

# IAM Policy for Lambda
resource "aws_iam_policy" "iam_policy_for_esm_lambda_with_filter" {
    name   = "iam_policy_for_esm_lambda_with_filter_${random_id.random_generator_with_filter.hex}"
    policy = templatefile("${path.module}/iam_policy_for_lambda.tftpl", 
                            {esm_filter_lambda_arn = aws_lambda_function.esm_lambda_with_filter.arn,
                            stream_arn = var.stream_arn})
}

# Attach IAM Role with IAM Policy for Lambda
resource "aws_iam_role_policy_attachment" "attach_iam_role_with_iam_policy_with_filter" {
    policy_arn      = aws_iam_policy.iam_policy_for_esm_lambda_with_filter.arn
    role            = aws_iam_role.iam_role_for_esm_lambda_with_filter.name
}

# Event Source Mapping 
resource "aws_lambda_event_source_mapping" "esm_lambda_with_filter" {
    event_source_arn               = var.stream_arn
    function_name                  = aws_lambda_function.esm_lambda_with_filter.arn
    starting_position              = "LATEST"
    batch_size                     = 5 //default - 100


    filter_criteria {
        filter {
            pattern = jsonencode({
                data = {                
                    "ticker" : ["AMZN"]
                }
            })
        }
    }
}

# Cloudwatch Log Group
resource "aws_cloudwatch_log_group" "esm_lambda_with_filter_log_group" {
    name              = "/aws/lambda/${aws_lambda_function.esm_lambda_with_filter.function_name}"
    retention_in_days = 3
    
    lifecycle {
        prevent_destroy = false
    }
}