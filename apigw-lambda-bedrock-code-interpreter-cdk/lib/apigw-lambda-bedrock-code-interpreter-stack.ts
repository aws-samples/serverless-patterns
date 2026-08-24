import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as agentcore from 'aws-cdk-lib/aws-bedrockagentcore';
import * as apigateway from 'aws-cdk-lib/aws-apigateway';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as logs from 'aws-cdk-lib/aws-logs';

export class ApigwLambdaBedrockCodeInterpreterStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Amazon Bedrock AgentCore Code Interpreter for safe code execution
    const codeInterpreter = new agentcore.CodeInterpreterCustom(this, 'CodeInterpreter', {
      codeInterpreterCustomName: 'data_analyst',
      description: 'Sandboxed Python execution for AI-generated data analysis code',
      networkConfiguration: agentcore.CodeInterpreterNetworkConfiguration.usingSandboxNetwork(),
    });

    // Region-portable model configuration.
    // Cross-Region inference profiles are prefixed by geo (us. / eu. / apac.).
    // Derive the prefix from the deployment Region so the pattern works in US,
    // EU, and APAC without code edits. The model name is a single constant, so
    // bumping to a newer model (e.g. a later Claude Sonnet) is a one-line change.
    const modelName = 'anthropic.claude-sonnet-4-5-20250929-v1:0';
    const geoPrefix = this.region.startsWith('eu-')
      ? 'eu'
      : this.region.startsWith('ap-')
        ? 'apac'
        : 'us';
    const inferenceProfileId = `${geoPrefix}.${modelName}`;

    // Foundation-model ARNs the chosen geo's inference profile can route to.
    // Inference profiles fan out across all Regions in the geo, so IAM must
    // authorize the model in each of them (region wildcard scoped to the model).
    const foundationModelArn = `arn:aws:bedrock:*::foundation-model/${modelName}`;

    // AWS Lambda function: Bedrock generates code, Code Interpreter executes it
    const fn = new lambda.Function(this, 'AnalystFunction', {
      runtime: lambda.Runtime.PYTHON_3_12,
      handler: 'index.handler',
      code: lambda.Code.fromAsset('src/handler'),
      timeout: cdk.Duration.seconds(29),
      logRetention: logs.RetentionDays.ONE_WEEK,
      environment: {
        CODE_INTERPRETER_ID: (codeInterpreter.node.defaultChild as cdk.CfnResource).ref,
        MODEL_ID: inferenceProfileId,
      },
    });

    // Grant permissions for Amazon Bedrock AgentCore Code Interpreter
    codeInterpreter.grantUse(fn);

    // Grant permission to invoke Amazon Bedrock models (least privilege).
    // Scoped to the specific model: the geo inference profile plus the
    // foundation-model ARN the profile routes to within that geo.
    fn.addToRolePolicy(new iam.PolicyStatement({
      actions: ['bedrock:InvokeModel'],
      resources: [
        `arn:aws:bedrock:${this.region}:${this.account}:inference-profile/${inferenceProfileId}`,
        foundationModelArn,
      ],
    }));

    // Amazon API Gateway REST API
    const api = new apigateway.RestApi(this, 'AnalystApi', {
      restApiName: 'AI Data Analyst',
      description: 'Ask data questions in natural language — Amazon Bedrock writes Python, Amazon Bedrock AgentCore Code Interpreter executes it safely',
    });

    api.root.addResource('analyze').addMethod('POST', new apigateway.LambdaIntegration(fn));

    // Outputs
    new cdk.CfnOutput(this, 'ApiEndpoint', { value: api.url });
    new cdk.CfnOutput(this, 'FunctionName', { value: fn.functionName });
  }
}
