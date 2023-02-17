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
    lambda_function_arn = aws_lambda_function.first_glue_job_trigger_glue_workflow.arn
    events              = ["s3:ObjectCreated:*"]
#    filter_prefix       = "file_landing/"
#    filter_suffix       = "file-extension"
  }
}
resource "aws_lambda_permission" "file_lambda_permission" {
  statement_id  = "AllowS3Invoke"
  action        = "lambda:InvokeFunction"
  function_name = "${aws_lambda_function.first_glue_job_trigger_glue_workflow.function_name}"
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
resource "aws_lambda_function" "first_glue_job_trigger_glue_workflow" {
  function_name = "first_glue_job_trigger_glue_workflow"
 
  s3_bucket = aws_s3_bucket.landing_bucket.bucket
  s3_key    = "lambda_scripts/first_glue_job_trigger_glue_workflow.zip"
  source_code_hash = "${data.archive_file.lambda_zip_dir.output_base64sha256}"
 
  runtime = "python3.9"
  handler = "first_glue_job_trigger_glue_workflow.lambda_handler"
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
  key        = "lambda_scripts/first_glue_job_trigger_glue_workflow.zip"
  bucket     = aws_s3_bucket.landing_bucket.bucket
  source     = data.archive_file.lambda_zip_dir.output_path
  etag       = data.archive_file.lambda_zip_dir.output_base64sha256
}
data "archive_file" "lambda_zip_dir" {
  type        = "zip"
  output_path = "/tmp/file_trigger_lambda-${random_string.randomstring_fileingestion.result}.zip"
  source_dir  = "src"
 
}

#### sample glue workflow
resource "aws_glue_workflow" "sample_glue_workflow" {
  name = "sample_glue_workflow"
}
resource "aws_glue_trigger" "sample_glue_workflow-start" {
  name          = "sample_glue_workflow-start"
  type          = "ON_DEMAND"
  workflow_name = aws_glue_workflow.sample_glue_workflow.name
 
  actions {
    job_name = "first_glue_job"
    arguments = {"--run_type"="NORMAL","--process_name"="sample_glue_workflow","--config_path"="first_glue_job_conf_DEV.json","--database_name"="test_db"}
  }
}
 
 
resource "aws_glue_trigger" "sample_glue_workflow-first_crawler" {
  name          = "sample_glue_workflow-start_first_crawler"
  type          = "CONDITIONAL"
  workflow_name = aws_glue_workflow.sample_glue_workflow.name
 
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

resource "aws_glue_trigger" "sample_glue_workflow-second_glue_job" {
  name          = "sample_glue_workflow-start_second_glue_job"
  type          = "CONDITIONAL"
  workflow_name = aws_glue_workflow.sample_glue_workflow.name
 
  predicate {
    conditions {
      job_name = "first_crawler"
      state    = "SUCCEEDED"
      logical_operator = "EQUALS"
    }
  }
 
  actions {
    job_name = "second_glue_job"
    arguments = {"--run_type"="NORMAL","--process_name"="sample_glue_workflow","--config_path"="second_glue_job_conf_DEV.json","--database_name"="test_db"}
  }
}

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
# CloudWatch Log group to store Lambda logs
resource "aws_cloudwatch_log_group" "lambda_demo_loggroup" {
  name = "/aws/lambda/${aws_lambda_function.first_glue_job_trigger_glue_workflow.function_name}"
  retention_in_days = 365
}


# IAM policies to allow access to the S3 bucket
data "aws_iam_policy_document" "policy_document" {
  statement {
    effect = "Allow"
    actions = [
      "s3:ListBucket"
    ]
    resources = [
      var.s3_bucket_arn
    ]
  }
  statement {
    effect = "Allow"
    actions = [
      "s3:GetObject",
      "s3:PutObject"
    ]
    resources = [
      "${var.s3_bucket_arn}/*"
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

resource "aws_s3_object" "s3_copy_glue_script" {
  bucket = var.glue_script_bucket
  key    = "scripts/app.py"
  source = "src/app.py"
  source_hash = filemd5("src/app.py")
}

resource "aws_glue_job" "first_glue_job" {
    name = var.first_glue_job
    role_arn = var.sample_glue_role
    command {
     
      script_location = "s3://${var.glue_script_bucket}/scripts/app.py"
 
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
      "--extra-py-files" = "s3://${var.glue_script_bucket}/codebase/pyspark_etl_utilities/,s3://${var.glue_script_bucket}/codebase/database/src/"
      "--extra-files" = "s3://${var.glue_script_bucket}/GlueJars/hadooptrust.jks"
      "--extra-jars" = "s3://${var.glue_script_bucket}/GlueJars/db2jcc4-10.1.jar,s3://${var.glue_script_bucket}/GlueJars/jtds-1.3.1.jar,s3://${var.glue_script_bucket}/GlueJars/snowflake-jdbc-3.13.5.jar"
    }
    connections = [aws_glue_connection.sample-glue-connection.name]
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
  role          = var.sample_glue_role
 
  s3_target {
    path = "s3://${var.glue_script_bucket}/test_db/first/"
  }
}
 

 
resource "aws_s3_bucket" "s3_buckets" {
  count = length(var.bucket_names)
  bucket = var.bucket_names[count.index]
 
  tags = {
    Name        = var.bucket_names[count.index]
    Environment = var.env
  }
  versioning {
    enabled = "true"
  }
 
  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        kms_master_key_id = data.aws_kms_alias.s3_kms.arn
        sse_algorithm     = "aws:kms"
        #sse_algorithm = "AES256"
      }
    }
  }
}
 
 
// resource "aws_kms_key" "datalake_dev_kms_key" {
//   description             = "KMS Key for datalake dev"
//   deletion_window_in_days = 30
//   tags = {
//     Name         = "Datalake-dev-kms"
//   }
// }
 
// resource "aws_kms_alias" "datalake_dev_kms_key_alias" {
//   name          = "alias/Datalake-dev-kms"
//   target_key_id = aws_kms_key.datalake_dev_kms_key.key_id
// }
 
 
# resource "aws_s3_bucket" "datalake_bucket_landing" {
#   bucket = "hnb-dl-s3-landing-np"
 
#   tags = {
#     Name    = "DataLake bucket for np"
#   }
# }
 
# resource "aws_s3_bucket_versioning" "datalake_bucket_landing_versioning" { 
#   bucket = aws_s3_bucket.datalake_bucket_landing.bucket
#   versioning_configuration {
#     status = "Enabled"
#   }
# }
 
# resource "aws_s3_bucket_server_side_encryption_configuration" "s3_bucket_kms" {
#   bucket = aws_s3_bucket.datalake_bucket_landing.bucket
#   rule {
#     apply_server_side_encryption_by_default {
#       kms_master_key_id = data.aws_kms_alias.s3_kms.arn
#       sse_algorithm     = "aws:kms"
#     }
#   }
# }
 
// resource "aws_s3_bucket_public_access_block" "dl-landing-s3-public-policy" {
//   bucket = aws_s3_bucket.datalake_bucket_landing.bucket
 
//   block_public_acls   = true
//   block_public_policy = true
// }
 
 
# resource "aws_efs_mount_target" "mount" {
#   file_system_id = aws_efs_file_system.efs.id
#   //subnet_id      = module.single_instance.subnet_id
#   subnet_id      = "subnet-048a58756ed2dfcf9" #subnet_ids - Add it to mount all subnet ids.
#   //security_groups = ["sg-0917ac2279de65674", aws_security_group.security-group-dl-nfs.id]
#   security_groups = [module.dl-ssh-sg.security_group_id, module.dl-nfs-sg.security_group_id]
#   //security_groups = ["sg-0c601488dfd07c956","sg-0e2c5e4d1f9d9e0d6"]
# }
 
// resource "time_sleep" "waiting_300s" {
//   depends_on = [aws_efs_mount_target.mount, module.single_instance]
//   create_duration = "300s"
//   triggers = {
//     always_run = "${timestamp()}"
//     //id = module.single_instance.id
//   }
// }
 
// resource "null_resource" "configure_nfs" {
//   depends_on = [time_sleep.waiting_300s]
 
//   triggers = {
//     always_run = "${timestamp()}"
//     //id = module.single_instance.id
//   }
  
//   connection {
//     type     = "ssh"
//     user     = "ec2-user"
//     private_key = "${file("${var.key_name}.pem")}"
//     host     = module.single_instance.private_ip
//     timeout    = "6m"
//   }
 
//   provisioner "remote-exec" {
//     inline = [
//       "sudo yum install nfs-utils -y",
//       "sudo mkdir -p /opt/test-nfs",
//       "sudo mount -t nfs -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport ${aws_efs_file_system.efs.dns_name}:/ /opt/test-nfs",
//       "sudo sh -c \"echo '${aws_efs_file_system.efs.dns_name}:/ /opt/test-nfs nfs4 defaults,_netdev 0 0 sudo' >> /etc/fstab\"",
//       "sudo sh -c \"echo 'Testing EFS mount' > /opt/test-nfs/testNFS.txt\"",
//     ]
//   }
// }