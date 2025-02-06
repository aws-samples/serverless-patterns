from aws_cdk import Stack
from aws_cdk import CfnOutput
from constructs import Construct

from apigw_dynamodb_python_cdk.api_key_usage_plan_construct import UsagePlanConstruct
from apigw_dynamodb_python_cdk.apigateway_construct import ApiGatewayConstruct
from apigw_dynamodb_python_cdk.cognito_construct import CognitoConstruct
from apigw_dynamodb_python_cdk.dynamodb_construct import DynamoDBConstruct
from apigw_dynamodb_python_cdk.lambda_construct import LambdaConstruct
from apigw_dynamodb_python_cdk.user_pool_group_construct import UserPoolGroupConstruct

class ApigwDynamodbPythonStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        vtl_dir = self.node.try_get_context("vtl_dir")
        

        lambda_construct = LambdaConstruct(self, "LambdaConstruct")
        cognito_construct = CognitoConstruct(self, "CognitoConstruct")
        dynamodb_construct = DynamoDBConstruct(self, "DynamoDBConstruct")
        # Passing full construct is an option, specific ID can be used - Example: dynamodb_construct.table.table_arn
        apigateway_construct = ApiGatewayConstruct(self, "ApiGatewayConstruct", cognito_construct, dynamodb_construct, lambda_construct, vtl_dir)
        
        # Using the context defined in app.py to iterate and create multiple resources
        group_names = self.node.try_get_context("group_names")
        if group_names:
            for group_name in group_names:
                UserPoolGroupConstruct(
                    self,
                    f"UserPoolGroup{group_name}Construct",
                    cognito_construct,
                    group_name
                )


        api_key_ids = []
        usage_plans = self.node.try_get_context("usage_plans")
        if usage_plans:
            for usage_plan_name, usage_plan_config in usage_plans.items():
                use_plan_construct = UsagePlanConstruct(
                    self,
                    f"ApiGateway{usage_plan_name}Construct",
                    apigateway_construct,
                    usage_plan_name,
                    usage_plan_config
                )
                api_key_ids.append(use_plan_construct.api_key_id)

        for index, api_key_id in enumerate(api_key_ids):
            CfnOutput(self, f"ApiKeyId{index}", value=api_key_id)
        # Outputs - used also by the tests
        CfnOutput(self, "CognitoUserPoolId", value=cognito_construct.user_pool.user_pool_id)
        CfnOutput(self, "CognitoClientId", value=cognito_construct.user_pool_client.user_pool_client_id)
        CfnOutput(self, "ApiUrl", value=apigateway_construct.api.url)
        CfnOutput(self, "DynamoDBTableName", value=dynamodb_construct.table.table_name)

