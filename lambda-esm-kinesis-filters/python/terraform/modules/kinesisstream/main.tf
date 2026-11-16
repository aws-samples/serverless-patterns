/* Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. */

# --- modules/kinesisstream/main.tf ---

# Create Kinesis Stream
resource "aws_kinesis_stream" "kinesis_stream" {
    name                      = var.name    
    retention_period          = var.retention_period
    
    // PROVISIONED or ON_DEMAND
    stream_mode_details {
        stream_mode = "ON_DEMAND"
    }
}