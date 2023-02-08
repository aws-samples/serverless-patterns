import { CfnOutput, Stack, StackProps } from 'aws-cdk-lib';
import { CfnEndpoint } from 'aws-cdk-lib/aws-events';
import { Construct } from 'constructs';

interface GlobalEndpointStackProps extends StackProps {
	readonly eventBusArn1: string;
	readonly eventBusArn2: string;
	readonly replicatedRegion: string;
	readonly healthCheckArn: string;
	readonly replicatedRoleArn: string;
	readonly env: any;
}

export class GlobalEndpointStack extends Stack {
	public readonly endpointName: string;
	public readonly endpointId: string;

	constructor(scope: Construct, id: string, props: GlobalEndpointStackProps) {
		super(scope, id, props);
		const region = props.env.region;

		const endpoint = new CfnEndpoint(this, 'EventBridgeGlobalEndpoint', {
			name: 'SimpleEventBridgeGlobalEndpoint',
			description: 'SimpleEventBridgeGlobalEndpoint',
			eventBuses: [
				{ eventBusArn: props.eventBusArn1 },
				{ eventBusArn: props.eventBusArn2 },
			],
			routingConfig: {
				failoverConfig: {
					primary: {
						healthCheck: props.healthCheckArn,
					},
					secondary: {
						route: props.replicatedRegion,
					},
				},
			},
			replicationConfig: {
				state: 'ENABLED',
			},

			roleArn: props.replicatedRoleArn,
		});

		this.endpointId = endpoint.attrEndpointId;

		new CfnOutput(this, 'endpoint id', {
			value: this.endpointId,
			description: 'endpoint id',
		});

		this.endpointName = endpoint.name;

		new CfnOutput(this, 'endpoint name', {
			value: endpoint.name,
			description: 'endpoint name',
		});
	}
}
