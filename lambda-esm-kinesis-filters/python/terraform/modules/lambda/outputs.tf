/* Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. */

# --- modules/lambda/outputs.tf ---

# Lambda ARN - ESM with Filter
output "esm_lambda_with_filter_arn" {
    value       = aws_lambda_function.esm_lambda_with_filter
    description = "Output of Lambda ARN - With Filter"
}

# Lambda ARN - ESM with no Filter
output "esm_lambda_with_no_filter_arn" {
    value       = aws_lambda_function.esm_lambda_with_no_filter
    description = "Output of Lambda ARN - No Filter"
}