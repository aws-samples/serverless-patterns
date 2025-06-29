import aws_cdk as core
import aws_cdk.assertions as assertions

from personalized_sms_briefing_bedrock.personalized_sms_briefing_bedrock_stack import PersonalizedSmsBriefingBedrockStack

# example tests. To run these tests, uncomment this file along with the example
# resource in personalized_sms_briefing_bedrock/personalized_sms_briefing_bedrock_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = PersonalizedSmsBriefingBedrockStack(app, "personalized-sms-briefing-bedrock")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
