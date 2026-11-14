import aws_cdk as core
import aws_cdk.assertions as assertions

from rds_sns_event_notification_cdk_python.rds_sns_event_notification_cdk_python_stack import RdsSnsEventNotificationCdkPythonStack

# example tests. To run these tests, uncomment this file along with the example
# resource in rds_sns_event_notification_cdk_python/rds_sns_event_notification_cdk_python_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = RdsSnsEventNotificationCdkPythonStack(app, "rds-sns-event-notification-cdk-python")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
