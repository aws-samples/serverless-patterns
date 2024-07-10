terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.57.0"
    }
  }

  required_version = ">= 0.14.9"
}

data "aws_caller_identity" "current" {}
data "aws_region" "current" {}


#################################################################
# S3 Buckets
#################################################################
# Create a new Source S3 bucket
resource "aws_s3_bucket" "MySourceS3Bucket" {
  bucket_prefix = "s3-sqs-lambda-tf-sources3bucket-"
}

# Send notifications to SQS for all events in the bucket
resource "aws_s3_bucket_notification" "MySourceS3BucketNotification" {
  bucket      = aws_s3_bucket.MySourceS3Bucket.id

  queue {
    queue_arn     = aws_sqs_queue.MyHandlerQueue.arn
    events        = [
      "s3:ObjectCreated:*"
    ]
    filter_suffix = ".jpg"
  }
  
}

#################################################################
# SQS - Queue
#################################################################
# Create SQS - Queue
resource "aws_sqs_queue" "MyHandlerQueue" {
  name      = "s3-sqs-lambda-tf-SQSResizerQueue"
}

# Create SQS - Policy
resource "aws_sqs_queue_policy" "MyHandlerQueuePolicy" {
  queue_url = aws_sqs_queue.MyHandlerQueue.id

  policy = <<POLICY
{
  "Version": "2012-10-17",
  "Id": "QueuePolicy",
  "Statement": [
    {
      "Sid": "Allow-SendMessage-To-Queue-From-S3-Event-Notification",
      "Effect": "Allow",
      "Principal": {
        "Service": "s3.amazonaws.com"
      },
      "Action": "sqs:SendMessage",
      "Resource": "arn:aws:sqs:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:${aws_sqs_queue.MyHandlerQueue.name}",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "${data.aws_caller_identity.current.account_id}"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:s3:::${aws_s3_bucket.MySourceS3Bucket.id}"
        }
      }
    }
  ]
}
POLICY
}


#################################################################
# Lambda Function
#################################################################
# Creating Lambda Function
resource "aws_lambda_function" "MyHandlerFunction-Function" {
  filename      = data.archive_file.LambdaZipFile.output_path
  function_name = "s3-sqs-lambda-tf-LambdaFunction"
  role          = aws_iam_role.MyHandlerFunction-Role.arn
  handler       = "app.handler"
  runtime       = "nodejs20.x"
}

# Create a zip file from the Lambda source code
data "archive_file" "LambdaZipFile" {
  type        = "zip"
  source_file = "${path.module}/src/app.mjs"
  output_path = "${path.module}/lambda-src.zip"
}

# Creating SQS Queue Trigger for Lambda Function
resource "aws_lambda_event_source_mapping" "MyHandlerFunction-Function-to-SQS" {
  event_source_arn = aws_sqs_queue.MyHandlerQueue.arn
  function_name    = aws_lambda_function.MyHandlerFunction-Function.arn
}

# Creating IAM Role for Lambda Function
resource "aws_iam_role" "MyHandlerFunction-Role" {
  name = "s3-sqs-lambda-tf-MyHandlerFunction-Role"

  assume_role_policy = jsonencode({
    Version   = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

# Creating IAM Policies for Lambda
resource "aws_iam_role_policy" "MyHandlerFunction-Policy-source" {
  name   = "s3-sqs-lambda-tf-MyHandlerFunction-Role"
  policy = jsonencode(
{
    "Statement": [
        {
            "Action": [
                "s3:GetObject",
                "s3:ListBucket",
                "s3:GetBucketLocation",
                "s3:GetObjectVersion",
                "s3:GetLifecycleConfiguration"
            ],
            "Resource": [
      				"arn:aws:s3:::${aws_s3_bucket.MySourceS3Bucket.id}",
      				"arn:aws:s3:::${aws_s3_bucket.MySourceS3Bucket.id}/*"
            ],
            "Effect": "Allow"
        }
    ]
}
  )
  role = aws_iam_role.MyHandlerFunction-Role.name
}

resource "aws_iam_role_policy_attachment" "AWSLambdaBasicExecutionRole" {
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
  role       = "${aws_iam_role.MyHandlerFunction-Role.name}"
}

resource "aws_iam_role_policy_attachment" "AWSLambdaSQSQueueExecutionRole" {
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaSQSQueueExecutionRole"
  role       = "${aws_iam_role.MyHandlerFunction-Role.name}"
}

  
#################################################################
# Outputs
#################################################################
# Displaying the SQS Queue, SourceS3 buckets and Lambda Function
output "SQSQueueName" {
  value       = aws_sqs_queue.MyHandlerQueue.name
  description = "SQS Queue for queuing the s3 events"
}
output "SourceS3BucketName" {
  value       = aws_s3_bucket.MySourceS3Bucket.id
  description = "S3 Bucket for object storage"
}
output "LambdaFunctionArn" {
  value       = aws_lambda_function.MyHandlerFunction-Function.arn
  description = "HandlerFunction function Arn"
}
