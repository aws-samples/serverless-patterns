from aws_cdk import (
        App,
        assertions
    )

from lambda_sqs_cdk.lambda_sqs_cdk_stack import LambdaSqsCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in lambda_sqs_cdk/lambda_sqs_cdk_stack.py
def test_sqs_queue_created():
    app = App()
    stack = LambdaSqsCdkStack(app, "lambda-sqs-cdk")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::SQS::Queue", {
        "VisibilityTimeout": 300
    })

def test_lambda_function_created():
    app = App()
    stack = LambdaSqsCdkStack(app, "lambda-sqs-cdk")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::Lambda::Function", 1)
