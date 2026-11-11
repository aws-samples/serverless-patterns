import os
import shutil
import subprocess
import sys

import jsii
from aws_cdk import BundlingOptions, ILocalBundling


@jsii.implements(ILocalBundling)
class AgentCodeBundling:
    """Builds the CodeZip contents locally, without Docker: the agent code plus its
    Linux arm64 dependencies for Python 3.14, downloaded as prebuilt wheels with pip.

    AgentCore Runtime supports only arm64, and the AgentCore guide downloads manylinux2014
    aarch64 wheels the same way (with uv instead of pip):
    https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-get-started-code-deploy-python.html
    For the pip options, see https://pip.pypa.io/en/stable/cli/pip_install/
    """

    def __init__(self, agent_code_dir: str) -> None:
        self._agent_code_dir = agent_code_dir

    def try_bundle(self, output_dir: str, options: BundlingOptions) -> bool:
        subprocess.run(
            [
                sys.executable, "-m", "pip", "install",
                "--requirement", os.path.join(self._agent_code_dir, "requirements.txt"),
                "--target", output_dir,
                "--platform", "manylinux2014_aarch64",
                "--implementation", "cp",
                "--python-version", "3.14",
                "--only-binary=:all:",
                "--quiet",
                "--disable-pip-version-check",
            ],
            check=True,
        )
        shutil.copytree(
            self._agent_code_dir,
            output_dir,
            dirs_exist_ok=True,
            ignore=shutil.ignore_patterns("__pycache__", "requirements.txt", ".DS_Store", "*.swp"),
        )
        return True
