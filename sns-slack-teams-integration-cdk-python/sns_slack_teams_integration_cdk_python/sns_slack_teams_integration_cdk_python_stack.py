from aws_cdk import (
    Duration,
    Stack,
    CfnOutput,
    aws_sns as sns,
    aws_sns_subscriptions as subscriptions,
    aws_lambda as _lambda
)
from constructs import Construct

class SnsSlackTeamsIntegrationCdkPythonStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Lambda function
        lambdaFn = _lambda.Function(self, "SlackTeamsIntegrationLambda",
                                    runtime=_lambda.Runtime.PYTHON_3_8,
                                    code=_lambda.Code.from_asset('lambda'),
                                    handler="lambda_function.lambda_handler", 
                                    timeout=Duration.seconds(10))

        # SNS topic
        topic = sns.Topic(self, "SlackTeamsIntegrationTopic", 
                          display_name="SlackTeamsIntegrationTopic")

        # Subscribe Lambda to SNS topic
        topic.add_subscription(subscriptions.LambdaSubscription(lambdaFn))

        # Output information about the created resources
        CfnOutput(self, 'snsTopicArn', 
                  value=topic.topic_arn, 
                  description='The ARN of the SNS topic')
        
        CfnOutput(self, 'functionName', value=lambdaFn.function_name, description="The name of the Lambda function")
