from constructs import Construct
from aws_cdk import (
    App, Stack,
    CfnOutput,
    Duration,
    RemovalPolicy,
    SecretValue,
    aws_s3 as s3,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as origins,
    aws_secretsmanager as secretsmanager,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    aws_iam as iam,
    aws_cognito as cognito,
)
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

class CloudFrontSignedCookiesStack(Stack):
    """CDK Stack for CloudFront signed cookies pattern."""

    def __init__(self, scope: Construct, construct_id: str, user_pool=None, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # ============================================================
        # Context Variables / Configuration
        # Important to mention that wildcards should only be used for development purposes
        allowed_cors_origin = self.node.try_get_context("allowed_cors_origin") or "*"
        cookie_domain = self.node.try_get_context("cookie_domain") or ""
        same_site = self.node.try_get_context("same_site") or "None"
        cookie_ttl_seconds = int(self.node.try_get_context("cookie_ttl_seconds") or "600")

        # ============================================================
        # Cognito User Pool
        # ============================================================
        user_pool = cognito.UserPool(
            self,
            "UserPool",
            user_pool_name="UserPool",
            auto_verify=cognito.AutoVerifiedAttrs(email=True),
            sign_in_aliases=cognito.SignInAliases(email=True),
            self_sign_up_enabled=True,
            password_policy=cognito.PasswordPolicy( # Enable symbol requirement and increase minimum length to 12 characters for non dev/test environments
                min_length=8,
                require_lowercase=True,
                require_uppercase=True,
                require_digits=True,
                require_symbols=False,
            ),
            standard_attributes=cognito.StandardAttributes(
                email=cognito.StandardAttribute(required=True, mutable=True),
            ),
            removal_policy=RemovalPolicy.DESTROY,
        )

        user_pool_client = cognito.UserPoolClient(
            self,
            "UserPoolClient",
            user_pool=user_pool,
            user_pool_client_name="WebApp",
            generate_secret=False,
            auth_flows=cognito.AuthFlow(
                user_srp=True,
                user_password=True,
                custom=False,
                admin_user_password=False,
            ),
            prevent_user_existence_errors=True,
        )

        # ============================================================
        # S3 Bucket for Private Assets
        # ============================================================
        private_assets_bucket = s3.Bucket(
            self,
            "PrivateAssetsBucket",
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            encryption=s3.BucketEncryption.S3_MANAGED,
            enforce_ssl=True,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
            versioned=False,
        )

        # ============================================================
        # CloudFront Origin Access Control (OAC)
        # ============================================================
        oac = cloudfront.CfnOriginAccessControl(
            self,
            "S3OriginAccessControl",
            origin_access_control_config=cloudfront.CfnOriginAccessControl.OriginAccessControlConfigProperty(
                name=f"{construct_id}-S3-OAC",
                origin_access_control_origin_type="s3",
                signing_behavior="always",
                signing_protocol="sigv4",
                description="OAC for private S3 bucket access via CloudFront",
            ),
        )

        # ============================================================
        # CloudFront Public Key and Key Group
        # ============================================================
        # Generate private key
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        
        # Serialize private key to PEM format
        private_key_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ).decode('utf-8')
        
        # Extract public key and serialize to PEM format
        public_key = private_key.public_key()
        public_key_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode('utf-8')

        cf_public_key = cloudfront.PublicKey(
            self,
            "CloudFrontPublicKey",
            encoded_key=public_key_pem,
            comment="Public key for CloudFront signed cookies",
        )

        cf_key_group = cloudfront.KeyGroup(
            self,
            "CloudFrontKeyGroup",
            items=[cf_public_key],
            comment="Key group for signed cookie validation",
        )

        # ============================================================
        # Secrets Manager - Private Key Storage
        # ============================================================
        private_key_secret = secretsmanager.Secret(
            self,
            "CloudFrontPrivateKeySecret",
            description="CloudFront private key for signing cookies (PEM format)",
            secret_string_value=SecretValue.unsafe_plain_text(private_key_pem),
            removal_policy=RemovalPolicy.DESTROY,
        )

        # ============================================================
        # CloudFront Distribution
        # ============================================================
        # Create the S3 origin without OAC first (we'll add OAC via escape hatch)
        s3_origin = origins.S3BucketOrigin.with_origin_access_control(
            private_assets_bucket
        )

        # Default behavior - public content (no signed cookies required)
        default_behavior = cloudfront.BehaviorOptions(
            origin=s3_origin,
            viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
            allowed_methods=cloudfront.AllowedMethods.ALLOW_GET_HEAD,
            cached_methods=cloudfront.CachedMethods.CACHE_GET_HEAD,
            cache_policy=cloudfront.CachePolicy.CACHING_OPTIMIZED,
            compress=True,
        )

        # Private behavior - requires signed cookies
        private_behavior = cloudfront.BehaviorOptions(
            origin=s3_origin,
            viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
            allowed_methods=cloudfront.AllowedMethods.ALLOW_GET_HEAD,
            cached_methods=cloudfront.CachedMethods.CACHE_GET_HEAD,
            cache_policy=cloudfront.CachePolicy.CACHING_OPTIMIZED,
            compress=True,
            trusted_key_groups=[cf_key_group],
        )

        distribution = cloudfront.Distribution(
            self,
            "PrivateContentDistribution",
            default_behavior=default_behavior,
            additional_behaviors={
                "private/*": private_behavior,
            },
            comment="Distribution for private S3 content with signed cookies",
            price_class=cloudfront.PriceClass.PRICE_CLASS_100,
            enabled=True,
        )

        # ============================================================
        # Apply OAC to CloudFront Distribution (L1 escape hatch)
        # ============================================================
        cfn_distribution = distribution.node.default_child

        # Remove OAI configuration and add OAC
        cfn_distribution.add_property_override(
            "DistributionConfig.Origins.0.S3OriginConfig.OriginAccessIdentity", ""
        )
        cfn_distribution.add_property_override(
            "DistributionConfig.Origins.0.OriginAccessControlId", oac.attr_id
        )

        # ============================================================
        # S3 Bucket Policy for CloudFront OAC
        # ============================================================
        private_assets_bucket.add_to_resource_policy(
            iam.PolicyStatement(
                sid="AllowCloudFrontServicePrincipalReadOnly",
                effect=iam.Effect.ALLOW,
                principals=[iam.ServicePrincipal("cloudfront.amazonaws.com")],
                actions=["s3:GetObject"],
                resources=[private_assets_bucket.arn_for_objects("*")],
                conditions={
                    "StringEquals": {
                        "AWS:SourceArn": f"arn:aws:cloudfront::{self.account}:distribution/{distribution.distribution_id}"
                    }
                },
            )
        )

        # ============================================================
        # Lambdas
        # ============================================================
        # IAM Policies for Lambda functions to access Cognito
        register_cognito_policy = iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions=[
                "cognito-idp:SignUp",
                "cognito-idp:AdminConfirmSignUp",
            ],
            resources=[user_pool.user_pool_arn],
        )

        login_cognito_policy = iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions=[
                "cognito-idp:InitiateAuth",
            ],
            resources=[user_pool.user_pool_arn],
        )

        # Register User Lambda Function
        register_lambda = _lambda.Function(
            self,
            "RegisterUserLambda",
            runtime=_lambda.Runtime.PYTHON_3_12,
            handler="lambda_handler.handler",
            code=_lambda.Code.from_asset(
                "./lambda/Register",
                bundling={
                    "image": _lambda.Runtime.PYTHON_3_12.bundling_image,
                    "command": ["bash", "-c", "pip install aws-lambda-powertools -t /asset-output && cp -r . /asset-output"],
                },
            ),
            environment={
                "POWERTOOLS_SERVICE_NAME": "authentication",
                "USER_POOL_ID": user_pool.user_pool_id,
                "USER_POOL_CLIENT_ID": user_pool_client.user_pool_client_id,
                "ALLOWED_ORIGIN": allowed_cors_origin,
            },
            timeout=Duration.seconds(30),
        )
        register_lambda.add_to_role_policy(register_cognito_policy)

        # Login User Lambda Function
        login_lambda = _lambda.Function(
            self,
            "LoginUserLambda",
            runtime=_lambda.Runtime.PYTHON_3_12,
            handler="lambda_handler.handler",
            code=_lambda.Code.from_asset(
                "./lambda/Login",
                bundling={
                    "image": _lambda.Runtime.PYTHON_3_12.bundling_image,
                    "command": [
                        "bash",
                        "-lc",
                        "pip install --platform manylinux2014_x86_64 --only-binary=:all: --no-cache-dir --upgrade "
                        "-t /asset-output aws-lambda-powertools 'cryptography>=41' 'PyJWT[crypto]>=2.11.0' "
                        "&& cp -au . /asset-output"
                    ],
                },

            ),
            environment={
                "POWERTOOLS_SERVICE_NAME": "authentication",
                "USER_POOL_ID": user_pool.user_pool_id,
                "USER_POOL_CLIENT_ID": user_pool_client.user_pool_client_id,
                "ALLOWED_ORIGIN": allowed_cors_origin,
                "PRIVATE_KEY_SECRET_ARN": private_key_secret.secret_arn,
                "CLOUDFRONT_DOMAIN": distribution.distribution_domain_name,
                "KEY_PAIR_ID": cf_public_key.public_key_id,
                "COGNITO_REGION": self.region,
                "COOKIE_TTL_SECONDS": str(cookie_ttl_seconds),
                "COOKIE_DOMAIN": cookie_domain,
                "COOKIE_SAME_SITE": same_site,
            },
            timeout=Duration.seconds(30),
            memory_size=256,
        )
        login_lambda.add_to_role_policy(login_cognito_policy)
        private_key_secret.grant_read(login_lambda)

        # ============================================================
        # API Gateway REST API
        # ============================================================
        api = apigw.RestApi(
            self,
            "AuthApi",
            rest_api_name="Auth and Cookie API",
            description="API for authentication and CloudFront signed cookies",
            deploy=True,
            deploy_options=apigw.StageOptions(stage_name="v1"),
            default_cors_preflight_options=apigw.CorsOptions(
                allow_origins=[allowed_cors_origin] if allowed_cors_origin != "*" else apigw.Cors.ALL_ORIGINS,
                allow_methods=["POST", "OPTIONS"],
                allow_headers=["Content-Type", "Authorization", "X-Amz-Date", "X-Api-Key"],
                allow_credentials=True,
            ),
        )

        # API Gateway Lambda Integration
        register_integration = apigw.LambdaIntegration(register_lambda)
        login_integration = apigw.LambdaIntegration(login_lambda)

        # API Gateway Resources and Methods
        api.root.add_resource("register").add_method("POST", register_integration)
        api.root.add_resource("login").add_method("POST", login_integration)


        # ============================================================
        # Outputs
        # ============================================================
        CfnOutput(
            self,
            "CloudFrontDistributionId",
            description="CloudFront Distribution ID",
            value=distribution.distribution_id,
        )

        CfnOutput(
            self,
            "ApiEndpoint",
            description="API Gateway Endpoint URL",
            value=api.url,
            export_name=f"{construct_id}-ApiEndpoint",
        )

        CfnOutput(
            self,
            "RegisterEndpoint",
            description="Register Lambda API Endpoint",
            value=f"{api.url}register",
        )

        CfnOutput(
            self,
            "LoginEndpoint",
            description="Login Lambda API Endpoint",
            value=f"{api.url}login",
        )

        CfnOutput(
            self,
            "CLOUDFRONT_DOMAIN",
            description="CloudFront Distribution URL",
            value=f"https://{distribution.distribution_domain_name}",
        )

        CfnOutput(
            self,
            "BUCKET_NAME",
            description="S3 Bucket Name",
            value=private_assets_bucket.bucket_name,
        )

app = App()
CloudFrontSignedCookiesStack(app, "CloudFrontSignedCookiesStack")
app.synth()
