
from aws_cdk import (
    Stack,
    CfnOutput,
    RemovalPolicy,
    aws_ec2 as ec2,
    aws_efs as efs,
    aws_lambda as _lambda
)
from constructs import Construct
import aws_cdk.aws_apigatewayv2_alpha as api_gateway
import aws_cdk.aws_apigatewayv2_integrations_alpha as integrations


class LambdaEfsCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

    
        _vpc = ec2.Vpc(self, 'theVpc', max_azs=2)

        _fs = efs.FileSystem(self, 'theFileSystem', vpc=_vpc, removal_policy=RemovalPolicy.DESTROY)

        _access_point = _fs.add_access_point('theAccessPoint', 
                                            create_acl=efs.Acl(owner_gid='1001', owner_uid='1001', permissions='750'),
                                            path="/export/lambda",
                                            posix_user=efs.PosixUser(gid="1001",uid="1001"))

        _efs_lambda = _lambda.Function(self, 'lambdaEfsHandler',
                                    runtime = _lambda.Runtime.PYTHON_3_8,
                                    code = _lambda.Code.from_asset('lambda_function'),
                                    handler='lambda_function.lambda_handler',
                                    vpc = _vpc,
                                    filesystem= _lambda.FileSystem.from_efs_access_point(_access_point,'/mnt/text'))

        _api = api_gateway.HttpApi(self, 'EFS LAMBDA APIGATEWAY',
                                default_integration=integrations.HttpLambdaIntegration(id="LambdaFunction",handler=_efs_lambda))

        CfnOutput(self, 'API Url', value=_api.url)