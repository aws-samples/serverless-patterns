import { CfnOutput, Duration, Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { Function, Code, Runtime } from 'aws-cdk-lib/aws-lambda';
import * as path from 'path';
import { Effect, PolicyStatement } from 'aws-cdk-lib/aws-iam';

interface PutEventsStackProps extends StackProps {
	readonly eventBusName: string;
	readonly endpointId: string;
}

export class PutEventsStack extends Stack {
	constructor(scope: Construct, id: string, props: PutEventsStackProps) {
		super(scope, id, props);

		const eventbridgePutPolicy = new PolicyStatement({
			effect: Effect.ALLOW,
			resources: ['*'],
			actions: ['events:PutEvents'],
		});

		/* Lambda function that put messages */
		const putFunction = new Function(this, 'PutFunction', {
			code: Code.fromAsset(path.join(__dirname, '../function')),
			runtime: Runtime.NODEJS_16_X,
			handler: 'put-events.handler',
			timeout: Duration.minutes(15),
			environment: {
				ENDPOINT: props.endpointId,
				EVENTBUS_NAME: props.eventBusName,
			},
		});

		putFunction.addToRolePolicy(eventbridgePutPolicy);

		new CfnOutput(this, 'function name', {
			value: putFunction.functionName,
			description: 'function name',
		});
	}
}
