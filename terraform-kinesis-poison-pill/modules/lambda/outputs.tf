/* Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. */

# --- modules/lambda/outputs.tf ---

# Lambda ARN
output "kinesis_strem_lambda_arn" {
    value       = aws_lambda_function.kinesis_stream_lambda.arn
    description = "Output of Lambda ARN"
}