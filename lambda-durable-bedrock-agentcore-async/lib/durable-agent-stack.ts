import * as cdk from 'aws-cdk-lib';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as logs from 'aws-cdk-lib/aws-logs';
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';
import * as path from 'path';
import { Construct } from 'constructs';

interface DurableAgentStackProps extends cdk.StackProps {
  /** ARN of the AgentCore Runtime to invoke */
  agentRuntimeArn: string;
  /** AgentCore Runtime endpoint URL */
  agentRuntimeEndpointUrl: string;
}

export class DurableAgentStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props: DurableAgentStackProps) {
    super(scope, id, props);

    const logGroup = new logs.LogGroup(this, 'DurableFunctionLogGroup', {
      logGroupName: '/aws/lambda/durableAgentCaller',
      retention: logs.RetentionDays.ONE_WEEK,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    const durableFunction = new NodejsFunction(this, 'DurableAgentCaller', {
      functionName: 'durableAgentCaller',
      runtime: lambda.Runtime.NODEJS_22_X,
      entry: path.join(__dirname, '../durable-lambda/index.ts'),
      handler: 'handler',
      timeout: cdk.Duration.minutes(15),
      memorySize: 512,
      logGroup,
      environment: {
        AGENT_RUNTIME_ARN: props.agentRuntimeArn,
        AGENT_RUNTIME_ENDPOINT_URL: props.agentRuntimeEndpointUrl,
      },
      durableConfig: {
        executionTimeout: cdk.Duration.minutes(10),
        retentionPeriod: cdk.Duration.days(3),
      }
    });

    // Allow invoking the AgentCore Runtime
    durableFunction.addToRolePolicy(
      new iam.PolicyStatement({
        actions: ['bedrock-agentcore:InvokeAgentRuntime'],
        resources: [
          props.agentRuntimeArn,
          `${props.agentRuntimeArn}/*`],
      }),
    );

    // Durable execution checkpoint permissions
    durableFunction.role!.addManagedPolicy(
      iam.ManagedPolicy.fromAwsManagedPolicyName(
        'service-role/AWSLambdaBasicDurableExecutionRolePolicy',
      ),
    );

    // Create version and alias for qualified invocation
    const version = durableFunction.currentVersion;
    const alias = new lambda.Alias(this, 'ProdAlias', {
      aliasName: 'prod',
      version,
    });

    new cdk.CfnOutput(this, 'DurableFunctionArn', {
      value: durableFunction.functionArn,
      description: 'Durable function ARN',
    });

    new cdk.CfnOutput(this, 'DurableFunctionAliasArn', {
      value: alias.functionArn,
      description: 'Qualified ARN (use this for invocation)',
    });
  }
}
