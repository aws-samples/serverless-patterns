/* Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. */

# --- main.tf ---

# Create Kinesis Stream
module "kinesis_stream" {
    source = "./modules/kinesisstream" 
}

# Create Lambda Event Filtering
module "esm_filter_lambda" {
    source     = "./modules/lambda" 
    stream_arn = module.kinesis_stream.stream_arn
}
