resource "aws_lambda_layer_version" "boto3_bedrock_layer" {
  filename            = "${path.module}/lambda-layer/boto3-bedrock-layer.zip"
  layer_name          = "boto3-bedrock-layer"
  compatible_runtimes = ["python3.14"]
}

resource "aws_lambda_function" "content_generation" {
  filename         = "${path.module}/lambda_function.zip"
  function_name    = "ContentGenerationFunction"
  role             = aws_iam_role.lambda_role.arn
  handler          = "bedrock_integration.lambda_handler"
  runtime          = "python3.14"
  architectures    = ["arm64"]
  
  layers           = [aws_lambda_layer_version.boto3_bedrock_layer.arn]
  
  memory_size      = 256
  timeout          = 30

  environment {
    variables = {
      LOG_LEVEL = "INFO"
    }
  }
}


resource "aws_lambda_permission" "api_gateway" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.content_generation.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_api_gateway_rest_api.generate_content_api.execution_arn}/*/*"
}
