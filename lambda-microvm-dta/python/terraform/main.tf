data "aws_caller_identity" "current" {}
data "aws_partition" "current" {}

locals {
  account_id = data.aws_caller_identity.current.account_id
  partition  = data.aws_partition.current.partition
  common_tags = merge({
    Project   = var.project_name
    ManagedBy = "terraform"
  }, var.tags)
}

# --------------------------------------------------------------------------- #
# Artifact + report bucket
# --------------------------------------------------------------------------- #
resource "aws_s3_bucket" "artifacts" {
  bucket        = var.artifact_bucket_name != "" ? var.artifact_bucket_name : null
  bucket_prefix = var.artifact_bucket_name == "" ? "${var.project_name}-" : null
  force_destroy = true
  tags          = local.common_tags
}

resource "aws_s3_bucket_public_access_block" "artifacts" {
  bucket                  = aws_s3_bucket.artifacts.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_server_side_encryption_configuration" "artifacts" {
  bucket = aws_s3_bucket.artifacts.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_versioning" "artifacts" {
  bucket = aws_s3_bucket.artifacts.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_lifecycle_configuration" "artifacts" {
  bucket = aws_s3_bucket.artifacts.id
  rule {
    id     = "expire-artifacts"
    status = "Enabled"
    filter { prefix = "artifacts/" }
    expiration { days = 14 }
  }
  rule {
    id     = "expire-reports"
    status = "Enabled"
    filter { prefix = "reports/" }
    expiration { days = 30 }
  }
}

# --------------------------------------------------------------------------- #
# MicroVM build role (assumed by the Lambda MicroVMs service during image build)
# --------------------------------------------------------------------------- #
data "aws_iam_policy_document" "microvm_service_trust" {
  statement {
    effect  = "Allow"
    actions = ["sts:AssumeRole", "sts:TagSession"]
    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
  }
}

resource "aws_iam_role" "build" {
  name               = "${var.project_name}-build-role"
  assume_role_policy = data.aws_iam_policy_document.microvm_service_trust.json
  tags               = local.common_tags
}

data "aws_iam_policy_document" "build" {
  statement {
    sid       = "ReadArtifact"
    effect    = "Allow"
    actions   = ["s3:GetObject"]
    resources = ["${aws_s3_bucket.artifacts.arn}/*"]
  }
  statement {
    sid       = "BuildLogs"
    effect    = "Allow"
    actions   = ["logs:CreateLogGroup", "logs:CreateLogStream", "logs:PutLogEvents"]
    resources = ["arn:${local.partition}:logs:${var.region}:${local.account_id}:*"]
  }
}

resource "aws_iam_role_policy" "build" {
  name   = "microvm-build-policy"
  role   = aws_iam_role.build.id
  policy = data.aws_iam_policy_document.build.json
}

# --------------------------------------------------------------------------- #
# MicroVM execution role (assumed by the running MicroVM). The sample grants no
# application permissions; an explicit deny is belt-and-suspenders only.
# --------------------------------------------------------------------------- #
resource "aws_iam_role" "execution" {
  name               = "${var.project_name}-execution-role"
  assume_role_policy = data.aws_iam_policy_document.microvm_service_trust.json
  tags               = local.common_tags
}

data "aws_iam_policy_document" "execution_deny" {
  statement {
    sid    = "DenySecretsAndParameters"
    effect = "Deny"
    actions = [
      "secretsmanager:GetSecretValue",
      "ssm:GetParameter",
      "ssm:GetParameters",
      "ssm:GetParametersByPath",
      "kms:Decrypt",
    ]
    resources = ["*"]
  }
}

resource "aws_iam_role_policy" "execution" {
  name   = "microvm-execution-minimal"
  role   = aws_iam_role.execution.id
  policy = data.aws_iam_policy_document.execution_deny.json
}

# --------------------------------------------------------------------------- #
# GitHub Actions OIDC CI role
# --------------------------------------------------------------------------- #
resource "aws_iam_openid_connect_provider" "github" {
  count           = var.enable_github_oidc_role && var.create_github_oidc_provider ? 1 : 0
  url             = "https://token.actions.githubusercontent.com"
  client_id_list  = ["sts.amazonaws.com"]
  thumbprint_list = ["6938fd4d98bab03faadb97b34396831e3780aea1"]
  tags            = local.common_tags
}

locals {
  github_oidc_provider_arn = var.create_github_oidc_provider ? try(aws_iam_openid_connect_provider.github[0].arn, "") : "arn:${local.partition}:iam::${local.account_id}:oidc-provider/token.actions.githubusercontent.com"
}

data "aws_iam_policy_document" "ci_trust" {
  count = var.enable_github_oidc_role ? 1 : 0
  statement {
    effect  = "Allow"
    actions = ["sts:AssumeRoleWithWebIdentity"]
    principals {
      type        = "Federated"
      identifiers = [local.github_oidc_provider_arn]
    }
    condition {
      test     = "StringEquals"
      variable = "token.actions.githubusercontent.com:aud"
      values   = ["sts.amazonaws.com"]
    }
    condition {
      test     = "StringLike"
      variable = "token.actions.githubusercontent.com:sub"
      values   = ["repo:${var.github_org}/${var.github_repo}:ref:refs/heads/${var.github_branch}"]
    }
  }
}

resource "aws_iam_role" "ci" {
  count              = var.enable_github_oidc_role ? 1 : 0
  name               = "${var.project_name}-github-actions-role"
  assume_role_policy = data.aws_iam_policy_document.ci_trust[0].json
  tags               = local.common_tags
}

# IAM actions verified against the AWS Service Authorization Reference for the
# `lambda` service: Lambda MicroVMs actions live under the `lambda:` prefix with
# `Microvm` casing. Run/Create/Update additionally require iam:PassRole and
# lambda:PassNetworkConnector (declared below).
data "aws_iam_policy_document" "ci" {
  count = var.enable_github_oidc_role ? 1 : 0
  statement {
    sid       = "S3ArtifactAccess"
    effect    = "Allow"
    actions   = ["s3:GetObject", "s3:PutObject", "s3:DeleteObject", "s3:ListBucket"]
    resources = [aws_s3_bucket.artifacts.arn, "${aws_s3_bucket.artifacts.arn}/*"]
  }

  statement {
    sid    = "LambdaMicrovmsControlPlane"
    effect = "Allow"
    actions = [
      "lambda:CreateMicrovmImage",
      "lambda:UpdateMicrovmImage",
      "lambda:GetMicrovmImage",
      "lambda:GetMicrovmImageBuild",
      "lambda:ListMicrovmImages",
      "lambda:ListMicrovmImageBuilds",
      "lambda:RunMicrovm",
      "lambda:GetMicrovm",
      "lambda:ListMicrovms",
      "lambda:CreateMicrovmAuthToken",
      "lambda:SuspendMicrovm",
      "lambda:ResumeMicrovm",
      "lambda:TerminateMicrovm",
    ]
    # The control-plane resource type (microvm-image) is scoped where supported;
    # list/run operations that the service models as account-level still require "*".
    resources = ["*"]
  }

  statement {
    sid       = "PassRolesToMicrovmService"
    effect    = "Allow"
    actions   = ["iam:PassRole"]
    resources = [aws_iam_role.build.arn, aws_iam_role.execution.arn]
    condition {
      test     = "StringEquals"
      variable = "iam:PassedToService"
      values   = ["lambda.amazonaws.com"]
    }
  }

  statement {
    sid       = "PassNetworkConnector"
    effect    = "Allow"
    actions   = ["lambda:PassNetworkConnector"]
    resources = ["*"]
  }

  statement {
    sid       = "ReadBuildLogs"
    effect    = "Allow"
    actions   = ["logs:DescribeLogGroups", "logs:DescribeLogStreams", "logs:GetLogEvents", "logs:FilterLogEvents"]
    resources = ["arn:${local.partition}:logs:${var.region}:${local.account_id}:*"]
  }

  statement {
    sid    = "ExplicitDenyDangerousAdminActions"
    effect = "Deny"
    actions = [
      "iam:CreateAccessKey",
      "iam:CreateUser",
      "iam:CreateRole",
      "iam:PutUserPolicy",
      "iam:PutRolePolicy",
      "iam:AttachUserPolicy",
      "iam:AttachRolePolicy",
      "iam:UpdateAssumeRolePolicy",
      "iam:CreatePolicyVersion",
      "organizations:*",
      "cloudtrail:StopLogging",
      "cloudtrail:DeleteTrail",
    ]
    resources = ["*"]
  }
}

resource "aws_iam_role_policy" "ci" {
  count  = var.enable_github_oidc_role ? 1 : 0
  name   = "microvm-dta-ci-policy"
  role   = aws_iam_role.ci[0].id
  policy = data.aws_iam_policy_document.ci[0].json
}
