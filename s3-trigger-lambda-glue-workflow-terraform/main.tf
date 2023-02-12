data "aws_caller_identity" "current" {}

data "aws_region" "current" {}

# Create a new S3 bucket
resource "aws_s3_bucket" "landing_bucket" {
  bucket = "s3-landing-${data.aws_caller_identity.current.account_id}"
}

# Archive source code for Lambda
data "archive_file" "lambda_zip_file" {
  type = "zip"
  source_file = "${path.module}/src/app.py"
  output_path = "${path.module}/lambda.zip"
}

# Lambda Function
# resource "aws_lambda_function" "lambda_demo_function" {
#   function_name = "lambda-demo-${data.aws_caller_identity.current.account_id}"
#   filename = data.archive_file.lambda_zip_file.output_path
#   source_code_hash = filebase64sha256(data.archive_file.lambda_zip_file.output_path)
#   role = aws_iam_role.lambda_demo_functionrole.arn
#   handler = "app.lambda_handler"
#   runtime = "python3.9"
#   layers = ["arn:aws:lambda:${data.aws_region.current.name}:017000801446:layer:AWSLambdaPowertoolsPython:13"]
#   environment {
#     variables = {
#       POWERTOOLS_SERVICE_NAME = "lambda-demo"
#     }
#   }
# }

##################
# Adding S3 bucket as trigger to my lambda and giving the permissions
##################
resource "aws_s3_bucket_notification" "aws-lambda-trigger" {
  bucket = aws_s3_bucket.landing_bucket.id
  lambda_function {
    lambda_function_arn = aws_lambda_function.file_ingestion_trigger_glue_workflow.arn
    events              = ["s3:ObjectCreated:*"]
#    filter_prefix       = "file_landing/"
#    filter_suffix       = "file-extension"
  }
}
resource "aws_lambda_permission" "file_lambda_permission" {
  statement_id  = "AllowS3Invoke"
  action        = "lambda:InvokeFunction"
  function_name = "${aws_lambda_function.file_ingestion_trigger_glue_workflow.function_name}"
  principal = "s3.amazonaws.com"
  source_arn = "arn:aws:s3:::${aws_s3_bucket.landing_bucket.id}"
}
resource "random_string" "randomstring_fileingestion" {
  length  = 4
  special = false
}
# resource "aws_lambda_layer_version" "lambda_layer_wrangler" {
#   filename   = "${path.module}/../../../../build_tools/awswrangler-layer-2.17.0-py3.9.zip"
#   layer_name = "aws_wrangler"
#   compatible_runtimes = ["python3.9"]
# }
resource "aws_lambda_function" "file_ingestion_trigger_glue_workflow" {
  function_name = "file_ingestion_trigger_glue_workflow"
 
  s3_bucket = aws_s3_bucket.landing_bucket.bucket
  s3_key    = "lambda_scripts/file_ingestion_trigger_glue_workflow.zip"
  source_code_hash = "${data.archive_file.lambda_zip_dir.output_base64sha256}"
 
  runtime = "python3.9"
  handler = "file_ingestion_trigger_glue_workflow.lambda_handler"
  timeout = 900
  role = aws_iam_role.terraform_function_role.arn
  memory_size = 512
  # vpc_config {
  #   # Every subnet should be able to reach an EFS mount target in the same Availability Zone. Cross-AZ mounts are not permitted.
  #   subnet_ids         = var.subnet_id
  #   security_group_ids = var.lambda_sg
  # }
  # layers = [aws_lambda_layer_version.lambda_layer_wrangler.arn]
  ephemeral_storage {
    size = 2048 # Min 512 MB and the Max 10240 MB
  }
}

data "aws_iam_policy_document" "AWSLambdaTrustPolicy" {
  statement {
    actions    = ["sts:AssumeRole"]
    effect     = "Allow"
    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
  }
}
data "aws_iam_policy_document" "AWSLambdaPolicy" {
  statement {
    effect = "Allow"
    actions = [
      "s3:GetBucket*",
      "s3:GetObject*",
      "s3:List*",
      "s3:Abort*",
      "s3:DeleteObject*",
      "s3:GetBucket*",
      "s3:GetObject*",
      "s3:List*",
      "s3:PutObject",
      "s3:PutObjectLegalHold",
      "s3:PutObjectRetention",
      "s3:PutObjectTagging",
      "s3:PutObjectVersionTagging"
    ]

    # principals {
    #   type = "AWS"
    #   identifiers = [
    #     data.aws_caller_identity.current.account_id
    #   ]
    # }

    resources = [
      aws_s3_bucket.landing_bucket.arn
    ]
  }
  statement {
    effect = "Allow"
    actions = [
    "logs:CreateLogGroup",
    "logs:CreateLogStream",
    "logs:PutLogEvents"
    ]

    # principals {
    #   type = "AWS"
    #   identifiers = [
    #     data.aws_caller_identity.current.account_id
    #   ]
    # }

    resources = [
      aws_cloudwatch_log_group.lambda_demo_loggroup.arn
    ]
  }

}
resource "aws_iam_role" "terraform_function_role" {
  name               = "terraform_function_role"
  assume_role_policy = "${data.aws_iam_policy_document.AWSLambdaTrustPolicy.json}"
  # managed_policy_arns = [aws_iam_policy.lambda_policy.arn]
}
resource "aws_iam_policy" "lambda_policy" {
  name        = "lambda_policy"
  description = "Policy to access S3"

  policy = "${data.aws_iam_policy_document.AWSLambdaPolicy.json}"

}

#   policy = <<EOF
#   {
#     "Version": "2012-10-17",
#     "Statement": [
#         {
#             "Action": [
#                 "s3:GetBucket*",
#                 "s3:GetObject*",
#                 "s3:List*"
#             ],
#             "Resource": [
#                 "arn:aws:s3:::cdk-hnb659fds-assets-757674668339-us-east-1/*",
#                 "arn:aws:s3:::cdk-hnb659fds-assets-757674668339-us-east-1"
#             ],
#             "Effect": "Allow"
#         },
#         {
#             "Action": [
#                 "s3:Abort*",
#                 "s3:DeleteObject*",
#                 "s3:GetBucket*",
#                 "s3:GetObject*",
#                 "s3:List*",
#                 "s3:PutObject",
#                 "s3:PutObjectLegalHold",
#                 "s3:PutObjectRetention",
#                 "s3:PutObjectTagging",
#                 "s3:PutObjectVersionTagging"
#             ],
#             "Resource": [
#                 "arn:aws:s3:::glue-assets-757674668339",
#                 "arn:aws:s3:::glue-assets-757674668339/*"
#             ],
#             "Effect": "Allow"
#         }
#     ]
#   }
# EOF

resource "aws_iam_role_policy_attachment" "terraform_lambda_policy" {
  role       = "${aws_iam_role.terraform_function_role.name}"
  policy_arn = aws_iam_policy.lambda_policy.arn
}

resource "aws_s3_object" "lambda_code_upload" {
  key        = "lambda_scripts/file_ingestion_trigger_glue_workflow.zip"
  bucket     = aws_s3_bucket.landing_bucket.bucket
  source     = data.archive_file.lambda_zip_dir.output_path
  etag       = data.archive_file.lambda_zip_dir.output_base64sha256
}
data "archive_file" "lambda_zip_dir" {
  type        = "zip"
  output_path = "/tmp/file_trigger_lambda-${random_string.randomstring_fileingestion.result}.zip"
  source_dir  = "src"
 
}

# #### First American
# resource "aws_glue_workflow" "first_american" {
#   name = "first_american"
# }
# resource "aws_glue_trigger" "first_american-start" {
#   name          = "first_american-start"
#   type          = "ON_DEMAND"
#   workflow_name = aws_glue_workflow.first_american.name
 
#   actions {
#     job_name = "file_ingestion"
#     arguments = {"--run_type"="NORMAL","--process_name"="first_american","--config_path"="file_ingestion_conf_DEV.json","--file_name"="ALL"}
#   }
# }
 
# resource "aws_glue_trigger" "first_american-raw-crawler" {
#   name          = "first_american-raw-crawler"
#   type          = "CONDITIONAL"
#   workflow_name = aws_glue_workflow.first_american.name
 
#   predicate {
#     conditions {
#       job_name = "file_ingestion"
#       state    = "SUCCEEDED"
#       logical_operator = "EQUALS"
#     }
#   }
 
#   actions {
#     crawler_name = "first_american_raw_crawler"
#   }
# }
 
# resource "aws_glue_trigger" "first_american-curated-crawler" {
#   name          = "first_american-curated-crawler"
#   type          = "CONDITIONAL"
#   workflow_name = aws_glue_workflow.first_american.name
 
#   predicate {
#     conditions {
#       job_name = "file_ingestion"
#       state    = "SUCCEEDED"
#       logical_operator = "EQUALS"
#     }
#   }
 

#   actions {
#     crawler_name = "first_american_curated_crawler"
#   }
# }
# CloudWatch Log group to store Lambda logs
resource "aws_cloudwatch_log_group" "lambda_demo_loggroup" {
  name = "/aws/lambda/${aws_lambda_function.file_ingestion_trigger_glue_workflow.function_name}"
  retention_in_days = 365
}


