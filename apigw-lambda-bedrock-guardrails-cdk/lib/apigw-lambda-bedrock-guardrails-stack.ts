import * as cdk from 'aws-cdk-lib';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as apigateway from 'aws-cdk-lib/aws-apigateway';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as bedrock from 'aws-cdk-lib/aws-bedrock';
import { Construct } from 'constructs';

export class ApigwLambdaBedrockGuardrailsStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Bedrock Guardrail with content and topic filters
    const guardrail = new bedrock.CfnGuardrail(this, 'AppGuardrail', {
      name: 'app-content-guardrail',
      blockedInputMessaging: 'Your request was blocked by our content policy.',
      blockedOutputsMessaging: 'The response was blocked by our content policy.',
      contentPolicyConfig: {
        filtersConfig: [
          { type: 'SEXUAL', inputStrength: 'HIGH', outputStrength: 'HIGH' },
          { type: 'VIOLENCE', inputStrength: 'HIGH', outputStrength: 'HIGH' },
          { type: 'HATE', inputStrength: 'HIGH', outputStrength: 'HIGH' },
          { type: 'INSULTS', inputStrength: 'HIGH', outputStrength: 'MEDIUM' },
          { type: 'MISCONDUCT', inputStrength: 'HIGH', outputStrength: 'HIGH' },
        ],
      },
      topicPolicyConfig: {
        topicsConfig: [
          {
            name: 'Financial Advice',
            definition: 'Providing specific investment recommendations, stock picks, or financial planning advice.',
            type: 'DENY',
          },
        ],
      },
    });

    // Guardrail version (required for InvokeModel)
    const guardrailVersion = new bedrock.CfnGuardrailVersion(this, 'GuardrailVersion', {
      guardrailIdentifier: guardrail.attrGuardrailId,
    });

    // Lambda function
    const fn = new lambda.Function(this, 'BedrockGuardrailsFunction', {
      runtime: lambda.Runtime.NODEJS_20_X,
      handler: 'index.handler',
      code: lambda.Code.fromAsset('src'),
      timeout: cdk.Duration.seconds(30),
      memorySize: 256,
      environment: {
        MODEL_ID: 'us.anthropic.claude-sonnet-4-20250514-v1:0',
        GUARDRAIL_ID: guardrail.attrGuardrailId,
        GUARDRAIL_VERSION: guardrailVersion.attrVersion,
      },
    });

    fn.addToRolePolicy(new iam.PolicyStatement({
      actions: ['bedrock:InvokeModel', 'bedrock:ApplyGuardrail'],
      resources: [
        'arn:aws:bedrock:*::foundation-model/*',
        `arn:aws:bedrock:*:${this.account}:inference-profile/*`,
        guardrail.attrGuardrailArn,
      ],
    }));

    // REST API
    const api = new apigateway.RestApi(this, 'BedrockGuardrailsApi', {
      restApiName: 'bedrock-guardrails-api',
      description: 'API Gateway -> Lambda -> Bedrock with per-request Guardrails',
    });

    api.root.addResource('invoke').addMethod('POST', new apigateway.LambdaIntegration(fn));

    new cdk.CfnOutput(this, 'ApiEndpoint', { value: api.url + 'invoke' });
    new cdk.CfnOutput(this, 'GuardrailId', { value: guardrail.attrGuardrailId });
    new cdk.CfnOutput(this, 'FunctionName', { value: fn.functionName });
  }
}
