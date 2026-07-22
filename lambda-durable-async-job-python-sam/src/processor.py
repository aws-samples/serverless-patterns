"""
Durable function that processes a job in checkpointed steps.
Each step updates progress in DynamoDB. If the function is interrupted,
it resumes from the last checkpoint without re-executing completed steps.
"""

import os
import logging
from datetime import datetime, timezone
from decimal import Decimal

import boto3
from aws_durable_execution_sdk_python.config import Duration
from aws_durable_execution_sdk_python.context import DurableContext, StepContext, durable_step
from aws_durable_execution_sdk_python.execution import durable_execution

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["JOBS_TABLE"])


def update_job_status(job_id: str, status: str, progress: int, result=None, error=None):
    """Update job status in DynamoDB."""
    update_expr = "SET #s = :status, progress = :progress, updated_at = :now"
    expr_values = {
        ":status": status,
        ":progress": progress,
        ":now": datetime.now(timezone.utc).isoformat(),
    }
    expr_names = {"#s": "status"}

    if result is not None:
        update_expr += ", #r = :result"
        expr_values[":result"] = result
        expr_names["#r"] = "result"

    if error is not None:
        update_expr += ", #e = :error"
        expr_values[":error"] = error
        expr_names["#e"] = "error"

    table.update_item(
        Key={"job_id": job_id},
        UpdateExpression=update_expr,
        ExpressionAttributeValues=expr_values,
        ExpressionAttributeNames=expr_names,
    )


@durable_step
def validate_input(step_context: StepContext, job_id: str, input_data: dict) -> dict:
    """Step 1: Validate the input data."""
    step_context.logger.info("Validating input for job %s", job_id)
    update_job_status(job_id, "VALIDATING", 25)

    # Simulate validation logic
    if not input_data.get("data"):
        raise ValueError("Missing required field: data")

    return {"validated": True, "item_count": len(str(input_data.get("data", "")))}


@durable_step
def process_data(step_context: StepContext, job_id: str, validation: dict) -> dict:
    """Step 2: Process the data (simulates work)."""
    step_context.logger.info("Processing data for job %s", job_id)
    update_job_status(job_id, "PROCESSING", 50)

    # Simulate processing — in real use, this could be:
    # - Calling an ML inference endpoint
    # - Transforming and loading data
    # - Generating a report
    processed_items = validation["item_count"] * 2
    return {"processed_items": processed_items, "quality_score": Decimal("0.95")}


@durable_step
def finalize_result(step_context: StepContext, job_id: str, processing: dict) -> dict:
    """Step 3: Finalize and store the result."""
    step_context.logger.info("Finalizing job %s", job_id)
    update_job_status(job_id, "FINALIZING", 75)

    final_result = {
        "processed_items": processing["processed_items"],
        "quality_score": str(processing["quality_score"]),
        "summary": f"Successfully processed {processing['processed_items']} items",
    }
    return final_result


@durable_execution
def lambda_handler(event, context: DurableContext) -> dict:
    """
    Durable job processor with 3 checkpointed steps.
    If interrupted at any point, resumes from the last completed step.
    """
    job_id = event["job_id"]
    input_data = event.get("input", {})

    try:
        update_job_status(job_id, "IN_PROGRESS", 10)

        # Step 1: Validate (checkpointed)
        validation = context.step(validate_input(job_id, input_data))

        # Brief pause between steps (simulates rate limiting or cooldown)
        context.wait(Duration.from_seconds(2))

        # Step 2: Process (checkpointed)
        processing = context.step(process_data(job_id, validation))

        # Step 3: Finalize (checkpointed)
        result = context.step(finalize_result(job_id, processing))

        # Mark complete
        update_job_status(job_id, "COMPLETED", 100, result=result)
        context.logger.info("Job %s completed successfully", job_id)

        return {"status": "COMPLETED", "job_id": job_id, "result": result}

    except Exception as err:
        context.logger.error("Job %s failed: %s", job_id, str(err))
        update_job_status(job_id, "FAILED", 0, error=str(err))
        return {"status": "FAILED", "job_id": job_id, "error": str(err)}
