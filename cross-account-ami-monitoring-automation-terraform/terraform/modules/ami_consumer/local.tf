locals {
  consumer_account_id      = data.aws_caller_identity.consumer_account.account_id
  consumer_region          = data.aws_region.consumer_account.id
  external_assume_role_arn = var.configuration_inputs["external_assume_role_arn"]
  ami_share_ddb_table      = var.configuration_inputs["ami_share_ddb_table"]
}