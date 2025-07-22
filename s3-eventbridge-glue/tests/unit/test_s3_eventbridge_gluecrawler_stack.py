import aws_cdk as core
import aws_cdk.assertions as assertions

from s3_eventbridge_gluecrawler.s3_eventbridge_gluecrawler_stack import S3EventbridgeGluecrawlerStack

# example tests. To run these tests, uncomment this file along with the example
# resource in s3_eventbridge_gluecrawler/s3_eventbridge_gluecrawler_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = S3EventbridgeGluecrawlerStack(app, "s3-eventbridge-gluecrawler")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
