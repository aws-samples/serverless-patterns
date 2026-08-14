import * as path from 'path';
import * as cdk from 'aws-cdk-lib';
import * as bedrockagentcore from 'aws-cdk-lib/aws-bedrockagentcore';
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb';
import * as ecrAssets from 'aws-cdk-lib/aws-ecr-assets';
import * as events from 'aws-cdk-lib/aws-events';
import * as eventsTargets from 'aws-cdk-lib/aws-events-targets';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as sns from 'aws-cdk-lib/aws-sns';
import { Construct } from 'constructs';

/**
 * AgentCore Runtime → AgentCore Gateway → EventBridge (Outbound pattern)
 *
 * An AI agent on AgentCore Runtime emits structured business events to
 * EventBridge through a governed AgentCore Gateway MCP tool.
 *
 * Flow:
 *   Strands Agent (Runtime) → emit_event tool (Gateway MCP, Streamable HTTP)
 *     → Lambda tool backend → events:PutEvents → Custom Bus
 *       → Fan-out rules → DynamoDB (decision log) + SNS (notifications)
 *
 * Why Gateway over direct SDK:
 * - Governance: Gateway tool definition constrains allowed event schemas
 * - Observability: Gateway logs every tool invocation automatically
 * - Rate limiting: Gateway enforces per-tool rate limits
 * - Schema evolution: Update Gateway tool definition only, no agent redeploy
 * - Multi-agent consistency: All agents use the same governed tool
 *
 * Auth model:
 * - Runtime → Gateway: authorizerType=NONE (same-account trust via
 *   AgentCore workload identity). The Gateway and Runtime are both
 *   managed by AgentCore within the same account.
 * - Runtime invocation (external caller): IAM SigV4 — caller needs
 *   bedrock-agentcore:InvokeAgentRuntime permission.
 * - Gateway → Lambda: Gateway IAM role has lambda:InvokeFunction.
 */
export class AgentCoreGatewayEventBridgeStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // -------------------------------------------------------------------
    // 1. EventBridge Custom Bus
    // -------------------------------------------------------------------
    const eventBus = new events.EventBus(this, 'AgentEventBus', {
      eventBusName: 'agent-outbound-events',
    });

    // -------------------------------------------------------------------
    // 2. Lambda Tool Backend (emit_event)
    // -------------------------------------------------------------------
    const emitEventFn = new lambda.Function(this, 'EmitEventFunction', {
      functionName: 'agentcore-emit-event',
      runtime: lambda.Runtime.PYTHON_3_12,
      handler: 'handler.handler',
      code: lambda.Code.fromAsset(path.join(__dirname, '..', '..', 'src', 'emit_event')),
      environment: {
        EVENT_BUS_NAME: eventBus.eventBusName,
        ALLOWED_SOURCES: 'agent.',
      },
      timeout: cdk.Duration.seconds(10),
    });

    eventBus.grantPutEventsTo(emitEventFn);

    // -------------------------------------------------------------------
    // 3. AgentCore Gateway (MCP server with Lambda target)
    // -------------------------------------------------------------------
    const gatewayRole = new iam.Role(this, 'GatewayRole', {
      assumedBy: new iam.ServicePrincipal('bedrock-agentcore.amazonaws.com', {
        conditions: {
          StringEquals: { 'aws:SourceAccount': this.account },
          ArnLike: { 'aws:SourceArn': `arn:aws:bedrock-agentcore:${this.region}:${this.account}:*` },
        },
      }),
      inlinePolicies: {
        GatewayPolicy: new iam.PolicyDocument({
          statements: [
            new iam.PolicyStatement({
              actions: ['lambda:InvokeFunction'],
              resources: [emitEventFn.functionArn],
            }),
            new iam.PolicyStatement({
              actions: ['logs:CreateLogGroup', 'logs:CreateLogStream', 'logs:PutLogEvents'],
              resources: [`arn:aws:logs:${this.region}:${this.account}:log-group:/aws/bedrock-agentcore/*`],
            }),
          ],
        }),
      },
    });

    const gateway = new bedrockagentcore.CfnGateway(this, 'EventEmitterGateway', {
      name: 'event-emitter-gateway',
      authorizerType: 'NONE',
      protocolType: 'MCP',
      protocolConfiguration: {
        mcp: {
          supportedVersions: ['2025-03-26'],
        },
      },
      roleArn: gatewayRole.roleArn,
      description: 'MCP Gateway exposing emit_event tool for agents to publish events to EventBridge',
    });

    emitEventFn.addPermission('GatewayInvoke', {
      principal: new iam.ServicePrincipal('bedrock-agentcore.amazonaws.com'),
      sourceArn: gateway.attrGatewayArn,
    });

    new bedrockagentcore.CfnGatewayTarget(this, 'EmitEventTarget', {
      gatewayIdentifier: gateway.attrGatewayIdentifier,
      name: 'emit-event-target',
      description: 'Lambda tool backend that publishes events to EventBridge',
      credentialProviderConfigurations: [
        { credentialProviderType: 'GATEWAY_IAM_ROLE' },
      ],
      targetConfiguration: {
        mcp: {
          lambda: {
            lambdaArn: emitEventFn.functionArn,
            toolSchema: {
              inlinePayload: [
                {
                  name: 'emit_event',
                  description: 'Emit a structured business event to the EventBridge bus. Use this to publish results, decisions, or state changes that other systems or agents should react to.',
                  inputSchema: {
                    type: 'object',
                    properties: {
                      source: { type: 'string', description: "Event source identifier. Must start with 'agent.'" },
                      detail_type: { type: 'string', description: "Event type (e.g. 'ClaimApproved', 'RiskAssessed')" },
                      detail: { type: 'object', description: 'Event payload with business data' },
                      notify: { type: 'boolean', description: 'If true, downstream rules also send an SNS notification' },
                    },
                    required: ['source', 'detail_type', 'detail'],
                  },
                },
              ],
            },
          },
        },
      },
    });

    // -------------------------------------------------------------------
    // 4. AgentCore Runtime (self-contained agent)
    // -------------------------------------------------------------------
    const agentImage = new ecrAssets.DockerImageAsset(this, 'AgentImage', {
      directory: path.join(__dirname, '..', '..', 'agent-code'),
      platform: ecrAssets.Platform.LINUX_ARM64,
    });

    const agentRuntimeName = 'agentcore_gateway_eventbridge_demo';

    const agentRuntimeRole = new iam.Role(this, 'AgentRuntimeRole', {
      assumedBy: new iam.ServicePrincipal('bedrock-agentcore.amazonaws.com', {
        conditions: {
          StringEquals: { 'aws:SourceAccount': this.account },
          ArnLike: { 'aws:SourceArn': `arn:aws:bedrock-agentcore:${this.region}:${this.account}:*` },
        },
      }),
      inlinePolicies: {
        AgentRuntimePolicy: new iam.PolicyDocument({
          statements: [
            new iam.PolicyStatement({ sid: 'ECRImageAccess', actions: ['ecr:BatchGetImage', 'ecr:GetDownloadUrlForLayer'], resources: [agentImage.repository.repositoryArn] }),
            new iam.PolicyStatement({ sid: 'ECRTokenAccess', actions: ['ecr:GetAuthorizationToken'], resources: ['*'] }),
            new iam.PolicyStatement({ actions: ['logs:DescribeLogStreams', 'logs:CreateLogGroup', 'logs:DescribeLogGroups'], resources: [`arn:aws:logs:${this.region}:${this.account}:log-group:/aws/bedrock-agentcore/*`] }),
            new iam.PolicyStatement({ actions: ['logs:CreateLogStream', 'logs:PutLogEvents'], resources: [`arn:aws:logs:${this.region}:${this.account}:log-group:/aws/bedrock-agentcore/runtimes/*:log-stream:*`] }),
            new iam.PolicyStatement({ actions: ['xray:PutTraceSegments', 'xray:PutTelemetryRecords', 'xray:GetSamplingRules', 'xray:GetSamplingTargets'], resources: ['*'] }),
            new iam.PolicyStatement({ actions: ['cloudwatch:PutMetricData'], resources: ['*'], conditions: { StringEquals: { 'cloudwatch:namespace': 'bedrock-agentcore' } } }),
            new iam.PolicyStatement({ sid: 'GetAgentAccessToken', actions: ['bedrock-agentcore:GetWorkloadAccessToken', 'bedrock-agentcore:GetWorkloadAccessTokenForJWT', 'bedrock-agentcore:GetWorkloadAccessTokenForUserId'], resources: [`arn:aws:bedrock-agentcore:${this.region}:${this.account}:workload-identity-directory/default`, `arn:aws:bedrock-agentcore:${this.region}:${this.account}:workload-identity-directory/default/workload-identity/${agentRuntimeName}-*`] }),
            new iam.PolicyStatement({ sid: 'BedrockModelInvocation', actions: ['bedrock:InvokeModel', 'bedrock:InvokeModelWithResponseStream'], resources: ['arn:aws:bedrock:*::foundation-model/*', `arn:aws:bedrock:${this.region}:${this.account}:*`] }),
          ],
        }),
      },
    });

    const agentRuntime = new bedrockagentcore.CfnRuntime(this, 'AgentRuntime', {
      agentRuntimeName,
      agentRuntimeArtifact: { containerConfiguration: { containerUri: agentImage.imageUri } },
      networkConfiguration: { networkMode: 'PUBLIC' },
      roleArn: agentRuntimeRole.roleArn,
      environmentVariables: { GATEWAY_MCP_URL: gateway.attrGatewayUrl },
    });

    // -------------------------------------------------------------------
    // 5. Downstream Consumers (fan-out from EventBridge)
    // -------------------------------------------------------------------
    const decisionLog = new dynamodb.Table(this, 'AgentDecisionLog', {
      tableName: 'agent-decision-log',
      partitionKey: { name: 'pk', type: dynamodb.AttributeType.STRING },
      sortKey: { name: 'sk', type: dynamodb.AttributeType.STRING },
      billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
      timeToLiveAttribute: 'ttl',
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    const notifyTopic = new sns.Topic(this, 'AgentNotifyTopic', {
      topicName: 'agent-event-notifications',
    });

    const allAgentEventsRule = new events.Rule(this, 'AllAgentEventsRule', {
      ruleName: 'agent-events-to-dynamodb',
      eventBus,
      eventPattern: { source: [{ prefix: 'agent.' }] as any },
    });

    const logWriterFn = new lambda.Function(this, 'LogWriterFunction', {
      functionName: 'agent-decision-log-writer',
      runtime: lambda.Runtime.PYTHON_3_12,
      handler: 'index.handler',
      code: lambda.Code.fromInline(`
import boto3, json, time, os
table = boto3.resource('dynamodb').Table(os.environ['TABLE_NAME'])
def handler(event, ctx):
    table.put_item(Item={
        'pk': f"{event['source']}#{event['detail-type']}",
        'sk': event['time'],
        'detail': json.dumps(event['detail']),
        'eventId': event['id'],
        'ttl': int(time.time()) + 30*86400
    })
    return {'statusCode': 200}
`),
      environment: { TABLE_NAME: decisionLog.tableName },
      timeout: cdk.Duration.seconds(10),
    });
    decisionLog.grantWriteData(logWriterFn);
    allAgentEventsRule.addTarget(new eventsTargets.LambdaFunction(logWriterFn));

    const notifyRule = new events.Rule(this, 'NotifyRule', {
      ruleName: 'agent-notify-events-to-sns',
      eventBus,
      eventPattern: { source: [{ prefix: 'agent.' }] as any, detail: { notify: [true] } },
    });
    notifyRule.addTarget(new eventsTargets.SnsTopic(notifyTopic));

    // -------------------------------------------------------------------
    // Outputs
    // -------------------------------------------------------------------
    new cdk.CfnOutput(this, 'GatewayUrl', { value: gateway.attrGatewayUrl, description: 'AgentCore Gateway MCP endpoint URL' });
    new cdk.CfnOutput(this, 'GatewayId', { value: gateway.attrGatewayIdentifier, description: 'Gateway identifier' });
    new cdk.CfnOutput(this, 'AgentRuntimeId', { value: agentRuntime.attrAgentRuntimeId, description: 'AgentCore Runtime ID' });
    new cdk.CfnOutput(this, 'AgentRuntimeArn', { value: agentRuntime.attrAgentRuntimeArn, description: 'AgentCore Runtime ARN (use for SigV4 invocation)' });
    new cdk.CfnOutput(this, 'EventBusName', { value: eventBus.eventBusName, description: 'EventBridge custom bus for agent-emitted events' });
    new cdk.CfnOutput(this, 'DecisionLogTableName', { value: decisionLog.tableName, description: 'DynamoDB table storing agent decision log' });
    new cdk.CfnOutput(this, 'NotifyTopicArn', { value: notifyTopic.topicArn, description: 'SNS topic for agent event notifications' });
  }
}
