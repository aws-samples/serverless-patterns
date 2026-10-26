"""
Run the durable job locally, no AWS account needed:

    pip install -r tests/requirements.txt
    pytest tests/
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "after"))

import job
from aws_durable_execution_sdk_python_testing import DurableFunctionTestRunner


def _run(job_id: str, text: str):
    runner = DurableFunctionTestRunner(handler=job.lambda_handler)
    return runner.run(
        input=json.dumps({"job_id": job_id, "payload": {"input": text}}),
        execution_name=job_id,
    )


def test_happy_path_completes_all_three_steps():
    result = _run("job-ok", "hello")
    assert result.execution_status.name == "SUCCEEDED", result.error
    output = json.loads(result.result)
    assert output["job_id"] == "job-ok"
    assert output["published"] is True
    for name in ("fetch_source", "transform", "publish_result"):
        assert result.get_step(name).status.name == "SUCCEEDED"
        assert result.get_step(name).attempt == 1


def test_flaky_step_is_retried_by_the_runtime():
    result = _run("job-flaky", "this input is flaky")
    assert result.execution_status.name == "SUCCEEDED", result.error
    transform_step = result.get_step("transform")
    # First attempt raised TransientError; the SDK retried and the second attempt succeeded.
    assert transform_step.attempt == 2
    assert transform_step.status.name == "SUCCEEDED"
    # The steps around it ran exactly once -- no re-execution of finished work.
    assert result.get_step("fetch_source").attempt == 1
    assert result.get_step("publish_result").attempt == 1


def test_replay_is_deterministic():
    # Same input, same execution name, run twice: a durable function must produce
    # the same checkpoints and the same result on replay, and every operation is
    # a named step (tests fetch operations by name, never by index).
    first = _run("job-replay", "hello")
    second = _run("job-replay", "hello")
    assert first.execution_status.name == "SUCCEEDED", first.error
    assert second.execution_status.name == "SUCCEEDED", second.error
    assert json.loads(first.result) == json.loads(second.result)
    expected = {"fetch_source", "transform", "publish_result"}
    for result in (first, second):
        assert {op.name for op in result.get_all_operations()} == expected
        for name in expected:
            assert result.get_step(name).status.name == "SUCCEEDED"
