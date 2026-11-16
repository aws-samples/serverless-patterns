from constructs import Construct
import aws_cdk.aws_apigateway as apigateway
import aws_cdk.aws_iam as iam
import os

class ApiGatewayConstruct(Construct):
    def __init__(self, scope: Construct, id: str, cognito_construct, dynamodb_construct, lambda_construct, vtl_dir ,**kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.vtl_dir = vtl_dir

        # Define the Cognito Authorizer
        cognito_authorizer = apigateway.CognitoUserPoolsAuthorizer(self, "CognitoAuthorizer",
            cognito_user_pools=[cognito_construct.user_pool]
        )

        # Define lambda authorizer
        lambda_authorizer = apigateway.RequestAuthorizer(self, "LambdaAuthorizer",
            handler=lambda_construct.lambda_function,
            identity_sources=[apigateway.IdentitySource.header("Authorization")]
        )

        # Create IAM role
        api_gateway_role = iam.Role(self, "ApiGatewayDynamoDBRole",
            assumed_by=iam.ServicePrincipal("apigateway.amazonaws.com"),
            inline_policies={
                "DynamoDBAccess": iam.PolicyDocument(
                    statements=[
                        iam.PolicyStatement(
                            actions=["dynamodb:PutItem","dynamodb:DeleteItem", "dynamodb:Scan", "dynamodb:Query", "dynamodb:DescribeTable"],
                            resources=[dynamodb_construct.table.table_arn]
                        )
                    ]
                )
            }
        )

        # Define API Gateway
        self.api = apigateway.RestApi(self, "MyApi",
            rest_api_name="My Service",
            description="This service serves my DynamoDB table.",
            cloud_watch_role=True,
            deploy_options=apigateway.StageOptions(
                stage_name="prod",
                logging_level=apigateway.MethodLoggingLevel.INFO,
                data_trace_enabled=True,
                metrics_enabled=True,
                variables={
                    "TableName": dynamodb_construct.table.table_name}
            )
        )

        # Change default response for Bad Request Body
        self.api.add_gateway_response(
            "BadRequestBody",
            type=apigateway.ResponseType.BAD_REQUEST_BODY,
            templates={
                "application/json": '{"message": "Invalid Request Body: $context.error.validationErrorString"}'
            }
        )

        # Create request model schema
        request_model_schema = apigateway.JsonSchema(
            type=apigateway.JsonSchemaType.OBJECT,
            required=["ID","FirstName", "Age"],
            properties={
                "ID": {"type": apigateway.JsonSchemaType.STRING},
                "FirstName": {"type": apigateway.JsonSchemaType.STRING},
                "Age": {"type": apigateway.JsonSchemaType.NUMBER}
            },
            # Allow to send additional properites - handled in putItem.vtl to construct them to the request
            additional_properties=True
        )

        # Create a request validator
        request_validator = apigateway.RequestValidator(self, "RequestValidator",
            rest_api=self.api,
            validate_request_body=True,
            validate_request_parameters=False
        )

        # Create the request model
        request_model = apigateway.Model(self, "RequestModel",
            rest_api=self.api,
            content_type="application/json",
            schema=request_model_schema,
            model_name="PutObjectRequestModel"
        )

        # Create integration request
        integration_request = apigateway.AwsIntegration(
            service="dynamodb",
            action="PutItem",
            options=apigateway.IntegrationOptions(
                credentials_role=api_gateway_role,
                request_templates={
                    "application/json": 
                    self.get_vtl_template("putItem.vtl")
                },
                integration_responses=[
                    apigateway.IntegrationResponse(
                        status_code="200",
                        response_templates={
                            "application/json": self.get_vtl_template("response.vtl")
                        }
                    ),
                ]
            )
        )

        # Create a resource and method for the API Gateway
        put_resource = self.api.root.add_resource("put")
        self.put_method = put_resource.add_method(
            "POST",
            integration_request,
            authorization_type=apigateway.AuthorizationType.CUSTOM,
            authorizer=lambda_authorizer,
            request_validator=request_validator,
            request_models={"application/json": request_model},
            method_responses=[
                apigateway.MethodResponse(status_code="200",response_models={
                        "application/json": apigateway.Model.EMPTY_MODEL
                    }   ),
            ]
        )

        # Add GET method with response mapping
        get_integration = apigateway.AwsIntegration(
            service="dynamodb",
            action="Scan",
            options=apigateway.IntegrationOptions(
                credentials_role=api_gateway_role,
                request_templates={
                    "application/json": self.get_vtl_template('scan_request.vtl')
                },
                integration_responses=[
                    apigateway.IntegrationResponse(
                        status_code="200",
                        response_templates={
                            "application/json": self.get_vtl_template('scan.vtl')
                        }
                    ),
                ]
            )
        )

        get_resource = self.api.root.add_resource('get')
        self.get_method = get_resource.add_method(
            "GET", get_integration,
            api_key_required=True,
            method_responses=[
                apigateway.MethodResponse(
                    status_code="200",
                    response_models={
                        "application/json": apigateway.Model.EMPTY_MODEL
                    }
                ),
            ]
        )

        delete_resource = self.api.root.add_resource('delete')
        delete_resource_id = delete_resource.add_resource('{id}')
        self.delete_method = delete_resource_id.add_method(
            "POST",
            apigateway.AwsIntegration(
                service="dynamodb",
                action="DeleteItem",
                options=apigateway.IntegrationOptions(
                    credentials_role=api_gateway_role,
                    request_templates={
                        "application/json": 
                        self.get_vtl_template("deleteItem.vtl")
                    },
                    integration_responses=[
                        apigateway.IntegrationResponse(
                            status_code="200",
                            response_templates={
                                "application/json": '{"message": "Item deleted"}'
                            }
                        ),
                    ]
                )
            ),
            authorization_type=apigateway.AuthorizationType.COGNITO,
            authorizer=cognito_authorizer,
            request_validator=request_validator,
            method_responses=[
                apigateway.MethodResponse(
                    status_code="200",
                    response_models={
                        "application/json": apigateway.Model.EMPTY_MODEL
                    }
                ),
            ]
        )


    def get_vtl_template(self, filename: str) -> str:
        """
        Reads a VTL template from a file and returns its contents as a string.
        """
        template_path = os.path.join(self.vtl_dir, filename)
        with open(template_path, "r") as f:
            return f.read()
