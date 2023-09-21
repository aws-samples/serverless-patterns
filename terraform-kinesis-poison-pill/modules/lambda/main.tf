# This is required to get the AWS region via ${data.aws_region.current}.
data "aws_region" "current" {
}

data "archive_file" "lambda_code_in_zip_format" {
    type        = "zip"
    source_dir  = "${path.module}/bin"
    output_path = "${path.module}/src/kinesis-stream.zip"
}

// build the binary for the lambda function in a specified path
/*resource "null_resource" "function_binary" {
  provisioner "local-exec" {
    interpreter = ["/bin/bash", "-c"]
    command     = "cd ${path.module} && GOOS=linux go build -ldflags '-s -w' -o ${path.module} ${path.module}"
  }
}*/

# Define a Lambda function.
#
# The handler is the name of the executable for go1.x runtime.
resource "aws_lambda_function" "kinesis_stream_lambda" {
  depends_on = [ data.archive_file.lambda_code_in_zip_format ]
  function_name    = "error_handling_function"
  filename         = "${path.module}/src/kinesis-stream.zip"
  handler          = "kinesis_stream"
  role             = aws_iam_role.iam_role_for_lambda.arn
  runtime          = "go1.x"
  memory_size      = 128
  timeout          = 10
}

resource "null_resource" "delete_lambda_code" {

  provisioner "local-exec" {
    when       = destroy
    command    = "rm -r ${path.module}/bin ${path.module}/src"
    on_failure = continue
  }
}

# A Lambda function may access to other AWS resources such as S3 bucket. So an
# IAM role needs to be defined. This hello world example does not access to
# any resource, so the role is empty.
#
# The date 2012-10-17 is just the version of the policy language used here [1].
#
# [1]: https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_version.html


resource "aws_iam_role" "iam_role_for_lambda" {
    name               = "kinesis_iam_role_for_lambda"
    assume_role_policy = file("${path.module}/iam_role_for_lambda.json")
}

# IAM Policy for Lambda
resource "aws_iam_policy" "iam_policy_for_lambda" {
    name   = "iam_policy_for_lambda"
    policy = templatefile("${path.module}/iam_policy_for_lambda.tftpl", {kinesis_strem_lambda_arn = aws_lambda_function.kinesis_stream_lambda.arn})
}

# Attach IAM Role with IAM Policy for Lambda
resource "aws_iam_role_policy_attachment" "attach_iam_role_with_iam_policy" {
    policy_arn = aws_iam_policy.iam_policy_for_lambda.arn
    role       = aws_iam_role.iam_role_for_lambda.name
}

# Permission for Lambda
resource "aws_lambda_permission" "permission_for_lambda" {
    action        = "lambda:InvokeFunction"
    function_name = aws_lambda_function.kinesis_stream_lambda.function_name
    principal     = "kinesisanalytics.amazonaws.com"
    source_arn    = var.kinesis_stream_arn    
}

resource "aws_lambda_event_source_mapping" "kinesis_lambda_event_mapping" {
    batch_size = 10
    event_source_arn = var.kinesis_stream_arn
    enabled = true
    function_name = "${aws_lambda_function.kinesis_stream_lambda.arn}"
    starting_position = "TRIM_HORIZON"
    bisect_batch_on_function_error = true
    maximum_retry_attempts = 5
    destination_config {
    on_failure {
      destination_arn = var.sqs_arn
    }
   
  }
}