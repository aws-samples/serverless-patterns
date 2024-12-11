terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  required_version = ">= 0.14.9"
}

# Fetching current Account ID and AWS region
data "aws_caller_identity" "current" {}
data "aws_region" "current" {}

#################################################################
# API Gateway REST
#################################################################
# Creating the API Gateway
resource "aws_api_gateway_rest_api" "API_SF_CRUD-tf_API" {
  name        = "API_SF_CRUD-tf_API"
}

# Creating a CloudWatch Log Group for API Gateway access logs
resource "aws_cloudwatch_log_group" "API_SF_CRUD-tf_APILogGroup" {
  name = "/aws/vendedlogs/api/API_SF_CRUD-tf_APILogGroup"
}

# Creating necessary IAM roles and policies for API Gateway
resource "aws_iam_role" "API_SF_CRUD-tf_APIRole" {
  name = "API_SF_CRUD-tf_APIRole"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "apigateway.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_role_policy" "API_SF_CRUD-tf_APIPolicy" {
  name = "API_SF_CRUD-tf_APIPolicy"
  role = aws_iam_role.API_SF_CRUD-tf_APIRole.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "states:StartExecution"
        ]
        Resource = "${aws_sfn_state_machine.API_SF_CRUD-tf_CF.arn}"
      },
      {
        Effect = "Allow"
        Action = [
          "states:StartSyncExecution"
        ]
        Resource = "${aws_sfn_state_machine.API_SF_CRUD-tf_CF.arn}"
      },
    ]
  })
}

resource "aws_iam_role_policy_attachment" "API_SF_CRUD-tf_APIPolicyAttachment1" {
  role       = aws_iam_role.API_SF_CRUD-tf_APIRole.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonAPIGatewayPushToCloudWatchLogs"
  depends_on = [ aws_iam_role.API_SF_CRUD-tf_APIRole ]
}

resource "aws_iam_role_policy_attachment" "API_SF_CRUD-tf_APIPolicyAttachment2" {
  role       = aws_iam_role.API_SF_CRUD-tf_APIRole.name
  policy_arn = "arn:aws:iam::aws:policy/AWSXrayWriteOnlyAccess"
  depends_on = [ aws_iam_role.API_SF_CRUD-tf_APIRole ]
}

# Root resource is build-in, but child (/{id}) resource is needed
resource "aws_api_gateway_resource" "API_SF_CRUD-tf_APIRes_Child" {
  parent_id   = aws_api_gateway_rest_api.API_SF_CRUD-tf_API.root_resource_id
  path_part   = "{id}"
  rest_api_id = aws_api_gateway_rest_api.API_SF_CRUD-tf_API.id
}

# Creating a ANY method for both resources
resource "aws_api_gateway_method" "API_SF_CRUD-tf_API_method" {
  resource_id   = aws_api_gateway_rest_api.API_SF_CRUD-tf_API.root_resource_id
  rest_api_id   = aws_api_gateway_rest_api.API_SF_CRUD-tf_API.id
  http_method   = "ANY"
  authorization = "NONE"
  depends_on = [aws_api_gateway_rest_api.API_SF_CRUD-tf_API]
}

resource "aws_api_gateway_method" "API_SF_CRUD-tf_API_method_child" {
  resource_id   = aws_api_gateway_resource.API_SF_CRUD-tf_APIRes_Child.id
  rest_api_id   = aws_api_gateway_rest_api.API_SF_CRUD-tf_API.id
  http_method   = "ANY"
  authorization = "NONE"
  request_parameters = {
    "method.request.path.id" = true
  }
  depends_on = [aws_api_gateway_resource.API_SF_CRUD-tf_APIRes_Child]
}

# Creating API Gateway behaviour for root / resource ANY method
resource "aws_api_gateway_integration" "API_SF_CRUD-tf_APIInt" {
  rest_api_id             = aws_api_gateway_rest_api.API_SF_CRUD-tf_API.id
  resource_id             = aws_api_gateway_rest_api.API_SF_CRUD-tf_API.root_resource_id
  http_method             = aws_api_gateway_method.API_SF_CRUD-tf_API_method.http_method
  integration_http_method = "POST"
  type                    = "AWS"
  uri                     = "arn:aws:apigateway:${data.aws_region.current.name}:states:action/StartExecution"
  credentials             = aws_iam_role.API_SF_CRUD-tf_APIRole.arn
  passthrough_behavior    = "NEVER"
  request_templates = {
    "application/json" = <<EOF
#set($body= $input.json('$'))#set($inputRoot='{"data" :'+$body+',"httpMethod" :"'+$context.httpMethod+'"}')#set($apiData=$util.escapeJavaScript($inputRoot))#set($apiData=$apiData.replaceAll("\\'","'")){"input" :"$apiData","stateMachineArn": "arn:aws:states:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:stateMachine:${aws_sfn_state_machine.API_SF_CRUD-tf_CF.name}"}
    EOF
  }
}

resource "aws_api_gateway_integration_response" "API_SF_CRUD-tf_APIIntRes200" {
  rest_api_id             = aws_api_gateway_rest_api.API_SF_CRUD-tf_API.id
  resource_id             = aws_api_gateway_rest_api.API_SF_CRUD-tf_API.root_resource_id
  http_method             = aws_api_gateway_method.API_SF_CRUD-tf_API_method.http_method
  status_code             = "200"
  selection_pattern       = "200"
  response_templates    = {
    "application/json" = <<EOF
#set($inputRoot = $input.path('$')) $inputRoot.output
    EOF
  }
  depends_on              = [ aws_api_gateway_rest_api.API_SF_CRUD-tf_API, aws_api_gateway_integration.API_SF_CRUD-tf_APIInt, aws_api_gateway_method.API_SF_CRUD-tf_API_method, aws_api_gateway_method.API_SF_CRUD-tf_API_method_child ]
}

resource "aws_api_gateway_integration_response" "API_SF_CRUD-tf_APIIntRes400" {
  rest_api_id             = aws_api_gateway_rest_api.API_SF_CRUD-tf_API.id
  resource_id             = aws_api_gateway_rest_api.API_SF_CRUD-tf_API.root_resource_id
  http_method             = aws_api_gateway_method.API_SF_CRUD-tf_API_method.http_method
  status_code             = "400"
  selection_pattern       = "400"
  depends_on              = [ aws_api_gateway_rest_api.API_SF_CRUD-tf_API, aws_api_gateway_integration.API_SF_CRUD-tf_APIInt, aws_api_gateway_method.API_SF_CRUD-tf_API_method, aws_api_gateway_method.API_SF_CRUD-tf_API_method_child ]
}

resource "aws_api_gateway_method_response" "API_SF_CRUD-tf_APIMethRes200" {
  rest_api_id             = aws_api_gateway_rest_api.API_SF_CRUD-tf_API.id
  resource_id             = aws_api_gateway_rest_api.API_SF_CRUD-tf_API.root_resource_id
  http_method             = aws_api_gateway_method.API_SF_CRUD-tf_API_method.http_method
  status_code             = "200"
  depends_on              = [ aws_api_gateway_rest_api.API_SF_CRUD-tf_API, aws_api_gateway_method.API_SF_CRUD-tf_API_method, aws_api_gateway_integration_response.API_SF_CRUD-tf_APIIntRes200, aws_api_gateway_integration_response.API_SF_CRUD-tf_APIIntRes400 ]
}

resource "aws_api_gateway_method_response" "API_SF_CRUD-tf_APIMethRes400" {
  rest_api_id             = aws_api_gateway_rest_api.API_SF_CRUD-tf_API.id
  resource_id             = aws_api_gateway_rest_api.API_SF_CRUD-tf_API.root_resource_id
  http_method             = aws_api_gateway_method.API_SF_CRUD-tf_API_method.http_method
  status_code             = "400"
  depends_on              = [ aws_api_gateway_rest_api.API_SF_CRUD-tf_API, aws_api_gateway_method.API_SF_CRUD-tf_API_method, aws_api_gateway_integration_response.API_SF_CRUD-tf_APIIntRes200, aws_api_gateway_integration_response.API_SF_CRUD-tf_APIIntRes400 ]
}

# Creating API Gateway behaviour for child /{id} resource ANY method
resource "aws_api_gateway_integration" "API_SF_CRUD-tf_APIIntChild" {
  rest_api_id             = aws_api_gateway_rest_api.API_SF_CRUD-tf_API.id
  resource_id             = aws_api_gateway_resource.API_SF_CRUD-tf_APIRes_Child.id
  http_method             = aws_api_gateway_method.API_SF_CRUD-tf_API_method_child.http_method
  integration_http_method = "POST"
  type                    = "AWS"
  uri                     = "arn:aws:apigateway:${data.aws_region.current.name}:states:action/StartExecution"
  credentials             = aws_iam_role.API_SF_CRUD-tf_APIRole.arn
  passthrough_behavior    = "NEVER"
  request_templates = {
    "application/json" = <<EOF
#set($body= $input.json('$'))#set($inputRoot='{"data" :'+$body+',"httpMethod" :"'+$context.httpMethod+'"}')#set($apiData=$util.escapeJavaScript($inputRoot))#set($apiData=$apiData.replaceAll("\\'","'")){"input" :"$apiData","stateMachineArn": "arn:aws:states:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:stateMachine:${aws_sfn_state_machine.API_SF_CRUD-tf_CF.name}"}
    EOF
  }
}

resource "aws_api_gateway_integration_response" "API_SF_CRUD-tf_APIIntChildRes200" {
  rest_api_id             = aws_api_gateway_rest_api.API_SF_CRUD-tf_API.id
  resource_id             = aws_api_gateway_resource.API_SF_CRUD-tf_APIRes_Child.id
  http_method             = aws_api_gateway_method.API_SF_CRUD-tf_API_method_child.http_method
  status_code             = "200"
  selection_pattern       = "200"
  response_templates      = {
    "application/json"    = <<EOF
#set($inputRoot = $input.path('$')) $inputRoot.output
    EOF
  }
  depends_on              = [ aws_api_gateway_rest_api.API_SF_CRUD-tf_API, aws_api_gateway_integration.API_SF_CRUD-tf_APIIntChild, aws_api_gateway_resource.API_SF_CRUD-tf_APIRes_Child, aws_api_gateway_method.API_SF_CRUD-tf_API_method_child ]
}

resource "aws_api_gateway_integration_response" "API_SF_CRUD-tf_APIIntChildRes400" {
  rest_api_id             = aws_api_gateway_rest_api.API_SF_CRUD-tf_API.id
  resource_id             = aws_api_gateway_resource.API_SF_CRUD-tf_APIRes_Child.id
  http_method             = aws_api_gateway_method.API_SF_CRUD-tf_API_method_child.http_method
  status_code             = "400"
  selection_pattern       = "400"
  depends_on              = [ aws_api_gateway_rest_api.API_SF_CRUD-tf_API, aws_api_gateway_integration.API_SF_CRUD-tf_APIIntChild, aws_api_gateway_resource.API_SF_CRUD-tf_APIRes_Child, aws_api_gateway_method.API_SF_CRUD-tf_API_method_child ]
}

resource "aws_api_gateway_method_response" "API_SF_CRUD-tf_APIMethChildRes200" {
  rest_api_id             = aws_api_gateway_rest_api.API_SF_CRUD-tf_API.id
  resource_id             = aws_api_gateway_resource.API_SF_CRUD-tf_APIRes_Child.id
  http_method             = aws_api_gateway_method.API_SF_CRUD-tf_API_method_child.http_method
  status_code             = "200"
}

resource "aws_api_gateway_method_response" "API_SF_CRUD-tf_APIMethChildRes400" {
  rest_api_id             = aws_api_gateway_rest_api.API_SF_CRUD-tf_API.id
  resource_id             = aws_api_gateway_resource.API_SF_CRUD-tf_APIRes_Child.id
  http_method             = aws_api_gateway_method.API_SF_CRUD-tf_API_method_child.http_method
  status_code             = "400"
}

# Creating "Prod" and "Stage" deployment stages
resource "aws_api_gateway_stage" "API_SF_CRUD-tf_API_Stage_Prod" {
  deployment_id = aws_api_gateway_deployment.API_SF_CRUD-tf_API_deployment_Prod.id
  rest_api_id   = aws_api_gateway_rest_api.API_SF_CRUD-tf_API.id
  stage_name    = "Prod"
  
  access_log_settings {
    destination_arn = aws_cloudwatch_log_group.API_SF_CRUD-tf_APILogGroup.arn
    format          = jsonencode({
      requestId                      = "$context.requestId",
      waf_error                      = "$context.waf.error",
      waf_status                     = "$context.waf.status",
      waf_latency                    = "$context.waf.latency",
      waf_response                   = "$context.wafResponseCode",
      authenticate_error             = "$context.authenticate.error",
      authenticate_status            = "$context.authenticate.status",
      authenticate_latency           = "$context.authenticate.latency",
      authorize_error                = "$context.authorize.error",
      authorize_status               = "$context.authorize.status",
      authorize_latency              = "$context.authorize.latency",
      integration_error              = "$context.integration.error",
      integration_status             = "$context.integration.status",
      integration_latency            = "$context.integration.latency",
      integration_requestId          = "$context.integration.requestId",
      integration_integrationStatus  = "$context.integration.integrationStatus",
      response_latency               = "$context.responseLatency",
      status                         = "$context.status"
    })
  }
}

resource "aws_api_gateway_stage" "API_SF_CRUD-tf_API_Stage_Stage" {
  deployment_id = aws_api_gateway_deployment.API_SF_CRUD-tf_API_deployment_Prod.id
  rest_api_id   = aws_api_gateway_rest_api.API_SF_CRUD-tf_API.id
  stage_name    = "Stage"
}

# Deploying the API
resource "aws_api_gateway_deployment" "API_SF_CRUD-tf_API_deployment_Prod" {
  depends_on = [aws_api_gateway_integration.API_SF_CRUD-tf_APIInt]
  rest_api_id = aws_api_gateway_rest_api.API_SF_CRUD-tf_API.id
}

#################################################################
# DynamoDB Table
#################################################################
# Creating the DynamoDB Table
resource "aws_dynamodb_table" "API_SF_CRUD-DB" {
  name         = "API_SF_CRUD-DB"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "Id"

  attribute {
    name = "Id"
    type = "S"
  }

  tags = {
    Name = "API_SF_CRUD-DB"
  }
}

#################################################################
# Step Functions - State Machine
#################################################################
# Creating the state machine
resource "aws_sfn_state_machine" "API_SF_CRUD-tf_CF" {
  name     = "API_SF_CRUD-tf_CF"
  role_arn = aws_iam_role.API_SF_CRUD-tf_CFRole.arn
  definition = file("./crud-asl.json")
  type     = "EXPRESS"

  logging_configuration {
    log_destination        = "${aws_cloudwatch_log_group.API_SF_CRUD-tf_CFLogGroup.arn}:*"
    include_execution_data = true
    level                  = "ALL"
  }

  tracing_configuration {
    enabled = true
  }

  tags = {
    Name = "API_SF_CRUD-tf_CF"
  }
  
}

# Creating a CloudWatch Log Group for Step Functions logs
resource "aws_cloudwatch_log_group" "API_SF_CRUD-tf_CFLogGroup" {
  name = "/aws/vendedlogs/states/API_SF_CRUD-tf_CFLogGroup"
}

# Creating necessary IAM roles and policies for the Step Functions
resource "aws_iam_role" "API_SF_CRUD-tf_CFRole" {
  name = "API_SF_CRUD-tf_StateMachineRole"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "states.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })

  inline_policy {
    name = "StateMachineRolePolicyDynamoDB"
    policy = jsonencode({
      "Version": "2012-10-17",
      "Statement": [
        {
          "Action": [
            "dynamodb:GetItem",
            "dynamodb:DeleteItem",
            "dynamodb:PutItem",
            "dynamodb:Scan",
            "dynamodb:Query",
            "dynamodb:UpdateItem",
            "dynamodb:BatchWriteItem",
            "dynamodb:BatchGetItem",
            "dynamodb:DescribeTable",
            "dynamodb:ConditionCheckItem"
          ],
          "Resource": [
            "arn:aws:dynamodb:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:table/${aws_dynamodb_table.API_SF_CRUD-DB.name}",
            "arn:aws:dynamodb:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:table/${aws_dynamodb_table.API_SF_CRUD-DB.name}index/*"
          ],
          "Effect": "Allow"
        }
      ]
    })
  }

  inline_policy {
    name = "StateMachineRolePolicyLogs"
    policy = jsonencode({
      "Version": "2012-10-17",
      "Statement": [
        {
          "Action": [
            "logs:CreateLogDelivery",
            "logs:GetLogDelivery",
            "logs:UpdateLogDelivery",
            "logs:DeleteLogDelivery",
            "logs:ListLogDeliveries",
            "logs:PutResourcePolicy",
            "logs:DescribeResourcePolicies",
            "logs:DescribeLogGroups"
          ],
          "Resource": "*",
          "Effect": "Allow"
        }
      ]
    })
  }
  
  depends_on = [aws_dynamodb_table.API_SF_CRUD-DB]
}

resource "aws_iam_role_policy_attachment" "API_SF_CRUD-tf_StateMachineRolePolicyAttachment" {
  role       = aws_iam_role.API_SF_CRUD-tf_CFRole.name
  policy_arn = "arn:aws:iam::aws:policy/AWSXrayWriteOnlyAccess"
}

#################################################################
# Outputs
#################################################################
# Displaying the values
output "api_endpoint_Prod" {
  description = "API Gateway endpoint URL for Prod stage"
  value       = "${aws_api_gateway_deployment.API_SF_CRUD-tf_API_deployment_Prod.invoke_url}${aws_api_gateway_stage.API_SF_CRUD-tf_API_Stage_Prod.stage_name}"
}
output "api_endpoint_Stage" {
  description = "API Gateway endpoint URL for Stage stage"
  value       = "${aws_api_gateway_deployment.API_SF_CRUD-tf_API_deployment_Prod.invoke_url}${aws_api_gateway_stage.API_SF_CRUD-tf_API_Stage_Stage.stage_name}"
}
