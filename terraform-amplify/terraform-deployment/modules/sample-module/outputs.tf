# AWS Current Region
output "aws_current_region" {
  value = data.aws_region.current

}

# S3
output "sample_input_bucket_id" {
  value       = aws_s3_bucket.sample_input_bucket
  description = "The name of the S3 input bucket"
}
output "sample_input_bucket_arn" {
  value       = aws_s3_bucket.sample_input_bucket
  description = "The Arn of the S3 input bucket"
}
output "sample_output_bucket_id" {
  value       = aws_s3_bucket.sample_output_bucket
  description = "The name of the S3 output bucket"
}
output "sample_output_bucket_arn" {
  value       = aws_s3_bucket.sample_output_bucket
  description = "The Arn of the S3 input bucket"
}
output "sample_app_storage_bucket_id" {
  value       = aws_s3_bucket.sample_app_storage_bucket
  description = "The name of the S3 app storage bucket"
}
output "sample_app_storage_bucket_arn" {
  value       = aws_s3_bucket.sample_app_storage_bucket
  description = "The ARN of the S3 app storage bucket"
}

# Amplify

# Step Function
output "sample_step_function_arn" {
  value = aws_sfn_state_machine.sample_sfn_state_machine.arn

}

# IAM

# DynamoDB
output "sample_dynamodb_output_table_name" {
  value = aws_dynamodb_table.sample_output.name
}



# Cognito
output "sample_user_pool_region" {
  value = data.aws_region.current
}
output "sample_user_pool_id" {
  value = aws_cognito_user_pool.sample_user_pool
}
output "sample_user_pool_client_id" {
  value = aws_cognito_user_pool_client.sample_user_pool_client
}
output "sample_identity_pool_id" {
  value = aws_cognito_identity_pool.sample_identity_pool
}


# AppSync (GraphQL)
output "sample_appsync_graphql_api_region" {
  value = data.aws_region.current
}
output "sample_appsync_graphql_api_id" {
  value = aws_appsync_graphql_api.sample_appsync_graphql_api
}
output "sample_appsync_graphql_api_uris" {
  value = aws_appsync_graphql_api.sample_appsync_graphql_api
}
