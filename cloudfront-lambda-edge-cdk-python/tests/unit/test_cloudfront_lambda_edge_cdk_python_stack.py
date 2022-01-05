import aws_cdk as core
import aws_cdk.assertions as assertions

from cloudfront_lambda_edge_cdk_python.cloudfront_lambda_edge_cdk_python_stack import CloudfrontLambdaEdgeCdkPythonStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cloudfront_lambda_edge_cdk_python/cloudfront_lambda_edge_cdk_python_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CloudfrontLambdaEdgeCdkPythonStack(app, "cloudfront-lambda-edge-cdk-python")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
