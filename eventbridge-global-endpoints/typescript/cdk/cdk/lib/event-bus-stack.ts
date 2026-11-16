import { CfnOutput, RemovalPolicy, Stack, StackProps } from 'aws-cdk-lib';
import { EventBus, Rule } from 'aws-cdk-lib/aws-events';
import { LogGroup, RetentionDays } from 'aws-cdk-lib/aws-logs';
import { Construct } from 'constructs';
import * as targets from 'aws-cdk-lib/aws-events-targets';

interface EventBusStackProps extends StackProps {
	readonly env: any;
	readonly eventBusName: string;
}

export class EventBusStack extends Stack {
	public readonly eventBusArn: string;

	constructor(scope: Construct, id: string, props: EventBusStackProps) {
		super(scope, id, props);

		//Create a new bus with a given bus name
		const AppEventBus = new EventBus(this, 'AppEventBus', {
			eventBusName: props.eventBusName,
		});

		this.eventBusArn = AppEventBus.eventBusArn;

		const testingRule = new Rule(this, 'testingRule', {
			eventBus: AppEventBus,
			eventPattern: {
				source: [{ prefix: '' }] as any[], // Matches all the events in the bus
			},
		});

		const cloudwatchLog = new LogGroup(this, 'cloudwatchlog', {
			retention: RetentionDays.ONE_DAY,
			removalPolicy: RemovalPolicy.DESTROY,
		});

		testingRule.addTarget(new targets.CloudWatchLogGroup(cloudwatchLog));

		new CfnOutput(this, 'log group', {
			value: cloudwatchLog.logGroupName,
			description: 'cloud watch log group name',
		});
	}
}
