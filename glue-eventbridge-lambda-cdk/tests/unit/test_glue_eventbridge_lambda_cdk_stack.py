import aws_cdk as cdk
from aws_cdk import (
        assertions
    )

from glue_eventbridge_lambda_cdk.glue_eventbridge_lambda_cdk_stack import GlueEventBridgeLambda

# example tests. To run these tests, uncomment this file along with the example
# resource in glue_eventbridge_lambda_cdk/glue_eventbridge_lambda_cdk_stack.py
def test_sqs_queue_created():
    app = cdk.App()
    stack = GlueEventBridgeLambda(app, "glue-eventbridge-lambda-cdk")
    template = assertions.Template.from_stack(stack)

def test_lambda_function_created():
    app = cdk.App()
    stack = GlueEventBridgeLambda(app, "glue-eventbridge-lambda-cdk")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::Lambda::Function", 1)
