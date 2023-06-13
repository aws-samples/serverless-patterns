resource "aws_kms_key" "kms" {
  description             = "KMS key for SNS"
  provider = aws.default
}


resource "aws_kms_key_policy" "example" {
  key_id = aws_kms_key.kms.id
  policy = jsonencode({
    Id = "KMSKeyForSNS"
    Statement = [
      {
        Action = "kms:*"
        Effect = "Allow"
        Principal = {
          AWS = ["arn:aws:iam::${var.snsAccountId}:root",
                    "arn:aws:iam::${var.lambdaAccountId}:root"]
        }

        Resource = "*"
        Sid      = "Enable IAM User Permissions"
      },
    ]
    Version = "2012-10-17"
  })
  provider = aws.default
}

resource "aws_kms_alias" "alias" {
  name          = "alias/${var.kmsAlias}"
  target_key_id = aws_kms_key.kms.key_id
  provider = aws.default
}