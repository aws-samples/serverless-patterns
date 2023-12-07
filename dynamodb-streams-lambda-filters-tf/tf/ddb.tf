resource "aws_dynamodb_table" "dynamodb_request_table" {
  name             = var.dynamodb_table_name
  billing_mode     = "PAY_PER_REQUEST"
  hash_key         = "request_id"
  stream_enabled   = true
  stream_view_type = "NEW_AND_OLD_IMAGES"

  attribute {
    name = "request_id"
    type = "S"
  }

  server_side_encryption {
    enabled = true
  }

  tags = {
    Name = "dynamodb_table"
  }
}
