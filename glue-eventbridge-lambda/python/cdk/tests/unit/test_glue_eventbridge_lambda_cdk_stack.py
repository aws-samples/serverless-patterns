import aws_cdk as cdk
from aws_cdk import (
        assertions
    )

from glue_eventbridge_lambda_cdk.glue_eventbridge_lambda_cdk_stack import GlueEventBridgeLambda

# example tests. To run these tests, uncomment this file along with the example
# resource in glue_eventbridge_lambda_cdk/glue_eventbridge_lambda_cdk_stack.py
def test_event_rule_created():
    app = cdk.App()
    stack = GlueEventBridgeLambda(app, "glue-eventbridge-lambda-cdk")
    template = assertions.Template.from_stack(stack)

    print(template)

    template.has_resource_properties("AWS::Events::Rule", {
        "EventPattern":{ "detail": { "jobName": ["cdk-python-streaming-glue-job"],"state": ["TIMEOUT"]},"detail-type": ["Glue Job State Change"],"source": ["aws.glue"]}
    })

def test_lambda_function_created():
    app = cdk.App()
    stack = GlueEventBridgeLambda(app, "glue-eventbridge-lambda-cdk")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::Lambda::Function", 3)

def test_lambda_function_handler_created():
    app = cdk.App()
    stack = GlueEventBridgeLambda(app, "glue-eventbridge-lambda-cdk")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::Lambda::Function", {
        "Handler": "lambdaFunctionFromEventBridge.handler"
    })

def test_s3_bucket_created():
    app = cdk.App()
    stack = GlueEventBridgeLambda(app, "glue-eventbridge-lambda-cdk")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::S3::Bucket", 1)

def test_glue_job_created():
    app = cdk.App()
    stack = GlueEventBridgeLambda(app, "glue-eventbridge-lambda-cdk")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::Glue::Job", 1)
