import subprocess  # nosec

import jsii
from aws_cdk import (
    BundlingOptions,
    ILocalBundling,
    RemovalPolicy,
    Stack,
)
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_ssm as ssm
from constructs import Construct

LAMBDA_RUNTIME = _lambda.Runtime.PYTHON_3_9
bundle_commands = [
    "pip",
    "install",
    "-q",
    "-r",
    "requirements.txt",
    "--platform",
    "manylinux2014_x86_64",
    "--only-binary=:all:",
]


@jsii.implements(ILocalBundling)
class LocalBundle:
    """This class contains custom method to attempt local bundling if it Returns false the calling Function should revert to
    utilizing a docker container for the bundling"""

    def try_bundle(self, output_dir, options) -> bool:
        """Local Bundling approach"""
        try:
            if "layers" in options.working_directory:
                # Bundling for a Lambda Layer
                bundle_commands.extend(["-t", f"{output_dir}/python"])
                subprocess.check_call(["mkdir", "python"], cwd=output_dir)  # nosec
                subprocess.check_call(
                    [
                        "rsync",
                        "-ar",
                        "--relative",
                        "--exclude=__pycache__*",
                        "--exclude='*.pyc'",
                        ".",
                        f"{output_dir}/python",
                    ],
                    cwd=options.working_directory,
                )  # nosec
            else:
                bundle_commands.extend(["-t", output_dir])
                subprocess.check_call(bundle_commands, cwd=options.working_directory)  # nosec
                subprocess.check_call(
                    [
                        "rsync",
                        "-avr",
                        "--exclude='*_tests.py'",
                        "--exclude='__pycache__*'",
                        "--exclude='*.pyc'",
                        ".",
                        output_dir,
                    ],
                    cwd=options.working_directory,
                )  # nosec
            subprocess.check_call(bundle_commands, cwd=options.working_directory)  # nosec
            return True
        except subprocess.CalledProcessError as err:
            print(str(err))
            return False


class CommonLambdaLayerStack(Stack):
    """Contains CDK Code to Deploy Authorization API"""

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        layer_path = "src/layers/common_layer"
        self.common_lambda_layer = _lambda.LayerVersion(
            self,
            "CommonLambdaLayer",
            code=_lambda.Code.from_asset(
                layer_path,
                bundling=BundlingOptions(
                    local=LocalBundle(),
                    working_directory=layer_path,
                    image=LAMBDA_RUNTIME.bundling_image,  # pylint: disable=no-member
                    entrypoint=["/bin/sh", "-c"],
                    command=bundle_commands,
                ),
            ),
            removal_policy=RemovalPolicy.RETAIN,
            layer_version_name="CommonLambdaLayer",
            description="Contains Dependencies to run Backend Services.",
        )

        # Publish Prefix version
        self.common_lambda_layer_ssm_param = ssm.StringParameter(
            self,
            "CommonLambdaLayerParamLayer",
            parameter_name="/common-lambda-layer-arn",
            string_value=self.common_lambda_layer.layer_version_arn,
            description="This parameter contains a common Lambda Layer version ARN for the given Region",
        )
