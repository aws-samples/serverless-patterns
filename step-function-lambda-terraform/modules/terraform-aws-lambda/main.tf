locals{
  lambda_zip_location = "./outputs/example-lambda-package.zip"
  source_file_name= "./resources/lambda.py"
  handler_name = "lambda.lambda_handler"
}

# AWS Lambda IAM roles and Policies
resource "aws_iam_role" "example_lambda_role" {
  name = "aws-lambda-role-example"
  assume_role_policy = <<EOF
{
   "Version":"2012-10-17",
   "Statement":[
      {
         "Action":"sts:AssumeRole",
         "Principal":{
            "Service":[
                "lambda.amazonaws.com"
            ]
         },
         "Effect":"Allow",
         "Sid":""
      }
   ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "lambda_service" {
  role = aws_iam_role.example_lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"

}

# AWS Lambda resources
data "archive_file" "archive-file-example" {
  type        = "zip"
  source_file = local.source_file_name
  output_path = local.lambda_zip_location
}

resource "aws_lambda_function" "aws_lambda_example" {
  filename      = local.lambda_zip_location
  function_name = "aws_lambda_example"
  role          = aws_iam_role.example_lambda_role.arn
  handler       = local.handler_name

  runtime = "python3.7"

  environment {
    variables = {
      application_name = "aws_lambda_example"
      env = "dev"
    }
  }
}

# outputs
output "lambda_role_arn" {
  value = aws_lambda_function.aws_lambda_example.arn
}

output "lambda_function_name" {
  value = aws_lambda_function.aws_lambda_example.function_name
}
