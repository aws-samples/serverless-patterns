from aws_cdk import core as cdk
from aws_cdk import aws_lambda
from aws_cdk import aws_iam as iam
from aws_cdk import aws_logs as logs

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


class LambdaSnsSmsCdkStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        phoneNumber = core.CfnParameter(self, "phoneNumber", type="String",
                                        description="Recipient phone number")
        tenDLC = core.CfnParameter(self, "tenDLC", type="String",
                                   description="10DLC origination number")

        # We create a log group so it will be gracefully cleaned up on a destroy event.  By default
        # logs never expire and won't be removed.
        lambdaLogGroup = logs.LogGroup(self,
                                       'SMSPublisherFunctionLogGroup',
                                       log_group_name='/aws/lambda/SMSPublisherFunction',
                                       removal_policy=core.RemovalPolicy.DESTROY,
                                       retention=logs.RetentionDays.FIVE_DAYS,
                                       )

        SMSPublisherFunction = aws_lambda.Function(self,
                                                   'SMSPublisherFunction',
                                                   code=aws_lambda.Code.from_asset('src'),
                                                   function_name='SMSPublisherFunction',
                                                   handler='app.handler',
                                                   runtime=aws_lambda.Runtime.NODEJS_12_X,
                                                   timeout=core.Duration.seconds(3),
                                                   memory_size=128,
                                                   environment={'phoneNumber': phoneNumber.value_as_string,
                                                                'tenDLC': tenDLC.value_as_string},
                                                   initial_policy=[
                                                       iam.PolicyStatement(
                                                           actions=['sns:Publish'],
                                                           effect=iam.Effect.DENY,
                                                           resources=['arn:aws:sns:*:*:*']
                                                       ),
                                                       iam.PolicyStatement(
                                                           actions=['sns:Publish'],
                                                           effect=iam.Effect.ALLOW,
                                                           resources=['*']
                                                       )
                                                   ],
                                                   )
        # Make sure the log group is created prior to the function so CDK doesn't create a new one
        SMSPublisherFunction.node.add_dependency(lambdaLogGroup)

        core.CfnOutput(self,
                       'SMSPublisherFunctionName',
                       description='SMSPublisherFunction function name',
                       value=SMSPublisherFunction.function_name
                       )
