terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }
  }

  required_version = ">= 0.14.9"
}

# Storing current Account ID and actual AWS region
data "aws_caller_identity" "current" {}
data "aws_region" "current" {}


#################################################################
# S3 Bucket
#################################################################
# Creating a new S3 bucket
resource "aws_s3_bucket" "MyS3Bucket" {
  bucket_prefix = "s3-eventbridge-sfn-tf-"
}

# Sending notifications to EventBridge for all events in the bucket
resource "aws_s3_bucket_notification" "MyS3BucketNotification" {
  bucket      = aws_s3_bucket.MyS3Bucket.id
  eventbridge = true
}

# Blocking s3 bucket non secure access
resource "aws_s3_bucket_policy" "MyS3BucketPolicy" {
  bucket = aws_s3_bucket.MyS3Bucket.id
  policy = data.aws_iam_policy_document.MyS3BucketPolicyDocument.json
}

data "aws_iam_policy_document" "MyS3BucketPolicyDocument" {
  statement  {
    effect = "Deny"
    principals {
      type        = "AWS"
      identifiers = ["*"]
    }
    actions = [
      "s3:*"
    ]
    resources = [
      "arn:aws:s3:::${aws_s3_bucket.MyS3Bucket.id}",
      "arn:aws:s3:::${aws_s3_bucket.MyS3Bucket.id}/*"
    ]
    condition {
      test     = "Bool"
      variable = "aws:SecureTransport"
      values   = ["false"]
    }
  }
}


#################################################################
# EventBridge Rule
#################################################################
# Creating an EventBridge rule
resource "aws_cloudwatch_event_rule" "MyEventRule" {
  name          = "s3-eventbridge-sfn-tf-eventrule"
  description   = "Object create events on bucket s3://${aws_s3_bucket.MyS3Bucket.id}"
  event_pattern = <<EOF
{
  "detail-type": ["Object Created"],
  "source": ["aws.s3"],
  "detail": {
    "bucket": {
      "name": ["${aws_s3_bucket.MyS3Bucket.id}"]
    }
  }
}
EOF
}

# Setting Event Target, DLQ and transformer of the EventBridge rule
resource "aws_cloudwatch_event_target" "MyEventRuleTarget" {
  rule      = aws_cloudwatch_event_rule.MyEventRule.name
  arn       = aws_sfn_state_machine.MySTFRoleMachine.arn
  role_arn  = aws_iam_role.MyEventRuleTargetRole.arn
  
  dead_letter_config {
    arn = aws_sqs_queue.MySQSDLQ-Queue.arn
  }
  
  input_transformer {
    input_paths = {
      "detail": "$.detail"
    } 
    input_template = <<EOF
{"input":{"detail":<detail>},"inputType":0}
EOF
}
}

# Creating Event Target IAM Role
resource "aws_iam_role" "MyEventRuleTargetRole" {
  name               = "s3-eventbridge-sfn-tf-EventRole"
  assume_role_policy = jsonencode({
    Version   = "2012-10-17"
    Statement = [
      {
        Effect    = "Allow"
        Principal = { Service = "events.amazonaws.com" }
        Action    = "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_role_policy" "MyEventRuleTargetPolicy" {
  name   = "s3-eventbridge-sfn-tf-EventRolePolicy"
  policy = jsonencode(
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": "states:StartExecution",
            "Resource": "${aws_sfn_state_machine.MySTFRoleMachine.arn}",
            "Effect": "Allow"
        }
    ]
}
)
  role = aws_iam_role.MyEventRuleTargetRole.name
}


#################################################################
# SQS - Dead Letter Queue (DLQ)
#################################################################
# Creating SQS - Dead Letter Queue (DLQ)
resource "aws_sqs_queue" "MySQSDLQ-Queue" {
  name            = "s3-eventbridge-sfn-tf-SQSDLQQueue"
}

resource "aws_sqs_queue_policy" "MySQSDLQ-Policy" {
  queue_url = aws_sqs_queue.MySQSDLQ-Queue.id

  policy = <<POLICY
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Principal": {
        "AWS": "*"
      },
      "Action": "sqs:*",
      "Resource": "arn:aws:sqs:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:${aws_sqs_queue.MySQSDLQ-Queue.name}",
      "Condition": {
        "Bool": {
          "aws:SecureTransport": "false"
        }
      }
    },
    {
      "Sid": "AllowEventRuleS3EventBridgeSfnStackStackpatternEventsRule",
      "Effect": "Allow",
      "Principal": {
        "Service": "events.amazonaws.com"
      },
      "Action": "sqs:SendMessage",
      "Resource": "arn:aws:sqs:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:${aws_sqs_queue.MySQSDLQ-Queue.name}",
      "Condition": {
        "ArnEquals": {
          "aws:SourceArn": "${aws_cloudwatch_event_rule.MyEventRule.arn}"
        }
      }
    }
  ]
}
POLICY
}


#################################################################
# Step Funcions 
#################################################################
# Creating Step Functions Machine
resource "aws_sfn_state_machine" "MySTFRoleMachine" {
  name     = "s3-eventbridge-sfn-tf-StepFunctions"
  role_arn = aws_iam_role.MySTFRole.arn
  type     = "STANDARD"

  definition = <<EOF
{
    "StartAt": "state",
    "States": {
      "state": {
        "Type": "Pass",
        "End": true
      }
    }
}
EOF

}

# Creating Step Functions Machine Role
resource "aws_iam_role" "MySTFRole" {
  name               = "s3-eventbridge-sfn-tf-StepFunctionsRole"
  assume_role_policy = jsonencode({
    Version   = "2012-10-17"
    Statement = [
      {
        Effect    = "Allow"
        Principal = { Service = "states.${data.aws_region.current.name}.amazonaws.com" }
        Action    = "sts:AssumeRole"
      }
    ]
  })
}


#################################################################
# Outputs
#################################################################
# Displaying the SQS Dead Letter Queue, EventBridge rule, S3 bucket and StepFunctions
output "SQSDeadLetterQueue" {
  value       = aws_sqs_queue.MySQSDLQ-Queue.arn
  description = "The SQS Dead Letter Queue ARN"
}
output "EventBridgeRuleARN" {
  value       = aws_cloudwatch_event_rule.MyEventRule.arn
  description = "The EventBridge Rule ARN"
}
output "S3BucketName" {
  value       = aws_s3_bucket.MyS3Bucket.id
  description = "The S3 Bucket Name"
}
output "StepFunctions" {
  value       = aws_sfn_state_machine.MySTFRoleMachine.arn
  description = "The StepFunctions Machine ARN"
}
