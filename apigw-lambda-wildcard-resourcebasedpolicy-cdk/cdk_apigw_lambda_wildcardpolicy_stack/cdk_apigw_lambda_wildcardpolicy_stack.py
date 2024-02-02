from constructs import Construct
from aws_cdk import (
    Stack,
    aws_apigateway as apigateway,
    aws_lambda as _lambda,
    aws_iam as iam
)
from aws_cdk.aws_lambda import CfnPermission

class CdkApigwLambdaWildCardPolicyStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # Create a Lambda function
        lambda_function = _lambda.Function(self, 'CDKFunction',runtime=_lambda.Runtime.PYTHON_3_11,handler='appfunc.handler',code=_lambda.Code.from_asset('function'))
        
        # Create an API Gateway REST API
        api = apigateway.RestApi(self, 'CDKAPI', rest_api_name='CDKAPI', default_integration=LambdaIntegrationNoPermission(lambda_function))
        lambda_function.add_permission(id='1', principal=iam.ServicePrincipal('apigateway.amazonaws.com'), action='lambda:InvokeFunction', source_arn=f'arn:aws:execute-api:{self.region}:{self.account}:{api.rest_api_id}/*/*/*')
        
        # Create resources and associate the Lambda integration without resource-based policy creation
        resource = api.root.add_resource('resource1')
        resource.add_method('GET', LambdaIntegrationNoPermission(lambda_function))
        resource = api.root.add_resource('resource2')
        resource.add_method('POST', LambdaIntegrationNoPermission(lambda_function))
        resource = api.root.add_resource('resourceN')
        resource.add_method('POST', LambdaIntegrationNoPermission(lambda_function))
        

class LambdaIntegrationNoPermission(apigateway.LambdaIntegration):
    def __init__(self, handler, **kwargs):
        super().__init__(handler, **kwargs)
    def bind(self, method: apigateway.Method):
        integration_config = super().bind(method)
        permissions = filter(lambda x: isinstance(x, CfnPermission), method.node.children)
        # Removing permissions policy for each integration
        for p in permissions:
            method.node.try_remove_child(p.node.id)
        return integration_config
