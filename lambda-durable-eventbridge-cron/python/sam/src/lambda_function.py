from aws_durable_execution_sdk_python.config import Duration
from aws_durable_execution_sdk_python.context import DurableContext, StepContext, durable_step
from aws_durable_execution_sdk_python.execution import durable_execution

@durable_step
def fetch_data(step_context: StepContext) -> dict:
    """Simulate fetching data from an external source."""
    # This runs only once — on replay, the checkpointed result is returned.
    print("Fetching data from external API...")
    return {"items": [1, 2, 3], "source": "external-api"}


@durable_step
def process_data(step_context: StepContext, data: dict) -> dict:
    """Simulate processing the fetched data."""
    print("Processing data...")
    total = sum(data["items"])
    return {"total": total, "source": data["source"], "status": "processed"}


@durable_execution
def lambda_handler(event: dict, context: DurableContext) -> dict:
    """
    Durable function triggered by EventBridge cron.

    Execution flow:
      Invocation 1: fetch_data runs → checkpoint → wait suspends execution
      Invocation 2: fetch_data replays from cache → wait completes → process_data runs → done
    """
    # Step 1: Fetch data (checkpointed, won't re-execute on replay)
    data = context.step(fetch_data())

    # Step 2: Wait 10 seconds (Lambda suspends, no idle compute cost)
    context.wait(Duration.from_seconds(10))

    # Step 3: Process the data
    result = context.step(process_data(data))

    return result


