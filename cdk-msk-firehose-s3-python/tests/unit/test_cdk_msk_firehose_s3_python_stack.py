import aws_cdk as core
import aws_cdk.assertions as assertions
from cdk_msk_firehose_s3_python.cdk_msk_firehose_s3_python_stack import CdkMskFirehoseS3PythonStack


def test_sqs_queue_created():
    app = core.App()
    stack = CdkMskFirehoseS3PythonStack(app, "cdk-msk-firehose-s3-python")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::SQS::Queue", {
        "VisibilityTimeout": 300
    })


def test_sns_topic_created():
    app = core.App()
    stack = CdkMskFirehoseS3PythonStack(app, "cdk-msk-firehose-s3-python")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::SNS::Topic", 1)
