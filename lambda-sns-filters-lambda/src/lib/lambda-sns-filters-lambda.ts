import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { CfnOutput } from 'aws-cdk-lib';
import { SubscriptionFilter, Topic } from 'aws-cdk-lib/aws-sns';
import { Function, Runtime, Code } from 'aws-cdk-lib/aws-lambda';
import path = require('path');
import { LambdaSubscription } from 'aws-cdk-lib/aws-sns-subscriptions';

export class LambdaSNSFiltersLambdaStack extends cdk.Stack {
	constructor(scope: Construct, id: string, props?: cdk.StackProps) {
		super(scope, id, props);

		const snsTopic = new Topic(this, 'SNSTopic', {
			displayName: 'Lambda subscription topic',
		});

		/* Lambda function that sends messages */
		const sender = new Function(this, 'SenderFunction', {
			code: Code.fromAsset(path.join(__dirname, '../functions')),
			runtime: Runtime.NODEJS_16_X,
			handler: 'senderFilter.handler',
			environment: {
				TOPIC_ARN: snsTopic.topicArn,
			},
		});

		// Give permission to the function to publish messages in the topic
		snsTopic.grantPublish(sender);

		/* Lambda function that consumes */
		const consumerRed = new Function(this, 'ConsumerRedFunction', {
			code: Code.fromAsset(path.join(__dirname, '../functions')),
			runtime: Runtime.NODEJS_16_X,
			handler: 'consumerRed.handler',
		});

		const consumerAll = new Function(this, 'ConsumerAllFunction', {
			code: Code.fromAsset(path.join(__dirname, '../functions')),
			runtime: Runtime.NODEJS_16_X,
			handler: 'consumer.handler',
		});

		//Subscribes the consumer lambda to the topic
		snsTopic.addSubscription(
			new LambdaSubscription(consumerRed, {
				filterPolicy: {
					color: SubscriptionFilter.stringFilter({
						allowlist: ['red'],
					}),
				},
			})
		);

		snsTopic.addSubscription(new LambdaSubscription(consumerAll));

		new CfnOutput(this, 'SenderFunctionName', {
			value: sender.functionName,
		});

		new CfnOutput(this, 'SNSTopicARN', { value: snsTopic.topicArn });
	}
}
