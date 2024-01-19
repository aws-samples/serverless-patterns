import aws_cdk as core
import aws_cdk.assertions as assertions

from eventbridge_scheduler_ssm_cdk_python.eventbridge_scheduler_ssm_cdk_python_stack import EventbridgeSchedulerSsmCdkPythonStack

# example tests. To run these tests, uncomment this file along with the example
# resource in eventbridge_scheduler_ssm_cdk_python/eventbridge_scheduler_ssm_cdk_python_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = EventbridgeSchedulerSsmCdkPythonStack(app, "eventbridge-scheduler-ssm-cdk-python")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
