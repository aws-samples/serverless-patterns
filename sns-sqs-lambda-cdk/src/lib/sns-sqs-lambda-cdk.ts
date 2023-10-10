import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { CfnOutput } from 'aws-cdk-lib';
import { Topic } from 'aws-cdk-lib/aws-sns';
import {
	Function,
	Runtime,
	Code,
	EventSourceMapping,
} from 'aws-cdk-lib/aws-lambda';
import path = require('path');
import { Queue } from 'aws-cdk-lib/aws-sqs';
import { SqsSubscription } from 'aws-cdk-lib/aws-sns-subscriptions';

export class SNSSQSLambdaStack extends cdk.Stack {
	constructor(scope: Construct, id: string, props?: cdk.StackProps) {
		super(scope, id, props);

		// SNS Topic
		const snsTopic = new Topic(this, 'SNSTopic', {
			displayName: 'Lambda subscription topic',
		});

		// SQS Queue
		const sqsQueue = new Queue(this, 'SQSQueue');

		/* Lambda function that sends messages */
		const sender = new Function(this, 'SenderFunction', {
			code: Code.fromAsset(path.join(__dirname, '../functions')),
			runtime: Runtime.NODEJS_16_X,
			handler: 'sender.handler',
			environment: {
				TOPIC_ARN: snsTopic.topicArn,
			},
		});

		// Give permission to the function to publish messages in the topic
		snsTopic.grantPublish(sender);

		//Subscribes the consumer lambda to the topic
		snsTopic.addSubscription(new SqsSubscription(sqsQueue));

		/* Lambda function that consumes messages from the queue */
		const consumer = new Function(this, 'ConsumerFunction', {
			code: Code.fromAsset(path.join(__dirname, '../functions')),
			runtime: Runtime.NODEJS_16_X,
			handler: 'consumer.handler',
		});

		const consumerEventSourceMapping = new EventSourceMapping(
			this,
			'QueueConsumerFunctionMySQSEvent',
			{
				target: consumer,
				batchSize: 1,
				eventSourceArn: sqsQueue.queueArn,
			}
		);

		sqsQueue.grantConsumeMessages(consumer);

		new CfnOutput(this, 'SenderFunctionName', {
			value: sender.functionName,
		});

		new CfnOutput(this, 'SNSTopicARN', { value: snsTopic.topicArn });
	}
}
