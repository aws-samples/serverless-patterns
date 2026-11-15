import aws_cdk as cdk
from constructs import Construct
import aws_cdk.aws_cognito as cognito


class CognitoConstruct(Construct):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create Cognito user pool
        self.user_pool = cognito.UserPool(self, "MyUserPool",
            user_pool_name="my_user_pool",
            self_sign_up_enabled=True,
            auto_verify=cognito.AutoVerifiedAttrs(email=True),
            sign_in_aliases=cognito.SignInAliases(email=True),
            standard_attributes={
                "email": {
                    "required": True,
                    "mutable": False
                }
            },
            removal_policy=cdk.RemovalPolicy.DESTROY
        )

        # Create user pool client
        self.user_pool_client = cognito.UserPoolClient(self, "UserPoolClient",
            user_pool=self.user_pool,
            generate_secret=False,
            auth_flows=cognito.AuthFlow(
                user_password=True,
                admin_user_password=True,
                # user_srp=True,
            ),
            o_auth=cognito.OAuthSettings(
                callback_urls=["http://localhost"],
                flows=cognito.OAuthFlows(
                    authorization_code_grant=True
                ),
                scopes=[
                    cognito.OAuthScope.EMAIL,
                    cognito.OAuthScope.OPENID,
                    cognito.OAuthScope.COGNITO_ADMIN
                ]
            ),
            supported_identity_providers=[cognito.UserPoolClientIdentityProvider.COGNITO]
        )

        # Define the user pool domain
        cognito.UserPoolDomain(self, "UserPoolDomain_",
            user_pool=self.user_pool,
            cognito_domain=cognito.CognitoDomainOptions(
                domain_prefix="a1faegn"  # This must be unique across all AWS accounts and regions
            )
        )
