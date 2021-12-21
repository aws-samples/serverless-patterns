
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_efs as efs
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_apigatewayv2 as api_gateway
from aws_cdk import aws_apigatewayv2_integrations as integrations

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


class LambdaEfsCdkStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

    
        _vpc = ec2.Vpc(self, 'theVpc', max_azs=2)

        _fs = efs.FileSystem(self, 'theFileSystem', vpc=_vpc, removal_policy=core.RemovalPolicy.DESTROY)

        _access_point = _fs.add_access_point('theAccessPoint', 
                                            create_acl=efs.Acl(owner_gid='1001', owner_uid='1001', permissions='750'),
                                            path="/export/lambda",
                                            posix_user=efs.PosixUser(gid="1001",uid="1001"))

        _efs_lambda = _lambda.Function(self, 'lambdaEfsHandler',
                                    runtime = _lambda.Runtime.PYTHON_3_8,
                                    code = _lambda.Code.asset('lambda_function'),
                                    handler='lambda_function.lambda_handler',
                                    vpc = _vpc,
                                    filesystem= _lambda.FileSystem.from_efs_access_point(_access_point,'/mnt/text'))

        _api = api_gateway.HttpApi(self, 'EFS LAMBDA APIGATEWAY',
                                default_integration=integrations.LambdaProxyIntegration(handler=_efs_lambda))

        core.CfnOutput(self, 'API Url', value=_api.url)