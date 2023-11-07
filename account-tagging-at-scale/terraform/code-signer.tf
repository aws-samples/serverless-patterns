resource "aws_sqs_queue" "aftlambdadlq" {
  name                       = "sampledlq"
  delay_seconds              = 300
  max_message_size           = 2048
  message_retention_seconds  = 1209600
  visibility_timeout_seconds = 310
  receive_wait_time_seconds  = 20
  sqs_managed_sse_enabled    = true
  tags                       = var.default_tags
}


resource "aws_lambda_code_signing_config" "this" {
  description = "Code signing config for AFT Lambda"

  allowed_publishers {
    signing_profile_version_arns = [
      aws_signer_signing_profile.this.arn,
    ]
  }

  policies {
    untrusted_artifact_on_deployment = "Warn"
  }
}

resource "aws_signer_signing_profile" "this" {
  name_prefix = "AwsLambdaCodeSigningAction"
  platform_id = "AWSLambda-SHA384-ECDSA"

  signature_validity_period {
    value = 5
    type  = "YEARS"
  }

  tags = var.default_tags
}
