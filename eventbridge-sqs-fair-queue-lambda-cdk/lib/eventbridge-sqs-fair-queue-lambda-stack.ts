import * as cdk from "aws-cdk-lib";
import * as sqs from "aws-cdk-lib/aws-sqs";
import * as lambda from "aws-cdk-lib/aws-lambda";
import * as events from "aws-cdk-lib/aws-events";
import * as iam from "aws-cdk-lib/aws-iam";
import * as logs from "aws-cdk-lib/aws-logs";
import { Construct } from "constructs";

export class EventBridgeSqsFairQueueLambdaStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Dead-letter queue for failed messages
    const dlq = new sqs.Queue(this, "DLQ", {
      queueName: "fair-queue-dlq",
      retentionPeriod: cdk.Duration.days(14),
    });

    // SQS Fair Queue (uses CfnQueue — fair queues are a new queue type)
    const cfnFairQueue = new sqs.CfnQueue(this, "FairQueue", {
      queueName: "tenant-fair-queue",
      visibilityTimeout: 60,
      messageRetentionPeriod: 345600, // 4 days
      redrivePolicy: {
        deadLetterTargetArn: dlq.queueArn,
        maxReceiveCount: 3,
      },
    });

    // Enable fair queue configuration via property override
    (cfnFairQueue as any).addPropertyOverride("FairQueueConfiguration", {
      NumberOfMessageGroups: 100,
    });

    const fairQueueArn = cfnFairQueue.attrArn;
    const fairQueueUrl = cfnFairQueue.ref;

    // Import the fair queue as an IQueue for event source mapping
    const fairQueue = sqs.Queue.fromQueueAttributes(this, "FairQueueImport", {
      queueArn: fairQueueArn,
      queueUrl: fairQueueUrl,
    });

    // Custom EventBridge bus
    const bus = new events.EventBus(this, "OrdersBus", {
      eventBusName: "orders-bus",
    });

    // EventBridge rule — match order events and route to fair queue
    // Uses CfnRule because L2 SqsQueue target rejects messageGroupId on non-FIFO queues
    const rule = new events.CfnRule(this, "OrderRule", {
      eventBusName: bus.eventBusName,
      eventPattern: {
        source: ["com.myapp.orders"],
      },
      targets: [
        {
          id: "FairQueueTarget",
          arn: fairQueueArn,
          sqsParameters: {
            messageGroupId: "$.detail.tenantId",
          },
        },
      ],
    });

    // Grant EventBridge permission to send to the fair queue
    const sendPolicy = new iam.PolicyStatement({
      actions: ["sqs:SendMessage"],
      resources: [fairQueueArn],
      principals: [new iam.ServicePrincipal("events.amazonaws.com")],
    });
    const queuePolicy = new sqs.CfnQueuePolicy(this, "FairQueuePolicy", {
      queues: [fairQueueUrl],
      policyDocument: {
        Statement: [
          {
            Effect: "Allow",
            Principal: { Service: "events.amazonaws.com" },
            Action: "sqs:SendMessage",
            Resource: fairQueueArn,
            Condition: {
              ArnEquals: { "aws:SourceArn": rule.attrArn },
            },
          },
        ],
      },
    });

    // Lambda consumer
    const fn = new lambda.Function(this, "ConsumerFn", {
      runtime: lambda.Runtime.NODEJS_20_X,
      handler: "index.handler",
      code: lambda.Code.fromAsset("src"),
      timeout: cdk.Duration.seconds(30),
      memorySize: 128,
      logRetention: logs.RetentionDays.ONE_WEEK,
    });

    // SQS event source mapping
    fn.addEventSource(
      new (require("aws-cdk-lib/aws-lambda-event-sources").SqsEventSource)(
        fairQueue,
        { batchSize: 10, maxBatchingWindow: cdk.Duration.seconds(5) }
      )
    );

    new cdk.CfnOutput(this, "EventBusName", { value: bus.eventBusName });
    new cdk.CfnOutput(this, "FairQueueUrl", { value: fairQueueUrl });
    new cdk.CfnOutput(this, "FunctionName", { value: fn.functionName });
    new cdk.CfnOutput(this, "DLQUrl", { value: dlq.queueUrl });
  }
}
