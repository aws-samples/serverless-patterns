resource "aws_lambda_function" "lambda_function" {
  function_name = var.function_name
  role          = aws_iam_role.lambda_role.arn
  handler       = "app.lambda_handler"
  runtime       = var.runtime
  filename      = var.filename
  source_code_hash = data.archive_file.python_lambda_package.output_base64sha256
  timeout = 300
  environment {
    variables = {
      SAGEMAKER_ROLE = aws_iam_role.sagemaker_role.arn
      VPC_ID = var.vpc_id
      SUBNETS = join(", ", data.aws_subnets.example.ids)
      STATEMACHINE_ARN = aws_sfn_state_machine.manage_sagemaker.arn
    }
  }
}

data "archive_file" "python_lambda_package" {  
  type = "zip"  
  source_file = "${path.module}/../src/app.py" 
  output_path = var.filename
}

variable "function_name" {
  default = "create_sagemaker_domain"
}
variable "runtime" {
  default = "python3.10"
}
variable "filename" {
    default = "artifacts/function.zip"
}