import {
  aws_events as events,
  aws_events_targets as targets,
  aws_sqs as sqs,
  CfnOutput as cfnOutput,
} from 'aws-cdk-lib';
import { Construct } from 'constructs';

export interface EventBridgeSqsProps {

  /**
   * EventBridge event bus object
   */
  readonly eventBus? : events.IEventBus;

  /**
   * SQS Queue object
   */
  readonly sqsQueue? : sqs.Queue;

}

/**
* To create an EventBridge rule that involes an SQS queue
*/
export class EventBridgeSqsConstruct extends Construct {
 public customEventBus: events.IEventBus;
 public customQueue: sqs.IQueue;

  constructor(scope: Construct, id: string, props: EventBridgeSqsProps) {
    super(scope, id);

    // Create EventBus
    this.customEventBus = props.eventBus ?? (new events.EventBus(this, 'eventbridgeSqs-eventbus', {eventBusName: 'eventbridgeSqs-eventbus'}));
    
    // Create rule
    const rule = new events.Rule(this, 'eventbridgeSqs-eventRule', {
      ruleName: 'eventbridgeSqs-eventRule',
      eventBus: this.customEventBus
    });

    // Add event pattern to rule
    rule.addEventPattern({
      source: ['my-cdk-application'],
      detailType: ['message-for-queue']
    });

    // Create SQS queue;
    this.customQueue = props.sqsQueue ?? (new sqs.Queue(this, 'eventbridgeSqs-queue', {queueName: 'eventbridgeSqs-queue'}))

    // Set SQS queue as destination of event bus
    rule.addTarget(new targets.SqsQueue(this.customQueue));

    new cfnOutput(this, 'EventBusName', { value: this.customEventBus.eventBusName });
    new cfnOutput(this, 'RuleName', { value: rule.ruleName });
    new cfnOutput(this, 'SqsQueueName', { value: this.customQueue.queueName });

  }
}

  