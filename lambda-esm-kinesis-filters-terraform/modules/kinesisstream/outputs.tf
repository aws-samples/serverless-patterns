/* Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. */

# --- modules/kinesisstream/outputs.tf ---

# Kinesis Stream Name
output "stream_name" {
    value       = aws_kinesis_stream.kinesis_stream.name
    description = "Output of Kinesis stream name"
}

# Kinesis Stream ARN
output "stream_arn" {
    value       = aws_kinesis_stream.kinesis_stream.arn
    description = "Output of Kinesis stream ARN"
}

