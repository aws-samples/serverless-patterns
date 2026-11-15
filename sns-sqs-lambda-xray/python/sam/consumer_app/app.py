
import random
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools import Tracer

tracer = Tracer()

@tracer.capture_method
def hello(rid):
    
    tracer.put_annotation(key="t_id", value=rid)
    tracer.put_metadata(key="func_response", value=f"Hello Lambda!! with ID: {rid}")
    print(f"Hello Lambda!! with ID: {rid}")

@tracer.capture_method
def process_message(event):
    print(f"event={event}")

@tracer.capture_lambda_handler
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    random_id = random.randrange(1, 100)
    tracer.put_annotation(key="t_id", value=random_id)
    tracer.put_metadata(key="func_response", value=context)
    hello(random_id)
    process_message(event)

    return "Complete handler"
