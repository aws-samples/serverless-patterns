import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as bedrock from 'aws-cdk-lib/aws-bedrock';
import * as path from 'path';

export class BedrockGuardrailsEnforcementStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const modelId = new cdk.CfnParameter(this, 'BedrockModelId', {
      type: 'String',
      default: 'us.anthropic.claude-sonnet-4-20250514-v1:0',
      description: 'Bedrock model ID for testing',
    });

    // Create the Bedrock Guardrail (DRAFT) with content and topic filters
    const guardrail = new bedrock.CfnGuardrail(this, 'Guardrail', {
      name: 'AccountEnforcedGuardrail',
      blockedInputMessaging: 'Your request was blocked by the guardrail.',
      blockedOutputsMessaging: 'The response was blocked by the guardrail.',
      contentPolicyConfig: {
        filtersConfig: [
          { type: 'HATE', inputStrength: 'MEDIUM', outputStrength: 'MEDIUM' },
          { type: 'INSULTS', inputStrength: 'MEDIUM', outputStrength: 'MEDIUM' },
          { type: 'SEXUAL', inputStrength: 'MEDIUM', outputStrength: 'MEDIUM' },
          { type: 'VIOLENCE', inputStrength: 'MEDIUM', outputStrength: 'MEDIUM' },
          { type: 'MISCONDUCT', inputStrength: 'MEDIUM', outputStrength: 'MEDIUM' },
          { type: 'PROMPT_ATTACK', inputStrength: 'MEDIUM', outputStrength: 'NONE' },
        ],
      },
      topicPolicyConfig: {
        topicsConfig: [
          {
            name: 'InvestmentAdvice',
            definition: 'Providing specific investment recommendations, stock picks, or financial advice',
            type: 'DENY',
          },
        ],
      },
    });

    // Publish a numbered guardrail version using the native CloudFormation resource
    const guardrailVersion = new bedrock.CfnGuardrailVersion(this, 'GuardrailVersion', {
      guardrailIdentifier: guardrail.attrGuardrailId,
      description: 'Version enforced at the account level',
    });

    // Enable account-level enforcement using the native AWS::Bedrock::EnforcedGuardrailConfiguration
    // resource. No custom resource / Lambda-backed workaround is required.
    const enforcedGuardrail = new cdk.CfnResource(this, 'EnforcedGuardrail', {
      type: 'AWS::Bedrock::EnforcedGuardrailConfiguration',
      properties: {
        GuardrailIdentifier: guardrail.attrGuardrailId,
        GuardrailVersion: guardrailVersion.attrVersion,
      },
    });
    enforcedGuardrail.node.addDependency(guardrailVersion);

    // Test Lambda that calls the Converse API WITHOUT a guardrailIdentifier
    const testFn = new lambda.Function(this, 'TestFunction', {
      runtime: new lambda.Runtime('nodejs24.x', lambda.RuntimeFamily.NODEJS),
      handler: 'test.handler',
      code: lambda.Code.fromAsset(path.join(__dirname, '..', 'src')),
      memorySize: 256,
      timeout: cdk.Duration.seconds(60),
      environment: {
        MODEL_ID: modelId.valueAsString,
      },
    });

    // Inference profiles route cross-region, so the foundation-model ARN keeps a
    // wildcard region while the inference-profile ARN is scoped to this account/region.
    testFn.addToRolePolicy(new iam.PolicyStatement({
      actions: ['bedrock:InvokeModel'],
      resources: [
        `arn:aws:bedrock:${this.region}:${this.account}:inference-profile/${modelId.valueAsString}`,
        'arn:aws:bedrock:*::foundation-model/*',
      ],
    }));

    // With an account-level enforced guardrail active, the caller must be authorized
    // to apply the guardrail even though no guardrailIdentifier is passed in the call.
    testFn.addToRolePolicy(new iam.PolicyStatement({
      actions: ['bedrock:ApplyGuardrail'],
      resources: [guardrail.attrGuardrailArn],
    }));

    testFn.node.addDependency(enforcedGuardrail);

    // Outputs
    new cdk.CfnOutput(this, 'GuardrailId', {
      value: guardrail.attrGuardrailId,
    });

    new cdk.CfnOutput(this, 'GuardrailArn', {
      value: guardrail.attrGuardrailArn,
    });

    new cdk.CfnOutput(this, 'TestFunctionName', {
      value: testFn.functionName,
    });
  }
}
