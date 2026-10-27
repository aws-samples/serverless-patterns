"""
AFTER - the job as a Lambda durable function.

Same three steps as before/worker.py. The difference is what is NOT here:
no scan, no claim, no stale-row detection, no hand-written checkpoint
writes, no attempt counter. context.step() records each step's result;
on a crash or retry the runtime replays and skips finished steps.

Public job id -> durable execution name. The API passes the job_id as
DurableExecutionName, so the same id can never start the job twice.
"""

from aws_durable_execution_sdk_python import (
    DurableContext,
    StepContext,
    durable_execution,
    durable_step,
)
from aws_durable_execution_sdk_python.config import StepConfig
from aws_durable_execution_sdk_python.retries import RetryPresets
from steps import fetch_source, publish_result, transform

# Step 2 is the flaky one. Give it the SDK's transient-failure retry policy
# (bounded exponential backoff with jitter) instead of a hand-rolled attempt counter.
RETRY_TRANSIENT = StepConfig(retry_strategy=RetryPresets.transient())


@durable_step
def step_fetch_source(step: StepContext, job_id: str, payload: dict) -> dict:
    step.logger.info("fetching source for %s", job_id)
    return fetch_source(job_id, payload)


@durable_step
def step_transform(step: StepContext, job_id: str, source: dict) -> dict:
    # step.attempt is the runtime's retry counter; before/worker.py keeps this by hand.
    step.logger.info("transform attempt %d for %s", step.attempt, job_id)
    return transform(job_id, source, attempt=step.attempt)


@durable_step
def step_publish_result(step: StepContext, job_id: str, result: dict) -> dict:
    # Steps run at-least-once per retry by default: if the invocation dies
    # between the step body finishing and its checkpoint landing, the body
    # runs again on replay. This stand-in has no external effect, so that is
    # safe. A real publish to a non-idempotent sink needs an idempotency key
    # minted in an earlier step, or StepSemantics.AT_MOST_ONCE_PER_RETRY.
    step.logger.info("publishing result for %s", job_id)
    return publish_result(job_id, result)


@durable_execution
def lambda_handler(event: dict, context: DurableContext) -> dict:
    job_id = event["job_id"]
    payload = event.get("payload", {})
    context.logger.info("job %s started", job_id)

    source = context.step(step_fetch_source(job_id, payload), name="fetch_source")
    result = context.step(
        step_transform(job_id, source), name="transform", config=RETRY_TRANSIENT
    )
    published = context.step(step_publish_result(job_id, result), name="publish_result")

    context.logger.info("job %s done", job_id)
    # Same shape the status table stored under `result`, so GET responses match.
    return published
