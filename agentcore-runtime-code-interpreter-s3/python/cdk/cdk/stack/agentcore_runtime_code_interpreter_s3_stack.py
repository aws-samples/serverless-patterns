import os

from aws_cdk import CfnOutput, Stack
from constructs import Construct

from l3_constructs.agent_runtime import AgentRuntime
from l3_constructs.code_interpreter import CodeInterpreter
from l3_constructs.document_bucket import DocumentBucket
from l3_constructs.document_file_system import DocumentFileSystem
from l3_constructs.function_logs import FunctionLogs
from l3_constructs.network import Network

AGENT_CODE_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "agent")
DOCUMENT_PREFIX = "demo/"
MOUNT_PATH = "/mnt/s3data"


class AgentCoreRuntimeCodeInterpreterS3Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        network = Network(
            self,
            "Network",
            # Optional Availability Zone IDs for the subnets, for example:
            #   cdk deploy -c availabilityZoneIds=usw2-az1,usw2-az2
            availability_zone_ids=self.node.try_get_context("availabilityZoneIds"),
        )

        document_bucket = DocumentBucket(self, "DocumentBucket")

        file_system = DocumentFileSystem(
            self,
            "DocumentFileSystem",
            bucket=document_bucket.bucket,
            prefix=DOCUMENT_PREFIX,
            vpc=network.vpc,
        )

        code_interpreter = CodeInterpreter(
            self,
            "CodeInterpreter",
            vpc=network.vpc,
            file_system=file_system,
        )

        agent_runtime = AgentRuntime(
            self,
            "AgentRuntime",
            agent_code_dir=AGENT_CODE_DIR,
            model_name="anthropic.claude-sonnet-5-5",
            code_interpreter=code_interpreter,
            file_system=file_system,
            mount_path=MOUNT_PATH,
        )

        FunctionLogs(self, "FunctionLogs")

        CfnOutput(self, "AgentRuntimeArn", value=agent_runtime.agent_runtime_arn)
        CfnOutput(self, "AgentLogGroupName", value=agent_runtime.log_group_name)
        CfnOutput(self, "DocumentBucketName", value=document_bucket.bucket.bucket_name)
