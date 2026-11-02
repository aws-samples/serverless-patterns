import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as agentcore from 'aws-cdk-lib/aws-bedrockagentcore';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as sfn from 'aws-cdk-lib/aws-stepfunctions';
import * as tasks from 'aws-cdk-lib/aws-stepfunctions-tasks';
import * as sqs from 'aws-cdk-lib/aws-sqs';

export class AgentcoreGatewaySfnStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Approver inbox: the workflow puts the task token and the request here.
    // Task tokens are secrets, so the queue is encrypted and only accepts TLS.
    const inbox = new sqs.Queue(this, 'ApproverInbox', {
      encryption: sqs.QueueEncryption.SQS_MANAGED,
      enforceSSL: true,
      retentionPeriod: cdk.Duration.hours(2),
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    // Standard workflow with one callback task: it sends the task token to the
    // queue and waits until someone calls SendTaskSuccess or SendTaskFailure.
    const askApprover = new tasks.SqsSendMessage(this, 'AskApprover', {
      queue: inbox,
      messageBody: sfn.TaskInput.fromObject({
        taskToken: sfn.JsonPath.taskToken,
        request: sfn.JsonPath.entirePayload,
      }),
      integrationPattern: sfn.IntegrationPattern.WAIT_FOR_TASK_TOKEN,
      // SDK integrations have no timeout unless one is set.
      taskTimeout: sfn.Timeout.duration(cdk.Duration.hours(1)),
    });
    // No Retry on purpose: States.TaskFailed would also match a SendTaskFailure
    // from the approver and would ask again after a rejection. Other errors
    // end the execution with the error and cause from the task.
    askApprover.addCatch(
      new sfn.Fail(this, 'ApprovalTimedOut', {
        error: 'ApprovalTimedOut',
        cause: 'No SendTaskSuccess or SendTaskFailure arrived within one hour.',
      }),
      { errors: [sfn.Errors.TIMEOUT] },
    );

    const workflow = new sfn.StateMachine(this, 'ApprovalWorkflow', {
      stateMachineType: sfn.StateMachineType.STANDARD,
      definitionBody: sfn.DefinitionBody.fromChainable(askApprover),
    });

    // Gateway service role. AgentCore Gateway assumes it to call Step Functions.
    // Only the four operations that the two targets expose are allowed.
    // The Gateway ID does not exist yet when the role is created (the Gateway needs the role),
    // so the trust policy covers every Gateway in this account and Region.
    const gatewayRole = new iam.Role(this, 'GatewayRole', {
      assumedBy: new iam.ServicePrincipal('bedrock-agentcore.amazonaws.com', {
        conditions: {
          StringEquals: { 'aws:SourceAccount': this.account },
          ArnLike: {
            'aws:SourceArn': `arn:${this.partition}:bedrock-agentcore:${this.region}:${this.account}:gateway/*`,
          },
        },
      }),
      inlinePolicies: {
        StepFunctionsTools: new iam.PolicyDocument({
          statements: [
            new iam.PolicyStatement({
              actions: ['states:StartExecution'],
              resources: [workflow.stateMachineArn],
            }),
            new iam.PolicyStatement({
              actions: ['states:DescribeExecution'],
              resources: [
                this.formatArn({
                  service: 'states',
                  resource: 'execution',
                  resourceName: `${workflow.stateMachineName}:*`,
                  arnFormat: cdk.ArnFormat.COLON_RESOURCE_NAME,
                }),
              ],
            }),
            new iam.PolicyStatement({
              // IAM has no resource-level permissions for these two actions, so
              // "*" is required. The task token is the only control: treat it as a secret.
              actions: ['states:SendTaskSuccess', 'states:SendTaskFailure'],
              resources: ['*'],
            }),
          ],
        }),
      },
    });

    // The Gateway endpoint requires a SigV4 signature (AWS_IAM). Callers need
    // bedrock-agentcore:InvokeGateway on this Gateway. The protocol configuration is passed
    // explicitly because the L2 default turns on semantic search for the Gateway's tools.
    const gateway = new agentcore.Gateway(this, 'Gateway', {
      // Derived from the stack name so a second stack in the same Region does not collide.
      gatewayName: `${this.stackName}-gateway`,
      role: gatewayRole,
      authorizerConfiguration: agentcore.GatewayAuthorizer.usingAwsIam(),
      protocolConfiguration: agentcore.GatewayProtocol.mcp({
        // Requests without an MCP-Protocol-Version header are treated as 2025-03-26, so list both versions.
        supportedVersions: [agentcore.MCPProtocolVersion.MCP_2025_06_18, agentcore.MCPProtocolVersion.MCP_2025_03_26],
      }),
    });

    // The Step Functions connector has no L2 target class in aws-cdk-lib, so the targets use the L1.
    // Every configuration entry carries parameterValues. An entry without it makes target
    // creation fail in CloudFormation with "Connector configurations must not be empty",
    // so operations that are not pinned get an empty object.
    new agentcore.CfnGatewayTarget(this, 'OrdersTarget', {
      gatewayIdentifier: gateway.gatewayId,
      name: 'orders',
      credentialProviderConfigurations: [{ credentialProviderType: 'GATEWAY_IAM_ROLE' }],
      targetConfiguration: {
        mcp: {
          connector: {
            source: { connectorId: 'states' },
            configurations: [
              // Pinned: the agent cannot see or change the state machine.
              { name: 'StartExecution', parameterValues: { stateMachineArn: workflow.stateMachineArn } },
              { name: 'DescribeExecution', parameterValues: {} },
            ],
          },
        },
      },
    });
    // Task-token operations go once per Gateway on a separate target.
    new agentcore.CfnGatewayTarget(this, 'TasksTarget', {
      gatewayIdentifier: gateway.gatewayId,
      name: 'tasks',
      credentialProviderConfigurations: [{ credentialProviderType: 'GATEWAY_IAM_ROLE' }],
      targetConfiguration: {
        mcp: {
          connector: {
            source: { connectorId: 'states' },
            configurations: [
              { name: 'SendTaskSuccess', parameterValues: {} },
              { name: 'SendTaskFailure', parameterValues: {} },
            ],
          },
        },
      },
    });

    new cdk.CfnOutput(this, 'GatewayUrl', { value: gateway.gatewayUrl! });
    new cdk.CfnOutput(this, 'GatewayArn', { value: gateway.gatewayArn });
    new cdk.CfnOutput(this, 'StateMachineArn', { value: workflow.stateMachineArn });
    new cdk.CfnOutput(this, 'QueueUrl', { value: inbox.queueUrl });
  }
}
