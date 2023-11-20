provider "aws" {
  region = "us-east-1"
}

variable "destination_bucket_name" {
  description = "Enter a bucket name"
  type        = string
}

resource "random_id" "unique_suffix" {
  byte_length = 4
}

resource "aws_s3_bucket" "destination_bucket" {
  bucket = "${var.destination_bucket_name}-${random_id.unique_suffix.hex}"

  # Additional S3 bucket configurations go here
}

resource "aws_iam_role" "sns_subscription_role" {
  name = "SNSSubscriptionRole-TF"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "sns.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF
}

resource "aws_iam_role" "delivery_stream_role" {
  name = "DeliveryStreamRole-TF"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "firehose.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF
}

resource "aws_iam_policy" "sns_firehose_access_policy" {
  name        = "SNS_Firehose_access_policy_tf"
  description = "IAM policy for SNS to access Kinesis Firehose"
  
  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "firehose:DescribeDeliveryStream",
        "firehose:ListDeliveryStreams",
        "firehose:ListTagsForDeliveryStream",
        "firehose:PutRecord",
        "firehose:PutRecordBatch"
      ],
      "Resource": [
        "${aws_kinesis_firehose_delivery_stream.extended_s3_stream.arn}"
      ]
    }
  ]
}
EOF
}

resource "aws_iam_policy" "delivery_stream_policy" {
  name        = "firehose_delivery_policy_tf"
  description = "IAM policy for Kinesis Firehose to access S3 bucket"

  policy = <<EOF
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
        "${aws_s3_bucket.destination_bucket.arn}",
        "${aws_s3_bucket.destination_bucket.arn}/*"
      ]
    }
  ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "sns_firehose_access_attachment" {
  policy_arn = aws_iam_policy.sns_firehose_access_policy.arn
  role       = aws_iam_role.sns_subscription_role.name
}

resource "aws_iam_role_policy_attachment" "delivery_stream_access_attachment" {
  policy_arn = aws_iam_policy.delivery_stream_policy.arn
  role       = aws_iam_role.delivery_stream_role.name
}

resource "aws_sns_topic" "sns_topic" {
  name      = "SourceSNSTopic-TF"
  fifo_topic = false
}

resource "aws_sns_topic_subscription" "sns_subscription" {
  protocol  = "firehose"
  topic_arn = aws_sns_topic.sns_topic.arn
  endpoint  = aws_kinesis_firehose_delivery_stream.extended_s3_stream.arn
  depends_on = [aws_sns_topic.sns_topic, aws_kinesis_firehose_delivery_stream.extended_s3_stream]
  subscription_role_arn = aws_iam_role.sns_subscription_role.arn
}

resource "aws_kinesis_firehose_delivery_stream" "extended_s3_stream" {
  name                    = "Firehost-stream-TF"
  destination = "extended_s3"

  extended_s3_configuration {
    bucket_arn         = aws_s3_bucket.destination_bucket.arn
    role_arn           = aws_iam_role.delivery_stream_role.arn
    buffering_size     = 1
    buffering_interval = 60
    compression_format = "GZIP"
    
    cloudwatch_logging_options {
      enabled           = true
      log_group_name    = "/aws/kinesisfirehose/ibcd"
      log_stream_name   = "S3Delivery"
    }

  }
}

output "sns_subscription_role_arn" {
  value = aws_iam_role.sns_subscription_role.arn
}

output "delivery_stream_role_arn" {
  value = aws_iam_role.delivery_stream_role.arn
}

output "sns_firehose_access_policy_arn" {
  value = aws_iam_policy.sns_firehose_access_policy.arn
}

output "delivery_stream_policy_arn" {
  value = aws_iam_policy.delivery_stream_policy.arn
}

output "sns_topic_arn" {
  value = aws_sns_topic.sns_topic.arn
}

output "sns_subscription_arn" {
  value = aws_sns_topic_subscription.sns_subscription.arn
}

output "kinesis_firehose_stream_arn" {
  value = aws_kinesis_firehose_delivery_stream.extended_s3_stream.arn
}


output "destination_bucket_arn" {
  value = aws_s3_bucket.destination_bucket.arn
}

