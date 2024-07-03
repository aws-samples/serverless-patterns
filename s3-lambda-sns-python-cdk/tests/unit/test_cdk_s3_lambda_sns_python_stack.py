import aws_cdk as core
import aws_cdk.assertions as assertions

from src.cdk_s3_lambda_sns_python_stack import CdkS3LambdaSnsPythonStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_s3_lambda_sns_python/cdk_s3_lambda_sns_python_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkS3LambdaSnsPythonStack(app, "cdk-s3-lambda-sns-python")
    template = assertions.Template.from_stack(stack)
