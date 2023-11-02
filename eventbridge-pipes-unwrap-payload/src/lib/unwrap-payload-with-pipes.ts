import { CfnOutput, Duration, RemovalPolicy, Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { Queue } from 'aws-cdk-lib/aws-sqs';
import { CfnPipe } from 'aws-cdk-lib/aws-pipes';
import { EventBus, Rule, Match } from 'aws-cdk-lib/aws-events';
import { PolicyDocument, PolicyStatement, ServicePrincipal, Role } from 'aws-cdk-lib/aws-iam';
import { LogGroup } from 'aws-cdk-lib/aws-logs';
import { CloudWatchLogGroup } from 'aws-cdk-lib/aws-events-targets';
import { Code, Function, Runtime } from 'aws-cdk-lib/aws-lambda';
import { Topic } from 'aws-cdk-lib/aws-sns';
import { SqsSubscription } from 'aws-cdk-lib/aws-sns-subscriptions';
import { StateMachineType, StateMachine, Pass, Result, LogLevel, Map, JsonPath } from 'aws-cdk-lib/aws-stepfunctions';


// This code snippet demonstrates how to use Amazon EventBridge pipes to unwrap the payload of an event.

// 1. Event creation
//   a. Lambda puts three sample events on SNS
//   b. An SQS queue is subscribed to SNS topic, receiving the three events

// 2. Event processing
//   a. Using an EventBridge pipe, the events are sent to an EventBridge bus
//   b. A Lambda function is invoked by the pipe, enriching the event payload

// 3. Receiving and logging
//   a. The enriched event is sent to a second EventBridge bus
//   b. A CloudWatch Logs rule is subscribed to the second EventBridge bus, receiving the enriched event

export class UnwrapStack extends Stack {

  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    // create SNS topic
    const sourceTopic = new Topic(this, 'UnwrapSourceTopic', {
      fifo: false,
    });

    // Create AWS Lambda function that writes three sample messages to the topic to easily test the pipe
    const sampleDataCreatorLambda = new Function(this, 'UnwrapSampleDataCreatorLambda', {
      runtime: Runtime.NODEJS_18_X,
      timeout: Duration.seconds(30),
      code: Code.fromAsset('lib/lambda'),
      handler: 'unwrapSampleDataCreator.handler',
      environment: {
        SNS_TOPIC_ARN: sourceTopic.topicArn,
      }
    });
    sourceTopic.grantPublish(sampleDataCreatorLambda);

    // create SQS queue for option 1: using Lambda Enrichment
    const lamdaEnrichmentSourceQueue = new Queue(this, 'UnwrapSourceQueue1', {
      enforceSSL: true,
      deadLetterQueue: {
        maxReceiveCount: 1,
        queue: new Queue(this, 'UnwrapSourceDeadLetterQueue1', {
          enforceSSL: true,
        }),
      }
    });

    // create SQS queue for option 2: using Step Functions Enrichment
    const stepFunctionsEnrichmentSourceQueue = new Queue(this, 'UnwrapSourceQueue2', {
      enforceSSL: true,
      deadLetterQueue: {
        maxReceiveCount: 1,
        queue: new Queue(this, 'UnwrapSourceDeadLetterQueue2', {
          enforceSSL: true,
        }),
      }
    });

    // subscribe SQS queue to SNS topic
    sourceTopic.addSubscription(new SqsSubscription(lamdaEnrichmentSourceQueue));
    sourceTopic.addSubscription(new SqsSubscription(stepFunctionsEnrichmentSourceQueue));


    // create AWS Lambda function that unwraps the event payload
    // this is option 1 to unwrap the payload: using Lambda Enrichment
    const enrichmentLambda = new Function(this, 'UnwrapEnrichmentLambda', {
      runtime: Runtime.NODEJS_18_X,
      code: Code.fromAsset('lib/lambda'),
      handler: 'unwrapEnricher.handler',
    });

    // create AWS Step Functions state machine that unwraps the event payload
    // this is option 2 to unwrap the payload: using Step Functions Enrichment
    const enrichmentStepFunction = new StateMachine(this, 'UnwrapEnrichmentStepFunction', {
      stateMachineType: StateMachineType.EXPRESS,
      tracingEnabled: true,
      logs: {
        destination: new LogGroup(this, 'UnwrapEnrichmentSFNLogGroup', {
          logGroupName: '/aws/vendedlogs/UnwrapEnrichmentSFNLogGroup',
          removalPolicy: RemovalPolicy.DESTROY,
        }),
        includeExecutionData: true,
        level: LogLevel.ALL
      },
      definition: new Map(this, 'Map')
        .iterator(new Pass(this, 'UnwrapBody', {
          parameters: {
            Message: JsonPath.stringToJson(JsonPath.stringAt("$.body.Message")),
          },
          resultPath: '$.body',
        })
        
      /*  
        .next(new Pass(this, 'MergePayload', {
          parameters: {
            Message: JsonPath.jsonMerge(
              JsonPath.objectAt("$.body.Message"),
              JsonPath.objectAt("$.unwrappedPayload"),
            ),
          },
          resultPath: '$.mergedPayload',
        }))
        .next(new Pass(this, 'MergeAlreadyStringifiedContent', {
          parameters: {
            payload: JsonPath.jsonMerge(
              JsonPath.objectAt("$.mergedPayload.Message.payload"),
              JsonPath.objectAt("$.unwrappedAlreadyStringifiedContent")
            ),
          },
          resultPath: '$.mergedAlreadyStringifiedContent',
        }))
        .next(new Pass(this, 'MergeBack', {
          parameters: {
            Message: JsonPath.jsonMerge(
              JsonPath.objectAt("$.body.Message"),
              JsonPath.objectAt("$.mergedAlreadyStringifiedContent")
            ),
          },
          outputPath: '$.Message',
        }))*/
        ),
    });
       
    const unwrapTargetBus = new EventBus(this, 'UnwrapTargetBus', {
      eventBusName: 'unwrapTargetBus'
    });

    // create an Amazon EventBridge rule to send all events to Amazon CloudWatch Logs:
    const unwrapTargetLogRule = new Rule(this, 'UnwrapTargetLog', {
      ruleName: 'unwrapTargetLog',
      eventBus: unwrapTargetBus,
      eventPattern: {
        source: Match.prefix(''),
      },
      targets: [new CloudWatchLogGroup(new LogGroup(this, 'UnwrapLogGroup', {
        logGroupName: '/aws/events/unwrapTargetLog',
        removalPolicy: RemovalPolicy.DESTROY,
      }))],
    });

    const allowEventBridgePolicy = new PolicyDocument({
      statements: [
        new PolicyStatement({
          resources: [
            `arn:aws:logs:${process.env.CDK_DEFAULT_REGION}:${process.env.CDK_DEFAULT_ACCOUNT}:log-group:/aws/events/*:*"`,
          ],
          actions: ["logs:CreateLogStream", "logs:PutLogEvents"],
          principals: [new ServicePrincipal("amazonaws.com"), new ServicePrincipal("delivery.logs.amazonaws.com")],
        }),
      ],
    });

    // Create the pipe 1
    const pipeRole1 = new Role(this, 'UnwrapRole1', {
      assumedBy: new ServicePrincipal('pipes.amazonaws.com'),
    });

    lamdaEnrichmentSourceQueue.grantConsumeMessages(pipeRole1);
    enrichmentLambda.grantInvoke(pipeRole1);
    unwrapTargetBus.grantPutEventsTo(pipeRole1);

    const unwrapPipe1 = new CfnPipe(this, 'UnwrapPipe', {
      roleArn: pipeRole1.roleArn,
      source: lamdaEnrichmentSourceQueue.queueArn,
      sourceParameters: {
        sqsQueueParameters: {
          batchSize: 3,
        },
      },
      enrichment: enrichmentLambda.functionArn,
      // The stringified JSON payload within "body" can be unwrapped using an inputTemplate.
      // However, the attribute xx which is nested inside is still stringified.
      // This will be addressed within the enrichment function.
      enrichmentParameters: {
        inputTemplate: '{"body": <$.body>}',
      },
      target: unwrapTargetBus.eventBusArn,
    });

    // Create the pipe 2
    const pipeRole2 = new Role(this, 'UnwrapRole2', {
      assumedBy: new ServicePrincipal('pipes.amazonaws.com'),
    });

    stepFunctionsEnrichmentSourceQueue.grantConsumeMessages(pipeRole2);
    enrichmentStepFunction.grantStartSyncExecution(pipeRole2);
    unwrapTargetBus.grantPutEventsTo(pipeRole2);

    const unwrapPipe2 = new CfnPipe(this, 'UnwrapPipe2', {
      roleArn: pipeRole2.roleArn,
      source: stepFunctionsEnrichmentSourceQueue.queueArn,
      sourceParameters: {
        sqsQueueParameters: {
          batchSize: 3,
        },
      },
      enrichment: enrichmentStepFunction.stateMachineArn,
      // The stringified JSON payload within "body" can be unwrapped using an inputTemplate.
      // However, the attribute xx which is nested inside is still stringified.
      // This will be addressed within the enrichment function.
      enrichmentParameters: {
        inputTemplate: '{"body": <$.body>}',
      },
      target: unwrapTargetBus.eventBusArn,
    });

    // Relevant outputs so that the user can trigger this pattern and watch it in action.
    new CfnOutput(this, "UnwrapSampleDataCreatorLambdaArn", {
      value: sampleDataCreatorLambda.functionArn,
      exportName: "UnwrapSampleDataCreatorLambdaArn",
    });
  }
}