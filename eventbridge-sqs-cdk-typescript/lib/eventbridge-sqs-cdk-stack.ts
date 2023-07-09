import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as eventbridgesqs from './eventbridge-sqs';


export class EventbridgeSqsCdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Create custom event bus
    const customEventBus = new cdk.aws_events.EventBus(this, 'eventbridgeSqs-eventbus', {
      eventBusName: 'MyCustomEventBus'
    });

    // Create custom sqs queue
    const customQueue = new cdk.aws_sqs.Queue(this, 'eventbridgeSqs-queue', {
      queueName: 'MyCustomQueue'
    })

    // Integrate eventbridge and sqs queue
    new eventbridgesqs.EventBridgeSqsConstruct(this, 'eventbridgeSqs', {
      eventBus: customEventBus,
      sqsQueue: customQueue,
    })
  }
}