import aws_cdk as core
import aws_cdk.assertions as assertions

from apigw_vpclink_pvtnlb_fargate_cdk_python.apigw_vpclink_pvtnlb_fargate_cdk_python_stack import ApigwVpclinkPvtnlbFargateCdkPythonStack

# example tests. To run these tests, uncomment this file along with the example
# resource in apigw_vpclink_pvtnlb_fargate_cdk_python/apigw_vpclink_pvtnlb_fargate_cdk_python_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ApigwVpclinkPvtnlbFargateCdkPythonStack(app, "apigw-vpclink-pvtnlb-fargate-cdk-python")
    template = assertions.Template.from_stack(stack)
