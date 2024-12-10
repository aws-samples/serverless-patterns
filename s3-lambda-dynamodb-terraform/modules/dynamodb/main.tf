locals {
  table_name = "${var.project}-${var.table_name}"
}

# Create the Dynamodb table
resource "aws_dynamodb_table" "basic-dynamodb-table" {
  name           = local.table_name
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = var.hash_key

  attribute {
    name = var.hash_key
    type = "S"
  }
}