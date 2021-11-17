from aws_cdk import (
        core,
        assertions
    )

from sfn_comprehend_sdk.sfn_comprehend_sdk_stack import SfnComprehendSdkStack


# example tests. To run these tests, uncomment this file along with the example
# resource in sfn_comprehend_sdk/sfn_comprehend_sdk_stack.py
def test_sfn_queue_created():
    app = core.App()
    stack = SfnComprehendSdkStack(app, "sfn-comprehend-sdk")
    template = assertions.Template.from_stack(stack)
    template.has_resource_properties("AWS::StepFunctions::StateMachine", {})
    pass
