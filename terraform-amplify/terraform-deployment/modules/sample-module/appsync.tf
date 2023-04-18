# TODO - Consider replacing 'Scan' DynamoDB operations with 'Query'
# https://docs.aws.amazon.com/appsync/latest/devguide/resolver-mapping-template-reference-dynamodb.html#aws-appsync-resolver-mapping-template-reference-dynamodb-getitem
# https://docs.aws.amazon.com/appsync/latest/devguide/security-authz.html#amazon-cognito-user-pools-authorization
# API Data Source
resource "aws_appsync_datasource" "sample_appsync_dynamodb_datasource" {
  api_id           = aws_appsync_graphql_api.sample_appsync_graphql_api.id
  name             = "sample_output_dynamodb_datasource"
  service_role_arn = aws_iam_role.sample_appsync_dynamodb_restricted_access[0].arn
  type             = "AMAZON_DYNAMODB"

  dynamodb_config {
    table_name = aws_dynamodb_table.sample_output.name
  }
}
# API
resource "aws_appsync_graphql_api" "sample_appsync_graphql_api" {
  authentication_type = "AMAZON_COGNITO_USER_POOLS"
  name                = var.sample_appsync_graphql_api_name

  user_pool_config {
    aws_region     = data.aws_region.current.name
    default_action = "ALLOW"
    user_pool_id   = aws_cognito_user_pool.sample_user_pool.id
  }


  schema = <<EOF
type Object  @aws_auth(cognito_groups: ["Admin", "Standard"])  {
  ObjectId: String!
  Version: String
  DetailType: String
  Source: String
  FileName: String
  FilePath: String
  AccountId: String
  CreatedAt: String
  Region: String
  CurrentBucket: String
  OriginalBucket: String
  ObjectSize: Int
  SourceIPAddress: String
  LifecycleConfig: String
}

type Objects {
  items: [Object]
  nextToken: String
  @aws_auth(cognito_groups: ["Admin", "Standard"])
}


type Query {
  listObjects(limit: Int, nextToken: String): Objects @aws_auth(cognito_groups: ["Admin", "Standard"])
  getObject(ObjectId: String!): Object @aws_auth(cognito_groups: ["Admin", "Standard"])
  }

type Mutation {
  deleteOneObject(ObjectId: String!): Object
  @aws_auth(cognito_groups: ["Admin",])
}

schema {
  query: Query
  mutation: Mutation
}
EOF
}


# Resolvers
# UNIT type resolver (default)
# Query - Get Object
# Returns data from one object specificied by 'ObjectId'
resource "aws_appsync_resolver" "sample_appsync_resolver_query_get_object" {
  api_id = aws_appsync_graphql_api.sample_appsync_graphql_api.id
  field  = "getObject"
  type   = "Query"
  data_source = aws_appsync_datasource.sample_appsync_dynamodb_datasource.name

  request_template = <<EOF
{
    "version" : "2017-02-28",
    "operation" : "GetItem",
    "key" : {
       "ObjectId" : $util.dynamodb.toDynamoDBJson($ctx.args.ObjectId)
    },
    "consistentRead" : false
}
EOF

  response_template = <<EOF
    $util.toJson($ctx.result)
EOF
}
# Scan - List Objects
# Returns data for all objects. If no limit is provided, default limit will be 50 items.
resource "aws_appsync_resolver" "sample_appsync_resolver_query_get_all_objects" {
  api_id      = aws_appsync_graphql_api.sample_appsync_graphql_api.id
  field       = "listObjects"
  type        = "Query"
  data_source = aws_appsync_datasource.sample_appsync_dynamodb_datasource.name

  request_template = <<EOF

{
    "version" : "2017-02-28",
    "operation" : "Scan",
    "limit": $util.defaultIfNull($ctx.args.limit, 50),
    "consistentRead" : false,
    "nextToken" : $util.toJson($util.defaultIfNullOrEmpty($ctx.args.nextToken, null)),
}
EOF

  response_template = <<EOF
   $util.toJson($ctx.result)
EOF
}



# Mutation - Delete One Object
resource "aws_appsync_resolver" "sample_appsync_resolver_mutation_delete_one_object" {
  api_id      = aws_appsync_graphql_api.sample_appsync_graphql_api.id
  field       = "deleteOneObject"
  type        = "Mutation"
  data_source = aws_appsync_datasource.sample_appsync_dynamodb_datasource.name

  request_template = <<EOF
{
    "version" : "2017-02-28",
    "operation" : "DeleteItem",
    "key" : {
        "ObjectId" : $util.dynamodb.toDynamoDBJson($ctx.args.ObjectId)
    }
}
EOF

  response_template = <<EOF
   $util.toJson($ctx.result)
EOF
}







