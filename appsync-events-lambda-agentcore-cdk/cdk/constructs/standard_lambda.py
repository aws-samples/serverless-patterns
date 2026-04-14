"""Reusable Lambda blueprint construct with Powertools, X-Ray, and log groups."""

from pathlib import Path
from aws_cdk import (
    aws_lambda as lambda_,
    aws_logs as logs,
    BundlingOptions,
    Duration,
    RemovalPolicy,
    Stack,
)
from constructs import Construct
from cdk_nag import NagSuppressions


class StandardLambda(Construct):
    """
    A reusable CDK Construct that provides a standardized blueprint for creating
    AWS Lambda functions — similar to the Global section of an AWS SAM template.

    This construct automatically includes:
    - A dedicated CloudWatch Log Group with configurable retention and removal policies,
      along with IAM permissions for the Lambda function to write logs.
    - The AWS Lambda Powertools for Python V3 layer (managed by AWS), pre-configured
      with POWERTOOLS_SERVICE_NAME and LOG_LEVEL environment variables.
    - X-Ray active tracing enabled by default.
    - Container-based dependency bundling when a requirements.txt file is detected.

    All default settings can be overridden per function. Environment variables and
    layers are merged (not replaced) so that Powertools config is always preserved
    unless explicitly overridden.

    The function and its execution role are exposed as public attributes (self.function
    and self.role) so consumers can grant additional IAM permissions after creation.
    """

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        handler: str,
        code_path: str,
        runtime: lambda_.Runtime = lambda_.Runtime.PYTHON_3_14,
        log_retention: logs.RetentionDays = logs.RetentionDays.ONE_WEEK,
        log_removal_policy: RemovalPolicy = RemovalPolicy.DESTROY,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id)

        stack = Stack.of(self)

        code = self._build_code(code_path, runtime)

        log_group = logs.LogGroup(
            self,
            "LogGroup",
            retention=log_retention,
            removal_policy=log_removal_policy,
        )

        # Default to ARM_64 for better price/performance
        architecture = kwargs.pop("architecture", lambda_.Architecture.ARM_64)

        # Resolve Powertools layer ARN from architecture + runtime.
        # Compare on .name because CDK Architecture objects are not singletons.
        arch_suffix = "arm64" if architecture.name == "arm64" else "x86_64"
        runtime_suffix = runtime.name.replace(".", "")

        powertools_layer = lambda_.LayerVersion.from_layer_version_arn(
            self,
            "PowertoolsLayer",
            f"arn:aws:lambda:{stack.region}:017000801446:layer:AWSLambdaPowertoolsPythonV3-{runtime_suffix}-{arch_suffix}:27",
        )

        defaults = {
            "runtime": runtime,
            "architecture": architecture,
            "timeout": Duration.seconds(30),
            "memory_size": 256,
            "layers": [powertools_layer],
            "environment": {
                "POWERTOOLS_SERVICE_NAME": construct_id,
                "LOG_LEVEL": "INFO",
            },
            "tracing": lambda_.Tracing.ACTIVE,
            "log_group": log_group,
        }

        # Pop layers and environment before the general merge so we can
        # combine them additively rather than replace the defaults.
        user_layers = kwargs.pop("layers", None)
        user_environment = kwargs.pop("environment", None)

        merged_config = {**defaults, **kwargs}

        if user_layers is not None:
            merged_config["layers"] = defaults.get("layers", []) + user_layers

        if user_environment is not None:
            merged_config["environment"] = {
                **defaults.get("environment", {}),
                **user_environment,
            }

        self.function = lambda_.Function(self, "Function", handler=handler, code=code, **merged_config)
        self.function_arn = self.function.function_arn
        self.function_name = self.function.function_name

        log_group.grant_write(self.function)
        self.role = self.function.role

        NagSuppressions.add_resource_suppressions(
            self.function,
            [
                {
                    "id": "AwsSolutions-IAM4",
                    "reason": "AWSLambdaBasicExecutionRole is the standard managed policy for Lambda logging.",
                    "applies_to": [
                        "Policy::arn:<AWS::Partition>:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole",
                    ],
                },
            ],
            apply_to_children=True,
        )

    def _build_code(self, code_path: str, runtime: lambda_.Runtime) -> lambda_.Code:
        """Build the Lambda deployment package.

        If the code directory has a requirements.txt with real dependencies,
        uses container bundling to pip install them into the deployment zip.
        Otherwise packages the code directory as-is.
        """
        code_dir = Path(code_path)
        requirements_file = code_dir / "requirements.txt"

        if requirements_file.exists() and self._has_dependencies(requirements_file):
            return lambda_.Code.from_asset(
                code_path,
                bundling=BundlingOptions(
                    image=runtime.bundling_image,
                    command=[
                        "bash",
                        "-c",
                        " && ".join(
                            [
                                "pip install -r requirements.txt -t /asset-output/",
                                "cp -r . /asset-output",
                            ]
                        ),
                    ],
                ),
            )

        return lambda_.Code.from_asset(code_path)

    def _has_dependencies(self, requirements_file: Path) -> bool:
        """Check if a requirements.txt contains actual package dependencies (not just comments)."""
        try:
            with open(requirements_file, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        return True
            return False
        except Exception:
            return False
