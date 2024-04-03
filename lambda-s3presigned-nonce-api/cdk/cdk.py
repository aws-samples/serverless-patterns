from aws_cdk import (
    aws_apigateway as apigateway,
    aws_dynamodb as dynamodb,
    aws_iam as iam,
    aws_lambda as lambda_,
    aws_s3 as s3,
    aws_s3_deployment  as s3deploy,
    Duration,
    Aws,
    Stack,
    RemovalPolicy,
    CfnOutput
)
from constructs import Construct


class PreSignedURLStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)


    # Create a new S3 bucket for testing
        bucket = s3.Bucket(
            self,
            "MyBucket",

            encryption=s3.BucketEncryption.S3_MANAGED,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=RemovalPolicy.DESTROY,  # This will delete the bucket when the stack is deleted (for demo purposes)
        )

        CfnOutput(self, 'BucketUrl', value=bucket.bucket_name)
                  
        s3deploy.BucketDeployment(self, 'UploadFile', 
                                  sources=[s3deploy.Source.asset('test')],
                                  destination_bucket=bucket)

        # DynamoDB(DDB) table for storing nonce
        nonce_table = dynamodb.Table(
            self,
            "NonceTable",
            partition_key=dynamodb.Attribute(
                name="nonce_id", type=dynamodb.AttributeType.STRING
            ),
            removal_policy=RemovalPolicy.DESTROY,  # This will delete the table when the stack is deleted (for demo purposes)
        )

        # Content Bucket
        # bucket = s3.Bucket.from_bucket_name(self, "MyBucket", "test-s3pre")

        # Lambda function for generating S3 Presigned URL and adding nonce to DynamoDB
        generate_url_lambda = self.create_generate_url_lambda(nonce_table, bucket)

        # Lambda Authorizer function for validating nonce and allowing access to presigned URL
        validate_nonce_lambda = self.create_validate_nonce_lambda(nonce_table)

        # Lambda function to get the presigned URL from DDB, after nonce validation
        access_object_lambda = self.create_access_object_lambda(nonce_table)

        # Add API Gateway Authorizer
        auth = apigateway.RequestAuthorizer(
            self,
            "authapi",
            handler=validate_nonce_lambda,
            identity_sources=[apigateway.IdentitySource.query_string("nonce")],
        )

        # API Gateway
        api = apigateway.RestApi(self, "ApiGateway", rest_api_name="presignedurlApi")

        # Create a Method Response
        response = apigateway.MethodResponse(
            status_code="200",
            response_models={"application/json": apigateway.Model.EMPTY_MODEL},
            response_parameters={
                "method.response.header.Access-Control-Allow-Origin": True
            },
        )

        # Resource for generating presigned URL
        generate_url_integration = apigateway.LambdaIntegration(generate_url_lambda)
        generate_url_resource = api.root.add_resource("generate-url")
        postmethod = generate_url_resource.add_method(
            "POST",
            generate_url_integration,
            authorization_type=apigateway.AuthorizationType.IAM,
        )
        # add the method response to the above method
        postmethod.method_responses = [response]
        request_template =  {
           "application/json": "{ \"nonce\": \"$input.params(\"nonce\")\"}"
            }
        
        # create a list of integration options for including in the integration like request_templates
        integration_options = apigateway.IntegrationOptions(
            request_templates=request_template
        )

        integration_request = [
                    {
                        "integrationOptions": integration_options
                    }
                ]
        integration_response = [
            {
                "statusCode": "200",
            }
        ]

        access_object_integration = apigateway.LambdaIntegration(
            access_object_lambda,
            proxy=True,
            request_templates=request_template,
            integration_responses=integration_response
        )
        access_object_resource = api.root.add_resource("access-object")
        getmethod = access_object_resource.add_method(
            "GET", access_object_integration, authorizer=auth
        )

        #    add response to the get method
        getmethod.add_method_response(
            status_code="200"
        )

    def create_access_object_lambda(self, nonce_table):
        layer = lambda_.LayerVersion(
            self,
            "MyLayer",
            code=lambda_.Code.from_asset("lambda_layers/python_modules.zip"),
            compatible_runtimes=[lambda_.Runtime.PYTHON_3_11],
        )
        fn = lambda_.Function(
            self,
            "AccessObjectLambda",
            runtime=lambda_.Runtime.PYTHON_3_11,
            handler="lambda.lambda_handler",
            code=lambda_.Code.from_asset("function/accessobject"),
            layers=[layer],
            timeout=Duration.seconds(900),
            memory_size=1024,
        )

        # Grant DynamoDB read and write permissions to the Lambda function
        nonce_table.grant_read_write_data(fn)
        fn.add_environment("NONCE_TABLE", nonce_table.table_name)
        return fn

    def create_generate_url_lambda(self, nonce_table, bucket):

        fn = lambda_.Function(
            self,
            "GenerateUrlLambda",
            runtime=lambda_.Runtime.PYTHON_3_11,
            handler="lambda.lambda_handler",
            code=lambda_.Code.from_asset("function/getpresigned"),
            timeout=Duration.seconds(900),
            memory_size=1024,
        )
        fn.add_to_role_policy(
            statement=iam.PolicyStatement(
                actions=["s3:GetObject"],  # Add more actions as needed
                resources=[
                    bucket.arn_for_objects("*")
                ],  # Specify the ARN of the objects in the bucket
            )
        )

        # Grant DynamoDB write permissions to the Lambda function
        nonce_table.grant_read_write_data(fn)

        fn.add_environment("NONCE_TABLE", nonce_table.table_name)

        return fn

    def create_validate_nonce_lambda(self, nonce_table):
        fn = lambda_.Function(
            self,
            "ValidateNonceLambda",
            runtime=lambda_.Runtime.PYTHON_3_11,
            handler="lambda.lambda_handler",
            code=lambda_.Code.from_asset("function/validatenonce"),
            timeout=Duration.seconds(900),
        )

        # Grant DynamoDB read permissions to the Lambda function
        nonce_table.grant_read_data(fn)
        fn.add_environment("NONCE_TABLE", nonce_table.table_name)

        return fn
