import * as cdk from 'aws-cdk-lib';
import { ApiDestination, Authorization, Connection,Rule,EventBus } from 'aws-cdk-lib/aws-events';
import * as targets from 'aws-cdk-lib/aws-events-targets';
import {Queue} from 'aws-cdk-lib/aws-sqs';
import { Construct } from 'constructs';

export class EbApiDestinationStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);


    // dummy value here because target has no auth but connection requires this parameter
    // ignore or replace with a secure password/token if needed
    const apisecret = cdk.SecretValue.unsafePlainText("notused")
    const conn = new Connection(this, "connection", {
      authorization: Authorization.apiKey("notused", apisecret)
    }
    )

    const webhookUrl = '<INSERT_VALUE>'
    const apiDestination = new ApiDestination(this, "apidestination",
      {
        connection: conn,
        endpoint: webhookUrl,
        rateLimitPerSecond: 1,
      }
    )

    const dlq = new Queue(this, 'dlq')
    const bus = new EventBus(this, 'bus')
    const target = new targets.ApiDestination(apiDestination, {
      deadLetterQueue: dlq,
      retryAttempts: 3,
      headerParameters: {
        // https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/
        'Idempotency-Key': '$.detail.customID' // replace with desired field from your event
      }
    })
    const rule = new Rule(this, 'rule', {
      eventBus: bus,
      eventPattern: { account: [this.account] },
      targets: [target]
    })

    new cdk.CfnOutput(this, 'busArn', { value: bus.eventBusArn })
    new cdk.CfnOutput(this, 'ruleArn', { value: rule.ruleArn })
    new cdk.CfnOutput(this, 'dlqArn', { value: dlq.queueArn })
    new cdk.CfnOutput(this, 'apiDestinationArn', { value: apiDestination.apiDestinationArn })
  }
}
