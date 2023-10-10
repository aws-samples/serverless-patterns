from aws_cdk import (
    Stack,
    aws_sns as sns,
    aws_sns_subscriptions as subscriptions,
    aws_events as events,
    aws_rds as rds,
    aws_iam as iam,
    CfnParameter,
    CfnOutput,
    Fn
)
from constructs import Construct


class RdsSnsEventNotificationCdkPythonStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # Parameters
        sns_endpoint = CfnParameter(self, "SNSEndpoint", type="String", description="Provide your email address to receive notification from SNS")
        rds_instance_name = CfnParameter(self, "RDSInstanceName", type="String", description="Provide name of your existing RDS Instance for which you want to receive event notifications")
        # SNS Topic for RDS Event Subscription
        topic = sns.Topic(self, "SnsForRdsEventSubscription", display_name="rds-subscription-topic")
        aws_account_id = Fn.ref("AWS::AccountId")
        # SNS Topic Policy
        topic_policy = sns.TopicPolicy(
            self,
            "SnsTopicPolicyEventRule",
            topics=[topic]
        )
        topic_policy.document.add_statements(iam.PolicyStatement(
            actions=[
                "SNS:GetTopicAttributes",
                "SNS:SetTopicAttributes",
                "SNS:AddPermission",
                "SNS:RemovePermission",
                "SNS:DeleteTopic",
                "SNS:Subscribe",
                "SNS:ListSubscriptionsByTopic",
                "SNS:Publish",
                "SNS:Receive"
                ],
            principals=[iam.AccountPrincipal(aws_account_id)],
            resources=[topic.topic_arn],
            conditions={
                        "StringEquals": {
                            "aws:SourceOwner": aws_account_id
                        }
                    }
        ),
        iam.PolicyStatement(
                    effect=iam.Effect.ALLOW,
                    actions=["sns:Publish"],
                    resources=[topic.topic_arn],
                    principals=[iam.ServicePrincipal("events.rds.amazonaws.com")]
                )
        )
        topic.add_subscription(subscriptions.EmailSubscription(sns_endpoint.value_as_string, json=True))
        # RDS Event Subscription
        rds_event_subscription = rds.CfnEventSubscription(
            self,
            "RdsEventSubscription",
            enabled=True,
            sns_topic_arn=topic.topic_arn,
            source_ids=[rds_instance_name.value_as_string],
            source_type="db-instance",
            event_categories=["failure", "low storage", "availability"]
        )
        # Outputs
        CfnOutput(self, "MySnsTopicName", value=topic.topic_name, description="SNS topic name")
        CfnOutput(self, "RDSInstanceNames", value=rds_instance_name.value_as_string)