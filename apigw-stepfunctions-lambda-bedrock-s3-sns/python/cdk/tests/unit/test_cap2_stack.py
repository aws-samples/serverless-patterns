import aws_cdk as core
import aws_cdk.assertions as assertions

from cap2.cap2_stack import Cap2Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in cap2/cap2_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Cap2Stack(app, "cap2")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
