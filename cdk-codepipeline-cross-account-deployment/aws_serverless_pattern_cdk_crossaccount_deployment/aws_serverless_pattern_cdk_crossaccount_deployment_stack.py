from aws_cdk import (
    Stack,
    aws_codecommit as codecommit,
    pipelines as pipelines,
)
from constructs import Construct
from aws_serverless_pattern_cdk_crossaccount_deployment.static_site import WebsiteStage

class AwsServerlessPatternCdkCrossaccountDeploymentStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create main demo repo
        repo = codecommit.Repository(
            self, "multiAccountDemoRepo", repository_name = "multiAccountDemoRepo"
        )

        # Create pipeline 
        pipeline = pipelines.CodePipeline(
            self,
            "Pipeline",
            cross_account_keys=True,
            synth=pipelines.ShellStep(
                "Synth",
                input=pipelines.CodePipelineSource.code_commit(repo, "main"),
                commands=[
                    "npm install -g aws-cdk",  # Installs the cdk cli on CodeBuild
                    "pip install -r requirements.txt",  # Instructs CodeBuild to install required packages
                    "cdk synth",
                ]
            ),
        )

        # Pipeline stage to deploy demo stake into first account
        account_a_stage = add_stage(WebsiteStage(self, "DemoWebsite", 
            env=cdk.Environment(account="<aws-account-a-number>", region="<region>")))
        
        # Pipeline stage to deploy demo stake into second account
        account_b_stage = add_stage(WebsiteStage(self, "DemoWebsite", 
            env=cdk.Environment(account="<aws-account-b-number>", region="<region>")))

        # You can add as many stages as you want, for as many environments as you want, as long as they have been bootstrapped and trust the primary (pipeline) account.