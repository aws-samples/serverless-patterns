# data source to lookup information about the current AWS partition in which Terraform is working
data "aws_partition" "current" {}

# data source to get the access to the effective Account ID, User ID, and ARN in which Terraform is authorized
data "aws_caller_identity" "current" {}

# data source to obtain the name of the AWS region configured on the provider
data "aws_region" "current" {}