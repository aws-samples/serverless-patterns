/* Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. */

# --- main.tf ---

# Create Amazon S3 Destination Bucket
module "s3_destination_bucket" {
    source = "./modules/s3"  
}

# Create Data Transformation Lambda
module "data_transformation_lambda" {
    source                       = "./modules/lambda" 
    firehose_delivery_stream_arn = module.firehose_delivery_stream.firehose_delivery_stream_arn

}

# Create Amazon Firehose Delivery Stream
module "firehose_delivery_stream" {
    source                         = "./modules/firehose"  
    s3_destination_bucket_arn      = module.s3_destination_bucket.bucket_arn
    data_transformation_lambda_arn = module.data_transformation_lambda.data_transformation_lambda_arn
}

