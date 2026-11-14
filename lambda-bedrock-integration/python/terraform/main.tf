provider "aws" {
  region = "us-east-1"
}

data "aws_region" "current" {}
data "aws_caller_identity" "current" {}

####################################################
# Locals and Tagging
####################################################

locals {
  common_tags = {
    organization = var.organization
    env          = var.env
  }
  region                 = data.aws_region.current.name
  account_id             = data.aws_caller_identity.current.account_id
  standard_resource_name = "${var.env}-${var.organization}-genai-app"
  ecr_base_arn           = "${local.account_id}.dkr.ecr.${local.region}.amazonaws.com"
  aws_path               = "/${var.env}/${var.organization}/"
  containercode_dir      = "./containercode/"
  aws_subnets            = var.aws_subnets
}

/* Uncomment to dynamically get list of subnets based on tags
#################################################################################
# Query Subnets (Assumption that you have a VPC with subnets tagged as Private)
#################################################################################
data "aws_subnets" "private_subnet" {
  filter {
    name   = "vpc-id"
    values = [var.aws_vpc_id]
  }
  tags = {
    Network = "private"
  }
}
*/

##############################
# Create Security Group
##############################
resource "aws_security_group" "this_aws_security_group" {
  name        = local.standard_resource_name
  description = "Allow only outbound traffic for Lambda Function"
  vpc_id      = var.aws_vpc_id
  tags        = local.common_tags
  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

##############################
# Create KMS Key & Policy
##############################
resource "aws_kms_key" "this_aws_kms_key" {
  description             = local.standard_resource_name
  deletion_window_in_days = 30
  policy = templatefile("templates/kms-policy.json",
    {
      account_number         = local.account_id
      standard_resource_name = "${var.env}-${var.organization}"
      region                 = local.region
    }
  )
  multi_region        = true
  enable_key_rotation = true
  tags                = merge(local.common_tags)
}

resource "aws_kms_alias" "this_aws_kms_alias" {
  name          = "alias/${local.standard_resource_name}"
  target_key_id = aws_kms_key.this_aws_kms_key.key_id
}

###########
# ECR
###########
resource "aws_ecr_repository" "this_aws_ecr_repository" {
  name                 = local.standard_resource_name
  tags                 = local.common_tags
  image_tag_mutability = "MUTABLE"
  force_delete         = true
  image_scanning_configuration {
    scan_on_push = true
  }
  encryption_configuration {
    encryption_type = "KMS"
    kms_key         = aws_kms_key.this_aws_kms_key.arn
  }
}

resource "aws_ecr_lifecycle_policy" "ecr_lifecycle_policy" {
  policy = templatefile("templates/ecr-lifecycle-policy.json",
    {}
  )
  repository = aws_ecr_repository.this_aws_ecr_repository.name
}

#####################################
# Checks if build folder has changed
#####################################
data "external" "this_external" {
  program = ["bash", "${path.module}/bin/dir_md5.sh", "${path.module}/${local.containercode_dir}"]
}

########################################################
# Builds service and pushes it into aws_ecr_repository
########################################################
resource "null_resource" "this_null_resource" {
  depends_on = [aws_ecr_repository.this_aws_ecr_repository]
  #triggers   = { always_run = "${timestamp()}" }
  triggers = { build_folder_content_md5 = data.external.this_external.result.md5 }
  provisioner "local-exec" {
    command = "bash ${path.module}/bin/build.sh ${local.ecr_base_arn} ${path.module}/${local.containercode_dir} ${aws_ecr_repository.this_aws_ecr_repository.name} ${aws_ecr_repository.this_aws_ecr_repository.repository_url} ${local.region}"
  }
}

data "aws_ecr_image" "this_aws_ecr_image" {
  depends_on      = [null_resource.this_null_resource]
  repository_name = aws_ecr_repository.this_aws_ecr_repository.name
  image_tag       = "latest"
}

########################################################
# Create IAM role, policy and policy attachment
########################################################
resource "aws_iam_role" "this_aws_iam_role" {
  name               = local.standard_resource_name
  path               = local.aws_path
  description        = "Role to be Assumed by Lambda Task"
  tags               = local.common_tags
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {"Service": "lambda.amazonaws.com"},
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

resource "aws_iam_policy" "this_aws_iam_policy" {
  name = local.standard_resource_name
  policy = templatefile("templates/lambda-role.json", {
    account_number         = local.account_id
    standard_resource_name = local.standard_resource_name
    kms_key_arn            = aws_kms_key.this_aws_kms_key.arn
  })
}

resource "aws_iam_policy_attachment" "this_aws_iam_policy_attachment" {
  name       = local.standard_resource_name
  roles      = [aws_iam_role.this_aws_iam_role.name]
  policy_arn = aws_iam_policy.this_aws_iam_policy.arn
}

###############################
# Cloudwatch log Group
###############################
resource "aws_cloudwatch_log_group" "this_aws_cloudwatch_log_group" {
  name              = "/aws/${local.standard_resource_name}"
  retention_in_days = 30
  kms_key_id        = aws_kms_key.this_aws_kms_key.arn
  tags              = local.common_tags
}

###############################
# AWS Lambda Function
###############################
resource "aws_lambda_function" "this_aws_lambda_function" {
  depends_on    = [null_resource.this_null_resource, aws_ecr_repository.this_aws_ecr_repository]
  description   = "Executes the ${local.standard_resource_name} Function"
  function_name = local.standard_resource_name
  role          = aws_iam_role.this_aws_iam_role.arn
  timeout       = var.timeout
  memory_size   = var.memory_size
  kms_key_arn   = aws_kms_key.this_aws_kms_key.arn
  image_uri     = "${aws_ecr_repository.this_aws_ecr_repository.repository_url}@${data.aws_ecr_image.this_aws_ecr_image.image_digest}"
  package_type  = "Image"
  tags          = local.common_tags
  vpc_config {
    subnet_ids         = local.aws_subnets
    security_group_ids = [aws_security_group.this_aws_security_group.id]
  }
  environment {
    variables = {
      ENV                      = var.env
      ORGANIZATION             = var.organization
      LOGGING_LEVEL            = var.logging_level
      BEDROCK_FOUNDATION_MODEL = var.bedrock_foundation_model
    }
  }
}
