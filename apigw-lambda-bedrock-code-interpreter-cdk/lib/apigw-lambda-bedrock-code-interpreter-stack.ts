import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as agentcore from 'aws-cdk-lib/aws-bedrockagentcore';
import * as apigateway from 'aws-cdk-lib/aws-apigateway';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as lambda from 'aws-cdk-lib/aws-lambda';

export class ApigwLambdaBedrockCodeInterpreterStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Amazon Bedrock AgentCore Code Interpreter for safe code execution
    const codeInterpreter = new agentcore.CodeInterpreterCustom(this, 'CodeInterpreter', {
      codeInterpreterCustomName: 'data_analyst',
      description: 'Sandboxed Python execution for AI-generated data analysis code',
      networkConfiguration: agentcore.CodeInterpreterNetworkConfiguration.usingPublicNetwork(),
    });

    // AWS Lambda function: Bedrock generates code, Code Interpreter executes it
    const fn = new lambda.Function(this, 'AnalystFunction', {
      runtime: lambda.Runtime.PYTHON_3_12,
      handler: 'index.handler',
      code: lambda.Code.fromAsset('src/handler'),
      timeout: cdk.Duration.seconds(90),
      environment: {
        CODE_INTERPRETER_ID: (codeInterpreter.node.defaultChild as cdk.CfnResource).ref,
        MODEL_ID: 'us.anthropic.claude-sonnet-4-6',
      },
    });

    // Grant permissions for Amazon Bedrock AgentCore Code Interpreter
    codeInterpreter.grantUse(fn);

    // Grant permission to invoke Amazon Bedrock models
    fn.addToRolePolicy(new iam.PolicyStatement({
      actions: ['bedrock:InvokeModel'],
      resources: [
        `arn:aws:bedrock:*::foundation-model/*`,
        `arn:aws:bedrock:*:${this.account}:inference-profile/*`,
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
