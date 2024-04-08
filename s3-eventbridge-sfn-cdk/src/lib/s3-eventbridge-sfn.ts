import { 
  aws_iam as iam,
  aws_stepfunctions as sfn,
  aws_events as events,
  aws_events_targets as targets,
  aws_s3 as s3,
  aws_sqs as sqs,
  } from 'aws-cdk-lib';
import { Construct } from 'constructs';

/**
 * The properties for the S3EventbridgeStepFunctions service.
 */
export interface S3EventbridgeStepFunctionsProps {
  /**
   * The Step Functions statemachine that will be triggered by EventBridge
   */
  stateMachine: sfn.IStateMachine,
  /**
   * The StateMachine input JSON object
   */
  stateMachineInput : object,
  /**
   * The source S3 bucket which will trigger the EventBridge rule
   */
  sourceBucket: s3.IBucket,
  /**
   * The event pattern to trigger the target action
   * 
   * @default - Object created in S3 source bucket
   */
  eventPattern ?: events.EventPattern,
  /**
   * Determines whether a dead letter queue will be created for the event rule
   * @default true 
   */
  deadLetterQueue ?: boolean,
  
}

export class S3EventbridgeStepFunctions extends Construct {
  /**
   * The event rule created in this construct
   */
  public readonly eventRule: events.Rule;
  
  constructor(scope: Construct, id: string, props: S3EventbridgeStepFunctionsProps) {
    super(scope, id);

    props.sourceBucket.enableEventBridgeNotification();

    
    this.eventRule = new events.Rule(
      this,
      "EventsRule",
    );

    if (props.eventPattern){
      this.eventRule.addEventPattern(props.eventPattern)
    } else {
      this.eventRule.addEventPattern({
        source: ["aws.s3"],
        detailType:["Object Created"],
        detail: {
          "bucket": {
          "name": [props.sourceBucket.bucketName],
          }
        }}
      );
    }
    
    const eventRole = new iam.Role(
      this,
      "eventRole",
      {
        assumedBy: new iam.ServicePrincipal("events.amazonaws.com")
      }
    );

    props.stateMachine.grantStartExecution(eventRole)


    if (props.deadLetterQueue == false){
      this.eventRule.addTarget(new targets.SfnStateMachine(props.stateMachine, {
        input: events.RuleTargetInput.fromObject(props.stateMachineInput),
        role: eventRole,
      }));
    } else {
      const dlq = new sqs.Queue(
        this, 
        'DeadLetterQueue',
        {
          encryption: sqs.QueueEncryption.SQS_MANAGED,
          enforceSSL: true,
        }
        );
      this.eventRule.addTarget(new targets.SfnStateMachine(props.stateMachine, {
        input: events.RuleTargetInput.fromObject(props.stateMachineInput),
        deadLetterQueue: dlq,
        role: eventRole,
      }));
    }
    
  }
}
