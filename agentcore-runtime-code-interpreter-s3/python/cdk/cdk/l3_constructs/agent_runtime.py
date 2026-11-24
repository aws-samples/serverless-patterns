from aws_cdk import (
    Aws,
    BundlingOptions,
    DockerImage,
    RemovalPolicy,
    aws_bedrockagentcore as agentcore,
    aws_iam as iam,
    aws_logs as logs,
)
from constructs import Construct

from bundling.agent_code_bundling import AgentCodeBundling
from l3_constructs.code_interpreter import CodeInterpreter
from l3_constructs.document_file_system import DocumentFileSystem


class AgentRuntime(Construct):
    """Amazon Bedrock AgentCore Runtime that hosts the Strands agent as a Python 3.14
    CodeZip deployment, with an execution role that can invoke one Amazon Bedrock
    model through its global cross-Region inference profile and run code in sessions
    on one Code Interpreter. The runtime has no access to the document bucket; its only
    Amazon S3 permission is read access to the CDK assets bucket that holds its code,
    which AgentRuntimeArtifact.from_code_asset grants:
    https://github.com/aws/aws-cdk/blob/v2.275.0/packages/aws-cdk-lib/aws-bedrockagentcore/lib/runtime/runtime-artifact.ts#L294

    The runtime uses the construct's default public network mode, so it reaches the Amazon
    Bedrock and AgentCore APIs without VPC endpoints. See networkConfiguration in
    https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_bedrockagentcore/Runtime.html"""

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        *,
        agent_code_dir: str,
        model_name: str,
        code_interpreter: CodeInterpreter,
        file_system: DocumentFileSystem,
        mount_path: str,
    ) -> None:
        super().__init__(scope, construct_id)

        inference_profile_id = f"global.{model_name}"

        # Direct code deployment: a zip of the agent code and its Linux arm64 dependencies. See
        # https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-get-started-code-deploy-python.html
        artifact = agentcore.AgentRuntimeArtifact.from_code_asset(
            path=agent_code_dir,
            runtime=agentcore.AgentCoreRuntime.PYTHON_3_14,
            entrypoint=["main.py"],
            bundling=BundlingOptions(
                local=AgentCodeBundling(agent_code_dir),
                # Required by BundlingOptions but not used: CDK falls back to Docker only when local
                # bundling returns False, and AgentCodeBundling either returns True or fails the synth.
                # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk/BundlingOptions.html
                image=DockerImage.from_registry("public.ecr.aws/sam/build-python3.14"),
            ),
        )

        self.runtime = agentcore.Runtime(
            self,
            "Runtime",
            agent_runtime_artifact=artifact,
            description=f"Strands agent that streams responses from {model_name}",
            environment_variables={
                "MODEL_ID": inference_profile_id,
                "CODE_INTERPRETER_ID": code_interpreter.code_interpreter_id,
                # The agent mounts the S3 Files access point when it starts a Code Interpreter session.
                "FILE_SYSTEM_ARN": file_system.file_system_arn,
                "ACCESS_POINT_ARN": file_system.access_point_arn,
                "MOUNT_PATH": mount_path,
            },
        )

        # AgentCore creates the agent's log group itself, with the execution role's logs:CreateLogGroup
        # permission (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-permissions.html),
        # so the stack doesn't define it. LogRetention sets 7-day retention on it, and with
        # RemovalPolicy.DESTROY deletes it when the stack is deleted:
        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_logs/LogRetention.html
        logs.LogRetention(
            self,
            "LogRetention",
            log_group_name=self.runtime.application_log_group.log_group_name,
            retention=logs.RetentionDays.ONE_WEEK,
            removal_policy=RemovalPolicy.DESTROY,
        )

        code_interpreter.grant_sessions(self.runtime)

        # The three statements that global cross-Region inference requires, as described in
        # https://docs.aws.amazon.com/bedrock/latest/userguide/global-cross-region-inference.html
        inference_profile_arn = (
            f"arn:{Aws.PARTITION}:bedrock:{Aws.REGION}:{Aws.ACCOUNT_ID}"
            f":inference-profile/{inference_profile_id}"
        )
        invoke_actions = ["bedrock:InvokeModel", "bedrock:InvokeModelWithResponseStream"]
        self.runtime.add_to_role_policy(iam.PolicyStatement(
            actions=invoke_actions,
            resources=[inference_profile_arn],
            conditions={"StringEquals": {"aws:RequestedRegion": Aws.REGION}},
        ))
        self.runtime.add_to_role_policy(iam.PolicyStatement(
            actions=invoke_actions,
            resources=[f"arn:{Aws.PARTITION}:bedrock:{Aws.REGION}::foundation-model/{model_name}"],
            conditions={"StringEquals": {
                "aws:RequestedRegion": Aws.REGION,
                "bedrock:InferenceProfileArn": inference_profile_arn,
            }},
        ))
        self.runtime.add_to_role_policy(iam.PolicyStatement(
            actions=invoke_actions,
            # The Region-less ARN is what Bedrock evaluates when it routes the request to another Region.
            resources=[f"arn:{Aws.PARTITION}:bedrock:::foundation-model/{model_name}"],
            conditions={"StringEquals": {
                "aws:RequestedRegion": "unspecified",
                "bedrock:InferenceProfileArn": inference_profile_arn,
            }},
        ))

    @property
    def agent_runtime_arn(self) -> str:
        return self.runtime.agent_runtime_arn

    @property
    def log_group_name(self) -> str:
        """Name of the log group that the agent writes to; see applicationLogGroup in
        https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_bedrockagentcore/Runtime.html"""
        return self.runtime.application_log_group.log_group_name
