import aws_cdk as core
import aws_cdk.assertions as assertions

from sfn_cfn_stacksets_pattern.sfn_cfn_stacksets_pattern_stack import SfnCfnStacksetsPatternStack

# example tests. To run these tests, uncomment this file along with the example
# resource in sfn_cfn_stacksets_pattern/sfn_cfn_stacksets_pattern_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SfnCfnStacksetsPatternStack(app, "sfn-cfn-stacksets-pattern")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
