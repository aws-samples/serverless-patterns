import aws_cdk as cdk
from constructs import Construct
from aws_serverless_pattern_cdk_crossaccount_deployment.static_site import DemoWebsiteStack

class WebsiteStage(cdk.Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        WebsiteStack = DemoWebsiteStack(self, "WebsiteStack")
