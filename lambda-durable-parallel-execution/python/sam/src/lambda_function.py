from aws_durable_execution_sdk_python import BatchResult, DurableContext, durable_execution, durable_step
from aws_durable_execution_sdk_python.retries import RetryPresets
from aws_durable_execution_sdk_python.config import StepConfig

@durable_execution
def lambda_handler(event: dict, context: DurableContext) -> dict:
    context.logger.info(event)
    num1 = event.get('num1', 0)
    num2 = event.get('num2', 0)

    # No retries
    step_config = StepConfig(retry_strategy=RetryPresets.none())

    # Define the functions for each step
    def add_nums(): 
        context.logger.info(f"Adding {num1} and {num2}")
        return num1 + num2

    def sub_nums(): 
        context.logger.info(f"Subtracting {num2} from {num1}")
        return num1 - num2

    def mul_nums(): 
        context.logger.info(f"Multiplying {num1} and {num2}")
        return num1 * num2

    def div_nums(): 
        context.logger.info(f"Dividing {num1} by {num2}")
        if num2 == 0:
            raise ValueError("Division by zero is not allowed")
        return num1 / num2

    try:
        # context.parallel takes a list of step definitions and executes them in parallel.
        # It returns a list of results in the same order as the input list.
        results = context.parallel([
            lambda ctx: ctx.step(lambda _: add_nums(), name="addition"),
            lambda ctx: ctx.step(lambda _: sub_nums(), name="subtraction"),
            lambda ctx: ctx.step(lambda _: mul_nums(), name="multiplication"),
            lambda ctx: ctx.step(lambda _: div_nums(), name="division", config=step_config)
        ])

        if results.failure_count != 0:
            raise Exception(f"One or more operations failed")

        add, sub, mul, div = results.get_results()
        return {        
            "Add": add,
            "Subtract": sub,
            "Multiply": mul,
            "Division": div
        }

    except Exception as e:
        return {
            "error_details": str(e)
        }