import { Stack, StackProps, aws_lambda_nodejs as nodejs_lambda, aws_ssm as ssm, aws_lambda as lambda, Duration, CfnParameter, aws_iam as iam } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as path from 'path';

export class LambdaExtensionParameterStoreCdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const parameterStoreExtensionArn = new CfnParameter(this, 'parameterStoreExtensionArn', { type: 'String' });

    const param = new ssm.StringParameter(this, 'MyStringParameter', {
      parameterName: '/my/test/parameter',
      stringValue: 'abc123xyz',
    });

    const checkParameterLambda = new nodejs_lambda.NodejsFunction(this, "CheckParameterLambda", {
      runtime: lambda.Runtime.NODEJS_14_X,
      entry: path.join(__dirname, `/../lambda/index.ts`),
      handler: "handler",
      retryAttempts: 0,
      timeout: Duration.seconds(15),
      environment: {
        PARAMETER_PATH: param.parameterName,
      }
    });

    // Add extension layer
    checkParameterLambda.addLayers(
      lambda.LayerVersion.fromLayerVersionArn(this, 'ParameterStoreExtension', parameterStoreExtensionArn.valueAsString)
    );

    // Set additional permissions for parameter store
    checkParameterLambda.role?.attachInlinePolicy(
      new iam.Policy(this, 'additionalPermissionsForParameterStore', {
        statements: [
          new iam.PolicyStatement({
            actions: ['ssm:GetParameter'],
            resources: ['*'],
          }),
        ],
      }),
    )
  }
}
