provider "aws" {
  region = "eu-west-1"
}

locals {
  bucket_name = "${random_pet.this.id}-bucket"
}

data "aws_caller_identity" "this" {}

####################################################
# Lambda Function (building from source)
####################################################

module "lambda_function" {
  source  = "terraform-aws-modules/lambda/aws"
  version = "~> 4.0"

  function_name = "${random_pet.this.id}-lambda"
  description   = "My awesome lambda function"
  handler       = "app.handler"
  runtime       = "nodejs12.x"
  publish       = true

  architectures = ["arm64"] # Set to "arm64" if you are running this from ARM, else use "x86_64"

  source_path     = "${path.module}/src"
  build_in_docker = true # This will create a package with the correct architecture for Lambda Function (when building on ARM, for example)

  attach_policy_statements = true
  policy_statements = {
    s3_object_lambda = {
      effect    = "Allow",
      actions   = ["s3-object-lambda:WriteGetObjectResponse"],
      resources = ["*"]
    },

    # Actions taken from https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-policy-template-list.html#s3-crud-policy
    s3_crud = {
      effect = "Allow",
      actions = [
        "s3:GetObject",
        "s3:ListBucket",
        "s3:GetBucketLocation",
        "s3:GetObjectVersion",
        "s3:PutObject",
        "s3:PutObjectAcl",
        "s3:GetLifecycleConfiguration",
        "s3:PutLifecycleConfiguration",
        "s3:DeleteObject"
      ],
      resources = [
        "arn:aws:s3:::${local.bucket_name}",
        "arn:aws:s3:::${local.bucket_name}/*",
      ]
    },
  }

  tags = {
    Pattern = "terraform-s3-object-lambda"
    Module  = "lambda_function"
  }
}


###################
# S3 bucket
###################

module "s3_bucket" {
  source  = "terraform-aws-modules/s3-bucket/aws"
  version = "~> 3.0"

  bucket        = local.bucket_name
  force_destroy = true

  attach_policy = true
  policy        = data.aws_iam_policy_document.bucket_policy.json

  # S3 bucket-level Public Access Block configuration
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true

  tags = {
    Pattern = "terraform-s3-object-lambda"
    Module  = "s3_bucket"
  }
}

data "aws_iam_policy_document" "bucket_policy" {
  statement {
    principals {
      type        = "AWS"
      identifiers = ["*"]
    }

    actions = [
      "*",
    ]

    resources = [
      "arn:aws:s3:::${local.bucket_name}",
      "arn:aws:s3:::${local.bucket_name}/*",
    ]

    condition {
      test     = "StringEquals"
      variable = "s3:DataAccessPointAccount"
      values   = [data.aws_caller_identity.this.account_id]
    }
  }
}

################################
# S3 Object Lambda Access Point
################################
resource "aws_s3_access_point" "this" {
  bucket = module.s3_bucket.s3_bucket_id
  name   = "resize-ap"
}

resource "aws_s3control_object_lambda_access_point" "this" {
  name = "resize-olap"

  configuration {
    supporting_access_point = aws_s3_access_point.this.arn

    transformation_configuration {
      actions = ["GetObject"]

      content_transformation {
        aws_lambda {
          function_arn = module.lambda_function.lambda_function_arn
        }
      }
    }
  }
}

resource "aws_s3control_object_lambda_access_point_policy" "this" {
  name = aws_s3control_object_lambda_access_point.this.name

  policy = data.aws_iam_policy_document.object_lambda_access_point_policy.json
  #  jsonencode({
  #    Version = "2008-10-17"
  #    Statement = [{
  #      Effect = "Allow"
  #      Action = "s3-object-lambda:GetObject"
  #      Principal = {
  #        AWS = data.aws_caller_identity.this.account_id
  #      }
  #      Resource = aws_s3control_object_lambda_access_point.this.arn
  #    }]
  #  })
}

data "aws_iam_policy_document" "object_lambda_access_point_policy" {
  statement {
    principals {
      type        = "AWS"
      identifiers = [data.aws_caller_identity.this.account_id]
    }

    actions = [
      "s3-object-lambda:GetObject",
    ]

    resources = [
      aws_s3control_object_lambda_access_point.this.arn
    ]
  }
}

##################
# Extra resources
##################

resource "random_pet" "this" {
  length = 2
}
