import aws_cdk as core
import aws_cdk.assertions as assertions

from eventbridge_lambda_bedrock.eventbridge_lambda_bedrock_stack import EventbridgeLambdaBedrockStack

# example tests. To run these tests, uncomment this file along with the example
# resource in eventbridge_lambda_bedrock/eventbridge_lambda_bedrock_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = EventbridgeLambdaBedrockStack(app, "eventbridge-lambda-bedrock")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
