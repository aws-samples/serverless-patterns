import aws_cdk as cdk

from cdk_apigw_lambda_wildcardpolicy_stack.cdk_apigw_lambda_wildcardpolicy_stack import CdkApigwLambdaWildCardPolicyStack

app = cdk.App()

# Instantiate the CDK stack
CdkApigwLambdaWildCardPolicyStack(app, 'CdkApigwLambdaWildCardPolicyStack')

# Synthesize the CloudFormation template
app.synth()