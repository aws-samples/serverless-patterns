# This is required to get the AWS region via ${data.aws_region.current}.
#data "aws_region" "current" {
#}

provider "aws" {
    region = var.region

}

# --- main.tf ---

# Create Amazon S3 Destination Bucket
module "kinesis-stream" {
    source = "./modules/kinesis-stream"  
}

module "sqs_queue" {
    source = "./modules/sqs"  
}

# Create Data Transformation Lambda
module "kinesis_stream_lambda" {
    source                       = "./modules/lambda" 
    kinesis_stream_arn = module.kinesis-stream.kinesis_stream_arn
    sqs_arn  = module.sqs_queue.sqs_arn

}
