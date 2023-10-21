from aws_cdk import (
    Stack,
    aws_codecommit as codecommit,
    pipelines as pipelines,
)
from constructs import Construct
from aws_serverless_pattern_cdk_crossaccount_deployment.static_site.website_stage import WebsiteStage

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
        # You will need to replace both "<aws-account-b-number>" and "<aws-account-a-number>"" with the account number for one of your accounts,
        # as well as updating the corresponding "<region>" fields, these will need to match the Account/Region pairs you bootsrapped during the 
        # deployment instructions.
        # Pipeline stage to deploy demo stack into first account
        account_a_stage = add_stage(WebsiteStage(self, "DemoWebsite", 
            env=cdk.Environment(account="<aws-account-a-number>", region="<region>")))
        
        # Pipeline stage to deploy demo stack into second account
        account_b_stage = add_stage(WebsiteStage(self, "DemoWebsite", 
            env=cdk.Environment(account="<aws-account-b-number>", region="<region>")))

        # You can add as many stages as you want, with as many stacks as you want, for as many environments as you want, as long as they have been bootstrapped and trust the primary (pipeline) account.