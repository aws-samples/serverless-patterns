import aws_cdk as core
import aws_cdk.assertions as assertions

from s3_lambda_bedrock_cdk_python.s3_lambda_bedrock_cdk_python_stack import S3LambdaBedrockCdkPythonStack

# example tests. To run these tests, uncomment this file along with the example
# resource in s3_lambda_bedrock_cdk_python/s3_lambda_bedrock_cdk_python_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = S3LambdaBedrockCdkPythonStack(app, "s3-lambda-bedrock-cdk-python")
    template = assertions.Template.from_stack(stack)


