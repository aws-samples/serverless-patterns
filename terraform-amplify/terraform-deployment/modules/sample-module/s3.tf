# TODO - Update this file to add S3 lifecycle rule for .temp files "/temp"
# TODO - Create optional S3 Remote State bucket
resource "random_uuid" "sample_landing_bucket_uuid" {
}
resource "random_uuid" "sample_input_bucket_uuid" {
}
resource "random_uuid" "sample_output_bucket_uuid" {
}
resource "random_uuid" "sample_app_storage_bucket_uuid" {
}

# [Notes:]
# Why are you using data sources instead of jsonencode() for policies?
# Data sources let you check the syntax of your json code by running 'terraform validate'
# This happens automatically when running 'terraform plan' and 'terraform apply'
# In the event your syntax is correct, it will tell you what is in correct
# When using jsonencode() you will just get a MalformedPolicy error if something is incorrect

# - S3 Bucket Policies -
# The S3 Bucket Polices do the following:
#  - Allow the s3:PutObject action only for objects that have specific extensions (suffix)
#  - Explicitly deny the s3:PutObject action for objects that don't have the specific extensions (suffix)
# Note: This explicit deny statement applies the file-type requirement to users with full access to your Amazon S3 resources.
# [More info]: https://aws.amazon.com/premiumsupport/knowledge-center/s3-allow-certain-file-types/


# Landing Bucket IAM Policy
data "aws_iam_policy_document" "sample_landing_bucket_restrict_file_types" {
  statement {
    principals {
      type = "AWS"
      identifiers = [
        "${data.aws_caller_identity.current.account_id}",
      ]
    }
    effect  = "Allow"
    actions = ["s3:PutObject", "s3:GetObject"]
    # Allows all S3 operations for files matching the below suffixes
    resources = [
      "${aws_s3_bucket.sample_landing_bucket.arn}/*.amr",
      "${aws_s3_bucket.sample_landing_bucket.arn}/*.flac",
      "${aws_s3_bucket.sample_landing_bucket.arn}/*.mp3",
      "${aws_s3_bucket.sample_landing_bucket.arn}/*.mp4",
      "${aws_s3_bucket.sample_landing_bucket.arn}/*.ogg",
      "${aws_s3_bucket.sample_landing_bucket.arn}/*.webm",
      "${aws_s3_bucket.sample_landing_bucket.arn}/*.wav",
    ]
  }
  statement {
    principals {
      type        = "AWS"
      identifiers = ["*"]
    }
    # WARNING - this is an EXPLICIT DENY. Be very careful of the action for this statement.condition {
    # If you accidentally change it to "s3:*", you will lock yourself out of the bucket.
    # To resolve this, you must log in to the root user account and delete the policy.
    effect  = "Deny"
    actions = ["s3:PutObject"]
    # Denys all S3 operations for files that do not match the below suffixes
    not_resources = [
      "${aws_s3_bucket.sample_landing_bucket.arn}/*.amr",
      "${aws_s3_bucket.sample_landing_bucket.arn}/*.flac",
      "${aws_s3_bucket.sample_landing_bucket.arn}/*.mp3",
      "${aws_s3_bucket.sample_landing_bucket.arn}/*.mp4",
      "${aws_s3_bucket.sample_landing_bucket.arn}/*.ogg",
      "${aws_s3_bucket.sample_landing_bucket.arn}/*.webm",
      "${aws_s3_bucket.sample_landing_bucket.arn}/*.wav",
    ]
  }
}
# Landing S3 Bucket Policy
resource "aws_s3_bucket_policy" "sample_landing_bucket_restrict_file_types" {
  count  = var.sample_s3_enable_bucket_policy ? 1 : 0
  bucket = aws_s3_bucket.sample_landing_bucket.id
  policy = data.aws_iam_policy_document.sample_landing_bucket_restrict_file_types.json
}

# Input Bucket IAM Policy
data "aws_iam_policy_document" "sample_input_bucket_restrict_file_types" {
  statement {
    principals {
      type = "AWS"
      identifiers = [
        "${data.aws_caller_identity.current.account_id}"
      ]
    }
    effect  = "Allow"
    actions = ["s3:PutObject", "s3:GetObject"]
    # Allows all S3 operations for files matching the below suffixes
    resources = [
      "${aws_s3_bucket.sample_input_bucket.arn}/*.amr",
      "${aws_s3_bucket.sample_input_bucket.arn}/*.flac",
      "${aws_s3_bucket.sample_input_bucket.arn}/*.mp3",
      "${aws_s3_bucket.sample_input_bucket.arn}/*.mp4",
      "${aws_s3_bucket.sample_input_bucket.arn}/*.ogg",
      "${aws_s3_bucket.sample_input_bucket.arn}/*.webm",
      "${aws_s3_bucket.sample_input_bucket.arn}/*.wav",
    ]
  }
}

# Input S3 Bucket Policy
resource "aws_s3_bucket_policy" "sample_input_bucket_restrict_file_types" {
  count  = var.sample_s3_enable_bucket_policy ? 1 : 0
  bucket = aws_s3_bucket.sample_input_bucket.id
  policy = data.aws_iam_policy_document.sample_input_bucket_restrict_file_types.json
}

# Output Bucket IAM Policy
data "aws_iam_policy_document" "sample_output_bucket_restrict_file_types" {
  statement {
    principals {
      type        = "AWS"
      identifiers = ["${data.aws_caller_identity.current.account_id}"]
    }
    effect  = "Allow"
    actions = ["s3:PutObject", "s3:GetObject"]
    # Allows all S3 operations for files matching the below suffixes
    resources = [
      "${aws_s3_bucket.sample_output_bucket.arn}/*.json",
      "${aws_s3_bucket.sample_output_bucket.arn}/*.temp",
    ]
  }
  statement {
    principals {
      type        = "AWS"
      identifiers = ["*"]
    }
    # WARNING - this is an EXPLICIT DENY. Be very careful of the action for this statement.condition {
    # If you accidentally change it to "s3:*", you will lock yourself out of the bucket.
    # To resolve this, you must log in to the root user account and delete the policy.
    effect  = "Deny"
    actions = ["s3:PutObject"]
    # Denys all S3 operations for files that do not match the below suffixes
    not_resources = [
      "${aws_s3_bucket.sample_output_bucket.arn}/*.json",
      "${aws_s3_bucket.sample_output_bucket.arn}/*.temp",
    ]
  }
}
# # - Output S3 Bucket Policy -
resource "aws_s3_bucket_policy" "sample_output_bucket_restrict_file_types" {
  count  = var.sample_s3_enable_bucket_policy ? 1 : 0
  bucket = aws_s3_bucket.sample_output_bucket.id
  policy = data.aws_iam_policy_document.sample_output_bucket_restrict_file_types.json
}

# - App Storage IAM Policy -
data "aws_iam_policy_document" "sample_app_storage_bucket_restrict_file_types" {
  statement {
    principals {
      type        = "AWS"
      identifiers = ["${data.aws_caller_identity.current.account_id}"]
    }
    effect  = "Allow"
    actions = ["s3:PutObject", "s3:GetObject"]
    # Allows all S3 operations for files matching the below suffixes
    resources = [
      "${aws_s3_bucket.sample_app_storage_bucket.arn}/*.json",
      "${aws_s3_bucket.sample_app_storage_bucket.arn}/*.amr",
      "${aws_s3_bucket.sample_app_storage_bucket.arn}/*.flac",
      "${aws_s3_bucket.sample_app_storage_bucket.arn}/*.mp3",
      "${aws_s3_bucket.sample_app_storage_bucket.arn}/*.mp4",
      "${aws_s3_bucket.sample_app_storage_bucket.arn}/*.ogg",
      "${aws_s3_bucket.sample_app_storage_bucket.arn}/*.webm",
      "${aws_s3_bucket.sample_app_storage_bucket.arn}/*.wav",
    ]
  }
}
# # - App Storage S3 Bucket Policy -
resource "aws_s3_bucket_policy" "sample_app_storage_bucket_restrict_file_types" {
  count  = var.sample_s3_enable_bucket_policy ? 1 : 0
  bucket = aws_s3_bucket.sample_app_storage_bucket.id
  policy = data.aws_iam_policy_document.sample_app_storage_bucket_restrict_file_types.json
}

# S3 Bucket Notifications -> EventBridge
resource "aws_s3_bucket_notification" "sample_landing_bucket_events" {
  bucket = aws_s3_bucket.sample_landing_bucket.id
  # Send all S3 events for this bucket to EventBridge
  eventbridge = true
}
# S3 Bucket Notifications -> EventBridge
resource "aws_s3_bucket_notification" "sample_input_bucket_events" {
  bucket = aws_s3_bucket.sample_input_bucket.id
  # Send all S3 events for this bucket to EventBridge
  eventbridge = true
}
resource "aws_s3_bucket_notification" "sample_output_bucket_events" {
  bucket = aws_s3_bucket.sample_output_bucket.id
  # Send all S3 events for this bucket to EventBridge
  eventbridge = true
}
resource "aws_s3_bucket_notification" "sample_app_storage_bucket_events" {
  bucket = aws_s3_bucket.sample_app_storage_bucket.id
  # Send all S3 events for this bucket to EventBridge
  eventbridge = true
}



# - LifeCycle Configurations -
# S3 Output Bucket has the necessary files copied to other S3 buckets automatically.
# This is handled by Lambda. This lifecycle configuration removes all of the objects
# in the bucket after 1 day. You can configure the number of days by changing the value
# for the variable 'sample_output_bucket_days_until_objects_expiration' or disable the
# lifecycle policy completely by setting 'sample_output_bucket_create_nuke_everything_lifecycle_config'
# to false.
resource "aws_s3_bucket_lifecycle_configuration" "sample_landing_bucket_lifecycle_config" {
  count  = var.sample_landing_bucket_create_nuke_everything_lifecycle_config ? 1 : 0
  bucket = aws_s3_bucket.sample_landing_bucket.id
  rule {
    id = "nuke-everything"
    filter {} // empty filter = rule applies to all objects in the bucket
    expiration {
      days = var.sample_landing_bucket_days_until_objects_expiration
    }
    status = "Enabled"
  }
}
resource "aws_s3_bucket_lifecycle_configuration" "sample_input_bucket_lifecycle_config" {
  count  = var.sample_input_bucket_create_nuke_everything_lifecycle_config ? 1 : 0
  bucket = aws_s3_bucket.sample_input_bucket.id
  rule {
    id = "nuke-everything"
    filter {} // empty filter = rule applies to all objects in the bucket
    expiration {
      days = var.sample_input_bucket_days_until_objects_expiration
    }
    status = "Enabled"
  }
}
resource "aws_s3_bucket_lifecycle_configuration" "sample_output_bucket_lifecycle_config" {
  count  = var.sample_output_bucket_create_nuke_everything_lifecycle_config ? 1 : 0
  bucket = aws_s3_bucket.sample_output_bucket.id
  rule {
    id = "nuke-everything"
    filter {} // empty filter = rule applies to all objects in the bucket
    expiration {
      days = var.sample_output_bucket_days_until_objects_expiration
    }
    status = "Enabled"
  }
}

# - S3 Buckets -
# S3 Landing Bucket
resource "aws_s3_bucket" "sample_landing_bucket" {
  bucket        = "${var.sample_landing_bucket_name}-${random_uuid.sample_landing_bucket_uuid.result}"
  force_destroy = var.s3_enable_force_destroy

  tags = merge(
    {
      "AppName" = var.app_name
    },
    var.tags,
  )
}
# S3 Landing Bucket - Block Public Access
resource "aws_s3_bucket_public_access_block" "sample_landing_bucket_block_public_access" {
  count               = var.sample_s3_block_public_access ? 1 : 0
  bucket              = aws_s3_bucket.sample_landing_bucket.id
  block_public_acls   = var.sample_s3_block_public_acls
  block_public_policy = var.sample_s3_block_public_policy
}
# S3 Landing Bucket - CORS Policy
resource "aws_s3_bucket_cors_configuration" "sample_landing_bucket_cors" {
  count  = var.sample_landing_bucket_enable_cors ? 1 : 0
  bucket = aws_s3_bucket.sample_landing_bucket.id

  cors_rule {
    allowed_headers = ["*"]
    allowed_methods = ["GET", "HEAD", "PUT", "POST", "DELETE"]
    allowed_origins = ["*"]
    expose_headers = [
      "x-amz-server-side-encryption",
      "x-amz-request-id",
      "x-amz-id-2", "ETag"
    ]
    max_age_seconds = 3000
  }

}
# S3 Input Bucket
resource "aws_s3_bucket" "sample_input_bucket" {
  bucket        = "${var.sample_input_bucket_name}-${random_uuid.sample_input_bucket_uuid.result}"
  force_destroy = var.s3_enable_force_destroy

  tags = merge(
    {
      "AppName" = var.app_name
    },
    var.tags,
  )
}
# S3 Input Bucket - Block Public Access
resource "aws_s3_bucket_public_access_block" "sample_input_bucket_block_public_access" {
  count               = var.sample_s3_block_public_access ? 1 : 0
  bucket              = aws_s3_bucket.sample_input_bucket.id
  block_public_acls   = var.sample_s3_block_public_acls
  block_public_policy = var.sample_s3_block_public_policy
}
# S3 Input Bucket - CORS Policy
resource "aws_s3_bucket_cors_configuration" "sample_input_bucket_cors" {
  count  = var.sample_input_bucket_enable_cors ? 1 : 0
  bucket = aws_s3_bucket.sample_input_bucket.id

  cors_rule {
    allowed_headers = ["*"]
    allowed_methods = ["GET", "HEAD", "PUT", "POST", "DELETE"]
    allowed_origins = ["*"]
    expose_headers = [
      "x-amz-server-side-encryption",
      "x-amz-request-id",
      "x-amz-id-2", "ETag"
    ]
    max_age_seconds = 3000
  }

}


# S3 Output Bucket
resource "aws_s3_bucket" "sample_output_bucket" {
  bucket        = "${var.sample_output_bucket_name}-${random_uuid.sample_output_bucket_uuid.result}"
  force_destroy = var.s3_enable_force_destroy

  tags = merge(
    {
      "AppName" = var.app_name
    },
    var.tags,
  )
}
# S3 Output Bucket - Block Public Access
resource "aws_s3_bucket_public_access_block" "sample_output_bucket_block_public_access" {
  count               = var.sample_s3_block_public_access ? 1 : 0
  bucket              = aws_s3_bucket.sample_output_bucket.id
  block_public_acls   = var.sample_s3_block_public_acls
  block_public_policy = var.sample_s3_block_public_policy
}
# S3 Output Bucket - CORS Policy
resource "aws_s3_bucket_cors_configuration" "sample_output_bucket_cors" {
  count  = var.sample_output_bucket_enable_cors ? 1 : 0
  bucket = aws_s3_bucket.sample_output_bucket.id

  cors_rule {
    allowed_headers = ["*"]
    allowed_methods = ["GET", "HEAD", "PUT", "POST", "DELETE"]
    allowed_origins = ["*"]
    expose_headers = [
      "x-amz-server-side-encryption",
      "x-amz-request-id",
      "x-amz-id-2", "ETag"
    ]
    max_age_seconds = 3000
  }

}


# S3 Amplify App Storage Bucket
resource "aws_s3_bucket" "sample_app_storage_bucket" {
  bucket        = "${var.sample_app_storage_bucket_name}-${random_uuid.sample_app_storage_bucket_uuid.result}"
  force_destroy = var.s3_enable_force_destroy

  tags = merge(
    {
      "AppName" = var.app_name
    },
    var.tags,
  )
}
# S3 Amplify App Storage Bucket - Block Public Access
resource "aws_s3_bucket_public_access_block" "sample_app_storage_bucket_block_public_access" {
  bucket              = aws_s3_bucket.sample_app_storage_bucket.id
  block_public_acls   = var.sample_s3_block_public_acls
  block_public_policy = var.sample_s3_block_public_policy
}
# S3 Amplify App Storage Bucket - CORS Policy
resource "aws_s3_bucket_cors_configuration" "sample_app_storage_bucket_cors" {
  bucket = aws_s3_bucket.sample_app_storage_bucket.id

  cors_rule {
    allowed_headers = ["*"]
    allowed_methods = ["GET", "HEAD", "PUT", "POST", "DELETE"]
    allowed_origins = ["*"]
    expose_headers = [
      "x-amz-server-side-encryption",
      "x-amz-request-id",
      "x-amz-id-2", "ETag"
    ]
    max_age_seconds = 3000
  }

}

