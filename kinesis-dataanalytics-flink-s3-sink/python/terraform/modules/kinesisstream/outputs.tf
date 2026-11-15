/* Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. */

# --- modules/kinesisstream/outputs.tf ---

# Kinesis Stream Name
output "stream_name" {
    value       = aws_kinesis_stream.kinesis_stream.name
    description = "Output of Kinesis stream name"
}
