import aws_cdk as core
import aws_cdk.assertions as assertions

from s3_sqs_lambda_bedrock_s3_cdk_python.s3_sqs_lambda_bedrock_s3_cdk_python_stack import S3SqsLambdaBedrockS3CdkPythonStack

# example tests. To run these tests, uncomment this file along with the example
# resource in s3_sqs_lambda_bedrock_s3_cdk_python/s3_sqs_lambda_bedrock_s3_cdk_python_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = S3SqsLambdaBedrockS3CdkPythonStack(app, "s3-sqs-lambda-bedrock-s3-cdk-python")
    template = assertions.Template.from_stack(stack)


