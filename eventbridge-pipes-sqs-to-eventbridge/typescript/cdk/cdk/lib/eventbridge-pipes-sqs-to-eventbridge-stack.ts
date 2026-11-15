import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { CfnPipe } from 'aws-cdk-lib/aws-pipes';
import { Queue } from 'aws-cdk-lib/aws-sqs';
import { EventBus } from 'aws-cdk-lib/aws-events';
import { PolicyDocument, Role, ServicePrincipal, PolicyStatement } from 'aws-cdk-lib/aws-iam';
import * as iam from 'aws-cdk-lib/aws-iam';

export class EventbridgePipesSqsToEventbridgeStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const source = new Queue(this, 'sqs-queue');
    const target = new EventBus(this, 'event-bus');

    const sourcePolicy = new PolicyDocument({
      statements: [
        new PolicyStatement({
          resources: [source.queueArn],
          actions: ['sqs:ReceiveMessage', 'sqs:DeleteMessage', 'sqs:GetQueueAttributes'],
          effect: iam.Effect.ALLOW,
        }),
      ],
    });

    const targetPolicy = new PolicyDocument({
      statements: [
        new PolicyStatement({
          resources: [target.eventBusArn],
          actions: ['events:PutEvents'],
          effect: iam.Effect.ALLOW,
        }),
      ],
    });

    const pipeRole = new Role(this, 'role', {
      assumedBy: new ServicePrincipal('pipes.amazonaws.com'),
      inlinePolicies: {
        sourcePolicy,
        targetPolicy,
      },
    });

    // Create new Pipe
    const pipe = new CfnPipe(this, 'pipe', {
      roleArn: pipeRole.roleArn,
      source: source.queueArn,
      sourceParameters: {
        sqsQueueParameters: {
          batchSize: 5,
          maximumBatchingWindowInSeconds: 120,
        },
      },
      target: target.eventBusArn,
      targetParameters: {
        eventBridgeEventBusParameters: {
          detailType: 'OrderCreated',
          source: 'myapp.orders',
        },
        inputTemplate: `{
          "orderId": "<$.body.orderId>",
          "customerId": "<$.body.customerId>"
        }`,
      },
    });
  }

}
