import * as cdk from 'aws-cdk-lib';
import { ApiDestination, Authorization, Connection, EventField, RuleTargetInput } from 'aws-cdk-lib/aws-events';
import * as targets from 'aws-cdk-lib/aws-events-targets';
import { Construct } from 'constructs';


export class EventbridgeApiDestinationsCloudeventsCdkTypescriptStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const dlq = new cdk.aws_sqs.Queue(this, 'DLQ', {
    })

    const bus = new cdk.aws_events.EventBus(this, 'Bus', {
    })

    // dummy value here because target has no auth but connection requires this parameter
    // ignore or replace with a secure password/token if needed
    const apisecret = cdk.SecretValue.unsafePlainText("notused")
    const conn = new Connection(this, "connection", {
      authorization: Authorization.apiKey("notused", apisecret)
    }
    )

    const webhookUrl = '<INSERT_YOUR_HTTPS_TARGET_URL>'
    const apiDestination = new ApiDestination(this, "apidestination",
      {
        connection: conn,
        endpoint: webhookUrl,
        rateLimitPerSecond: 1,
      }
    )

    // structured mode CloudEvent
    const structuredCeTransformer = {
      specversion: "1.0",
      id: EventField.eventId,
      source: EventField.source,
      type: EventField.detailType,
      time: EventField.time,
      region: EventField.region,
      data: EventField.fromPath('$.detail')
    }

    const structuredModeCeTarget = new targets.ApiDestination(apiDestination, {
      deadLetterQueue: dlq,
      retryAttempts: 3,
      event: RuleTargetInput.fromObject(structuredCeTransformer),
      headerParameters: {
        // https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/bindings/http-protocol-binding.md#321-http-content-type
        "Content-Type": "application/cloudevents+json; charset=UTF-8",
      }
    })

    // binary mode CloudEvent
    const binaryModeCeTarget = new targets.ApiDestination(apiDestination, {
      deadLetterQueue: dlq,
      retryAttempts: 3,
      event: RuleTargetInput.fromEventPath('$.detail'),
      headerParameters: {
        "Content-Type": "application/json; charset=UTF-8", // also EventBridge default
        "ce-specversion": "1.0",
        "ce-id": EventField.eventId,
        "ce-source": EventField.source,
        "ce-type": EventField.detailType,
        "ce-time": EventField.time,
        "region": EventField.region,
      }
    })

    const rule = new cdk.aws_events.Rule(this, 'Rule', {
      eventBus: bus,
      eventPattern: {
        account: [cdk.Stack.of(this).account],
      },
      targets: [structuredModeCeTarget, binaryModeCeTarget],
    }
    )

    new cdk.CfnOutput(this, "webhookUrl", {
      value: webhookUrl
    })

    new cdk.CfnOutput(this, "busArn", {
      value: bus.eventBusArn,
    })

    new cdk.CfnOutput(this, "dlqArn", {
      value: dlq.queueArn,
    })

    new cdk.CfnOutput(this, "ruleArn", {
      value: rule.ruleArn,
    })

    new cdk.CfnOutput(this, "apiDestinationArn", {
      value: apiDestination.apiDestinationArn,
    })
  }
}
