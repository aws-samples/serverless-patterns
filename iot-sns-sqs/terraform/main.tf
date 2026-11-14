resource "aws_sqs_queue" "iot_sns_sqs_tf_queue" {
    name                       = "IotSnsSqstfQueue"
    visibility_timeout_seconds = 300
  }
  
  
resource "aws_sns_topic" "iot_sns_sqs_tf_topic" {
    name = "IotSnsSqstfTopic"
  }
  
resource "aws_sns_topic_subscription" "iot_sns_sqs_tf_subscription" {
    topic_arn = aws_sns_topic.iot_sns_sqs_tf_topic.arn
    protocol  = "sqs"
    endpoint  = aws_sqs_queue.iot_sns_sqs_tf_queue.arn
  }

  
 resource "aws_sqs_queue_policy" "example_policy" {
    queue_url = aws_sqs_queue.iot_sns_sqs_tf_queue.id
  
    policy = jsonencode({
      "Version"    : "2012-10-17",
      "Id"         : "ExampleQueuePolicy",
      "Statement" : [
        {
          "Sid"       : "AllowSNSMessages",
          "Effect"    : "Allow",
          "Principal" : { "AWS" : "*" },
          "Action"    : "SQS:SendMessage",
          "Resource"  : aws_sqs_queue.iot_sns_sqs_tf_queue.arn,
          "Condition" : {
            "ArnEquals" : {
              "aws:SourceArn" : aws_sns_topic.iot_sns_sqs_tf_topic.arn
            }
          }
        }
      ]
    })
  }
  
resource "aws_iot_topic_rule" "iot_sns_sqs_tf_rule" {
    name         = "IotSnsSqstfRule"
    sql          = "SELECT * FROM 'device/data'"
    sql_version  = "2016-03-23"
    enabled = true
  
    sns {
      message_format = "RAW"
      role_arn       = aws_iam_role.role.arn
      target_arn     = aws_sns_topic.iot_sns_sqs_tf_topic.arn
    }
  }
  
  
data "aws_iam_policy_document" "assume_role" {
    statement {
      effect = "Allow"
  
      principals {
        type        = "Service"
        identifiers = ["iot.amazonaws.com"]
      }
  
      actions = ["sts:AssumeRole"]
    }
  }
  
resource "aws_iam_role" "role" {
    name               = "myrole"
    assume_role_policy = data.aws_iam_policy_document.assume_role.json
  }
    
  
data "aws_iam_policy_document" "iam_policy_for_lambda" {
    statement {
      effect    = "Allow"
      actions   = ["sns:Publish"]
      resources = [aws_sns_topic.iot_sns_sqs_tf_topic.arn]
    }
  }
  
resource "aws_iam_role_policy" "iam_policy_for_lambda" {
    name   = "mypolicy"
    role   = aws_iam_role.role.id
    policy = data.aws_iam_policy_document.iam_policy_for_lambda.json
  }
  