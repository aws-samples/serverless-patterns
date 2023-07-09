import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { CfnOutput, Duration } from 'aws-cdk-lib';
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';
import { aws_lambda as lambda, aws_events_targets as events_targets } from 'aws-cdk-lib';
import * as path from 'path';
import { Effect, PolicyStatement } from 'aws-cdk-lib/aws-iam';

import { EventBus, Rule } from 'aws-cdk-lib/aws-events';

const lambdaDefaults = {
  memorySize: 1024,
  timeout: Duration.seconds(5),
  runtime: lambda.Runtime.NODEJS_16_X,
  handler: 'handler',
};

export class SingleBusEnrichmentWithLambda extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // create event bus for this demo, or you can swap this out with your own
    const mainBus = new EventBus(this, 'myapp-event-bus', { eventBusName: 'MyMainBus' });

    // example of a producer, this lambda produces the event with the `enrichment` flag
    const producerLambda: NodejsFunction = new NodejsFunction(this, 'producer', {
      ...lambdaDefaults,
      entry: path.join(__dirname, '../src/producer/index.ts'),
      environment: {
        EVENT_BUS_NAME: mainBus.eventBusName,
      },
      initialPolicy: [
        new PolicyStatement({
          effect: Effect.ALLOW,
          resources: [mainBus.eventBusArn],
          actions: ['events:PutEvents'],
        }),
      ],
    });

    // the enricher (lambda), this takes the event, enriches it and throws it back onto te bus (without enrichment flag)
    const enricherLambda: NodejsFunction = new NodejsFunction(this, 'enrichFunction', {
      ...lambdaDefaults,
      entry: path.join(__dirname, '../src/enricher/index.ts'),
      environment: {
        EVENT_BUS_NAME: mainBus.eventBusName,
      },
      initialPolicy: [
        new PolicyStatement({
          effect: Effect.ALLOW,
          resources: [mainBus.eventBusArn],
          actions: ['events:PutEvents'],
        }),
      ],
    });

    // test consumer for the event, just to show you how the event will be consumed.
    const consumerLambda: NodejsFunction = new NodejsFunction(this, 'consumerFunction', {
      ...lambdaDefaults,
      entry: path.join(__dirname, '../src/consumer/index.ts'),
    });

    // rule to match all events that need enriching (important! You have to listen for enrich flags)
    new Rule(this, 'EnricherRule', {
      description: 'Enrich all events',
      eventPattern: {
        detail: {
          metadata: {
            // if the event needs enriching then forward it to the enricher
            enrich: [{ exists: true }],
          },
        },
      },
      eventBus: mainBus,
    }).addTarget(new events_targets.LambdaFunction(enricherLambda));

    // setup example rule for the consumer (important! you have to make sure enrich flag is not there)
    const rule = new Rule(this, 'OrderCreatedRule', {
      eventPattern: {
        detailType: ['OrderCreated'],
        detail: {
          metadata: {
            // node: you have to make sure you only consume events without `enrich` flag on.
            enrich: [{ exists: false }],
          },
        },
      },
      eventBus: mainBus,
    });

    rule.addTarget(new events_targets.LambdaFunction(consumerLambda));

    // Outputs
    new CfnOutput(this, 'ProducerFunctionName', { value: producerLambda.functionName });
    new CfnOutput(this, 'ConsumerFunctionName', { value: consumerLambda.functionName });
  }
}
