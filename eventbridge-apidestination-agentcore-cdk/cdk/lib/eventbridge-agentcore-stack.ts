import * as path from 'path';
import * as cdk from 'aws-cdk-lib';
import * as bedrockagentcore from 'aws-cdk-lib/aws-bedrockagentcore';
import * as cognito from 'aws-cdk-lib/aws-cognito';
import * as ecrAssets from 'aws-cdk-lib/aws-ecr-assets';
import * as events from 'aws-cdk-lib/aws-events';
import * as targets from 'aws-cdk-lib/aws-events-targets';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as sqs from 'aws-cdk-lib/aws-sqs';
import { Construct } from 'constructs';

/**
 * EventBridge API Destination -> Amazon Bedrock AgentCore Runtime
 * "Lambda-less" event-driven agent invocation.
 *
 * Flow:
 *   EventBridge Rule -> API Destination (HTTPS, OAuth via Cognito M2M)
 *     -> AgentCore Runtime InvokeAgentRuntime endpoint (async processing)
 *
 * This stack is fully self-contained: it builds and deploys the AgentCore
 * Runtime (from the bundled agent-code/ Docker image) alongside the
 * EventBridge plumbing, so `cdk deploy` produces a working, testable
 * pattern with no manual "update the runtime's authorizer" step.
 *
 * Key design decisions:
 *
 * 1. ASYNC execution: API Destinations enforce a hard 5-second timeout on
 *    target responses. Agent reasoning takes far longer than 5 seconds, so
 *    the AgentCore Runtime must acknowledge the request immediately (HTTP 2xx)
 *    and continue processing in the background (async invocation mode).
 *    See agent-code/agent.py for the entrypoint implementation.
 *
 * 2. URL encoding gotcha: API Destinations automatically decode %XX sequences
 *    in the endpoint URL. A URL-encoded runtime ARN in the path (which
 *    contains ":" and "/") gets decoded back and breaks the request. We
 *    therefore use the plain agent runtime ID (CfnRuntime.attrAgentRuntimeId)
 *    in the path and pass the account ID as a query parameter — no URL
 *    encoding needed.
 *
 * 3. Auth: Cognito User Pool with a Resource Server (client_credentials
 *    grant). The EventBridge Connection fetches OAuth tokens from the Cognito
 *    token endpoint; the AgentCore Runtime validates the JWT via its inbound
 *    identity (customJwtAuthorizer), configured at creation time against the
 *    same Cognito user pool — no two-step deploy required.
 */
export class EventBridgeAgentCoreStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // -------------------------------------------------------------------
    // 1. Cognito User Pool for machine-to-machine (M2M) authentication
    // -------------------------------------------------------------------
    const userPool = new cognito.UserPool(this, 'AgentAuthUserPool', {
      userPoolName: 'agentcore-m2m-pool',
      selfSignUpEnabled: false,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    // Hosted domain is required so the OAuth2 token endpoint exists.
    const userPoolDomain = userPool.addDomain('AgentAuthDomain', {
      cognitoDomain: {
        // Domain prefix must be globally unique per region.
        domainPrefix: `agentcore-invoke-${this.account}`,
      },
    });

    // Resource server defines the custom scope granted to the M2M client.
    const invokeScope = new cognito.ResourceServerScope({
      scopeName: 'invoke',
      scopeDescription: 'Invoke the AgentCore Runtime',
    });

    const resourceServer = userPool.addResourceServer('AgentResourceServer', {
      identifier: 'agentcore',
      userPoolResourceServerName: 'agentcore',
      scopes: [invokeScope],
    });

    // App client using the client_credentials grant (M2M, no user login).
    const appClient = userPool.addClient('EventBridgeM2MClient', {
      userPoolClientName: 'eventbridge-connection-client',
      generateSecret: true,
      oAuth: {
        flows: {
          clientCredentials: true,
        },
        scopes: [cognito.OAuthScope.resourceServer(resourceServer, invokeScope)],
      },
      authFlows: {
        userSrp: false,
        userPassword: false,
      },
    });

    const tokenEndpoint = `https://${userPoolDomain.domainName}.auth.${this.region}.amazoncognito.com/oauth2/token`;

    // -------------------------------------------------------------------
    // 2. EventBridge Connection (OAuth client_credentials -> Cognito)
    // -------------------------------------------------------------------
    const connection = new events.Connection(this, 'AgentCoreConnection', {
      connectionName: 'agentcore-cognito-oauth',
      description:
        'OAuth client_credentials connection to Cognito for AgentCore Runtime invocation',
      authorization: events.Authorization.oauth({
        authorizationEndpoint: tokenEndpoint,
        clientId: appClient.userPoolClientId,
        clientSecret: appClient.userPoolClientSecret,
        httpMethod: events.HttpMethod.POST,
        bodyParameters: {
          grant_type: events.HttpParameter.fromString('client_credentials'),
          scope: events.HttpParameter.fromString('agentcore/invoke'),
        },
      }),
    });

    // -------------------------------------------------------------------
    // 3. AgentCore Runtime — build from the bundled agent-code/ Dockerfile
    //    and deploy it, with its JWT authorizer pointed at the Cognito
    //    user pool created above. No separate "bring your own runtime"
    //    step: this stack is self-contained end to end.
    // -------------------------------------------------------------------
    const agentImage = new ecrAssets.DockerImageAsset(this, 'AgentImage', {
      directory: path.join(__dirname, '..', '..', 'agent-code'),
      platform: ecrAssets.Platform.LINUX_ARM64,
    });

    const agentRuntimeName = 'eventbridge_apidestination_agentcore_demo';

    // NOTE: these statements are attached as an INLINE policy on the role
    // (not via role.addToPolicy, which would create a separate
    // AWS::IAM::Policy resource). The CfnRuntime below only references the
    // role's ARN, so CloudFormation would not otherwise wait for a separate
    // policy to attach before creating the runtime — and the runtime
    // assumes this role immediately to validate the ECR image. Keeping the
    // permissions inline makes them part of the AWS::IAM::Role resource that
    // the runtime depends on, avoiding an IAM propagation race.
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
            new iam.PolicyStatement({
              sid: 'ECRImageAccess',
              actions: ['ecr:BatchGetImage', 'ecr:GetDownloadUrlForLayer'],
              resources: [agentImage.repository.repositoryArn],
            }),
            new iam.PolicyStatement({
              sid: 'ECRTokenAccess',
              actions: ['ecr:GetAuthorizationToken'],
              // ecr:GetAuthorizationToken does not support resource-level permissions.
              resources: ['*'],
            }),
            new iam.PolicyStatement({
              actions: ['logs:DescribeLogStreams', 'logs:CreateLogGroup'],
              resources: [`arn:aws:logs:${this.region}:${this.account}:log-group:/aws/bedrock-agentcore/runtimes/*`],
            }),
            new iam.PolicyStatement({
              actions: ['logs:DescribeLogGroups'],
              resources: [`arn:aws:logs:${this.region}:${this.account}:log-group:*`],
            }),
            new iam.PolicyStatement({
              actions: ['logs:CreateLogStream', 'logs:PutLogEvents'],
              resources: [`arn:aws:logs:${this.region}:${this.account}:log-group:/aws/bedrock-agentcore/runtimes/*:log-stream:*`],
            }),
            new iam.PolicyStatement({
              actions: ['xray:PutTraceSegments', 'xray:PutTelemetryRecords', 'xray:GetSamplingRules', 'xray:GetSamplingTargets'],
              // X-Ray actions do not support resource-level permissions.
              resources: ['*'],
            }),
            new iam.PolicyStatement({
              actions: ['cloudwatch:PutMetricData'],
              resources: ['*'],
              conditions: { StringEquals: { 'cloudwatch:namespace': 'bedrock-agentcore' } },
            }),
            new iam.PolicyStatement({
              sid: 'GetAgentAccessToken',
              actions: [
                'bedrock-agentcore:GetWorkloadAccessToken',
                'bedrock-agentcore:GetWorkloadAccessTokenForJWT',
                'bedrock-agentcore:GetWorkloadAccessTokenForUserId',
              ],
              resources: [
                `arn:aws:bedrock-agentcore:${this.region}:${this.account}:workload-identity-directory/default`,
                `arn:aws:bedrock-agentcore:${this.region}:${this.account}:workload-identity-directory/default/workload-identity/${agentRuntimeName}-*`,
              ],
            }),
            new iam.PolicyStatement({
              sid: 'BedrockModelInvocation',
              actions: ['bedrock:InvokeModel', 'bedrock:InvokeModelWithResponseStream'],
              resources: ['arn:aws:bedrock:*::foundation-model/*', `arn:aws:bedrock:${this.region}:${this.account}:*`],
            }),
          ],
        }),
      },
    });

    const discoveryUrl = `https://cognito-idp.${this.region}.amazonaws.com/${userPool.userPoolId}/.well-known/openid-configuration`;

    const agentRuntime = new bedrockagentcore.CfnRuntime(this, 'AgentRuntime', {
      agentRuntimeName,
      agentRuntimeArtifact: {
        containerConfiguration: {
          containerUri: agentImage.imageUri,
        },
      },
      networkConfiguration: {
        networkMode: 'PUBLIC',
      },
      roleArn: agentRuntimeRole.roleArn,
      authorizerConfiguration: {
        customJwtAuthorizer: {
          discoveryUrl,
          allowedClients: [appClient.userPoolClientId],
        },
      },
    });

    // -------------------------------------------------------------------
    // 4. API Destination -> AgentCore Runtime InvokeAgentRuntime endpoint
    // -------------------------------------------------------------------
    // NOTE: plain agent runtime ID in the path + accountId as a query
    // parameter. Do NOT use the URL-encoded full ARN — API Destinations
    // decode %XX sequences in the URL and would corrupt it.
    const invocationEndpoint =
      `https://bedrock-agentcore.${this.region}.amazonaws.com` +
      `/runtimes/${agentRuntime.attrAgentRuntimeId}/invocations` +
      `?accountId=${this.account}&qualifier=DEFAULT`;

    const apiDestination = new events.ApiDestination(this, 'AgentCoreApiDestination', {
      apiDestinationName: 'agentcore-runtime-invoke',
      connection,
      endpoint: invocationEndpoint,
      httpMethod: events.HttpMethod.POST,
      rateLimitPerSecond: 10,
      description:
        'Invokes the AgentCore Runtime asynchronously (runtime must ack within 5s)',
    });

    // -------------------------------------------------------------------
    // 5. Event bus, DLQ, and rule
    // -------------------------------------------------------------------
    const eventBus = new events.EventBus(this, 'AgentEventBus', {
      eventBusName: 'agentcore-events',
    });

    // Failed deliveries (after retries) land here for inspection/redrive.
    const dlq = new sqs.Queue(this, 'DeliveryDlq', {
      queueName: 'agentcore-invoke-dlq',
      retentionPeriod: cdk.Duration.days(14),
      enforceSSL: true,
    });

    const rule = new events.Rule(this, 'InvokeAgentRule', {
      ruleName: 'invoke-agentcore-on-order-event',
      eventBus,
      description: 'Routes order events to the AgentCore Runtime via API Destination',
      eventPattern: {
        source: ['demo.orders'],
        detailType: ['OrderCreated'],
      },
    });

    rule.addTarget(
      new targets.ApiDestination(apiDestination, {
        deadLetterQueue: dlq,
        retryAttempts: 3,
        maxEventAge: cdk.Duration.minutes(10),
        // Shape the payload the agent receives. AgentCore Runtime expects a
        // JSON body; the "prompt" key is what a typical agent entrypoint
        // reads. Adjust to match your agent's input contract.
        event: events.RuleTargetInput.fromObject({
          prompt: events.EventField.fromPath('$.detail.prompt'),
          orderId: events.EventField.fromPath('$.detail.orderId'),
          eventId: events.EventField.eventId,
          source: events.EventField.source,
        }),
      })
    );

    // -------------------------------------------------------------------
    // Outputs
    // -------------------------------------------------------------------
    new cdk.CfnOutput(this, 'EventBusName', {
      value: eventBus.eventBusName,
      description: 'Custom event bus to publish test events to',
    });

    new cdk.CfnOutput(this, 'ApiDestinationEndpoint', {
      value: invocationEndpoint,
      description: 'AgentCore Runtime invocation URL used by the API Destination',
    });

    new cdk.CfnOutput(this, 'CognitoTokenEndpoint', {
      value: tokenEndpoint,
      description: 'OAuth2 token endpoint used by the EventBridge Connection',
    });

    new cdk.CfnOutput(this, 'CognitoDiscoveryUrl', {
      value: discoveryUrl,
      description: 'OIDC discovery URL used by the AgentCore Runtime customJwtAuthorizer',
    });

    new cdk.CfnOutput(this, 'CognitoAppClientId', {
      value: appClient.userPoolClientId,
      description: 'App client ID trusted by the AgentCore Runtime customJwtAuthorizer',
    });

    new cdk.CfnOutput(this, 'AgentRuntimeArn', {
      value: agentRuntime.attrAgentRuntimeArn,
      description: 'ARN of the deployed AgentCore Runtime',
    });

    new cdk.CfnOutput(this, 'AgentRuntimeId', {
      value: agentRuntime.attrAgentRuntimeId,
      description: 'ID of the deployed AgentCore Runtime (used in the invocation URL)',
    });

    new cdk.CfnOutput(this, 'DeadLetterQueueUrl', {
      value: dlq.queueUrl,
      description: 'SQS DLQ for failed deliveries to the API Destination',
    });
  }
}
