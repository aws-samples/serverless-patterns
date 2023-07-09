##################
# This pattern creates a S3 file trigger that triggers a lambda that in turn triggers a Glue Workflow to process the file.
##################

data "aws_caller_identity" "current" {}

data "aws_region" "current" {}

# Create a new S3 bucket to store Glue jobs, Glue Job Logs, etc.
resource "aws_s3_bucket" "landing_bucket" {
  bucket = "s3-landing-${data.aws_caller_identity.current.account_id}"
}

# Archive source code for Lambda
data "archive_file" "lambda_zip_file" {
  type = "zip"
  source_file = "${path.module}/src/app.py"
  output_path = "${path.module}/lambda.zip"
}

##################
# Adding S3 bucket as trigger to my lambda and giving the permissions
##################
resource "aws_s3_bucket_notification" "aws-lambda-trigger" {
  bucket = aws_s3_bucket.landing_bucket.id
  lambda_function {
    lambda_function_arn = aws_lambda_function.first_glue_job_trigger_glue_workflow.arn
    events              = ["s3:ObjectCreated:*"]
#    filter_prefix       = "file_landing/"
#    filter_suffix       = "file-extension"
  }
}
# Provide permission to invoke lambda function when file is uploaded to S3 bucket
resource "aws_lambda_permission" "file_lambda_permission" {
  statement_id  = "AllowS3Invoke"
  action        = "lambda:InvokeFunction"
  function_name = "${aws_lambda_function.first_glue_job_trigger_glue_workflow.function_name}"
  principal = "s3.amazonaws.com"
  source_arn = "arn:aws:s3:::${aws_s3_bucket.landing_bucket.id}"
}
# Randomly generate a name for the lambda function
resource "random_string" "randomstring_fileingestion" {
  length  = 4
  special = false
}
# Archive/Zip the source code for Lambda
data "archive_file" "lambda_zip_dir" {
  type        = "zip"
  output_path = "/tmp/file_trigger_lambda-${random_string.randomstring_fileingestion.result}.zip"
  source_dir  = "src"
 
}
# Upload the Source code into S3 Bucket
resource "aws_s3_object" "lambda_code_upload" {
  key        = "lambda_scripts/first_glue_job_trigger_glue_workflow.zip"
  bucket     = aws_s3_bucket.landing_bucket.bucket
  source     = data.archive_file.lambda_zip_dir.output_path
  etag       = data.archive_file.lambda_zip_dir.output_base64sha256
}
# To Deploy Lambda Layers - Has been commented out for this version
# resource "aws_lambda_layer_version" "lambda_layer_wrangler" {
#   filename   = "${path.module}/../../../../build_tools/awswrangler-layer-2.17.0-py3.9.zip"
#   layer_name = "aws_wrangler"
#   compatible_runtimes = ["python3.9"]
# }

# Create Lambda Function
resource "aws_lambda_function" "first_glue_job_trigger_glue_workflow" {
  function_name = "first_glue_job_trigger_glue_workflow"
 
  s3_bucket = aws_s3_bucket.landing_bucket.bucket
  s3_key    = "lambda_scripts/first_glue_job_trigger_glue_workflow.zip" # S3 Key for the Lambda Function
  source_code_hash = "${data.archive_file.lambda_zip_dir.output_base64sha256}" # Archived source code hash
 
  runtime = "python3.9" # Choose from python3.6, python3.7, python3.8, python3.9
  handler = "first_glue_job_trigger_glue_workflow.lambda_handler" # This is the function that will be executed when the lambda is triggered
  timeout = 900 # 15 minutes is the maximum time allowed for the lambda function to run
  role = aws_iam_role.terraform_lambda_function_role.arn
  memory_size = 512
  # vpc_config {
  #   subnet_ids         = var.subnet_id
  #   security_group_ids = var.lambda_sg
  # }
  # layers = [aws_lambda_layer_version.lambda_layer_wrangler.arn]
  ephemeral_storage {
    size = 2048 # Min 512 MB and the Max 10240 MB
  }
}
# CloudWatch Log group to store Lambda logs
resource "aws_cloudwatch_log_group" "lambda_demo_loggroup" {
  name = "/aws/lambda/${aws_lambda_function.first_glue_job_trigger_glue_workflow.function_name}"
  retention_in_days = 365
}
##################
# Creating IAM Role for Lambda
##################
# IAM Policy Document for Lambda - Allows Trust Policy for Lambda
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
# IAM Policy Document for Lambda - Allows Writing to Logs and Read/Write from File that Triggers the Lambda

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

    resources = [
      aws_s3_bucket.landing_bucket.arn,
      "${aws_s3_bucket.landing_bucket.arn}/*"
    ]
  }
  statement {
    effect = "Allow"
    actions = [
    "logs:CreateLogGroup",
    "logs:CreateLogStream",
    "logs:PutLogEvents"
    ]

    resources = [
      aws_cloudwatch_log_group.lambda_demo_loggroup.arn
    ]
  }

}
# Create IAM Role for Lambda
resource "aws_iam_role" "terraform_lambda_function_role" {
  name               = "terraform_lambda_function_role"
  assume_role_policy = "${data.aws_iam_policy_document.AWSLambdaTrustPolicy.json}"
  # managed_policy_arns = [aws_iam_policy.lambda_policy.arn]
}
# Create IAM Policy for Lambda
resource "aws_iam_policy" "lambda_policy" {
  name        = "lambda_policy"
  description = "Policy to access S3"

  policy = "${data.aws_iam_policy_document.AWSLambdaPolicy.json}" # Attaching the Trust policy to the role

}

 # Attach Policy to Lambda IAM Role
resource "aws_iam_role_policy_attachment" "terraform_lambda_policy" {
  role       = "${aws_iam_role.terraform_lambda_function_role.name}"
  policy_arn = aws_iam_policy.lambda_policy.arn # Attaching the policy with access to Logs and S3 to the role
}

################
# Glue Workflow is created and the triggers are added to invoke the Glue jobs and Glue Crawlers
################
# Create Glue Workflow
resource "aws_glue_workflow" "sample_glue_workflow" {
  name = "sample_glue_workflow"
}
# Create a Glue trigger to invoke the first Glue job and add the trigger to the Glue Workflow
resource "aws_glue_trigger" "sample_glue_workflow-start" {
  name          = "sample_glue_workflow-start"
  type          = "ON_DEMAND"
  workflow_name = aws_glue_workflow.sample_glue_workflow.name
 
  actions {
    job_name = "first_glue_job"
    arguments = {"--run_type"="NORMAL","--process_name"="sample_glue_workflow","--config_path"="first_glue_job_conf_DEV.json","--database_name"="test_db"}
  }
}
 
# Create a Glue trigger to invoke the first Glue Crawler and add the trigger to the Glue Workflow
 
resource "aws_glue_trigger" "sample_glue_workflow-first_crawler" {
  name          = "sample_glue_workflow-start_first_crawler"
  type          = "CONDITIONAL"
  workflow_name = aws_glue_workflow.sample_glue_workflow.name # Workflow name created above
 
  predicate {
    conditions {
      job_name = "first_glue_job"
      state    = "SUCCEEDED"
      logical_operator = "EQUALS"
    }
  }
 
  actions {
    crawler_name = "first_crawler"
  }
}
# Create a Glue trigger to invoke the second Glue Job and add the trigger to the Glue Workflow

resource "aws_glue_trigger" "sample_glue_workflow-second_glue_job" {
  name          = "sample_glue_workflow-start_second_glue_job"
  type          = "CONDITIONAL"
  workflow_name = aws_glue_workflow.sample_glue_workflow.name # Workflow name created above
 
  predicate {
    conditions {
      crawler_name = "first_crawler"
      crawl_state    = "SUCCEEDED"
      logical_operator = "EQUALS"
    }
  }
 
  actions {
    job_name = "second_glue_job"
    arguments = {"--run_type"="NORMAL","--process_name"="sample_glue_workflow","--config_path"="second_glue_job_conf_DEV.json","--database_name"="test_db"}
  }
}
# Create a Glue trigger to invoke the second Glue Crawler and add the trigger to the Glue Workflow

resource "aws_glue_trigger" "sample_glue_workflow-second_crawler" {
  name          = "sample_glue_workflow-start_second_crawler"
  type          = "CONDITIONAL"
  workflow_name = aws_glue_workflow.sample_glue_workflow.name
 
  predicate {
    conditions {
      job_name = "second_glue_job"
      state    = "SUCCEEDED"
      logical_operator = "EQUALS"
    }
  }
 
  actions {
    crawler_name = "second_crawler"
  }
}



# IAM policies to allow access to the S3 bucket
data "aws_iam_policy_document" "policy_document" {
  statement {
    effect = "Allow"
    actions = [
      "s3:ListBucket"
    ]
    resources = [
      aws_s3_bucket.landing_bucket.arn
    ]
  }
  statement {
    effect = "Allow"
    actions = [
      "s3:GetObject",
      "s3:PutObject"
    ]
    resources = [
      "${aws_s3_bucket.landing_bucket.arn}/*"
    ]
  }
}

resource "aws_iam_policy" "s3_access_iam_policy" {
  name = "sample-glue-s3-access-policy"
  policy = data.aws_iam_policy_document.policy_document.json
}

# Glue IAM roles and Policies
resource "aws_iam_role" "sample_glue_role" {
  name = "sample-glue-role"
  assume_role_policy = <<EOF
{
   "Version":"2012-10-17",
   "Statement":[
      {
         "Action":"sts:AssumeRole",
         "Principal":{
            "Service":[
               "glue.amazonaws.com"
            ]
         },
         "Effect":"Allow",
         "Sid":""
      }
   ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "glue_service_policy" {
  role = aws_iam_role.sample_glue_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole"
}

resource "aws_iam_role_policy_attachment" "platform_metrics_glue_iam_policy" {
  role       = aws_iam_role.sample_glue_role.name
  policy_arn = aws_iam_policy.s3_access_iam_policy.arn
}

##############
# Glue job
##############

# Upload the Glue script to S3 bucket
resource "aws_s3_object" "s3_copy_glue_script" {
  bucket = aws_s3_bucket.landing_bucket.bucket
  key    = "scripts/app.py"
  source = "src/app.py"
  source_hash = filemd5("src/app.py")
}
# Create Glue Job
resource "aws_glue_job" "first_glue_job" {
    name = "first_glue_job"
    role_arn = aws_iam_role.sample_glue_role.arn
    command {
     
      script_location = "s3://${aws_s3_bucket.landing_bucket.bucket}/scripts/app.py"
 
    }
    glue_version = "4.0"
    timeout = 600
    default_arguments = {
      "--enable-continuous-cloudwatch-log" = "true"
      "--enable-continuous-log-filter"     = "true"
      "--enable-metrics"                   = ""
      "--enable-spark-ui" = "true"
      "--enable-glue-datacatalog" = ""
      "--job-bookmark-option" = "job-bookmark-disable"
      "--extra-py-files" = ""
      "--extra-files" = ""
      "--extra-jars" = ""
    }
    # connections = [aws_glue_connection.sample-glue-connection.name]
    execution_property {
      max_concurrent_runs = 200
    }
   
    number_of_workers = 10
    worker_type = "G.1X"
    max_retries = 0
   
}

resource "aws_glue_job" "second_glue_job" {
    name = "second_glue_job"
    role_arn = aws_iam_role.sample_glue_role.arn
    command {
     
      script_location = "s3://${aws_s3_bucket.landing_bucket.bucket}/scripts/app.py"
 
    }
    glue_version = "4.0"
    timeout = 600
    default_arguments = {
      "--enable-continuous-cloudwatch-log" = "true"
      "--enable-continuous-log-filter"     = "true"
      "--enable-metrics"                   = ""
      "--enable-spark-ui" = "true"
      "--enable-glue-datacatalog" = ""
      "--job-bookmark-option" = "job-bookmark-disable"
      "--extra-py-files" = ""
      "--extra-files" = ""
      "--extra-jars" = ""
    }
    # connections = [aws_glue_connection.sample-glue-connection.name]
    execution_property {
      max_concurrent_runs = 200
    }
   
    number_of_workers = 10
    worker_type = "G.1X"
    max_retries = 0
   
}


resource "aws_glue_crawler" "first_crawler" {
  database_name = "test_db"
  name          = "first_crawler"
  role          = aws_iam_role.sample_glue_role.arn
 
  s3_target {
    path = "s3://${aws_s3_bucket.landing_bucket.bucket}/test_db/first/"
  }
}
 
resource "aws_glue_crawler" "second_crawler" {
  database_name = "test_db"
  name          = "second_crawler"
  role          = aws_iam_role.sample_glue_role.arn
 
  s3_target {
    path = "s3://${aws_s3_bucket.landing_bucket.bucket}/test_db/second/"
  }
}