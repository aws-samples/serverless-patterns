import * as cdk from 'aws-cdk-lib';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as iam from 'aws-cdk-lib/aws-iam';
import { Construct } from 'constructs';

export class BedrockIamCostAllocationStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const modelId = new cdk.CfnParameter(this, 'BedrockModelId', {
      type: 'String',
      default: 'us.anthropic.claude-sonnet-4-20250514-v1:0',
      description: 'Bedrock model ID (inference profile)',
    });

    // Team A role — tagged for cost allocation
    const teamARole = new iam.Role(this, 'TeamABedrockRole', {
      assumedBy: new iam.ServicePrincipal('lambda.amazonaws.com'),
      managedPolicies: [iam.ManagedPolicy.fromAwsManagedPolicyName('service-role/AWSLambdaBasicExecutionRole')],
    });
    cdk.Tags.of(teamARole).add('team', 'data-science');
    cdk.Tags.of(teamARole).add('cost-center', '10001');

    teamARole.addToPolicy(new iam.PolicyStatement({
      actions: ['bedrock:InvokeModel'],
      resources: ['*'],
    }));

    // Team B role — tagged for cost allocation
    const teamBRole = new iam.Role(this, 'TeamBBedrockRole', {
      assumedBy: new iam.ServicePrincipal('lambda.amazonaws.com'),
      managedPolicies: [iam.ManagedPolicy.fromAwsManagedPolicyName('service-role/AWSLambdaBasicExecutionRole')],
    });
    cdk.Tags.of(teamBRole).add('team', 'engineering');
    cdk.Tags.of(teamBRole).add('cost-center', '10002');

    teamBRole.addToPolicy(new iam.PolicyStatement({
      actions: ['bedrock:InvokeModel'],
      resources: ['*'],
    }));

    // Team A Lambda
    const teamAFn = new lambda.Function(this, 'TeamAFunction', {
      runtime: lambda.Runtime.NODEJS_22_X,
      handler: 'index.handler',
      code: lambda.Code.fromAsset('src'),
      role: teamARole,
      timeout: cdk.Duration.seconds(30),
      environment: {
        MODEL_ID: modelId.valueAsString,
        TEAM_NAME: 'data-science',
      },
    });

    // Team B Lambda
    const teamBFn = new lambda.Function(this, 'TeamBFunction', {
      runtime: lambda.Runtime.NODEJS_22_X,
      handler: 'index.handler',
      code: lambda.Code.fromAsset('src'),
      role: teamBRole,
      timeout: cdk.Duration.seconds(30),
      environment: {
        MODEL_ID: modelId.valueAsString,
        TEAM_NAME: 'engineering',
      },
    });

    new cdk.CfnOutput(this, 'TeamAFunctionName', { value: teamAFn.functionName });
    new cdk.CfnOutput(this, 'TeamBFunctionName', { value: teamBFn.functionName });
    new cdk.CfnOutput(this, 'CostAllocationNote', {
      value: 'Activate cost allocation tags (team, cost-center) in AWS Billing console. Costs appear in CUR 2.0 within 24-48 hours.',
    });
  }
}
