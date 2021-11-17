from aws_cdk import (
    core as cdk,
    aws_stepfunctions as sfn,
    aws_stepfunctions_tasks as sfn_tasks,
    aws_iam as iam
)


class SfnComprehendSdkStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        detect_sentiment_task = sfn_tasks.CallAwsService(self, "DetectSentiment", service="comprehend",
                                                         action="detectSentiment", iam_resources=["*"],
                                                         parameters={"Text": "$.text", "LanguageCode": "en"})

        definition = detect_sentiment_task
        state_machine = sfn.StateMachine(
            self, "DetectSentimentStateMachine",
            definition=definition,
            timeout=cdk.Duration.minutes(5)
        )

        cdk.CfnOutput(scope=self, id='StateMachineArn',
                      value=state_machine.state_machine_arn)
