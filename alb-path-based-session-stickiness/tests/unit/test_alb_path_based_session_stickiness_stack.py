import aws_cdk as core
import aws_cdk.assertions as assertions

from alb_path_based_session_stickiness.alb_path_based_session_stickiness_stack import AlbPathBasedSessionStickinessStack

# example tests. To run these tests, uncomment this file along with the example
# resource in alb_path_based_session_stickiness/alb_path_based_session_stickiness_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AlbPathBasedSessionStickinessStack(app, "alb-path-based-session-stickiness")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
