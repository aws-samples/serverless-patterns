/* Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. */

# --- modules/firehose/outputs.tf ---

# Kinesis Firehose Delivery Stream ARN
output "firehose_delivery_stream_arn" {
    value       = aws_kinesis_firehose_delivery_stream.firehose_delivery_stream.arn
    description = "firehose_delivery_stream_arn"
}