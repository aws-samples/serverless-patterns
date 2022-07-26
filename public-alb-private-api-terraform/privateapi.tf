
resource "aws_api_gateway_rest_api" "private_api" {
    name = "private_api"

    endpoint_configuration {
        types = ["PRIVATE"]
        vpc_endpoint_ids = [aws_vpc_endpoint.execute_api.id]
    }
    provider = aws.crossaccount
}


resource "aws_api_gateway_method" "get" {
    authorization = "NONE"
    http_method   = "GET"
    resource_id   = aws_api_gateway_rest_api.private_api.root_resource_id
    rest_api_id   = aws_api_gateway_rest_api.private_api.id
    provider = aws.crossaccount
}

resource "aws_api_gateway_integration" "lambda_proxy" {
    rest_api_id             = aws_api_gateway_rest_api.private_api.id
    resource_id             = aws_api_gateway_rest_api.private_api.root_resource_id
    http_method             = aws_api_gateway_method.get.http_method
    integration_http_method = "POST"
    type                    = "AWS_PROXY"
    uri                     = aws_lambda_function.lambda.invoke_arn
    provider = aws.crossaccount
}

resource "aws_api_gateway_deployment" "deploy" {
    rest_api_id = aws_api_gateway_rest_api.private_api.id

  triggers = {
    # NOTE: The configuration below will satisfy ordering considerations,
    #       but not pick up all future REST API changes. More advanced patterns
    #       are possible, such as using the filesha1() function against the
    #       Terraform configuration file(s) or removing the .id references to
    #       calculate a hash against whole resources. Be aware that using whole
    #       resources will show a difference after the initial implementation.
    #       It will stabilize to only change when resources change afterwards.
    redeployment = sha1(jsonencode([
        aws_api_gateway_rest_api.private_api.root_resource_id,
        aws_api_gateway_method.get.id,
        aws_api_gateway_integration.lambda_proxy.id,
    ]))
  }

  lifecycle {
        create_before_destroy = true
  }
  provider = aws.crossaccount
}

resource "aws_api_gateway_stage" "dev" {
    deployment_id = aws_api_gateway_deployment.deploy.id
    rest_api_id   = aws_api_gateway_rest_api.private_api.id
    stage_name    = "dev"
    provider = aws.crossaccount
}

#output "invoke_url" {
#    value = "${aws_api_gateway_deployment.deploy.invoke_url}${aws_api_gateway_stage.dev.stage_name}"
#}

resource "aws_api_gateway_rest_api_policy" "policy" {
    rest_api_id   = aws_api_gateway_rest_api.private_api.id

  policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Deny",
            "Principal": "*",
            "Action": "execute-api:Invoke",
            "Resource": "${aws_api_gateway_rest_api.private_api.execution_arn}*",
            "Condition": {
                "StringNotEquals": {
                    "aws:sourceVpce": "${aws_vpc_endpoint.execute_api.id}"
                }
            }
        },
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "execute-api:Invoke",
            "Resource": "${aws_api_gateway_rest_api.private_api.execution_arn}*"
        }
    ]
}
EOF
    provider = aws.crossaccount
}