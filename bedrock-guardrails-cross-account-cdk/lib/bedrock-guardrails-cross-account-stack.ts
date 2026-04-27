import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as bedrock from 'aws-cdk-lib/aws-bedrock';
import * as cr from 'aws-cdk-lib/custom-resources';
import * as path from 'path';

export class BedrockGuardrailsCrossAccountStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const modelId = new cdk.CfnParameter(this, 'BedrockModelId', {
      type: 'String',
      default: 'us.anthropic.claude-sonnet-4-20250514-v1:0',
      description: 'Bedrock model ID for testing',
    });

    // Create Bedrock Guardrail
    const guardrail = new bedrock.CfnGuardrail(this, 'Guardrail', {
      name: 'CrossAccountEnforcedGuardrail',
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

    // Create guardrail version via AwsCustomResource
    const versionCr = new cr.AwsCustomResource(this, 'GuardrailVersion', {
      onCreate: {
        service: 'Bedrock',
        action: 'createGuardrailVersion',
        parameters: {
          guardrailIdentifier: guardrail.attrGuardrailId,
        },
        physicalResourceId: cr.PhysicalResourceId.fromResponse('version'),
      },
      policy: cr.AwsCustomResourcePolicy.fromStatements([
        new iam.PolicyStatement({
          actions: ['bedrock:CreateGuardrailVersion'],
          resources: [guardrail.attrGuardrailArn],
        }),
      ]),
    });

    // Enable account-level enforcement via AwsCustomResource
    const enforceCr = new cr.AwsCustomResource(this, 'GuardrailEnforcement', {
      onCreate: {
        service: 'Bedrock',
        action: 'putEnforcedGuardrailConfiguration',
        parameters: {
          guardrailInferenceConfig: {
            guardrailIdentifier: guardrail.attrGuardrailId,
            guardrailVersion: versionCr.getResponseField('version'),
            inputTags: 'IGNORE',
          },
        },
        physicalResourceId: cr.PhysicalResourceId.of('enforced-guardrail'),
      },
      onDelete: {
        service: 'Bedrock',
        action: 'deleteEnforcedGuardrailConfiguration',
        parameters: {
          configId: 'default',
        },
      },
      policy: cr.AwsCustomResourcePolicy.fromStatements([
        new iam.PolicyStatement({
          actions: [
            'bedrock:PutEnforcedGuardrailConfiguration',
            'bedrock:DeleteEnforcedGuardrailConfiguration',
          ],
          resources: ['*'],
        }),
      ]),
    });

    enforceCr.node.addDependency(versionCr);

    // Test Lambda
    const testFn = new lambda.Function(this, 'TestFunction', {
      runtime: lambda.Runtime.NODEJS_20_X,
      handler: 'test.handler',
      code: lambda.Code.fromAsset(path.join(__dirname, '..', 'src')),
      memorySize: 256,
      timeout: cdk.Duration.seconds(60),
      environment: {
        MODEL_ID: modelId.valueAsString,
      },
    });

    testFn.addToRolePolicy(new iam.PolicyStatement({
      actions: ['bedrock:InvokeModel'],
      resources: [
        `arn:aws:bedrock:${this.region}:${this.account}:inference-profile/${modelId.valueAsString}`,
        'arn:aws:bedrock:*::foundation-model/*',
      ],
    }));

    testFn.addToRolePolicy(new iam.PolicyStatement({
      actions: ['bedrock:ApplyGuardrail'],
      resources: [guardrail.attrGuardrailArn],
    }));

    testFn.node.addDependency(enforceCr);

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
