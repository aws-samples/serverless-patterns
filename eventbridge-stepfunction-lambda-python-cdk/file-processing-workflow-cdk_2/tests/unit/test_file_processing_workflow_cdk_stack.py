import aws_cdk as core
import aws_cdk.assertions as assertions

from file_processing_workflow_cdk.file_processing_workflow_cdk_stack import FileProcessingWorkflowCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in file_processing_workflow_cdk/file_processing_workflow_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = FileProcessingWorkflowCdkStack(app, "file-processing-workflow-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
