data "aws_caller_identity" "current" {}
data "aws_partition" "current" {}

resource "random_string" "suffix" {
  length  = 6
  special = false
  upper   = false
}

locals {
  account_id = data.aws_caller_identity.current.account_id
  partition  = data.aws_partition.current.partition
  region     = var.aws_region
  name       = "lambda-web-agentcore-${random_string.suffix.result}"

  # Pick the Claude Haiku 5.5 inference profile that matches the Region's geography.
  geography = split("-", local.region)[0]
  model_id = var.model_id != "" ? var.model_id : (
    contains(["us", "eu"], local.geography) ? "${local.geography}.anthropic.claude-haiku-5-5" : "global.anthropic.claude-haiku-5-5"
  )
  # The foundation model behind the profile, for example anthropic.claude-haiku-5-5.
  foundation_model_id = try(regex("^(?:us|eu|apac|au|jp|ca|global)\\.(.+)$", local.model_id)[0], local.model_id)

  build_dir = abspath("${path.module}/build")
}

# One versioned bucket holds both code packages. Lambda Web Functions deploy code from a specific
# object version, so versioning is required.
resource "aws_s3_bucket" "code" {
  bucket        = "${local.name}-code-${local.account_id}"
  force_destroy = true
}

resource "aws_s3_bucket_versioning" "code" {
  bucket = aws_s3_bucket.code.id

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_public_access_block" "code" {
  bucket                  = aws_s3_bucket.code.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
