from constructs import Construct
import aws_cdk.aws_cognito as cognito


class UserPoolGroupConstruct(Construct):
    def __init__(self, scope: Construct, id: str, cognito_construct, group_name, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        # Create user pool group. 
        # Required parameters - 
        # 1. User pool ID - taken from the cofnito construct
        # 2. Group name - taken from the stack context
        cognito.CfnUserPoolGroup(self, group_name,
            user_pool_id=cognito_construct.user_pool.user_pool_id,
            group_name=group_name,
            description=f"Group created {group_name}",
            precedence=1
        )

