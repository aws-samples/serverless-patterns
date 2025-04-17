// lib/lambda-stack.ts
import * as cdk from 'aws-cdk-lib';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as secretsmanager from 'aws-cdk-lib/aws-secretsmanager';
import { Construct } from 'constructs';

export interface LambdaStackProps extends cdk.NestedStackProps {
    stageName: string;
    apiKey: secretsmanager.Secret;
}

export class LambdaStack extends cdk.NestedStack {
  public readonly handleLambda: lambda.Function;
  public readonly searchLambda: lambda.Function;

  constructor(scope: Construct, id: string, props: LambdaStackProps) {
    super(scope, id, props);

    const powertoolsLayer = lambda.LayerVersion.fromLayerVersionArn(
      this,
      'powertools-layer',
      `arn:aws:lambda:${cdk.Stack.of(this).region}:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:3`
    );

    this.handleLambda = new lambda.Function(this, 'Handle', {
      runtime: lambda.Runtime.NODEJS_20_X,
      handler: 'index.handler',
      code: lambda.Code.fromAsset('lib/lambda/handle'),
      environment: {
        POWERTOOLS_SERVICE_NAME: 'handleOrders',
        POWERTOOLS_LOG_LEVEL: 'INFO',
        POWERTOOLS_METRICS_NAMESPACE: 'RestAPIGWLambda',
        POWERTOOLS_TRACE_ENABLED: 'true',
        POWERTOOLS_METRICS_FUNCTION_NAME: 'handle',
        POWERTOOLS_TRACER_CAPTURE_HTTPS_REQUESTS: 'true',
        POWERTOOLS_TRACER_CAPTURE_RESPONSE: 'true',
        POWERTOOLS_DEV: 'false',
        STAGE: props.stageName,
        API_KEY_SECRET_ARN: props.apiKey.secretArn
      },
      tracing: lambda.Tracing.ACTIVE,
      layers: [powertoolsLayer],
      timeout: cdk.Duration.seconds(30),
    });

    props.apiKey.grantRead(this.handleLambda);

    this.searchLambda = new lambda.Function(this, 'Search', {
        runtime: lambda.Runtime.NODEJS_20_X,
        handler: 'index.handler',
        code: lambda.Code.fromAsset('lib/lambda/search'),
        environment: {
          POWERTOOLS_SERVICE_NAME: 'searchOrders',
          POWERTOOLS_LOG_LEVEL: 'INFO',
          POWERTOOLS_METRICS_NAMESPACE: 'RestAPIGWLambda',
          POWERTOOLS_TRACE_ENABLED: 'true',
          POWERTOOLS_METRICS_FUNCTION_NAME: 'search',
          POWERTOOLS_TRACER_CAPTURE_HTTPS_REQUESTS: 'true',
          POWERTOOLS_TRACER_CAPTURE_RESPONSE: 'true',
          POWERTOOLS_DEV: 'false',
          STAGE: props.stageName,
        },
        tracing: lambda.Tracing.ACTIVE,
        layers: [powertoolsLayer],
        timeout: cdk.Duration.seconds(30),
      });



  }
 
}
