import aws_cdk as core
import aws_cdk.assertions as assertions

from translate_api.translate_api_stack import TranslateApiStack

# example tests. To run these tests, uncomment this file along with the example
# resource in translate_api/translate_api_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = TranslateApiStack(app, "translate-api")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
