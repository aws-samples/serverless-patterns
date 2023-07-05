module "consume_ami_in_creator_account" {
  count                = var.consumer ? 1 : 0
  source               = "../ami_consumer"
  ami_creator_account  = true
  configuration_inputs = local.configurations_details
}


resource "aws_cloudwatch_event_rule" "modify_image_attribute_event" {
  name        = "modify_image_attribute_event"
  description = "AMI Share events"

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
      "ModifyImageAttribute",
      "DeregisterImage"
    ]
  }
}
PATTERN
}

resource "aws_cloudwatch_event_target" "ami_share_event_target" {
  rule      = aws_cloudwatch_event_rule.modify_image_attribute_event.name
  target_id = "ami-share"
  arn       = aws_lambda_function.ami_share_lambda.arn
}



resource "aws_iam_role" "ami_share_lambda_role" {
  name               = "ami-share-lambda-role-${local.creation_account_id}-${local.creation_region}"
  assume_role_policy = data.aws_iam_policy_document.ami_share_assume_role.json
}

resource "aws_iam_role_policy" "ami_share_lambda_role_policy" {
  name   = "ami-share-lambda-role-policy-${local.creation_account_id}-${local.creation_region}"
  role   = aws_iam_role.ami_share_lambda_role.id
  policy = data.aws_iam_policy_document.ami_share_lambda_policy_document.json
}

resource "aws_iam_role_policy_attachment" "ami_share_role_policy_attachment" {
  role       = aws_iam_role.ami_share_lambda_role.name
  count      = length(var.iam_policy_arn)
  policy_arn = var.iam_policy_arn[count.index]
}

#tfsec:ignore:aws-lambda-enable-tracing
resource "aws_lambda_function" "ami_share_lambda" {
  #checkov:skip=CKV_AWS_117:Disable lambda function within AWS VPC
  #checkov:skip=CKV_AWS_116:Disable lambda function DLQ
  #checkov:skip=CKV_AWS_50:Disable lambda function X-ray tracing
  #checkov:skip=CKV_AWS_173:Lambda function environment variables
  #checkov:skip=CKV_AWS_272:Lambda function without code sign
  function_name                  = "${var.ami_share_function_name}-${local.creation_account_id}-${local.creation_region}"
  role                           = aws_iam_role.ami_share_lambda_role.arn
  handler                        = "share_ami.lambda_handler"
  filename                       = data.archive_file.ami_share_lambda_function.output_path
  source_code_hash               = data.archive_file.ami_share_lambda_function.output_base64sha256
  runtime                        = var.lambda_runtime
  timeout                        = var.lambda_timeout
  memory_size                    = var.lambda_memory_size
  reserved_concurrent_executions = 1
  environment {
    variables = {
      DYNAMODB_TABLE_NAME = aws_dynamodb_table.ami_share_dynamodb_table.id
      SSM_PREFIX          = var.ssm_prefix
    }
  }
}

resource "aws_lambda_permission" "allow_eventbridge_to_invoke_lambda" {
  statement_id  = "AllowExecutionFromEventBridge"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.ami_share_lambda.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.modify_image_attribute_event.arn
}


#tfsec:ignore:aws-dynamodb-table-customer-key
resource "aws_dynamodb_table" "ami_share_dynamodb_table" {
  #checkov:skip=CKV_AWS_119:Amazon dynamodb table encrypted using AWS managed CMK
  name         = "AmiShare"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "image_id"
  range_key    = "shared_entitiy_id"

  attribute {
    name = "image_id"
    type = "S"
  }

  attribute {
    name = "shared_entitiy_id"
    type = "S"
  }
  server_side_encryption {
    enabled = true
  }
  point_in_time_recovery {
    enabled = true
  }
  tags = {
    Environment = "development"
  }
}

resource "aws_iam_policy" "dynamodb_external_policy" {
  name   = "DynamoDb_External_policy-${local.creation_account_id}-${local.creation_region}"
  path   = "/"
  policy = data.aws_iam_policy_document.external_dynamodb_access_policy_document.json
}

resource "aws_iam_role" "external_ddb_role" {
  name               = "external-ddb-role-${local.creation_account_id}-${local.creation_region}"
  assume_role_policy = data.aws_iam_policy_document.external_assume_role.json
}

resource "aws_iam_policy_attachment" "external_ddb_role_attachment" {
  name       = "attachment"
  roles      = [aws_iam_role.external_ddb_role.name]
  policy_arn = aws_iam_policy.dynamodb_external_policy.arn
}


resource "aws_ssm_parameter" "emails" {
  for_each    = { for idx, mapping in var.account_email_mapping : idx => mapping }
  name        = "${var.ssm_prefix}/${each.value.account}"
  description = "Email ID of AWS Account owner"
  type        = "SecureString"
  value       = each.value.email
}

resource "aws_ses_email_identity" "this" {
  # for_each = toset(var.account_email_mapping)
  for_each = { for idx, mapping in var.account_email_mapping : idx => mapping }
  email    = each.value.email
}
