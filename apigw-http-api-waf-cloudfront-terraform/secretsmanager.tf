# Secret store for CloudFront header
resource "aws_secretsmanager_secret" "cf_api_header_secret_store" {
  name = var.cloudfront_api_secret_name
  description = "CloudFront secret"
}

# Secret value for CloudFront header
resource "aws_secretsmanager_secret_version" "cf_api_header_secret_value" {
  secret_id     = aws_secretsmanager_secret.cf_api_header_secret_store.id
  secret_string = random_id.secret_random_value.hex
}

# Random value for CloudFront header
resource "random_id" "secret_random_value" {
    byte_length = var.unique_key_length
}

# Secret rotation
resource "aws_secretsmanager_secret_rotation" "cf_api_header_secret_store_rotation" {
  secret_id           = aws_secretsmanager_secret.cf_api_header_secret_store.id
  rotation_lambda_arn = aws_lambda_function.secret_rotation_lambda.arn

  rotation_rules {
    automatically_after_days = 30
  }
}