from aws_cdk import (
    Stack,
    aws_cognito as cognito,
    RemovalPolicy,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
    aws_iam as iam,
    aws_ssm as ssm,
    CfnOutput,
    Duration,
    BundlingOptions,
    Aws as aws,
)
from constructs import Construct
import os


class ApigwBedrockCognitoCdkStack(Stack):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        organization_domain: str,
        api_throttle_settings: dict,
        api_quota_settings: dict,
        stage_name: str = "prod",
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create and configure Cognito User Pool
        self.user_pool = self.create_user_pool()
        self.ssm_user_pool_id = self.store_in_parameter_store(
            f"/{construct_id}/user_pool/id", self.user_pool.user_pool_id, "UserPoolID"
        )

        # Output Cognito User Pool ID
        CfnOutput(self, "CognitoUserPoolID", value=self.user_pool.user_pool_id)

        # Create and configure Cognito User Pool Client
        self.user_pool_client = self.create_user_pool_client(self.user_pool)
        self.ssm_user_pool_client_id = self.store_in_parameter_store(
            f"/{construct_id}/user_pool/client_id",
            self.user_pool_client.user_pool_client_id,
            "UserPoolClientID",
        )

        # Create and configure REST API and Usage Plan
        self.rest_api = self.create_rest_api(stage_name)
        api_throttle_settings = self.create_throttle_constructor(api_throttle_settings)
        api_quota_settings = self.create_quota_constructor(api_quota_settings)
        self.api_usage_plan = self.create_usage_plan(
            api_throttle_settings, api_quota_settings
        )
        self.ssm_api_usage_plan_id = self.store_in_parameter_store(
            f"/{construct_id}/api/usage_plan/id",
            self.api_usage_plan.usage_plan_id,
            "APIUsagePlanID",
        )

        # Configure pre-sign-up Lambda function
        if organization_domain:
            self.create_pre_signup_lambda(organization_domain)

        # Create and configure Lambda function for authentication
        self.auth_lambda = self.create_lambda_function(
            "AuthFunc", "auth", environment={"CONSTRUCT_ID": construct_id}
        )
        self.add_permissions_to_lambda(
            self.auth_lambda,
            [
                "apigateway:POST",
                "ssm:GetParameter",
                "cognito-idp:AdminUpdateUserAttributes",
            ],
            [
                "*",
                f"arn:aws:ssm:{aws.REGION}:{aws.ACCOUNT_ID}:parameter/{construct_id}/*",
                f"arn:aws:cognito-idp:{aws.REGION}:{aws.ACCOUNT_ID}:userpool/{self.user_pool.user_pool_id}",
            ],
        )

        # Create and configure Lambda function for Bedrock interaction
        self.bedrock_lambda = self.create_lambda_function(
            "BedrockFunc",
            "bedrock",
            None,
            BundlingOptions(
                image=_lambda.Runtime.PYTHON_3_12.bundling_image,
                command=[
                    "bash",
                    "-c",
                    "pip install --no-cache -r requirements.txt -t /asset-output && cp -au . /asset-output",
                ],
            ),
        )
        self.add_permissions_to_lambda(
            self.bedrock_lambda,
            ["bedrock:ListFoundationModels", "bedrock:InvokeModel"],
            ["*"],
        )

        # Create API resources
        self.create_api_resources()

    # Method to create Cognito User Pool
    def create_user_pool(self):
        return cognito.UserPool(
            self,
            "UserPool",
            user_pool_name="UserPool",
            self_sign_up_enabled=True,
            sign_in_case_sensitive=False,
            mfa=cognito.Mfa.OFF,
            standard_attributes=cognito.StandardAttributes(
                fullname=cognito.StandardAttribute(required=True, mutable=True),
                email=cognito.StandardAttribute(required=True, mutable=True),
            ),
            custom_attributes={"api_key": cognito.StringAttribute(mutable=True)},
            removal_policy=RemovalPolicy.DESTROY,
        )

    # Method to create Cognito User Pool Client
    def create_user_pool_client(self, user_pool: cognito.UserPool):
        return cognito.UserPoolClient(
            self,
            "UserPoolClient",
            user_pool=user_pool,
            auth_flows=cognito.AuthFlow(
                user_password=True,
            ),
            refresh_token_validity=Duration.hours(1),
        )

    # Method to create pre-sign-up Lambda trigger
    def create_pre_signup_lambda(self, organization_domain):
        user_pool = self.user_pool
        user_pool.add_trigger(
            cognito.UserPoolOperation.PRE_SIGN_UP,
            self.create_lambda_function(
                "PreSignUpFunc",
                "pre_signup",
                {"ORGANIZATION_DOMAIN": organization_domain},
            ),
        )

    # Method to create Lambda function
    def create_lambda_function(
        self, func_id: str, handler: str, environment=None, bundle_options=None
    ):
        return _lambda.Function(
            self,
            func_id,
            runtime=_lambda.Runtime.PYTHON_3_12,
            code=_lambda.Code.from_asset(
                os.path.join("src", handler), bundling=bundle_options
            ),
            handler=f"{handler}.handler",
            environment=environment or {},
            timeout=Duration.seconds(29),
        )

    # Method to add permissions to Lambda function
    def add_permissions_to_lambda(self, lambda_function, actions, resources):
        lambda_function.add_to_role_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=actions,
                resources=resources,
            ),
        )

    # Method to create REST API
    def create_rest_api(self, stage_name):
        return apigateway.RestApi(
            self,
            "RestAPI",
            default_cors_preflight_options={
                "allow_origins": apigateway.Cors.ALL_ORIGINS,
                "allow_methods": apigateway.Cors.ALL_METHODS,
            },
            cloud_watch_role=True,
            cloud_watch_role_removal_policy=RemovalPolicy.DESTROY,
            deploy_options=apigateway.StageOptions(
                logging_level=apigateway.MethodLoggingLevel.INFO,
                stage_name=stage_name,
            ),
        )

    # Method to create API resources
    def create_api_resources(self):
        authorizer = apigateway.CognitoUserPoolsAuthorizer(
            self, "CognitoAuthorizer", cognito_user_pools=[self.user_pool]
        )

        register = self.rest_api.root.add_resource("register")
        register.add_method("POST", apigateway.LambdaIntegration(self.auth_lambda))

        login = self.rest_api.root.add_resource("login")
        login.add_method("POST", apigateway.LambdaIntegration(self.auth_lambda))

        bedrock = self.rest_api.root.add_resource("bedrock")
        bedrock.add_method(
            "ANY",
            apigateway.LambdaIntegration(self.bedrock_lambda),
            authorization_type=apigateway.AuthorizationType.COGNITO,
            authorizer=authorizer,
            api_key_required=True,
        )

    # Method to create API throttle settings
    def create_throttle_constructor(self, config: dict()):
        return apigateway.ThrottleSettings(
            rate_limit=config.get("rate_limit"),
            burst_limit=config.get("burst_limit"),
        )

    # Method to create API quota settings
    def create_quota_constructor(self, config: dict()):
        period = config.get("period").upper()
        if period == "DAY":
            period = apigateway.Period.DAY
        elif period == "WEEK":
            period = apigateway.Period.WEEK
        else:
            period = apigateway.Period.MONTH

        return apigateway.QuotaSettings(
            limit=config.get("limit"),
            period=period,
        )

    # Method to create API usage plan
    def create_usage_plan(
        self,
        throttle_settings: apigateway.ThrottleSettings = None,
        quota_settings: apigateway.QuotaSettings = None,
    ):
        return self.rest_api.add_usage_plan(
            "APIUsagePlan",
            api_stages=[
                apigateway.UsagePlanPerApiStage(stage=self.rest_api.deployment_stage)
            ],
            throttle=throttle_settings,
            quota=quota_settings,
        )

    # Method to store values in AWS Systems Manager Parameter Store
    def store_in_parameter_store(self, name, value, id):
        return ssm.StringParameter(self, id, parameter_name=name, string_value=value)
