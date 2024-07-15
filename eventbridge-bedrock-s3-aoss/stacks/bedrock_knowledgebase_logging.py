from aws_cdk import (
    Duration,
    Stack,
    aws_iam as iam,
    aws_lambda as _lambda,
    aws_scheduler as scheduler,
    aws_sqs as sqs,
    aws_logs as logs,
)
from constructs import Construct

class KnowledgeBaseLoggingStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, stack_suffix,
                 knowledge_base_id,
                 **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        cfn_log_group = logs.CfnLogGroup(self, "MyCfnLogGroup",
            log_group_name=f"BedrockKnowledgeBase-{knowledge_base_id}",
            retention_in_days=14,
        )

        delivery_source_name = "bedrock_kb_log_delivery_source"

        cfn_delivery_destination = logs.CfnDeliveryDestination(self, "BedrockKBDeliveryDestination",
            name="BedrockKBDeliveryDestination",
            destination_resource_arn=cfn_log_group.attr_arn
        )
        cfn_delivery_source = logs.CfnDeliverySource(self, "BedrockKBDeliverySource",
            name=delivery_source_name,
            log_type="APPLICATION_LOGS",
            resource_arn=f"arn:aws:bedrock:{self.region}:{self.account}:knowledge-base/{knowledge_base_id}"
        )
        
        cfn_delivery = logs.CfnDelivery(self, "BedrockKBDelivery",
            delivery_destination_arn=cfn_delivery_destination.attr_arn,
            delivery_source_name=cfn_delivery_source.name,
        )
