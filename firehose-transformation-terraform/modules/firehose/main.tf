/* Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. */

# --- modules/firehose/main.tf ---

# Create Kinesis Firehose delivery stream
resource "aws_kinesis_firehose_delivery_stream" "firehose_delivery_stream" {
    name        = var.kinesis_firehose_name
    destination = var.kinesis_firehose_destination

    extended_s3_configuration {
        bucket_arn          = var.s3_destination_bucket_arn
        role_arn            = aws_iam_role.iam_role_for_firehose.arn
        buffering_interval  = var.buffer_interval
        buffering_size      = var.buffer_size
        compression_format  = var.compression_format  

        processing_configuration {
            enabled = "true"

            processors {
                type = var.kinesis_firehose_processing_type

                parameters {
                    parameter_name  = "LambdaArn"
                    parameter_value = var.data_transformation_lambda_arn
                }
            }
        }
    }
}

# IAM Role for Kinesis Firehose
resource "aws_iam_role" "iam_role_for_firehose" {
    name               = "iam_role_for_firehose"
    assume_role_policy = file("${path.module}/iam_role_for_firehose.json")
}

# IAM Policy for Kinesis Firehose
resource "aws_iam_policy" "iam_policy_for_firehose" {
    name   = "iam_policy_for_firehose"
    policy = templatefile("${path.module}/iam_policy_for_firehose.tftpl",{s3_destination_bucket_arn = var.s3_destination_bucket_arn , 
                                                                        data_transformation_lambda_arn = var.data_transformation_lambda_arn } )
}

# Attach IAM Role with IAM Policy for Kinesis Firehose
resource "aws_iam_role_policy_attachment" "attach_iam_role_with_iam_policy" {
    policy_arn = aws_iam_policy.iam_policy_for_firehose.arn
    role       = aws_iam_role.iam_role_for_firehose.name
}