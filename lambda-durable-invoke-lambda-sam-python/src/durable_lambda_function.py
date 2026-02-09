import json
import os
from aws_durable_execution_sdk_python import (
    DurableContext,
    StepContext,
    durable_execution,
    durable_step,
)

PROCESSOR_FUNCTION_NAME = os.environ["PROCESSOR_FUNCTION_NAME"]


@durable_step
def prepare_input(step_ctx: StepContext, raw_values: list) -> dict:
    """Prepare and validate input values before invoking the processor function."""
    step_ctx.logger.info("Preparing input values for processing")
    return {
        "values": raw_values,
        "operation": "sum_and_average",
    }


@durable_execution
def lambda_handler(event: dict, context: DurableContext) -> dict:
    """Durable function that orchestrates processing by invoking another Lambda."""
    raw_values = event.get("values", [10, 20, 30, 40, 50])
    context.logger.info("Starting durable orchestration", extra={"values": raw_values})

    # Step 1: Prepare the input (checkpointed)
    prepared = context.step(prepare_input(raw_values), name="prepare_input")

    # Step 2: Invoke the processor Lambda function (checkpointed)
    # If the durable function is interrupted after this completes,
    # it resumes with the stored result without re-invoking the processor.
    result = context.invoke(
        function_name=PROCESSOR_FUNCTION_NAME,
        payload=prepared,
        name="invoke_processor",
    )

    context.logger.info("Processing complete", extra={"result": result})

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Durable orchestration completed successfully",
            "input_values": raw_values,
            "processing_result": result,
        }),
    }
