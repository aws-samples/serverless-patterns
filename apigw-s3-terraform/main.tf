terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }
  }

  required_version = ">= 0.14.9"
}

# Storing current Account ID and actual AWS region
data "aws_caller_identity" "current" {}
data "aws_region" "current" {}


#################################################################
# S3 Bucket
#################################################################
# Creating a new S3 bucket
resource "aws_s3_bucket" "MyS3Bucket" {
  bucket_prefix = "apigw-s3-tf-s3bucket-"
}

# Sending notifications to EventBridge for all events in the bucket
resource "aws_s3_bucket_notification" "MyS3BucketNotification" {
  bucket      = aws_s3_bucket.MyS3Bucket.id
  eventbridge = true
}

# Blocking s3 bucket non secure access
resource "aws_s3_bucket_policy" "MyS3BucketPolicy" {
  bucket = aws_s3_bucket.MyS3Bucket.id
  policy = data.aws_iam_policy_document.MyS3BucketPolicyDocument.json
}

data "aws_iam_policy_document" "MyS3BucketPolicyDocument" {
  statement  {
    sid = "AllowSSLRequestsOnly"
    effect = "Deny"
    principals {
      type        = "*"
      identifiers = ["*"]
    }
    actions = [
      "s3:*"
    ]
    resources = [
      "arn:aws:s3:::${aws_s3_bucket.MyS3Bucket.id}",
      "arn:aws:s3:::${aws_s3_bucket.MyS3Bucket.id}/*"
    ]
    condition {
      test     = "Bool"
      variable = "aws:SecureTransport"
      values   = ["false"]
    }
  }
}

#################################################################
# API Gateway REST
#################################################################
# Creating a new API Gateway
resource "aws_api_gateway_rest_api" "MyAPIGatewayREST" {
    name          = "apigw-s3-tf-apigateway-rest"
    binary_media_types = [ "application/octet-stream", "image/jpeg"]
}

resource "aws_api_gateway_resource" "MyAPIGatewayResourceFolder" {
  parent_id   = aws_api_gateway_rest_api.MyAPIGatewayREST.root_resource_id
  path_part   = "{folder}"
  rest_api_id = aws_api_gateway_rest_api.MyAPIGatewayREST.id
}

resource "aws_api_gateway_resource" "MyAPIGatewayResourceFolderItem" {
  parent_id   = aws_api_gateway_resource.MyAPIGatewayResourceFolder.id
  path_part   = "{item}"
  rest_api_id = aws_api_gateway_rest_api.MyAPIGatewayREST.id
}

# Creating API Gateway Role
resource "aws_iam_role" "MyAPIGatewayS3Role" {
  name = "apigw-s3-tf-apigateway-role"

# Create Trust Policy for API Gateway
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
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

resource "aws_iam_policy" "MyAPIGatewayS3Policy" {
  name        = "apigw-s3-tf-apigateway-policy"

  policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": "s3:ListAllMyBuckets",
            "Resource": "*",
            "Effect": "Allow"
        },
        {
            "Action": "s3:ListBucket",
            "Resource": "*",
            "Effect": "Allow"
        },
        {
            "Action": "s3:GetObject",
            "Resource": "*",
            "Effect": "Allow"
        },
        {
            "Action": "s3:PutObject",
            "Resource": "*",
            "Effect": "Allow"
        }
    ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "MyAPIGatewayRoleManagedPolicy" {
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonAPIGatewayPushToCloudWatchLogs"
  role       = "${aws_iam_role.MyAPIGatewayS3Role.name}"
}

# Attaching S3 Access Policy to the API Gateway Role
resource "aws_iam_role_policy_attachment" "MyAPIGatewayPolicyAttach" {
  role       = aws_iam_role.MyAPIGatewayS3Role.name
  policy_arn = aws_iam_policy.MyAPIGatewayS3Policy.arn
}

# Deploying and stages 
resource "aws_api_gateway_deployment" "MyAPIGatewayDeployment" {
  rest_api_id = aws_api_gateway_rest_api.MyAPIGatewayREST.id

  triggers = {
    # NOTE: The configuration below will satisfy ordering considerations,
    #       but not pick up all future REST API changes. More advanced patterns
    #       are possible, such as using the filesha1() function against the
    #       Terraform configuration file(s) or removing the .id references to
    #       calculate a hash against whole resources. Be aware that using whole
    #       resources will show a difference after the initial implementation.
    #       It will stabilize to only change when resources change afterwards.
    redeployment = sha1(jsonencode([
      aws_api_gateway_resource.MyAPIGatewayResourceFolder,
      aws_api_gateway_method.MyAPIGatewayMethodFolderGet,
      aws_api_gateway_method.MyAPIGatewayMethodFolderItemGet,
      aws_api_gateway_method.MyAPIGatewayMethodFolderItemHead,
      aws_api_gateway_method.MyAPIGatewayMethodFolderItemPut,
      aws_api_gateway_integration.MyAPIGatewayIntRootGet,
      aws_api_gateway_integration.MyAPIGatewayIntFolderGet,
      aws_api_gateway_integration.MyAPIGatewayIntFolderItemGet,
      aws_api_gateway_integration.MyAPIGatewayIntFolderItemHead,
      aws_api_gateway_integration.MyAPIGatewayIntFolderItemPut,
      aws_iam_role.MyAPIGatewayS3Role,
      aws_iam_role.MyAPIGatewayAccountRole
    ]))
  }

  lifecycle {
    create_before_destroy = true
  }
  
  depends_on = [
    aws_api_gateway_method.MyAPIGatewayMethodFolderGet,
    aws_api_gateway_method.MyAPIGatewayMethodFolderItemGet,
    aws_api_gateway_method.MyAPIGatewayMethodFolderItemHead,
    aws_api_gateway_method.MyAPIGatewayMethodFolderItemPut,
    aws_api_gateway_integration.MyAPIGatewayIntRootGet,
    aws_api_gateway_integration.MyAPIGatewayIntFolderGet,
    aws_api_gateway_integration.MyAPIGatewayIntFolderItemGet,
    aws_api_gateway_integration.MyAPIGatewayIntFolderItemHead,
    aws_api_gateway_integration.MyAPIGatewayIntFolderItemPut,
    aws_iam_role.MyAPIGatewayS3Role,
    aws_iam_role.MyAPIGatewayAccountRole
  ]
}

resource "aws_api_gateway_stage" "MyAPIGatewayStage" {
  deployment_id = aws_api_gateway_deployment.MyAPIGatewayDeployment.id
  rest_api_id   = aws_api_gateway_rest_api.MyAPIGatewayREST.id
  stage_name    = "prod"
  
  access_log_settings {
    destination_arn = aws_cloudwatch_log_group.MyAPIGatewayLogGroup.arn
    format          = "{\"requestId\":\"$context.requestId\",\"ip\": \"$context.identity.sourceIp\",\"caller\":\"$context.identity.caller\",\"user\":\"$context.identity.user\",\"requestTime\":\"$context.requestTime\",\"httpMethod\":\"$context.httpMethod\",\"resourcePath\":\"$context.resourcePath\",\"status\":\"$context.status\",\"protocol\":\"$context.protocol\",\"responseLength\":\"$context.responseLength\"}"
  }
  
}

# Creating Logas configuration on CloudWatch
resource "aws_api_gateway_account" "MyAPIGatewayAccount" {
  cloudwatch_role_arn = aws_iam_role.MyAPIGatewayAccountRole.arn
}

data "aws_iam_policy_document" "MyAPIGatewayAccountPolicy" {
  version = "2012-10-17"
  statement {
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["apigateway.amazonaws.com"]
    }

    actions = ["sts:AssumeRole"]
  }
}

resource "aws_iam_role" "MyAPIGatewayAccountRole" {
  name               = "apigw-s3-tf-apigateway-account-role"
  assume_role_policy = data.aws_iam_policy_document.MyAPIGatewayAccountPolicy.json
}

resource "aws_iam_role_policy_attachment" "MyAPIGatewayAccountManagedPolicy" {
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonAPIGatewayPushToCloudWatchLogs"
  role       = "${aws_iam_role.MyAPIGatewayAccountRole.name}"
}

resource "aws_cloudwatch_log_group" "MyAPIGatewayLogGroup" {
  name = "/aws/api-gateway/${aws_api_gateway_rest_api.MyAPIGatewayREST.name}"
}

#################################################################
# API Gateway REST Methods, integrations and responses
#################################################################

# /               GET
resource "aws_api_gateway_method" "MyAPIGatewayMethodRootGet" {
  authorization = "AWS_IAM"
  http_method   = "GET"
  resource_id   = aws_api_gateway_rest_api.MyAPIGatewayREST.root_resource_id
  rest_api_id   = aws_api_gateway_rest_api.MyAPIGatewayREST.id
  
}

# /{folder}       GET
resource "aws_api_gateway_method" "MyAPIGatewayMethodFolderGet" {
  authorization = "AWS_IAM"
  http_method   = "GET"
  resource_id   = aws_api_gateway_resource.MyAPIGatewayResourceFolder.id
  rest_api_id   = aws_api_gateway_rest_api.MyAPIGatewayREST.id
  
  request_parameters = {
    "method.request.path.folder"   = true
  }
  
}

# /{folder}/{item} GET
resource "aws_api_gateway_method" "MyAPIGatewayMethodFolderItemGet" {
  authorization = "AWS_IAM"
  http_method   = "GET"
  resource_id   = aws_api_gateway_resource.MyAPIGatewayResourceFolderItem.id
  rest_api_id   = aws_api_gateway_rest_api.MyAPIGatewayREST.id
  
  request_parameters = {
    "method.request.path.folder"  = true,
    "method.request.path.item"    = true,
    "method.request.header.Accept" = true
  }
  
}

# /{folder}/{item} HEAD
resource "aws_api_gateway_method" "MyAPIGatewayMethodFolderItemHead" {
  authorization = "AWS_IAM"
  http_method   = "HEAD"
  resource_id   = aws_api_gateway_resource.MyAPIGatewayResourceFolderItem.id
  rest_api_id   = aws_api_gateway_rest_api.MyAPIGatewayREST.id
  
  request_parameters = {
    "method.request.path.folder"  = true,
    "method.request.path.item"    = true,
    "method.request.header.Accept" = true
  }
  
}

# /{folder}/{item} PUT
resource "aws_api_gateway_method" "MyAPIGatewayMethodFolderItemPut" {
  authorization = "AWS_IAM"
  http_method   = "PUT"
  resource_id   = aws_api_gateway_resource.MyAPIGatewayResourceFolderItem.id
  rest_api_id   = aws_api_gateway_rest_api.MyAPIGatewayREST.id
  
  request_parameters = {
    "method.request.path.folder"  = true,
    "method.request.path.item"    = true,
    "method.request.header.Accept" = true
  }
  
}

# /               - GET - Method, execution and response
resource "aws_api_gateway_integration" "MyAPIGatewayIntRootGet" {
  http_method = aws_api_gateway_method.MyAPIGatewayMethodRootGet.http_method
  resource_id = aws_api_gateway_rest_api.MyAPIGatewayREST.root_resource_id
  rest_api_id = aws_api_gateway_rest_api.MyAPIGatewayREST.id
  type        = "AWS"
  passthrough_behavior = "WHEN_NO_TEMPLATES"
  integration_http_method = "GET"
  uri         = "arn:aws:apigateway:${data.aws_region.current.name}:s3:path/"
  credentials = aws_iam_role.MyAPIGatewayS3Role.arn
}

resource "aws_api_gateway_method_response" "MyAPIGatewayIntRootGetResponse200" {
  rest_api_id = aws_api_gateway_rest_api.MyAPIGatewayREST.id
  resource_id = aws_api_gateway_rest_api.MyAPIGatewayREST.root_resource_id
  http_method = aws_api_gateway_method.MyAPIGatewayMethodRootGet.http_method
  status_code = "200"

  response_parameters = {
    "method.response.header.Content-Type"   = true
  }
  
}

resource "aws_api_gateway_integration_response" "MyAPIGatewayIntRootGetIntegrationResponse" {
  rest_api_id = aws_api_gateway_rest_api.MyAPIGatewayREST.id
  resource_id = aws_api_gateway_rest_api.MyAPIGatewayREST.root_resource_id
  http_method = aws_api_gateway_method.MyAPIGatewayMethodRootGet.http_method
  status_code = aws_api_gateway_method_response.MyAPIGatewayIntRootGetResponse200.status_code

  response_parameters = { "method.response.header.Content-Type" = "integration.response.header.Content-Type" }

  depends_on = [aws_api_gateway_rest_api.MyAPIGatewayREST,
                aws_api_gateway_method.MyAPIGatewayMethodRootGet,
                aws_api_gateway_method_response.MyAPIGatewayIntRootGetResponse200,
                aws_api_gateway_method.MyAPIGatewayMethodFolderItemGet,
                aws_iam_role_policy_attachment.MyAPIGatewayPolicyAttach]

}

# /{folder}       - GET - Method, execution and response
resource "aws_api_gateway_integration" "MyAPIGatewayIntFolderGet" {
  http_method = aws_api_gateway_method.MyAPIGatewayMethodFolderGet.http_method
  resource_id = aws_api_gateway_resource.MyAPIGatewayResourceFolder.id
  rest_api_id = aws_api_gateway_rest_api.MyAPIGatewayREST.id
  type        = "AWS"
  passthrough_behavior    = "WHEN_NO_TEMPLATES"
  integration_http_method = "GET"
  uri         = "arn:aws:apigateway:${data.aws_region.current.name}:s3:path/{bucket}"
  credentials = aws_iam_role.MyAPIGatewayS3Role.arn
  request_parameters = {
    "integration.request.path.bucket"   = "method.request.path.folder"
  }
  
}

resource "aws_api_gateway_method_response" "MyAPIGatewayIntFolderGetResponse200" {
  rest_api_id = aws_api_gateway_rest_api.MyAPIGatewayREST.id
  resource_id = aws_api_gateway_resource.MyAPIGatewayResourceFolder.id
  http_method = aws_api_gateway_method.MyAPIGatewayMethodFolderGet.http_method
  status_code = "200"

  response_parameters = {
    "method.response.header.Content-Type"   = true
  }
  
}

resource "aws_api_gateway_integration_response" "MyAPIGatewayIntFolderGetIntegrationResponse" {
  rest_api_id = aws_api_gateway_rest_api.MyAPIGatewayREST.id
  resource_id = aws_api_gateway_resource.MyAPIGatewayResourceFolder.id
  http_method = aws_api_gateway_method.MyAPIGatewayMethodFolderGet.http_method
  status_code = aws_api_gateway_method_response.MyAPIGatewayIntFolderGetResponse200.status_code

  response_parameters = { "method.response.header.Content-Type" = "integration.response.header.Content-Type" }

  depends_on = [aws_api_gateway_rest_api.MyAPIGatewayREST,
                aws_api_gateway_method.MyAPIGatewayMethodRootGet,
                aws_api_gateway_method_response.MyAPIGatewayIntFolderGetResponse200,
                aws_api_gateway_method.MyAPIGatewayMethodFolderItemGet,
                aws_iam_role_policy_attachment.MyAPIGatewayPolicyAttach]

}

# /{folder}/{item} - GET - Method, execution and response
resource "aws_api_gateway_integration" "MyAPIGatewayIntFolderItemGet" {
  http_method = aws_api_gateway_method.MyAPIGatewayMethodFolderItemGet.http_method
  resource_id = aws_api_gateway_resource.MyAPIGatewayResourceFolderItem.id
  rest_api_id = aws_api_gateway_rest_api.MyAPIGatewayREST.id
  type        = "AWS"
  passthrough_behavior    = "WHEN_NO_TEMPLATES"
  integration_http_method = "GET"
  uri         = "arn:aws:apigateway:${data.aws_region.current.name}:s3:path/{bucket}/{object}"
  credentials = aws_iam_role.MyAPIGatewayS3Role.arn
  request_parameters = {
    "integration.request.path.bucket"   = "method.request.path.folder",
    "integration.request.path.object"   = "method.request.path.item",
    "integration.request.header.Accept" = "method.request.header.Accept"
  }
}

resource "aws_api_gateway_method_response" "MyAPIGatewayIntFolderItemGetResponse200" {
  rest_api_id = aws_api_gateway_rest_api.MyAPIGatewayREST.id
  resource_id = aws_api_gateway_resource.MyAPIGatewayResourceFolderItem.id
  http_method = aws_api_gateway_method.MyAPIGatewayMethodFolderItemGet.http_method
  status_code = "200"

  response_parameters = {
    "method.response.header.Content-Type"   = true
  }
  
}

resource "aws_api_gateway_integration_response" "MyAPIGatewayIntFolderItemGetIntegrationResponse" {
  rest_api_id = aws_api_gateway_rest_api.MyAPIGatewayREST.id
  resource_id = aws_api_gateway_resource.MyAPIGatewayResourceFolderItem.id
  http_method = aws_api_gateway_method.MyAPIGatewayMethodFolderItemGet.http_method
  status_code = aws_api_gateway_method_response.MyAPIGatewayIntFolderItemGetResponse200.status_code

  response_parameters = { "method.response.header.Content-Type" = "integration.response.header.Content-Type" }

  depends_on = [aws_api_gateway_rest_api.MyAPIGatewayREST,
                aws_api_gateway_method.MyAPIGatewayMethodRootGet,
                aws_api_gateway_method_response.MyAPIGatewayIntFolderItemGetResponse200,
                aws_api_gateway_method.MyAPIGatewayMethodFolderItemGet,
                aws_iam_role_policy_attachment.MyAPIGatewayPolicyAttach]

}

# /{folder}/{item} - HEAD - Method, execution and response
resource "aws_api_gateway_integration" "MyAPIGatewayIntFolderItemHead" {
  http_method = aws_api_gateway_method.MyAPIGatewayMethodFolderItemHead.http_method
  resource_id = aws_api_gateway_resource.MyAPIGatewayResourceFolderItem.id
  rest_api_id = aws_api_gateway_rest_api.MyAPIGatewayREST.id
  type        = "AWS"
  passthrough_behavior    = "WHEN_NO_TEMPLATES"
  integration_http_method = "HEAD"
  uri         = "arn:aws:apigateway:${data.aws_region.current.name}:s3:path/{bucket}/{object}"
  credentials = aws_iam_role.MyAPIGatewayS3Role.arn
  request_parameters = {
    "integration.request.path.bucket"   = "method.request.path.folder",
    "integration.request.path.object"   = "method.request.path.item",
    "integration.request.header.Accept" = "method.request.header.Accept"
  }
}

resource "aws_api_gateway_method_response" "MyAPIGatewayIntFolderItemHeadResponse200" {
  rest_api_id = aws_api_gateway_rest_api.MyAPIGatewayREST.id
  resource_id = aws_api_gateway_resource.MyAPIGatewayResourceFolderItem.id
  http_method = aws_api_gateway_method.MyAPIGatewayMethodFolderItemHead.http_method
  status_code = "200"

  response_parameters = {
    "method.response.header.Content-Type"   = true
  }
  
}

resource "aws_api_gateway_integration_response" "MyAPIGatewayIntFolderItemHeadIntegrationResponse" {
  rest_api_id = aws_api_gateway_rest_api.MyAPIGatewayREST.id
  resource_id = aws_api_gateway_resource.MyAPIGatewayResourceFolderItem.id
  http_method = aws_api_gateway_method.MyAPIGatewayMethodFolderItemHead.http_method
  status_code = aws_api_gateway_method_response.MyAPIGatewayIntFolderItemHeadResponse200.status_code

  response_parameters = { "method.response.header.Content-Type" = "integration.response.header.Content-Type" }

  depends_on = [aws_api_gateway_rest_api.MyAPIGatewayREST,
                aws_api_gateway_method.MyAPIGatewayMethodRootGet,
                aws_api_gateway_method_response.MyAPIGatewayIntFolderItemHeadResponse200,
                aws_api_gateway_method.MyAPIGatewayMethodFolderItemHead,
                aws_iam_role_policy_attachment.MyAPIGatewayPolicyAttach]

}

# /{folder}/{item} - PUT - Method, execution and response
resource "aws_api_gateway_integration" "MyAPIGatewayIntFolderItemPut" {
  http_method = aws_api_gateway_method.MyAPIGatewayMethodFolderItemPut.http_method
  resource_id = aws_api_gateway_resource.MyAPIGatewayResourceFolderItem.id
  rest_api_id = aws_api_gateway_rest_api.MyAPIGatewayREST.id
  type        = "AWS"
  passthrough_behavior    = "WHEN_NO_TEMPLATES"
  integration_http_method = "PUT"
  uri         = "arn:aws:apigateway:${data.aws_region.current.name}:s3:path/{bucket}/{object}"
  credentials = aws_iam_role.MyAPIGatewayS3Role.arn
  request_parameters = {
    "integration.request.path.bucket"   = "method.request.path.folder",
    "integration.request.path.object"   = "method.request.path.item",
    "integration.request.header.Accept" = "method.request.header.Accept"
  }
}

resource "aws_api_gateway_method_response" "MyAPIGatewayIntFolderItemPutResponse200" {
  rest_api_id = aws_api_gateway_rest_api.MyAPIGatewayREST.id
  resource_id = aws_api_gateway_resource.MyAPIGatewayResourceFolderItem.id
  http_method = aws_api_gateway_method.MyAPIGatewayMethodFolderItemPut.http_method
  status_code = "200"

  response_parameters = {
    "method.response.header.Content-Type"   = true
  }
  
}

resource "aws_api_gateway_integration_response" "MyAPIGatewayIntFolderItemPutIntegrationResponse" {
  rest_api_id = aws_api_gateway_rest_api.MyAPIGatewayREST.id
  resource_id = aws_api_gateway_resource.MyAPIGatewayResourceFolderItem.id
  http_method = aws_api_gateway_method.MyAPIGatewayMethodFolderItemPut.http_method
  status_code = aws_api_gateway_method_response.MyAPIGatewayIntFolderItemPutResponse200.status_code

  response_parameters = { "method.response.header.Content-Type" = "integration.response.header.Content-Type" }

  depends_on = [aws_api_gateway_rest_api.MyAPIGatewayREST,
                aws_api_gateway_method.MyAPIGatewayMethodRootGet,
                aws_api_gateway_method_response.MyAPIGatewayIntFolderItemPutResponse200,
                aws_api_gateway_method.MyAPIGatewayMethodFolderItemPut,
                aws_iam_role_policy_attachment.MyAPIGatewayPolicyAttach]

}

#################################################################
# Outputs
#################################################################
# Displaying the S3 bucket and API Gateway REST values
output "S3BucketName" {
  value       = aws_s3_bucket.MyS3Bucket.id
  description = "The S3 Bucket Name"
}

output "APIGateway" {
  value       = aws_api_gateway_rest_api.MyAPIGatewayREST.arn
  description = "The API Gateway ARN"
}

output "APIGatewayDeploymentURL" {
  value = "${aws_api_gateway_deployment.MyAPIGatewayDeployment.invoke_url}${aws_api_gateway_stage.MyAPIGatewayStage.stage_name}"
  description = "The API Gateway Deployment URL"
}

output "InitialURL" {
  value = "${aws_api_gateway_deployment.MyAPIGatewayDeployment.invoke_url}${aws_api_gateway_stage.MyAPIGatewayStage.stage_name}/${aws_s3_bucket.MyS3Bucket.id}"
  description = "The Initial URL"
}

