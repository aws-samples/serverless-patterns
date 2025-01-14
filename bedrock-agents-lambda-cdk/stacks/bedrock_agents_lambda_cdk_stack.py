from aws_cdk import (
    Duration,
    Stack,
    aws_bedrock as bedrock,
    aws_iam as iam,
    aws_lambda 
)
from constructs import Construct

class BedrockAgentsLambdaCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # IAM role for Lambda
        lambda_role = iam.Role(
            self, 'ISSLocationLambdaRole',
            assumed_by=iam.ServicePrincipal('lambda.amazonaws.com'),
            description='Role for Lambda function',
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name('service-role/AWSLambdaBasicExecutionRole')
            ]
        )

        # Lambda Function
        ISS_lambda_function = aws_lambda.Function(
            self, 'ISSLocationLambda',
            runtime=aws_lambda.Runtime.PYTHON_3_12,
            code=aws_lambda.Code.from_asset('lambda'),
            handler='bedrock_agents_lambda.lambda_handler',
            function_name="ISSLocationLambda", 
            timeout=Duration.seconds(120),
            role=lambda_role
        )

        #IAM role for Bedrock agent
        bedrock_agent_role = iam.Role(
            self, 'ISSLocationBedrockAgentRole',
            assumed_by=iam.ServicePrincipal('bedrock.amazonaws.com'),
            description='Role for Bedrock agent'
        )
        bedrock_agent_role.add_to_policy(iam.PolicyStatement(
            actions=["bedrock:InvokeModel"],
            resources= [
                    f"arn:aws:bedrock:{self.region}::foundation-model/anthropic.claude-3-sonnet-20240229-v1:0"
                ]           
        ))

        # Bedrock Agent
        cfn_agent = bedrock.CfnAgent(self, "ISSLocationAgent",
        agent_name="ISSLocationAgent",
        agent_resource_role_arn=bedrock_agent_role.role_arn,
        foundation_model="anthropic.claude-3-sonnet-20240229-v1:0",
        action_groups=[bedrock.CfnAgent.AgentActionGroupProperty(
            action_group_name="get_iss_location",
            action_group_executor=bedrock.CfnAgent.ActionGroupExecutorProperty(
                lambda_= ISS_lambda_function.function_arn
            ),
            action_group_state="ENABLED",
            function_schema=bedrock.CfnAgent.FunctionSchemaProperty(
                functions=[bedrock.CfnAgent.FunctionProperty(
                    name="get_iss_location",
                    description="Get the current geographic location of the International Space Station",
                )]
        ),
        skip_resource_in_use_check_on_delete=False
        )],
        instruction="You are an agent skilled at tracking and reporting the location of the International Space Station. Your role is to help users understand where the ISS is currently located by providing its geographic coordinates and other relevant location details.",
        auto_prepare=True)

        # Lambda resource based policy to allow Bedrock agent to invoke the Lambda
        lambda_resource_policy = aws_lambda.CfnPermission(
            self, 'ISSLocationLambdaResourcePolicy',
            action='lambda:InvokeFunction',
            function_name=ISS_lambda_function.function_name,
            principal='bedrock.amazonaws.com',
            source_arn=cfn_agent.attr_agent_arn
        )   