# Data source
data "aws_ssm_parameter" "ssm_github_access_token" {
  count = var.lookup_ssm_github_access_token ? 1 : 0
  name  = var.ssm_github_access_token_name
}


# S3 Transcribe Input Bucket SSM Value to be used by Lambda as Environment Variable
resource "aws_ssm_parameter" "sample_input_bucket_name" {
  name  = "sample_input_bucket_name" // This is the 'unique key'
  type  = "String"
  value = aws_s3_bucket.sample_input_bucket.id // App storage S3 bucket

  tags = merge(
    {
      "AppName" = var.app_name
    },
    var.tags,
  )
}

# S3 Transcribe Output Bucket SSM Value to be used by Lambda as Environment Variable
resource "aws_ssm_parameter" "sample_output_bucket_name" {
  name  = "sample_output_bucket_name" // This is the 'unique key'
  type  = "String"
  value = aws_s3_bucket.sample_output_bucket.id // App storage S3 bucket

  tags = merge(
    {
      "AppName" = var.app_name
    },
    var.tags,
  )
}

# S3 App Storage Bucket SSM Value to be used by Lambda as Environment Variable
resource "aws_ssm_parameter" "sample_app_storage_bucket_name" {
  name  = "sample_app_storage_bucket_name" // This is the 'unique key'
  type  = "String"
  value = aws_s3_bucket.sample_app_storage_bucket.id // App storage S3 bucket

  tags = merge(
    {
      "AppName" = var.app_name
    },
    var.tags,
  )
}

# DynamoDB SSM Value to be used by Lambda as Environment Variables
resource "aws_ssm_parameter" "sample_dynamodb_output_table_name" {
  name  = "sample_dynamodb_output_table_name" // This is the 'unique key'
  type  = "String"
  value = aws_dynamodb_table.sample_output.id // Name of the DynamoDB table

  tags = merge(
    {
      "AppName" = var.app_name
    },
    var.tags,
  )
}
