import aws_cdk as cdk
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    aws_iam as iam,
    aws_cognito as cognito,
    aws_logs as logs,
    Duration,
    CfnOutput,
)
from constructs import Construct
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the environment variables and add error handling
redshift_cluster_arn = os.getenv("REDSHIFT_CLUSTER_ARN")
redshift_workgroup = os.getenv("REDSHIFT_WORKGROUP")
redshift_database = os.getenv("REDSHIFT_DATABASE")

if not redshift_cluster_arn:
    raise ValueError("REDSHIFT_CLUSTER_ARN environment variable is not set")
if not redshift_workgroup:
    raise ValueError("REDSHIFT_WORKGROUP environment variable is not set")
if not redshift_database:
    raise ValueError("REDSHIFT_DATABASE environment variable is not set")


class ApigwRedshiftDataApi(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create Cognito User Pool
        user_pool = cognito.UserPool(
            self,
            "RedshiftApiUserPool",
            sign_in_aliases=cognito.SignInAliases(username=True, email=True),
            auto_verify=cognito.AutoVerifiedAttrs(email=True),
            standard_attributes=cognito.StandardAttributes(
                email=cognito.StandardAttribute(required=True, mutable=True)
            ),
        )

        # Add a domain to the User Pool
        domain = user_pool.add_domain(
            "CognitoDomain",
            cognito_domain=cognito.CognitoDomainOptions(
                domain_prefix="apigwredshiftapi-" + self.account
            ),
        )

        # Define a custom scope
        redshift_api_scope = cognito.ResourceServerScope(
            scope_name="redshift-api",
            scope_description="Access to Redshift API",
        )

        # Create a resource server for custom scopes
        resource_server = user_pool.add_resource_server(
            "RedshiftApiResourceServer",
            identifier="redshiftapi",
            scopes=[redshift_api_scope],
        )

        # Create Cognito App Client
        app_client = user_pool.add_client(
            "RedshiftApiAppClient",
            generate_secret=True,
            o_auth=cognito.OAuthSettings(
                flows=cognito.OAuthFlows(
                    client_credentials=True,
                ),
                scopes=[
                    cognito.OAuthScope.resource_server(
                        resource_server, redshift_api_scope
                    )
                ],
            ),
            access_token_validity=Duration.minutes(60),
            prevent_user_existence_errors=True,
        )

        # Create Lambda function
        lambda_function = _lambda.Function(
            self,
            "RedshiftApiLambda",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="index.lambda_handler",
            code=_lambda.InlineCode(
                """
import json
import boto3
import time
import os
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    redshift_workgroup = os.environ['REDSHIFT_WORKGROUP']
    redshift_database = os.environ['REDSHIFT_DATABASE']
    sql_query = "SELECT * FROM tickit.users LIMIT 10;"

    client = boto3.client("redshift-data")
    
    try:
        # Execute the query
        response = client.execute_statement(
            WorkgroupName=redshift_workgroup,
            Database=redshift_database,
            Sql=sql_query
        )
        query_id = response["Id"]
        
        # Wait for the query to complete
        while True:
            status_response = client.describe_statement(Id=query_id)
            status = status_response['Status']
            
            if status == 'FINISHED':
                # Query completed successfully
                result = client.get_statement_result(Id=query_id)
                columns = [col["name"] for col in result["ColumnMetadata"]]
                rows = result["Records"]
                results = [
                    dict(zip(columns, [list(value.values())[0] for value in row]))
                    for row in rows
                ]
                return {"statusCode": 200, "body": json.dumps(results)}
            elif status == 'FAILED':
                # Query failed
                error = status_response.get('Error', 'Unknown error')
                return {"statusCode": 500, "body": json.dumps({"error": error})}
            elif status == 'ABORTED':
                return {"statusCode": 500, "body": json.dumps({"error": "Query was aborted"})}
            
            # Add a small delay before checking again
            time.sleep(0.5)
    
    except ClientError as e:
        error_message = e.response['Error']['Message']
        return {"statusCode": 500, "body": json.dumps({"error": error_message})}
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
                """
            ),
            timeout=Duration.seconds(29),
            environment={
                "REDSHIFT_WORKGROUP": redshift_workgroup,
                "REDSHIFT_DATABASE": redshift_database,
            },
        )

        # Grant Redshift Serverless and Redshift Data API access to Lambda
        redshift_serverless_arn = redshift_cluster_arn

        lambda_function.add_to_role_policy(
            iam.PolicyStatement(
                actions=[
                    "redshift-serverless:GetWorkgroup",
                    "redshift-serverless:ListWorkgroups",
                    "redshift-data:ExecuteStatement",
                    "redshift-data:DescribeStatement",
                    "redshift-data:GetStatementResult",
                    "redshift-data:ListStatements",
                    "redshift-data:CancelStatement",
                    "redshift-serverless:GetCredentials",
                ],
                resources=[redshift_serverless_arn, "*"],
            )
        )

        # Create API Gateway
        api = apigw.RestApi(
            self,
            "RedshiftApi",
            rest_api_name="Redshift API Service",
            endpoint_types=[apigw.EndpointType.REGIONAL],  # Specify REGIONAL endpoint
            deploy_options=apigw.StageOptions(
                stage_name="prod",
                logging_level=apigw.MethodLoggingLevel.INFO,
                data_trace_enabled=True,
                metrics_enabled=True,
            ),
        )

        # Create Cognito Authorizer specifically for the created app client
        auth = apigw.CognitoUserPoolsAuthorizer(
            self,
            "RedshiftApiAuthorizer",
            cognito_user_pools=[user_pool],
            authorizer_name="RedshiftApiCognitoAuthorizer",
            identity_source="method.request.header.Authorization",
        )

        # Create API Gateway integration with Lambda
        integration = apigw.LambdaIntegration(lambda_function)

        # Add a resource and method to the API Gateway with Cognito Authorizer and API Key
        api_resource = api.root.add_resource("api")
        api_resource.add_method(
            "POST",
            integration,
            authorizer=auth,
            authorization_type=apigw.AuthorizationType.COGNITO,
            authorization_scopes=[
                f"{resource_server.user_pool_resource_server_id}/redshift-api"
            ],
        )

        # Create IAM role for API Gateway to push logs to CloudWatch
        api_gateway_logging_role = iam.Role(
            self,
            "ApiGatewayLoggingRole",
            assumed_by=iam.ServicePrincipal("apigateway.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "service-role/AmazonAPIGatewayPushToCloudWatchLogs"
                )
            ],
        )

        # Create a log group for API Gateway
        api_log_group = logs.LogGroup(
            self, "ApiGatewayLogGroup", retention=logs.RetentionDays.ONE_WEEK
        )

        # Update the API's account settings to enable CloudWatch logging
        api_gateway_account = apigw.CfnAccount(
            self,
            "ApiGatewayAccount",
            cloud_watch_role_arn=api_gateway_logging_role.role_arn,
        )

        # Ensure the API Gateway account settings are updated before the API is created
        api.node.add_dependency(api_gateway_account)

        # Output the Cognito User Pool ID, App Client ID, Domain URL, API URL, and API Key
        CfnOutput(self, "UserPoolId", value=user_pool.user_pool_id)
        CfnOutput(self, "AppClientId", value=app_client.user_pool_client_id)
        CfnOutput(self, "TokenEndpoint", value=f"{domain.base_url()}/oauth2/token")
        CfnOutput(self, "ApiUrl", value=api.url)


if __name__ == "__main__":
    app = cdk.App()
    description = "Serverlessland Pattern for Redshift Data API. (uksb-1tthgi812) (tag:apigw-lambda-redshiftdataapi)"
    ApigwRedshiftDataApi(app, "ApigwRedshiftDataApi",description=description)
    app.synth()
