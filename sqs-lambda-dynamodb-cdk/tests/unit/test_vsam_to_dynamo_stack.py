from aws_cdk import (
        App,
        assertions
    )

from vsam_to_dynamo.vsam_to_dynamo_stack import VsamToDynamoStack


def test_sqs_queue_created():
    app = App()
    stack = VsamToDynamoStack(app, "vsam-to-dynamo")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::SQS::Queue", {
        "VisibilityTimeout": 300
    })


def test_lambda_function_created():
    app = App()
    stack = VsamToDynamoStack(app, "vsam-to-dynamo")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::Lambda::Function", 1)


def test_dynamodb_table_created():
    app = App()
    stack = VsamToDynamoStack(app, "vsam-to-dynamo")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::DynamoDB::Table", 1)
