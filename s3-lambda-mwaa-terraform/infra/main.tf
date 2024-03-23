locals {
  vpc_cidr = "10.0.0.0/16"
  azs      = slice(data.aws_availability_zones.available.names, 0, 2)
  vpc_name = "serverless-land-vpc"
  input_bucket_name = "input-${data.aws_region.current.name}-${data.aws_caller_identity.current.account_id}"
  mwaa_bucket_name = "mwaa-src-${data.aws_region.current.name}-${data.aws_caller_identity.current.account_id}"
  mwaa_environment_name = "mwaa-serverless-land"
  tags = {
    Project = "Trigger MWAA DAG using S3 Events"
    Category = "Pattern"
    Domain = "Serverless"
    URL = "https://serverlessland.com/"
  }
}

# Input S3 bucket to kick off MWAA DAG/workflow when input is placed
module "input_bucket" {
  #https://github.com/terraform-aws-modules/terraform-aws-s3-bucket
  source                   = "terraform-aws-modules/s3-bucket/aws"
  version                  = "4.1.0"
  bucket                   = local.input_bucket_name
  #https://github.com/terraform-aws-modules/terraform-aws-s3-bucket/issues/223#issuecomment-1516822132
  control_object_ownership = true
  object_ownership         = "BucketOwnerPreferred"
  acl                      = "private"
  force_destroy            = true
  server_side_encryption_configuration = {
    rule = {
      apply_server_side_encryption_by_default = {
        sse_algorithm     = "AES256"
      }
    }
  }
  versioning = {
    enabled = true
  }
  attach_deny_insecure_transport_policy    = true
  attach_require_latest_tls_policy         = true
  attach_deny_incorrect_encryption_headers = true
  # attach_deny_unencrypted_object_uploads   = true
  tags = local.tags
}

# S3 bucket for MWAA DAGS
module "mwaa_bucket" {
  #https://github.com/terraform-aws-modules/terraform-aws-s3-bucket
  source                   = "terraform-aws-modules/s3-bucket/aws"
  version                  = "4.1.0"
  bucket                   = local.mwaa_bucket_name
  #https://github.com/terraform-aws-modules/terraform-aws-s3-bucket/issues/223#issuecomment-1516822132
  control_object_ownership = true
  object_ownership         = "BucketOwnerPreferred"
  acl                      = "private"
  force_destroy            = true
  server_side_encryption_configuration = {
    rule = {
      apply_server_side_encryption_by_default = {
        sse_algorithm     = "AES256"
      }
    }
  }
  versioning = {
    enabled = true
  }
  tags = local.tags
}

# Upload DAGS
resource "aws_s3_object" "dags" {
  for_each = fileset("./src/dags/", "*")
  bucket   = module.mwaa_bucket.s3_bucket_id
  key      = "dags/${each.value}"
  source   = "src/dags/${each.value}"
  etag     = filemd5("src/dags/${each.value}")
}

# VPC and other infrastructure resources required for provisioning MWAA
module "vpc" {
  source               = "terraform-aws-modules/vpc/aws"
  version              = "5.7.0"
  name                 = local.vpc_name
  cidr                 = local.vpc_cidr
  azs                  = local.azs
  private_subnets      = [for k, v in local.azs : cidrsubnet(local.vpc_cidr, 8, k)]
  public_subnets       = [for k, v in local.azs : cidrsubnet(local.vpc_cidr, 8, k+10)]
  enable_nat_gateway   = true
  single_nat_gateway   = true
  enable_dns_hostnames = true
  tags                 = local.tags
}

# MWAA Instance
module "mwaa" {
  # https://github.com/aws-ia/terraform-aws-mwaa
  source                        = "aws-ia/mwaa/aws"
  version                       = "0.0.5"
  name                          = local.mwaa_environment_name
  airflow_version               = "2.8.1"
  environment_class             = "mw1.small"
  create_s3_bucket              = false
  source_bucket_arn             = module.mwaa_bucket.s3_bucket_arn
  dag_s3_path                   = "dags"
  vpc_id                        = module.vpc.vpc_id
  private_subnet_ids            = module.vpc.private_subnets
  source_cidr                   = [local.vpc_cidr]
  min_workers                   = 1
  max_workers                   = 2
  webserver_access_mode         = "PUBLIC_ONLY" # Choose the Private network option(PRIVATE_ONLY) if your Apache Airflow UI is only accessed within a corporate network, and you do not require access to public repositories for web server requirements installation
  tags                          = local.tags
  iam_role_additional_policies  = {
    "dag-policy" = aws_iam_policy.mwaa_policy.arn
  }
  logging_configuration         = {
    dag_processing_logs = {
      enabled   = true
      log_level = "INFO"
    }
    scheduler_logs = {
      enabled   = true
      log_level = "INFO"
    }
    task_logs = {
      enabled   = true
      log_level = "INFO"
    }
    webserver_logs = {
      enabled   = true
      log_level = "INFO"
    }
    worker_logs = {
      enabled   = true
      log_level = "INFO"
    }
  }
  airflow_configuration_options = {
    "core.load_default_connections" = "false"
    "core.load_examples"            = "false"
    "webserver.dag_default_view"    = "tree"
    "webserver.dag_orientation"     = "TB"
    "logging.logging_level"         = "INFO"
  }
}

# IAM policy for MWAA instance role
resource "aws_iam_policy" "mwaa_policy" {
  path        = "/"
  description = "Custom policy for MWAA DAG workflows"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "s3:ListBucket",
          "s3:GetObject",
          "s3:GetObjectVersion",
          "s3:GetObjectVersionAttributes",
          "s3:GetObjectAttributes"
        ]
        Effect = "Allow"
        Resource = [
          module.input_bucket.s3_bucket_arn,
          "${module.input_bucket.s3_bucket_arn}/*"
        ]
      },
    ]
  })
}

# Lambda function to trigger DAG
module "dag_trigger_lambda" {
  #https://github.com/terraform-aws-modules/terraform-aws-lambda
  source                                  = "terraform-aws-modules/lambda/aws"
  version                                 = "7.2.1"
  function_name                           = "dag-trigger-lambda"
  description                             = "Lambda to trigger DAG"
  handler                                 = "index.lambda_handler"
  runtime                                 = "python3.12"
  timeout                                 = 30
  source_path                             = "./src/lambda/trigger-dag/"
  ignore_source_code_hash                 = false
  tracing_mode                            = "Active"
  attach_policy_statements                = true
  policy_statements = {
    airflow_perm = {
      effect    = "Allow",
      actions   = ["airflow:CreateCliToken"],
      resources = [module.mwaa.mwaa_arn]
    }
  }
  environment_variables = {
    "ACCOUNT_ID"         = data.aws_caller_identity.current.account_id
    "MWAA_ENV_NAME"      = local.mwaa_environment_name
    "LOG_LEVEL"          = "DEBUG"
  }
  tags = local.tags
}

# S3-Lambda integration
# File upload events are filtered by prefix and suffix
# Expected filename is "input.json"
module "s3_lambda_notif" {
  #https://github.com/terraform-aws-modules/terraform-aws-s3-bucket/tree/v4.1.0/modules/notification
  source      = "terraform-aws-modules/s3-bucket/aws//modules/notification"
  version     = "4.1.0"
  bucket      = module.input_bucket.s3_bucket_id
  eventbridge = true
  lambda_notifications = {
    dag_trigger_lambda = {
      function_arn  = module.dag_trigger_lambda.lambda_function_arn
      function_name = module.dag_trigger_lambda.lambda_function_name
      events        = ["s3:ObjectCreated:*"]
      filter_prefix = "input"
      filter_suffix = ".json"
    }
  }
}