"""Strands sandbox that runs python_repl code in an AgentCore Code Interpreter session.

See "Building a Custom Sandbox" in the Strands docs:
https://strandsagents.com/docs/user-guide/sdk/sandbox/custom-sandbox/
"""

import asyncio
import logging
import os
from collections.abc import AsyncGenerator
from typing import Any

import boto3
from botocore.config import Config
from strands.sandbox.base import Sandbox
from strands.sandbox.errors import SandboxTimeoutError
from strands.sandbox.types import ExecutionResult, FileInfo

from log_events import log_event, truncate

# Maximum lifetime of a Code Interpreter session, whether or not it's busy (sessionTimeoutSeconds in
# https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartCodeInterpreterSession.html).
# The agent stops the session when the invocation ends, so this only matters if stopping it fails.
SESSION_TIMEOUT_SECONDS = 900
# Longest time a single code or command execution can take. python_repl waits 120 seconds by default
# and lets the model ask for a different timeout; the sandbox caps it at this value. See the timeout
# parameter in the python_repl source:
# https://github.com/strands-agents/harness-sdk/blob/a2524a556ce014d0909bad41822264c3d98ecd1e/strands-py/src/strands/vended_tools/python_repl/python_repl.py#L27
MAX_EXECUTION_SECONDS = 300

# A child of the AgentCore SDK's app logger, so records use its JSON format with request and session IDs:
# https://github.com/aws/bedrock-agentcore-sdk-python/blob/v1.25.4/src/bedrock_agentcore/runtime/app.py#L124
logger = logging.getLogger("bedrock_agentcore.app.sandbox")


class CodeInterpreterSandbox(Sandbox):
    """One Code Interpreter session with the S3 Files access point mounted at MOUNT_PATH.

    Use it as an async context manager, so that the session stops when the invocation ends.
    Strands requires all six abstract Sandbox methods, but only code and command execution are
    implemented, which is all that python_repl needs. The file methods raise NotImplementedError.
    The `language`, `cwd` and `env` arguments of the execution methods are ignored: the session
    runs Python in one working directory, and the mounted files are all the code needs.
    """

    def __init__(self) -> None:
        # Starting and stopping sessions use the default timeouts and retries.
        self._client = boto3.client("bedrock-agentcore")
        # The result event of invoke_code_interpreter arrives only when the code finishes, so the read
        # timeout must cover the longest execution. The botocore defaults (60 seconds, then retry) would
        # cut long runs short and send the same code to the session again, so this client never retries.
        # https://docs.aws.amazon.com/botocore/latest/reference/config.html
        # https://docs.aws.amazon.com/boto3/latest/guide/retries.html
        self._invoke_client = boto3.client(
            "bedrock-agentcore",
            config=Config(read_timeout=MAX_EXECUTION_SECONDS + 30, retries={"total_max_attempts": 1}),
        )
        self._code_interpreter_id = os.environ["CODE_INTERPRETER_ID"]
        self._session_id: str | None = None

    async def __aenter__(self) -> "CodeInterpreterSandbox":
        # The session mounts the S3 Files access point at MOUNT_PATH. See
        # https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-filesystem-configurations.html
        response = await asyncio.to_thread(
            self._client.start_code_interpreter_session,
            codeInterpreterIdentifier=self._code_interpreter_id,
            sessionTimeoutSeconds=SESSION_TIMEOUT_SECONDS,
            filesystemConfigurations=[{
                "s3FilesConfiguration": {
                    "fileSystemArn": os.environ["FILE_SYSTEM_ARN"],
                    "accessPointArn": os.environ["ACCESS_POINT_ARN"],
                    "mountPath": os.environ["MOUNT_PATH"],
                },
            }],
        )
        self._session_id = response["sessionId"]
        logger.info("Started Code Interpreter session %s", self._session_id)
        return self

    async def __aexit__(self, *_exc_info: object) -> None:
        try:
            await asyncio.to_thread(
                self._client.stop_code_interpreter_session,
                codeInterpreterIdentifier=self._code_interpreter_id,
                sessionId=self._session_id,
            )
            logger.info("Stopped Code Interpreter session %s", self._session_id)
        except Exception:
            # Don't let a cleanup failure hide the error that ended the invocation. The session
            # ends on its own SESSION_TIMEOUT_SECONDS after it started.
            logger.exception("Failed to stop Code Interpreter session %s", self._session_id)

    def _invoke(self, name: str, arguments: dict[str, Any]) -> ExecutionResult:
        # The response is an event stream; each result event is a CodeInterpreterResult:
        # https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeCodeInterpreter.html
        # https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_CodeInterpreterResult.html
        response = self._invoke_client.invoke_code_interpreter(
            codeInterpreterIdentifier=self._code_interpreter_id,
            sessionId=self._session_id,
            name=name,
            arguments=arguments,
        )
        results = [event["result"] for event in response["stream"] if "result" in event]
        if not results:
            raise RuntimeError(f"Code Interpreter returned no result for {name}")
        result = results[-1]
        output = result.get("structuredContent") or {}
        stderr = output.get("stderr", "")
        if "exitCode" not in output and result.get("isError"):
            # Errors raised by the Code Interpreter itself (not by the code) come back as text content,
            # with isError set and no exit code.
            stderr = "\n".join(item.get("text", "") for item in result.get("content", []))
        return ExecutionResult(
            exit_code=output.get("exitCode", 1 if result.get("isError") else 0),
            stdout=output.get("stdout", ""),
            stderr=stderr,
        )

    async def _run(self, name: str, arguments: dict[str, Any], timeout: float | None) -> ExecutionResult:
        timeout = min(timeout or MAX_EXECUTION_SECONDS, MAX_EXECUTION_SECONDS)
        log_event(logger, "run", operation=name, input=arguments.get("code") or arguments.get("command"))
        try:
            result = await asyncio.wait_for(asyncio.to_thread(self._invoke, name, arguments), timeout)
        except TimeoutError as error:
            # A running thread can't be cancelled, so the remote call keeps running and the session stays
            # busy until it finishes. https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future.cancel
            log_event(logger, "timeout", operation=name, timeoutSeconds=timeout)
            raise SandboxTimeoutError(timeout) from error
        log_event(
            logger, "result", operation=name, exitCode=result.exit_code,
            stdout=truncate(result.stdout), stderr=truncate(result.stderr),
        )
        return result

    async def execute_code_streaming(
        self, code: str, language: str, *, timeout: float | None = None, **kwargs: Any
    ) -> AsyncGenerator[ExecutionResult, None]:
        # The Code Interpreter names its Python interpreter "python"; python_repl passes "python3". See
        # language in https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ToolArguments.html
        yield await self._run("executeCode", {"language": "python", "code": code}, timeout)

    async def execute_streaming(
        self, command: str, *, timeout: float | None = None, **kwargs: Any
    ) -> AsyncGenerator[ExecutionResult, None]:
        yield await self._run("executeCommand", {"command": command}, timeout)

    async def read_file(self, path: str, **kwargs: Any) -> bytes:
        raise NotImplementedError

    async def write_file(self, path: str, content: bytes, **kwargs: Any) -> None:
        raise NotImplementedError

    async def remove_file(self, path: str, **kwargs: Any) -> None:
        raise NotImplementedError

    async def list_files(self, path: str, **kwargs: Any) -> list[FileInfo]:
        raise NotImplementedError
