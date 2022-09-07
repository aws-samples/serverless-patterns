import { Stack, StackProps, CfnOutput, Duration } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import {
	Function,
	Runtime,
	Code,
	LayerVersion,
	FunctionUrlAuthType,
} from 'aws-cdk-lib/aws-lambda';

export class LambdaAdapterCdkStack extends Stack {
	constructor(scope: Construct, id: string, props?: StackProps) {
		super(scope, id, props);

		// Lambda Adapter Layer
		const layerLambdaAdapter = LayerVersion.fromLayerVersionArn(
			this,
			'LambdaAdapterLayerX86',
			`arn:aws:lambda:${this.region}:753240598075:layer:LambdaAdapterLayerX86:3`
		);

		// Lambda
		const lambdaAdapterFunction = new Function(this, 'lambdaAdapterFunction', {
			runtime: Runtime.NODEJS_16_X,
			code: Code.fromAsset('app'),
			handler: 'run.sh',
			environment: {
				AWS_LAMBDA_EXEC_WRAPPER: '/opt/bootstrap',
				RUST_LOG: 'info',
			},
			memorySize: 1024,
			layers: [layerLambdaAdapter],
			timeout: Duration.minutes(1),
		});

		const lambdaAdapterFunctionUrl = lambdaAdapterFunction.addFunctionUrl({
			authType: FunctionUrlAuthType.NONE,
			cors: {
				allowedOrigins: ['*'],
			},
		});

		new CfnOutput(this, 'FunctionUrl', {
			value: lambdaAdapterFunctionUrl.url,
		});
	}
}
