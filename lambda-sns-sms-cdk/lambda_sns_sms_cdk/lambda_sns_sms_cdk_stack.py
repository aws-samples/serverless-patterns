from aws_cdk import (
    Stack,
    RemovalPolicy,
    Duration,
    CfnParameter,
    CfnOutput,
    aws_lambda,
    aws_iam as iam,
    aws_logs as logs
)
from constructs import Construct


class LambdaSnsSmsCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        phoneNumber = CfnParameter(self, "phoneNumber", type="String",
                                        description="Recipient phone number")
        tenDLC = CfnParameter(self, "tenDLC", type="String",
                                   description="10DLC origination number")

        # We create a log group so it will be gracefully cleaned up on a destroy event.  By default
        # logs never expire and won't be removed.
        lambdaLogGroup = logs.LogGroup(self,
                                       'SMSPublisherFunctionLogGroup',
                                       log_group_name='/aws/lambda/SMSPublisherFunction',
                                       removal_policy=RemovalPolicy.DESTROY,
                                       retention=logs.RetentionDays.FIVE_DAYS,
                                       )

        SMSPublisherFunction = aws_lambda.Function(self,
                                                   'SMSPublisherFunction',
                                                   code=aws_lambda.Code.from_asset('src'),
                                                   function_name='SMSPublisherFunction',
                                                   handler='app.handler',
                                                   runtime=aws_lambda.Runtime.NODEJS_12_X,
                                                   timeout=Duration.seconds(3),
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

        CfnOutput(self,
                       'SMSPublisherFunctionName',
                       description='SMSPublisherFunction function name',
                       value=SMSPublisherFunction.function_name
                       )
