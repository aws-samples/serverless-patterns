data "aws_caller_identity" "current" {}

resource "aws_cloudtrail" "foobar" {
  name                          = "slack_cloudtrail"
  s3_bucket_name                = aws_s3_bucket.foo.id
  s3_key_prefix                 = "prefix"
  include_global_service_events = false

  event_selector {
    read_write_type           = "All"
    include_management_events = false

  data_resource {
    type   = "AWS::Lambda::Function"
    values = var.function_names
    }
  }
  cloud_watch_logs_group_arn = "${aws_cloudwatch_log_group.LambdaInvokeEvents.arn}:*"
  cloud_watch_logs_role_arn = aws_iam_role.cloud_trail.arn
}

resource "aws_s3_bucket" "foo" {
  bucket        = var.bucket_name
  force_destroy = true
}

data "aws_iam_policy_document" "foo" {
  statement {
    sid    = "AWSCloudTrailAclCheck"
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["cloudtrail.amazonaws.com"]
    }

    actions   = ["s3:GetBucketAcl"]
    resources = [aws_s3_bucket.foo.arn]
  }

  statement {
    sid    = "AWSCloudTrailWrite"
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["cloudtrail.amazonaws.com"]
    }

    actions   = ["s3:PutObject"]
    resources = ["${aws_s3_bucket.foo.arn}/prefix/AWSLogs/${data.aws_caller_identity.current.account_id}/*"]

    condition {
      test     = "StringEquals"
      variable = "s3:x-amz-acl"
      values   = ["bucket-owner-full-control"]
    }
  }
}
resource "aws_s3_bucket_policy" "foo" {
  bucket = aws_s3_bucket.foo.id
  policy = data.aws_iam_policy_document.foo.json
}