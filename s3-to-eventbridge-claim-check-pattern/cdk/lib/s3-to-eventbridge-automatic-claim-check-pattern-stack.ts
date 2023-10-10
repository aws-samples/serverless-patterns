import * as path from 'path';
import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
// import * as sqs from 'aws-cdk-lib/aws-sqs';

import * as s3 from 'aws-cdk-lib/aws-s3';
import { Duration, RemovalPolicy } from 'aws-cdk-lib';
import { EventBus, Rule } from 'aws-cdk-lib/aws-events';
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';
import { Runtime } from 'aws-cdk-lib/aws-lambda';
import { aws_events_targets as events_targets } from 'aws-cdk-lib';

export class S3ToEventbridgeAutomaticClaimCheckPatternStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Create a new S3 bucket for claim processing
    const bucket = new s3.Bucket(this, 'claims-bucket', {
      removalPolicy: RemovalPolicy.DESTROY,
      // All s3 events will go to eventbridge here (default bus)
      eventBridgeEnabled: true,
    });

    const defaultBus = EventBus.fromEventBusName(this, 'defaultBus', 'default');

    const customEventBus = new EventBus(this, 'customBus', {
      eventBusName: 'InsuranceBus',
    });

    /**
     * Lambda function that will take orginal s3 event, enrich/transform into custom domain event
     */
    const transformerFunction: NodejsFunction = new NodejsFunction(this, 'transformerFunction', {
      memorySize: 1024,
      timeout: Duration.seconds(5),
      runtime: Runtime.NODEJS_16_X,
      handler: 'handler',
      environment: {
        EVENT_BUS_NAME: customEventBus.eventBusName,
      },
      entry: path.join(__dirname, '../src/s3-to-domain-event-transformer/index.ts'),
    });

    // Give lambda function access to put events onto the bus
    customEventBus.grantPutEventsTo(transformerFunction);
    bucket.grantRead(transformerFunction);

    // rule to match all events that need enriching
    new Rule(this, 'transformerRule', {
      description: 'Transform all s3 events from claims',
      eventPattern: {
        source: ['aws.s3'],
        detailType: ['Object Created', 'Object Deleted'],
        detail: {
          object: {
            key: [{ prefix: 'claims/' }],
          },
        },
      },
      // all events are sent to s3 so we have to listen to from there
      eventBus: defaultBus,
    }).addTarget(new events_targets.LambdaFunction(transformerFunction));

    // a consumer for the claim created event (requests information from s3...)
    const claimCreatedConsumer: NodejsFunction = new NodejsFunction(this, 'claimCreatedConsumer', {
      memorySize: 1024,
      timeout: Duration.seconds(5),
      runtime: Runtime.NODEJS_16_X,
      handler: 'handler',
      entry: path.join(__dirname, '../src/consumers/ClaimCreated/index.ts'),
    });

    // rule for claim created lambda
    new Rule(this, 'ClaimCreatedRule', {
      description: 'Listen to claim created',
      eventPattern: {
        detailType: ['ClaimCreated'],
      },
      // all events are sent to s3 so we have to listen to from there
      eventBus: customEventBus,
    }).addTarget(new events_targets.LambdaFunction(claimCreatedConsumer));

    // a consumer for the claim processed event (requests information from s3...)
    const claimProcessedConsumer: NodejsFunction = new NodejsFunction(this, 'claimProcessedConsumer', {
      memorySize: 1024,
      timeout: Duration.seconds(5),
      runtime: Runtime.NODEJS_16_X,
      handler: 'handler',
      entry: path.join(__dirname, '../src/consumers/ClaimProcessed/index.ts'),
    });

    // rule for claim created lambda
    new Rule(this, 'ClaimProcessedRule', {
      description: 'Listen to claim processed event',
      eventPattern: {
        detailType: ['ClaimProcessed'],
      },
      // all events are sent to s3 so we have to listen to from there
      eventBus: customEventBus,
    }).addTarget(new events_targets.LambdaFunction(claimProcessedConsumer));

   
  }
}
