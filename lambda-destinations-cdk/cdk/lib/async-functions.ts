import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { CfnOutput } from 'aws-cdk-lib';
import { Queue } from 'aws-cdk-lib/aws-sqs';
import { Function, Runtime, Code } from 'aws-cdk-lib/aws-lambda';
import * as path from 'path';
import {
	LambdaDestination,
	SqsDestination,
} from 'aws-cdk-lib/aws-lambda-destinations';

export class AsyncFunctionsStack extends cdk.Stack {
	constructor(scope: Construct, id: string, props?: cdk.StackProps) {
		super(scope, id, props);

		/* Lambda function that recieves messages */
		const reciever = new Function(this, 'RecieverFunction', {
			code: Code.fromAsset(path.join(__dirname, '../functions')),
			runtime: Runtime.NODEJS_16_X,
			handler: 'reciever.handler',
		});

		/* DLQ Queue */
		const dlqQueue = new Queue(this, 'MyDLQQueue');

		/* Lambda function that sends messages */
		const sender = new Function(this, 'SenderFunction', {
			code: Code.fromAsset(path.join(__dirname, '../functions')),
			runtime: Runtime.NODEJS_16_X,
			handler: 'senderDestination.handler',
			retryAttempts: 0,
			onSuccess: new LambdaDestination(reciever),
			onFailure: new SqsDestination(dlqQueue),
		});

		/* Cloudformation outputs */
		new CfnOutput(this, 'SenderFunctionName', {
			value: sender.functionName,
			description: 'SenderFunctionName function name',
		});
	}
}
