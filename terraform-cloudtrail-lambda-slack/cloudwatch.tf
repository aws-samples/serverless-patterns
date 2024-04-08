resource "aws_cloudwatch_log_group" "LambdaInvokeEvents" {
  name = "LambdaInvokeEvents"
}


resource "aws_cloudwatch_log_subscription_filter" "logfilter" {
  name            = "slack_lambda_logfilter"
  log_group_name  = aws_cloudwatch_log_group.LambdaInvokeEvents.name
  filter_pattern  = "{$.userIdentity.type=\"IAMUser\"}"
  destination_arn = aws_lambda_function.test_lambda.arn
}


resource "aws_iam_role" "cloud_trail" {
  name = "cloudTrail-cloudWatch-role"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "cloudtrail.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF
}

resource "aws_iam_role_policy" "aws_iam_role_policy_cloudTrail_cloudWatch" {
  name = "cloudTrail-cloudWatch-policy"
  role = aws_iam_role.cloud_trail.id

  policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AWSCloudTrailCreateLogStream2014110",
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogStream"
            ],
            "Resource": [
                "${aws_cloudwatch_log_group.LambdaInvokeEvents.arn}:*"
            ]
        },
        {
            "Sid": "AWSCloudTrailPutLogEvents20141101",
            "Effect": "Allow",
            "Action": [
                "logs:PutLogEvents"
            ],
            "Resource": [
                "${aws_cloudwatch_log_group.LambdaInvokeEvents.arn}:*"
            ]
        }
    ]
}
EOF
}