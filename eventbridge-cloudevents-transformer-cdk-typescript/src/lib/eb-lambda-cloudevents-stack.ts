import * as cdk from 'aws-cdk-lib';
import { EventBus, EventField, Rule, RuleTargetInput } from 'aws-cdk-lib/aws-events';
import { LambdaFunction } from 'aws-cdk-lib/aws-events-targets';
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';
import { RetentionDays } from 'aws-cdk-lib/aws-logs';
import { Queue } from 'aws-cdk-lib/aws-sqs';
import { Construct } from 'constructs';
import { join } from 'path';
import { Runtime } from 'aws-cdk-lib/aws-lambda';


export class EbLambdaCloudeventsStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const dlq = new Queue(this, "dlq");
    const lambdaTS = new NodejsFunction(this, "ts-function", {
      entry: join(__dirname, "..", "lambda", "index.ts"),
      handler: "handler",
      timeout: cdk.Duration.seconds(3),
      reservedConcurrentExecutions: 1,
      deadLetterQueue: dlq,
      logRetention: RetentionDays.ONE_DAY,
      runtime: Runtime.NODEJS_18_X,
    });


    const bus = new EventBus(this, "bus");

    const transformer = {
      specversion: "1.0",
      id: EventField.eventId,
      source: EventField.source,
      type: EventField.detailType,
      time: EventField.time,
      region: EventField.region,
      account: EventField.account,
      data: EventField.fromPath('$.detail')
    }
    
    const targetLambdaTS = new LambdaFunction(lambdaTS, {
      retryAttempts: 0,
      deadLetterQueue: dlq,
      event: RuleTargetInput.fromObject(transformer)
    });

    new Rule(this, "rule", {
      eventBus: bus,
      eventPattern: {
        account: [cdk.Stack.of(this).account],
      },
      targets: [targetLambdaTS],
    })

    new cdk.CfnOutput(this, "busArn", {
      value: bus.eventBusArn,
    })

    new cdk.CfnOutput(this, "functionArn", {
      value: lambdaTS.functionArn,
    })

    new cdk.CfnOutput(this, "dlqArn", {
      value: dlq.queueArn,
    })
  }
}

