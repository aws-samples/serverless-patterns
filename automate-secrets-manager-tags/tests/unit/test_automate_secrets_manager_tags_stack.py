import aws_cdk as core
import aws_cdk.assertions as assertions

from automate_secrets_manager_tags.automate_secrets_manager_tags_stack import AutomateSecretsManagerTagsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in automate_secrets_manager_tags/automate_secrets_manager_tags_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AutomateSecretsManagerTagsStack(app, "automate-secrets-manager-tags")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
