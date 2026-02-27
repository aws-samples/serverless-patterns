# Deploys Cognito resources

resource "aws_cognito_user_pool" "UserPool" {
  name                = "${var.contructID}_user_pool"
  mfa_configuration   = "OFF"
  username_attributes = ["email"]

  schema {
    name                = "fullname"
    attribute_data_type = "String"
    mutable             = true
    string_attribute_constraints {
      min_length = 1
      max_length = 256
    }
  }

  schema {
    name                = "email"
    attribute_data_type = "String"
    mutable             = true
    string_attribute_constraints {
      min_length = 1
      max_length = 256
    }
  }

  schema {
    name                = "api_key"
    attribute_data_type = "String"
    mutable             = true
    required            = false
    string_attribute_constraints {
      min_length = 1
      max_length = 256
    }
  }
}

resource "aws_cognito_user_pool_client" "client" {
  name         = "UserPoolClient"
  user_pool_id = aws_cognito_user_pool.UserPool.id
  explicit_auth_flows = [
    "ALLOW_USER_PASSWORD_AUTH",
    "ALLOW_REFRESH_TOKEN_AUTH"
  ]

  token_validity_units {
    refresh_token = "hours"
  }

  refresh_token_validity = 1
}

resource "aws_ssm_parameter" "userPoolID" {
  name        = "/${var.contructID}/user_pool/id"
  description = "User pool ID"
  type        = "String"
  value       = aws_cognito_user_pool.UserPool.id
}

resource "aws_ssm_parameter" "clientid" {
  name        = "/${var.contructID}/user_pool/client_id"
  description = "User pool client ID"
  type        = "String"
  value       = aws_cognito_user_pool_client.client.id
}
