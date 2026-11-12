// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0
import * as path from 'path';
import { CfnOutput, Duration, Fn, RemovalPolicy, Stack, StackProps } from 'aws-cdk-lib';
import * as agentcore from 'aws-cdk-lib/aws-bedrockagentcore';
import * as cognito from 'aws-cdk-lib/aws-cognito';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as logs from 'aws-cdk-lib/aws-logs';
import { Construct } from 'constructs';

// The target name and the tool names form the Cedar action ids:
// AgentCore::Action::"<TARGET_NAME>___<tool name>" (three underscores).
const TARGET_NAME = 'OrdersTarget';
const RESOURCE_SERVER_ID = 'orders';

export class AgentcoreGatewayCedarStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    // Amazon Cognito: one resource server with two scopes and one app client per scope
    // (OAuth 2.0 client credentials). Each client can request only its own scope.
    const userPool = new cognito.UserPool(this, 'UserPool', {
      removalPolicy: RemovalPolicy.DESTROY,
    });
    const readScope = new cognito.ResourceServerScope({ scopeName: 'read', scopeDescription: 'Look up orders' });
    const cancelScope = new cognito.ResourceServerScope({ scopeName: 'cancel', scopeDescription: 'Cancel orders' });
    const resourceServer = userPool.addResourceServer('ResourceServer', {
      identifier: RESOURCE_SERVER_ID,
      scopes: [readScope, cancelScope],
    });
    // A Cognito domain prefix must be unique in the Region, so it includes the id of this stack.
    const domain = userPool.addDomain('Domain', {
      cognitoDomain: { domainPrefix: `agentcore-cedar-${Fn.select(2, Fn.split('/', this.stackId))}` },
    });
    const clientFor = (clientId: string, scope: cognito.ResourceServerScope) =>
      userPool.addClient(clientId, {
        generateSecret: true,
        oAuth: { flows: { clientCredentials: true }, scopes: [cognito.OAuthScope.resourceServer(resourceServer, scope)] },
      });
    const readerClient = clientFor('ReaderClient', readScope);
    const cancelerClient = clientFor('CancelerClient', cancelScope);

    // AWS Lambda: one function that serves both tools of the target.
    const toolFunction = new lambda.Function(this, 'ToolFunction', {
      runtime: lambda.Runtime.NODEJS_24_X,
      handler: 'handler.handler',
      code: lambda.Code.fromAsset(path.join(__dirname, '..', 'src')),
      timeout: Duration.seconds(10),
      logGroup: new logs.LogGroup(this, 'ToolFunctionLogs', {
        retention: logs.RetentionDays.ONE_WEEK,
        removalPolicy: RemovalPolicy.DESTROY,
      }),
    });

    // Policy engine (Policy in Amazon Bedrock AgentCore). Cedar denies by default: a tool call is allowed only when a permit policy matches.
    const policyEngine = new agentcore.PolicyEngine(this, 'PolicyEngine', {
      description: 'Per-tool Cedar authorization for the orders gateway',
    });

    // Service role of the gateway. The trust policy is limited to this account and to gateways in this Region
    // (the gateway ARN cannot be used here because the role must exist before the gateway). The default role of
    // the Gateway construct also keeps a trust statement without these conditions, so the stack supplies its own.
    const gatewayRole = new iam.Role(this, 'GatewayRole', {
      assumedBy: new iam.ServicePrincipal('bedrock-agentcore.amazonaws.com', {
        conditions: {
          StringEquals: { 'aws:SourceAccount': this.account },
          ArnLike: { 'aws:SourceArn': `arn:${this.partition}:bedrock-agentcore:${this.region}:${this.account}:gateway/*` },
        },
      }),
    });

    // Optional context value for the Testing section: -c policyMode=LOG_ONLY evaluates the policies without enforcing them, so denied calls go through. This stack enables no decision logging.
    const policyMode = this.node.tryGetContext('policyMode') ?? 'ENFORCE';
    if (!['ENFORCE', 'LOG_ONLY'].includes(policyMode)) {
      throw new Error(`policyMode must be ENFORCE or LOG_ONLY, got ${policyMode}`);
    }

    // Amazon Bedrock AgentCore Gateway: the JWT authorizer accepts tokens from the two Cognito clients only.
    // ENFORCE (the default here) makes the policy decision binding. The Gateway construct grants
    // the role the policy evaluation actions on this engine and gateway, and lambda:InvokeFunction on the target.
    const gateway = new agentcore.Gateway(this, 'Gateway', {
      description: 'MCP gateway with Cedar policy enforcement',
      role: gatewayRole,
      protocolConfiguration: agentcore.GatewayProtocol.mcp({
        supportedVersions: [agentcore.MCPProtocolVersion.MCP_2025_06_18],
      }),
      authorizerConfiguration: agentcore.GatewayAuthorizer.usingCognito({
        userPool,
        allowedClients: [readerClient, cancelerClient],
      }),
      policyEngineConfiguration: { policyEngine, mode: agentcore.PolicyEngineMode.of(policyMode) },
    });

    const target = gateway.addLambdaTarget('OrdersTarget', {
      gatewayTargetName: TARGET_NAME,
      description: 'Two order tools',
      lambdaFunction: toolFunction,
      toolSchema: agentcore.ToolSchema.fromInline(
        ['lookup_order', 'cancel_order'].map((name) => ({
          name,
          description: name === 'lookup_order' ? 'Look up the status of an order' : 'Cancel an order',
          inputSchema: {
            type: agentcore.SchemaDefinitionType.OBJECT,
            properties: { orderId: { type: agentcore.SchemaDefinitionType.STRING, description: 'Order id, for example 1001' } },
            required: ['orderId'],
          },
        })),
      ),
    });

    // One permit policy per tool. The scope claim comes from the access token that the gateway authorizer
    // has accepted: Cedar reads it as a tag of the AgentCore::OAuthUser principal. The request body is never
    // used. A "like" pattern matches substrings, so scope names must not contain each other.
    for (const [policyName, tool, scope] of [
      ['permit_lookup_order', 'lookup_order', `${RESOURCE_SERVER_ID}/${readScope.scopeName}`],
      ['permit_cancel_order', 'cancel_order', `${RESOURCE_SERVER_ID}/${cancelScope.scopeName}`],
    ]) {
      const policy = policyEngine.addPolicy(policyName, {
        policyName,
        statement: agentcore.PolicyStatement.fromCedar(`
          permit(
            principal is AgentCore::OAuthUser,
            action == AgentCore::Action::"${TARGET_NAME}___${tool}",
            resource == AgentCore::Gateway::"${gateway.gatewayArn}"
          ) when {
            principal.hasTag("scope") && principal.getTag("scope") like "*${scope}*"
          };`),
        validationMode: agentcore.PolicyValidationMode.FAIL_ON_ANY_FINDINGS,
      });
      // Policy validation checks the action names against the tools of the gateway, so create the target first.
      policy.node.addDependency(target);
    }

    new CfnOutput(this, 'GatewayUrl', { value: gateway.gatewayUrl ?? '' });
    new CfnOutput(this, 'TokenEndpoint', { value: `https://${domain.domainName}.auth.${this.region}.amazoncognito.com/oauth2/token` });
    new CfnOutput(this, 'UserPoolId', { value: userPool.userPoolId });
    new CfnOutput(this, 'ReaderClientId', { value: readerClient.userPoolClientId });
    new CfnOutput(this, 'CancelerClientId', { value: cancelerClient.userPoolClientId });
    new CfnOutput(this, 'ToolFunctionLogGroup', { value: toolFunction.logGroup.logGroupName });
  }
}
