import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb';
import * as eventsv2 from 'aws-cdk-lib/aws-eventsv2';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as sfn from 'aws-cdk-lib/aws-stepfunctions';
import * as tasks from 'aws-cdk-lib/aws-stepfunctions-tasks';

// Event types the workflow stores. Any other type is acknowledged and ignored.
const KNOWN_TYPES = ['order.created', 'order.shipped'];
// Transient PutItem errors (DynamoDB API reference). Retriers match only the errors they name,
// so ConditionalCheckFailedException (a duplicate delivery) is never retried.
const TRANSIENT = [
  'States.Timeout',
  'DynamoDB.InternalServerError',
  'DynamoDB.ProvisionedThroughputExceededException',
  'DynamoDB.RequestLimitExceeded',
  'DynamoDB.ThrottlingException',
];
const ITEM = '$states.input';

export class EventbridgeWebhookSfnStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // AWS::EventsV2 resources need a Name. Derive each one from the stack name so that
    // two stacks can deploy side by side and IAM conditions can match them.
    const sourceName = `${this.stackName}-webhook`;
    const subscriberName = `${this.stackName}-workflow`;

    const bus = new eventsv2.CfnEventBus(this, 'EventBus', { name: `${this.stackName}-bus` });

    // Role that Amazon EventBridge assumes to read the signing secret and put accepted requests on the bus
    const webhookRole = new iam.Role(this, 'WebhookRole', {
      assumedBy: new iam.ServicePrincipal('events.amazonaws.com', {
        conditions: {
          StringEquals: { 'aws:SourceAccount': this.account },
          ArnLike: { 'aws:SourceArn': this.formatArn({ service: 'events', resource: 'event-sourcev2', resourceName: `webhook/${sourceName}/*` }) },
        },
      }),
      inlinePolicies: {
        PutWebhookEvents: new iam.PolicyDocument({
          statements: [new iam.PolicyStatement({ actions: ['events:PutWebhookEvents'], resources: [bus.attrEventBusArn] })],
        }),
      },
    });

    // Webhook event source: EventBridge hosts the HTTPS URL, generates the HMAC secret in AWS Secrets Manager,
    // checks the signature and timestamp of every request, and drops repeats of the same content within 5 minutes.
    // aws-cdk-lib 2.278.0 types only the AWS service and partner variants of Configuration and has no attribute
    // for Details, so the webhook variant is set with a property override and read with getAtt.
    const source = new eventsv2.CfnEventSource(this, 'WebhookSource', {
      name: sourceName,
      eventBusArn: bus.attrEventBusArn,
      configuration: {},
    });
    source.addPropertyOverride('Configuration.WebhookEventsConfiguration', {
      RoleArn: webhookRole.roleArn,
      DeduplicationConfiguration: { DeduplicationType: 'CONTENT_BASED' },
      AuthConfiguration: {
        HmacAuthConfiguration: {
          Algorithm: 'SHA256',
          Encoding: 'HEX',
          SignatureHttpHeader: 'X-Signature',
          SignedMessageComposition: 'TIMESTAMP_DOT_BODY', // signs "<X-Timestamp>.<raw body>"
          TimestampHttpHeader: 'X-Timestamp',
          TimestampToleranceInSeconds: 300,
        },
      },
    });
    const webhookUrl = source.getAtt('Details.WebhookDetails.WebhookUrl').toString();
    const secretArn = source.getAtt('Details.WebhookDetails.SecretArn').toString();

    // Read access to this source's secret only. A separate policy, because the secret ARN exists only after the source.
    new iam.Policy(this, 'WebhookSecretRead', {
      roles: [webhookRole],
      statements: [new iam.PolicyStatement({ actions: ['secretsmanager:GetSecretValue'], resources: [secretArn] })],
    });

    // One item per webhook event; the event id is the key that makes the write idempotent
    const table = new dynamodb.Table(this, 'WebhookEventsTable', {
      partitionKey: { name: 'pk', type: dynamodb.AttributeType.STRING },
      billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      deletionProtection: false,
    });

    // Per event: known type -> conditional PutItem; first write "stored", a later copy "duplicate"; other types "ignored"
    const summary = (result: string) => `{% {'id': $string(${ITEM}.id), 'type': ${ITEM}.type, 'result': '${result}'} %}`;
    const store = tasks.DynamoPutItem.jsonata(this, 'StoreEvent', {
      table,
      item: {
        pk: tasks.DynamoAttributeValue.fromString(`{% $string(${ITEM}.id) %}`),
        eventType: tasks.DynamoAttributeValue.fromString(`{% ${ITEM}.type %}`),
        body: tasks.DynamoAttributeValue.fromString(`{% $string(${ITEM}) %}`),
        storedAt: tasks.DynamoAttributeValue.fromString('{% $now() %}'),
        executionId: tasks.DynamoAttributeValue.fromString('{% $states.context.Execution.Id %}'),
      },
      conditionExpression: 'attribute_not_exists(pk)',
      taskTimeout: sfn.Timeout.duration(cdk.Duration.seconds(10)),
      outputs: summary('stored'),
    });
    store.addRetry({ errors: TRANSIENT, interval: cdk.Duration.seconds(2), backoffRate: 2, maxAttempts: 3 });
    store.addCatch(sfn.Succeed.jsonata(this, 'AlreadyStored'), {
      errors: ['DynamoDB.ConditionalCheckFailedException'],
      outputs: summary('duplicate'),
    });
    store.addCatch(sfn.Succeed.jsonata(this, 'WriteFailed'), {
      errors: ['States.ALL'],
      outputs: `{% {'id': $string(${ITEM}.id), 'type': ${ITEM}.type, 'result': 'error', 'error': $states.errorOutput.Error} %}`,
    });

    // A string or number id is stored as a string key; any other id type is reported as ignored
    const route = new sfn.Choice(this, 'KnownEventType?', { queryLanguage: sfn.QueryLanguage.JSONATA })
      .when(sfn.Condition.jsonata(`{% $type(${ITEM}.id) in ['string', 'number'] and ${ITEM}.type in ${JSON.stringify(KNOWN_TYPES)} %}`), store)
      .otherwise(sfn.Pass.jsonata(this, 'IgnoreEvent', { outputs: summary('ignored') }));

    // The subscriber delivers a batch, so the execution input is a JSON array of raw request bodies
    const forEach = sfn.Map.jsonata(this, 'ForEachWebhookEvent', {
      items: sfn.ProvideItems.jsonata('{% $type($states.input) = "array" ? $states.input : [$states.input] %}'),
      maxConcurrency: 10,
    });
    forEach.itemProcessor(route);

    const outcome = new sfn.Choice(this, 'AllEventsHandled?', { queryLanguage: sfn.QueryLanguage.JSONATA })
      .when(sfn.Condition.jsonata("{% $count($states.input[result = 'error']) = 0 %}"), sfn.Succeed.jsonata(this, 'Done'))
      .otherwise(sfn.Fail.jsonata(this, 'EventNotStored', {
        error: 'WebhookEventNotStored',
        cause: "{% 'Not stored: ' & $string($states.input[result = 'error']) %}",
      }));

    const stateMachine = new sfn.StateMachine(this, 'WebhookWorkflow', {
      queryLanguage: sfn.QueryLanguage.JSONATA,
      definitionBody: sfn.DefinitionBody.fromChainable(forEach.next(outcome)),
      timeout: cdk.Duration.minutes(5),
    });

    // Subscriber: starts one execution per batch of up to 10 events that carry an id and a type
    const subscriberRole = new iam.Role(this, 'SubscriberRole', {
      assumedBy: new iam.ServicePrincipal('events.amazonaws.com', {
        conditions: {
          StringEquals: { 'aws:SourceAccount': this.account },
          ArnLike: { 'aws:SourceArn': this.formatArn({ service: 'events', resource: 'subscriber', resourceName: `${subscriberName}/*` }) },
        },
      }),
    });
    stateMachine.grantStartExecution(subscriberRole);
    const subscriber = new eventsv2.CfnSubscriber(this, 'WorkflowSubscriber', {
      name: subscriberName,
      eventBusArn: bus.attrEventBusArn,
      filterConfiguration: {
        filters: [{ scope: 'DATA', pattern: JSON.stringify({ id: [{ exists: true }], type: [{ exists: true }] }) }],
      },
      batchConfiguration: { maxBatchSize: 10, maxBatchWindowInSeconds: 0 },
      invokeConfiguration: {
        targetArn: stateMachine.stateMachineArn,
        roleArn: subscriberRole.roleArn,
        stepFunctionsParameters: { invocationType: 'EVENT' },
      },
    });
    subscriber.node.addDependency(subscriberRole);

    // The schema that aws-cdk-lib 2.278.0 validates against predates the webhook variant and its Details attributes
    const reason = 'The webhook event source variant is newer than the schema bundled with aws-cdk-lib';
    cdk.Validations.of(this).acknowledge(
      { id: 'CloudFormation-Validate::F3002', reason },
      { id: 'CloudFormation-Validate::F3018', reason },
      { id: 'CloudFormation-Validate::F6101', reason },
      { id: 'CloudFormation-Validate::E9004', reason },
    );

    // The URL is a credential together with the secret; see Important Notes in the README
    new cdk.CfnOutput(this, 'WebhookUrl', { value: webhookUrl });
    new cdk.CfnOutput(this, 'SecretArn', { value: secretArn });
    new cdk.CfnOutput(this, 'StateMachineArn', { value: stateMachine.stateMachineArn });
    new cdk.CfnOutput(this, 'TableName', { value: table.tableName });
  }
}
