terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }
  }

  required_version = ">= 0.14.9"
}

provider "aws" {
  profile = "default"
  region  = "us-east-1"
}

data "aws_caller_identity" "current" {}

data "aws_region" "current" {}

# Create an IAM role for API Gateway
resource "aws_iam_role" "APIGWRole" {
  assume_role_policy = <<POLICY1
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Principal" : {
        "Service" : "apigateway.amazonaws.com"
      },
      "Action" : "sts:AssumeRole"
    }
  ]
}
POLICY1
}

# Create an IAM policy for API Gateway to PutItem & Query DynamoDB
resource "aws_iam_policy" "APIGWPolicy" {
  policy = <<POLICY2
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "dynamodb:PutItem",
        "dynamodb:Query"
      ],
      "Resource" : [ "${aws_dynamodb_table.MyDynamoDBTable.arn}",
      "${aws_dynamodb_table.MyDynamoDBTable.arn}/index/*" ]
    }
  ]
}
POLICY2
}

# Attach the IAM policies to the equivalent rule
resource "aws_iam_role_policy_attachment" "APIGWPolicyAttachment" {
  role       = aws_iam_role.APIGWRole.name
  policy_arn = aws_iam_policy.APIGWPolicy.arn
}

# Create a new DynamoDB table with all attributes and Indexes
resource "aws_dynamodb_table" "MyDynamoDBTable" {
  name           = "Pets"
  billing_mode   = "PROVISIONED"
  read_capacity  = 5
  write_capacity = 5
  hash_key       = "id"

  attribute {
    name = "id"
    type = "S"
  }

  attribute {
    name = "PetType"
    type = "S"
  }

  global_secondary_index {
    name               = "PetType-index"
    hash_key           = "PetType"
    write_capacity     = 5
    read_capacity      = 5
    projection_type    = "INCLUDE"
    non_key_attributes = ["PetName", "PetPrice"]
  }

}

#Create a new API Gateway rest api with DynamoDB Integration that requires an API Key for security
resource "aws_api_gateway_rest_api" "MyApiGatewayRestApi" {
  name = "APIGW DynamoDB Serverless Pattern Demo"
  body = jsonencode({
    "swagger" : "2.0",
    "info" : {
      "version" : "2022-03-21T11:36:12Z",
      "title" : "APIGW DynamoDB Serverless Pattern Demo"
    },
    "basePath" : "/v1",
    "schemes" : ["https"],
    "paths" : {
      "/pets" : {
        "post" : {
          "consumes" : ["application/json"],
          "produces" : ["application/json"],
          "responses" : {
            "200" : {
              "description" : "200 response"
            }
          },
          "security" : [{
            "api_key" : []
          }],
          "x-amazon-apigateway-integration" : {
            "type" : "aws",
            "credentials" : "${aws_iam_role.APIGWRole.arn}",
            "httpMethod" : "POST",
            "uri" : "arn:aws:apigateway:${data.aws_region.current.name}:dynamodb:action/PutItem",
            "responses" : {
              "default" : {
                "statusCode" : "200",
                "responseTemplates" : {
                  "application/json" : "{}"
                }
              }
            },
            "requestTemplates" : {
              "application/json" : "{\"TableName\":\"Pets\",\"Item\":{\"id\":{\"S\":\"$context.requestId\"},\"PetType\":{\"S\":\"$input.path('$.PetType')\"},\"PetName\":{\"S\":\"$input.path('$.PetName')\"},\"PetPrice\":{\"N\":\"$input.path('$.PetPrice')\"}}}"
            },
            "passthroughBehavior" : "when_no_templates"
          }
        }
      },
      "/pets/{PetType}" : {
        "get" : {
          "consumes" : ["application/json"],
          "produces" : ["application/json"],
          "parameters" : [{
            "name" : "PetType",
            "in" : "path",
            "required" : true,
            "PetType" : "string"
          }],
          "responses" : {
            "200" : {
              "description" : "200 response"
            }
          },
          "security" : [{
            "api_key" : []
          }],
          "x-amazon-apigateway-integration" : {
            "type" : "aws",
            "credentials" : "${aws_iam_role.APIGWRole.arn}",
            "httpMethod" : "POST",
            "uri" : "arn:aws:apigateway:${data.aws_region.current.name}:dynamodb:action/Query",
            "responses" : {
              "default" : {
                "statusCode" : "200",
                "responseTemplates" : {
                  "application/json" : "#set($inputRoot = $input.path('$'))\n{\n\t\"pets\": [\n\t\t#foreach($field in $inputRoot.Items) {\n\t\t\t\"id\": \"$field.id.S\",\n\t\t\t\"PetType\": \"$field.PetType.S\",\n\t\t\t\"PetName\": \"$field.PetName.S\",\n\t\t\t\"PetPrice\": \"$field.PetPrice.N\"\n\t\t}#if($foreach.hasNext),#end\n\t\t#end\n\t]\n}"
                }
              }
            },
            "requestParameters" : {
              "integration.request.path.PetType" : "method.request.path.PetType"
            },
            "requestTemplates" : {
              "application/json" : "{\"TableName\":\"Pets\",\"IndexName\":\"PetType-index\",\"KeyConditionExpression\":\"PetType=:v1\",\"ExpressionAttributeValues\":{\":v1\":{\"S\":\"$util.urlDecode($input.params('PetType'))\"}}}"
            },
            "passthroughBehavior" : "when_no_templates"
          }
        }
      }
    },
    "securityDefinitions" : {
      "api_key" : {
        "type" : "apiKey",
        "name" : "x-api-key",
        "in" : "header"
      }
    }
  })
}

# Create a new API Gateway deployment for the created rest api
resource "aws_api_gateway_deployment" "MyApiGatewayDeployment" {
  rest_api_id = aws_api_gateway_rest_api.MyApiGatewayRestApi.id
}

# Create a Log Group for API Gateway to push logs to
resource "aws_cloudwatch_log_group" "MyLogGroup" {
  name_prefix = "/aws/APIGW/terraform"
}

# Create a Log Policy to allow Cloudwatch to Create log streams and put logs
resource "aws_cloudwatch_log_resource_policy" "MyCloudWatchLogPolicy" {
  policy_name     = "Terraform-CloudWatchLogPolicy-${data.aws_caller_identity.current.account_id}"
  policy_document = <<POLICY3
{
  "Version": "2012-10-17",
  "Id": "CWLogsPolicy",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": [ 
          "apigateway.amazonaws.com",
          "delivery.logs.amazonaws.com"
          ]
      },
      "Action": [
        "logs:CreateLogStream",
        "logs:PutLogEvents"
        ],
      "Resource": "${aws_cloudwatch_log_group.MyLogGroup.arn}",
      "Condition": {
        "ArnEquals": {
          "aws:SourceArn": "${aws_api_gateway_rest_api.MyApiGatewayRestApi.arn}"
        }
      }
    }
  ]
}
POLICY3  
}

# Create a new API Gateway stage with logging enabled
resource "aws_api_gateway_stage" "MyApiGatewayStage" {
  deployment_id = aws_api_gateway_deployment.MyApiGatewayDeployment.id
  rest_api_id   = aws_api_gateway_rest_api.MyApiGatewayRestApi.id
  stage_name    = "v1"
  depends_on    = [aws_api_gateway_account.ApiGatewayAccountSetting]

  access_log_settings {
    destination_arn = aws_cloudwatch_log_group.MyLogGroup.arn
    format          = "{ \"requestId\":\"$context.requestId\", \"ip\": \"$context.identity.sourceIp\", \"requestTime\":\"$context.requestTime\", \"httpMethod\":\"$context.httpMethod\",\"routeKey\":\"$context.routeKey\", \"status\":\"$context.status\",\"protocol\":\"$context.protocol\", \"responseLength\":\"$context.responseLength\" }"
  }
}

# If you are using apigateway and you have an existing cloudwatch role ARN set to your account delete the aws_api_gateway_account block, the aws_iam_role block & the aws_iam_role_policy block.

## delete if you have this configured in your account
resource "aws_api_gateway_account" "ApiGatewayAccountSetting" {
  cloudwatch_role_arn = aws_iam_role.APIGatewayCloudWatchRole.arn
}

## delete if you have this configured in your account
resource "aws_iam_role" "APIGatewayCloudWatchRole" {
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "Service": "apigateway.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF
}

## delete if you have this configured in your account
resource "aws_iam_role_policy" "APIGatewayCloudWatchPolicy" {
  role = aws_iam_role.APIGatewayCloudWatchRole.id

  policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:DescribeLogGroups",
                "logs:DescribeLogStreams",
                "logs:PutLogEvents",
                "logs:GetLogEvents",
                "logs:FilterLogEvents"
            ],
            "Resource": "*"
        }
    ]
}
EOF
}

# Configure API Gateway to push all logs to CloudWatch Logs
resource "aws_api_gateway_method_settings" "MyApiGatewaySetting" {
  rest_api_id = aws_api_gateway_rest_api.MyApiGatewayRestApi.id
  stage_name  = aws_api_gateway_stage.MyApiGatewayStage.stage_name
  method_path = "*/*"

  settings {
    # Enable CloudWatch logging and metrics
    metrics_enabled = true
    logging_level   = "INFO"
  }
}

# Create an API Gateway usage plan to use with the created REST API
resource "aws_api_gateway_usage_plan" "MyApiGatewayUsagePlan" {
  name = "apigw-dynamodb-terraform-usage-plan"

  quota_settings {
    limit  = 1000
    period = "MONTH"
  }

  throttle_settings {
    burst_limit = 20
    rate_limit  = 100
  }

  api_stages {
    api_id = aws_api_gateway_rest_api.MyApiGatewayRestApi.id
    stage  = aws_api_gateway_stage.MyApiGatewayStage.stage_name
  }
}

# Create an API Gateway Key
resource "aws_api_gateway_api_key" "MyAPIKey" {
  name = "apigw-dynamodb-terraform-api-key"
}

# Create an API Gateway Usage Plan key and associate it to the previously created API Key
resource "aws_api_gateway_usage_plan_key" "MyAPIGWUsagePlanKey" {
  key_id        = aws_api_gateway_api_key.MyAPIKey.id
  key_type      = "API_KEY"
  usage_plan_id = aws_api_gateway_usage_plan.MyApiGatewayUsagePlan.id
}

# Display APIGW invocation URL 
output "APIGW-URL" {
  value       = "${aws_api_gateway_stage.MyApiGatewayStage.invoke_url}/pets"
  description = "The API Gateway Invocation URL"
}

# Display the APIGW Key to use for testing
output "APIGW-Key" {
  value       = aws_api_gateway_usage_plan_key.MyAPIGWUsagePlanKey.value
  description = "The APIGW Key to use for testing"
}