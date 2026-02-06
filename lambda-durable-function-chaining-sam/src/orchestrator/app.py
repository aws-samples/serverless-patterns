import os
from aws_durable_execution_sdk_python import DurableContext, durable_execution


@durable_execution
def lambda_handler(event, context: DurableContext):
    """Durable orchestrator that chains 3 Lambda functions."""
    step1_arn = os.environ['STEP1_FUNCTION_ARN']
    step2_arn = os.environ['STEP2_FUNCTION_ARN']
    step3_arn = os.environ['STEP3_FUNCTION_ARN']

    # Step 1: Add initial data
    result1 = context.invoke(step1_arn, event, name='step1-add')

    # Step 2: Transform data
    result2 = context.invoke(step2_arn, result1, name='step2-transform')

    # Step 3: Finalize
    result3 = context.invoke(step3_arn, result2, name='step3-finalize')

    return {
        'workflow': 'completed',
        'input': event,
        'output': result3
    }
