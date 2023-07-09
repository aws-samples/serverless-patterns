import { CfnOutput, Duration, Stack, StackProps } from 'aws-cdk-lib';
import {
	Alarm,
	ComparisonOperator,
	Metric,
	TreatMissingData,
} from 'aws-cdk-lib/aws-cloudwatch';
import {
	Effect,
	ManagedPolicy,
	PolicyStatement,
	Role,
	ServicePrincipal,
} from 'aws-cdk-lib/aws-iam';
import { CfnHealthCheck } from 'aws-cdk-lib/aws-route53';
import { Construct } from 'constructs';

interface BoilerPlateStackProps extends StackProps {
	readonly eventBusName: string;
	readonly env: any;
}

export class BoilerPlateStack extends Stack {
	public readonly replicationRoleArn: string;
	public readonly healthCheckArn: string;

	constructor(scope: Construct, id: string, props: BoilerPlateStackProps) {
		super(scope, id, props);
		const region = props.env.region;

		const metric = new Metric({
			metricName: 'IngestionToInvocationStartLatency',
			namespace: 'AWS/Events',
			statistic: 'Average',
			period: Duration.seconds(60),
		});

		const alarm = new Alarm(this, 'High latency Alarm', {
			alarmDescription: 'High Latency in Amazon EventBridge',
			metric: metric,
			evaluationPeriods: 5,
			threshold: 30000,
			comparisonOperator: ComparisonOperator.GREATER_THAN_THRESHOLD,
			treatMissingData: TreatMissingData.BREACHING,
		});

		const healthCheck = new CfnHealthCheck(this, 'HealthCheck', {
			healthCheckTags: [
				{
					key: 'Name',
					value: 'LatencyFailuresHealthCheck',
				},
			],
			healthCheckConfig: {
				type: 'CLOUDWATCH_METRIC',
				alarmIdentifier: {
					name: alarm.alarmName,
					region: region,
				},
				insufficientDataHealthStatus: 'Unhealthy',
			},
		});

		this.healthCheckArn = `arn:aws:route53:::healthcheck/${healthCheck.attrHealthCheckId}`;

		new CfnOutput(this, 'healthCheckArn', {
			value: this.healthCheckArn,
			description: 'healthCheckARN',
		});

		const replicationRole = new Role(this, 'role', {
			assumedBy: new ServicePrincipal('events.amazonaws.com'),
			description: 'Replication role for global endpoints',
		});

		const managedPolicy = new ManagedPolicy(this, 'managedPolicy', {
			statements: [
				new PolicyStatement({
					effect: Effect.ALLOW,
					actions: [
						'events:PutRule',
						'events:PutTargets',
						'events:DeleteRule',
						'events:RemoveTargets',
					],
					resources: [
						`arn:aws:events:*:${Stack.of(this).account}:rule/${
							props.eventBusName
						}/GlobalEndpointManagedRule-*`,
					],
				}),
				new PolicyStatement({
					effect: Effect.ALLOW,
					actions: ['events:PutEvents'],
					resources: [
						`arn:aws:events:*:${Stack.of(this).account}:event-bus/${
							props.eventBusName
						}`,
					],
				}),
				new PolicyStatement({
					effect: Effect.ALLOW,
					actions: ['iam:PassRole'],
					resources: [replicationRole.roleArn],
					conditions: {
						StringLike: {
							'iam:PassedToService': 'events.amazonaws.com',
						},
					},
				}),
			],
			roles: [replicationRole],
		});

		new CfnOutput(this, 'role ARN', {
			value: replicationRole.roleArn,
			description: 'role ARN',
		});

		this.replicationRoleArn = replicationRole.roleArn;
	}
}
