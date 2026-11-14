provider "aws" {
  region = var.region

  default_tags {
    tags = {
      metrics-test = "aws-metric-streams"
    }
  }
}

data "aws_availability_zones" "available" {
  state = "available"
}

data "aws_caller_identity" "current" {}

# Define role for firehose to send metrics to S3
resource "aws_iam_role" "firehose_to_s3" {
  name_prefix        = "test_streams"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "firehose.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

# Define a policy for permissios to write to S3
resource "aws_iam_role_policy" "firehose_to_s3" {
  name_prefix = "test_streams"
  role        = aws_iam_role.firehose_to_s3.id
  policy      = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:AbortMultipartUpload",
                "s3:GetBucketLocation",
                "s3:GetObject",
                "s3:ListBucket",
                "s3:ListBucketMultipartUploads",
                "s3:PutObject"
            ],
            "Resource": [
                "${aws_s3_bucket.metric_stream.arn}",
                "${aws_s3_bucket.metric_stream.arn}/*"
            ]
        }
    ]
}
EOF
}

# Associate the IAM role
resource "aws_iam_role" "metric_stream_to_firehose" {
  name_prefix        = "test_streams"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "streams.metrics.cloudwatch.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

resource "aws_iam_role_policy" "metric_stream_to_firehose" {
  name_prefix = "test_streams"
  role        = aws_iam_role.metric_stream_to_firehose.id
  policy      = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "firehose:PutRecord",
                "firehose:PutRecordBatch"
            ],
            "Resource": "${aws_kinesis_firehose_delivery_stream.metrics.arn}"
        }
    ]
}
EOF
}

# Create the S3 bucket to hold the metrics
resource "aws_s3_bucket" "metric_stream" {
  bucket = "test-streams-${data.aws_caller_identity.current.account_id}-${var.region}"

  tags = var.tags

  # 'true' allows terraform to delete this bucket even if it is not empty.
  force_destroy = true
}

# Create the Amazon Data Firehose instance
resource "aws_kinesis_firehose_delivery_stream" "metrics" {
  name        = "test_streams"
  destination = "extended_s3"

  extended_s3_configuration {
    role_arn   = aws_iam_role.firehose_to_s3.arn
    bucket_arn = aws_s3_bucket.metric_stream.arn

    compression_format = var.s3_compression_format
  }

}

# Create the metric streams for the desired services
resource "aws_cloudwatch_metric_stream" "metric-stream" {
  name          = "test_streams"
  role_arn      = aws_iam_role.metric_stream_to_firehose.arn
  firehose_arn  = aws_kinesis_firehose_delivery_stream.metrics.arn
  output_format = var.output_format


  # There can be an exclude_filter block, but it is
  # mutually exclusive with the include_filter, which means
  # you can have one of them at any time.
  
  include_filter {
    namespace = "AWS/EC2"
    metric_names = ["CPUUtilization", "NetworkOut"]
  }

  include_filter {
    namespace = "AWS/RDS"
    metric_names = ["CPUUtilization", "DatabaseConnections"]
  } 

  tags = var.tags
}
