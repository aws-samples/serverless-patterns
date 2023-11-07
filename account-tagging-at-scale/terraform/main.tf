## Lambda Layer install dependencies

resource "null_resource" "install_dependencies" {
  provisioner "local-exec" {
    command = "pip install -r ${var.layers_root}/requirements.txt -t ${var.layers_root}/python"
  }

  triggers = {
    dependencies_versions = filemd5("${var.layers_root}/requirements.txt")
    source_versions       = filemd5("${var.lambda_root}/apply_account_level_tags.py")
  }
}

## Lambda Source Code

resource "random_uuid" "lambda_src_hash" {
  keepers = {
    for filename in setunion(
      fileset(var.lambda_root, "apply_account_level_tags.py")
    ) :
    filename => filemd5("${var.lambda_root}/${filename}")
  }
}

data "archive_file" "lambda_source" {
  depends_on = [null_resource.install_dependencies]
  excludes = [
    "__pycache__",
    "venv",
  ]

  source_dir  = var.lambda_root
  output_path = "${random_uuid.lambda_src_hash.result}.zip"
  type        = "zip"
}


resource "random_uuid" "layers_src_hash" {
  keepers = {
    for filename in setunion(
      fileset(var.layers_root, "requirements.txt")
    ) :
    filename => filemd5("${var.layers_root}/${filename}")
  }
}


data "archive_file" "layer_source" {
  type        = "zip"
  source_dir  = var.layers_root
  output_path = "${random_uuid.layers_src_hash.result}.zip"
  depends_on  = [null_resource.install_dependencies]
}

resource "aws_lambda_layer_version" "layer" {
  layer_name          = "apply-tags-current-accounts-layer"
  filename            = data.archive_file.layer_source.output_path
  source_code_hash    = data.archive_file.layer_source.output_base64sha256
  compatible_runtimes = ["python3.11", "python3.10", "python3.9", "python3.8", "python3.7", "python3.6"]
}

resource "aws_sqs_queue" "lambdadlq" {
  name                       = "sampledlq"
  delay_seconds              = 300
  max_message_size           = 2048
  message_retention_seconds  = 1209600
  visibility_timeout_seconds = 310
  receive_wait_time_seconds  = 20
  sqs_managed_sse_enabled    = true
  tags                       = var.default_tags
}

resource "aws_lambda_function" "lambda" {
  function_name           = "apply-tags-current-accounts"
  timeout                 = 900
  role                    = aws_iam_role.iam_role.arn
  filename                = data.archive_file.lambda_source.output_path
  source_code_hash        = data.archive_file.lambda_source.output_base64sha256
  layers                  = [aws_lambda_layer_version.layer.arn]
  handler                 = "apply_account_level_tags.lambda_handler"
  runtime                 = "python3.11"
  code_signing_config_arn = aws_lambda_code_signing_config.this.arn
  vpc_config {
    subnet_ids         = [var.private1_subnet_id, var.private2_subnet_id]
    security_group_ids = [var.private_sg_id]
  }
  kms_key_arn = aws_kms_key.aft_kms_key.arn
  dead_letter_config {
    target_arn = aws_sqs_queue.aftlambdadlq.arn
  }
  environment {
    variables = {
      REGION              = "us-west-2",
      CROSS_ACC_ROLE_NAME = "AFTCrossAccountRole",
      AFT_CT_ACCOUNT      = "XXXXXXXXXXXXX"
    }
  }
  tracing_config {
    mode = "Active"
  }
  reserved_concurrent_executions = 1
  tags                           = var.default_tags
}


resource "aws_cloudwatch_log_group" "aft_suspend_account_lambda_log" {
  name              = "/aws/lambda/${aws_lambda_function.lambda.function_name}"
  retention_in_days = var.cloudwatch_log_group_retention
  tags              = var.default_tags
  kms_key_id        = aws_kms_key.aft_kms_key.arn
}