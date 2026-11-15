/* Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. */

# --- main.tf ---

# Create Amazon S3 - flink application landing zone 
module "s3_application_landing_zone" {
    source = "./modules/s3"  
}

# Create Kinesis Stream
module "kinesis_stream" {
    source = "./modules/kinesisstream" 
}

# Create Kinesis Analytics
module "kinesisanalytics" {
    source          = "./modules/kinesisanalytics"
    bucket_arn      = module.s3_application_landing_zone.bucket_arn
    bucket_name     = module.s3_application_landing_zone.bucket_id
    file_key        = module.s3_application_landing_zone.file_key
    stream_name     = module.kinesis_stream.stream_name
    region          = var.region
}
