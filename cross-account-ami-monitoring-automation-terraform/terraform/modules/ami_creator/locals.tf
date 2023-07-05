locals {
  creation_account_id = data.aws_caller_identity.creation_account.account_id
  creation_region     = data.aws_region.creation_account.id
  configurations_details = tomap({
    external_assume_role_arn : aws_iam_role.external_ddb_role.arn,
    ami_share_ddb_table : aws_dynamodb_table.ami_share_dynamodb_table.name
  })
}