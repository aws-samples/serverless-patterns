/* Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. */

# --- modules/lambda/outputs.tf ---

# Lambda ARN
output "data_transformation_lambda_arn" {
    value       = aws_lambda_function.data_transformation.arn
    description = "Output of Lambda ARN"
}