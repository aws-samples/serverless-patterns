import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as configuration from '../stackconfiguration.json';
import { AllowListReceiptFilter } from 'aws-cdk-lib/aws-ses';

export class SrcStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // parameters
    const account = cdk.Stack.of(this).account;
    const stackName = cdk.Stack.of(this).stackName;
    const snsName = `${account}-${stackName}-topic-${configuration.Sns.TopicName}`;

    // sns topic
    const sns = new cdk.aws_sns.Topic(this, 'cdk-sns-topic', {
      displayName: snsName,
      topicName: snsName
    });

    // create all required sqs
    for (let q = 0; q < configuration.Sqs.length; q++) {
      const queueConfig = configuration.Sqs[q];
      // dead queue
      const sqsDead = new cdk.aws_sqs.Queue(this, `cdk-sqs-dead-${q + 1}`, {
        queueName: `${account}-${stackName}-dead-${queueConfig.QueueName}`,
        removalPolicy: cdk.RemovalPolicy.DESTROY
      });
      // queue
      const sqs = new cdk.aws_sqs.Queue(this, `cdk-sqs-queue-${q + 1}`, {
        queueName: `${account}-${stackName}-queue-${queueConfig.QueueName}`,
        removalPolicy: cdk.RemovalPolicy.DESTROY,
        deadLetterQueue: {
          maxReceiveCount: 3,
          queue: sqsDead
        }
      });
      if (queueConfig.IsAttribute) {
        // subscription attribute
        sns.addSubscription(new cdk.aws_sns_subscriptions.SqsSubscription(sqs, {
          filterPolicy: {
            [queueConfig.Filter.FilterName]: cdk.aws_sns.SubscriptionFilter.stringFilter({
              allowlist: queueConfig.Filter.FilterValues
            })
          },
          rawMessageDelivery: true
        }));
      } else {
        // subscription content
        sns.addSubscription(new cdk.aws_sns_subscriptions.SqsSubscription(sqs, {
          filterPolicyWithMessageBody: {
            filter: cdk.aws_sns.FilterOrPolicy.policy({
              [queueConfig.Filter.FilterName]: cdk.aws_sns.FilterOrPolicy.filter(cdk.aws_sns.SubscriptionFilter.stringFilter({
                allowlist: queueConfig.Filter.FilterValues
              }))
            })

          },
          rawMessageDelivery: true
        }));
      }
    }
  }
}
