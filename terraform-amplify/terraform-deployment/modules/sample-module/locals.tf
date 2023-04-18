locals {
  # Workaround for "ValidationException: TimeToLive is already disabled"
  # when running terraform apply twice
  ttl = (var.dynamodb_ttl_enable == true ? [
    {
      ttl_enable = var.dynamodb_ttl_enable
      ttl_attribute : var.dynamodb_ttl_attribute
    }
  ] : [])
}

