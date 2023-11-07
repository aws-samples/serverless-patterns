resource "aws_kms_key" "aft_kms_key" {
  description         = "KMS Keys for Data Encryption for Apply Account tags solution"
  is_enabled          = true
  enable_key_rotation = true

  tags = {
    Name = "kms_key_apply_account_tags"
  }

  policy = data.aws_iam_policy_document.key_initial.json
}

resource "aws_kms_alias" "aft_kms_alias" {
  target_key_id = aws_kms_key.aft_kms_key.key_id
  name          = "alias/kms_key_apply_account_tags_alias"
}

data "aws_iam_policy_document" "key_initial" {
  statement {
    sid = "Enable IAM User Permissions"
    principals {
      type        = "AWS"
      identifiers = ["arn:aws:iam::${data.aws_caller_identity.aft_management_id.account_id}:root"]
    }
    actions   = ["kms:*"]
    resources = ["*"]
  }

  statement {
    sid = "allow-cloudwatch-logs-to-use"
    principals {
      type        = "Service"
      identifiers = ["logs.amazonaws.com"]
    }
    actions = [
      "kms:Encrypt*",
      "kms:Decrypt*",
      "kms:ReEncrypt*",
      "kms:GenerateDataKey*",
      "kms:Describe*"
    ]
    resources = ["*"]
    condition {
      test     = "ArnEquals"
      variable = "kms:EncryptionContext:aws:logs:arn"
      values   = ["arn:aws:logs:${local.region}:${data.aws_caller_identity.aft_management_id.account_id}:log-group:*"]
    }
  }
}