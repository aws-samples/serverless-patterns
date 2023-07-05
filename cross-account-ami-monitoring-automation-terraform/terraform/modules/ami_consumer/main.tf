resource "aws_cloudwatch_event_rule" "ami_usage_events" {
  name        = "ami_usage_events"
  description = "AMI Usage events"

  event_pattern = <<PATTERN
{
  "source": [
    "aws.ec2"
  ],
  "detail-type": [
    "AWS API Call via CloudTrail"
  ],
  "detail": {
    "eventSource": [
      "ec2.amazonaws.com"
    ],
    "eventName": [
      "RunInstances",
      "CreateLaunchTemplate",
      "TerminateInstances",
      "DeleteLaunchTemplate",
      "CreateLaunchTemplateVersion",
      "DeleteLaunchTemplateVersions"
    ]
  }
}
PATTERN
}

resource "aws_cloudwatch_event_target" "ami_usage_event_target" {
  count     = var.ami_creator_account ? 0 : 1
  rule      = aws_cloudwatch_event_rule.ami_usage_events.name
  target_id = "ami-usage"
  arn       = aws_lambda_function.ami_usage_lambda[0].arn
}

resource "aws_cloudwatch_event_target" "creator_ami_usage_event_target" {
  count     = var.ami_creator_account ? 1 : 0
  rule      = aws_cloudwatch_event_rule.ami_usage_events.name
  target_id = "ami-usage"
  arn       = aws_lambda_function.creator_ami_usage_lambda[0].arn
}

resource "aws_iam_role" "ami_usage_lambda_role" {
  name               = "ami-usage-lambda-role-${local.consumer_account_id}-${local.consumer_region}"
  assume_role_policy = data.aws_iam_policy_document.ami_usage_assume_role.json
}

resource "aws_iam_role_policy" "ami_usage_lambda_role_policy" {
  name   = "ami-usage-lambda-role-policy-${local.consumer_account_id}-${local.consumer_region}"
  role   = aws_iam_role.ami_usage_lambda_role.id
  policy = data.aws_iam_policy_document.ami_usage_lambda_policy_document.json
}

resource "aws_iam_role_policy_attachment" "ami_usage_role_policy_attachment" {
  role       = aws_iam_role.ami_usage_lambda_role.name
  count      = length(var.iam_policy_arn)
  policy_arn = var.iam_policy_arn[count.index]
}


#tfsec:ignore:aws-lambda-enable-tracing
resource "aws_lambda_function" "ami_usage_lambda" {
  #checkov:skip=CKV_AWS_117:Disable lambda function within AWS VPC
  #checkov:skip=CKV_AWS_116:Disable lambda function DLQ
  #checkov:skip=CKV_AWS_50:Disable lambda function X-ray tracing
  #checkov:skip=CKV_AWS_173:Lambda function environment variables
  #checkov:skip=CKV_AWS_272:Lambda function without code sign
  count                          = var.ami_creator_account ? 0 : 1
  function_name                  = var.ami_usage_function_name
  description                    = "This lambda function will monitor the AMI usage in this account and update dynamodb tables"
  role                           = aws_iam_role.ami_usage_lambda_role.arn
  handler                        = "ami_usage.lambda_handler"
  filename                       = data.archive_file.ami_usage_lambda_function[0].output_path
  source_code_hash               = data.archive_file.ami_usage_lambda_function[0].output_base64sha256
  runtime                        = var.lambda_runtime
  timeout                        = var.lambda_timeout
  memory_size                    = var.lambda_memory_size
  reserved_concurrent_executions = 1
  environment {
    variables = {
      EXTERNAL_ROLE_ARN  = local.external_assume_role_arn
      AMI_TABLE_NAME     = local.ami_share_ddb_table
      MAPPING_TABLE_NAME = aws_dynamodb_table.ami_mapping_table.id
    }
  }
}


#tfsec:ignore:aws-lambda-enable-tracing
resource "aws_lambda_function" "creator_ami_usage_lambda" {
  #checkov:skip=CKV_AWS_117:Disable lambda function within AWS VPC
  #checkov:skip=CKV_AWS_116:Disable lambda function DLQ
  #checkov:skip=CKV_AWS_50:Disable lambda function X-ray tracing
  #checkov:skip=CKV_AWS_173:Lambda function environment variables
  #checkov:skip=CKV_AWS_272:Lambda function without code sign
  count                          = var.ami_creator_account ? 1 : 0
  function_name                  = "${var.ami_usage_function_name}-${local.consumer_account_id}-${local.consumer_region}"
  description                    = "This lambda function will monitor the AMI usage in this account and update dynamodb tables"
  role                           = aws_iam_role.ami_usage_lambda_role.arn
  handler                        = "creator_ami_usage.lambda_handler"
  filename                       = data.archive_file.creator_ami_usage_lambda_function[0].output_path
  source_code_hash               = data.archive_file.creator_ami_usage_lambda_function[0].output_base64sha256
  runtime                        = var.lambda_runtime
  timeout                        = var.lambda_timeout
  memory_size                    = var.lambda_memory_size
  reserved_concurrent_executions = 1
  environment {
    variables = {
      EXTERNAL_ROLE_ARN  = local.external_assume_role_arn
      AMI_TABLE_NAME     = local.ami_share_ddb_table
      MAPPING_TABLE_NAME = aws_dynamodb_table.ami_mapping_table.id
    }
  }
}

resource "aws_lambda_permission" "allow_eventbridge_to_invoke_lambda_usage" {
  count         = var.ami_creator_account ? 0 : 1
  statement_id  = "AllowExecutionFromEventBridge"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.ami_usage_lambda[0].function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.ami_usage_events.arn
}
resource "aws_lambda_permission" "creator_allow_eventbridge_to_invoke_lambda_usage" {
  count         = var.ami_creator_account ? 1 : 0
  statement_id  = "AllowExecutionFromEventBridge"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.creator_ami_usage_lambda[0].function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.ami_usage_events.arn
}

#tfsec:ignore:aws-dynamodb-table-customer-key
resource "aws_dynamodb_table" "ami_mapping_table" {
  #checkov:skip=CKV_AWS_119:Amazon dynamodb table encrypted using AWS managed CMK
  name         = "Mapping"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "id"

  attribute {
    name = "id"
    type = "S"
  }
  point_in_time_recovery {
    enabled = true
  }

  tags = {
    Environment = "development"
  }
  server_side_encryption  {
    enabled = true
  }
}