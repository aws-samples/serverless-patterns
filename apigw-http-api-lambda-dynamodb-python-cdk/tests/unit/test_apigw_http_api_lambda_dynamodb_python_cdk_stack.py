import aws_cdk as core
import aws_cdk.assertions as assertions

from stack.apigw_http_api_lambda_dynamodb_python_cdk_stack import ApigwHttpApiLambdaDynamodbPythonCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in apigw_http_api_lambda_dynamodb_python_cdk/apigw_http_api_lambda_dynamodb_python_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ApigwHttpApiLambdaDynamodbPythonCdkStack(app, "apigw-http-api-lambda-dynamodb-python-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
