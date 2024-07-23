import * as cdk from 'aws-cdk-lib';
import { HttpApi, HttpMethod } from 'aws-cdk-lib/aws-apigatewayv2';
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';
import { Construct } from 'constructs';
import { Runtime } from 'aws-cdk-lib/aws-lambda';
import * as path from 'path';
import { CfnOutput } from 'aws-cdk-lib';
import { HttpLambdaIntegration } from 'aws-cdk-lib/aws-apigatewayv2-integrations';

export class HttpApiLambdaStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Dummy Lambda
    const dummyFn = new NodejsFunction(this, "HelloWorldHandler", {
      functionName: "dummy",
      runtime: Runtime.NODEJS_20_X,
      entry: path.join(__dirname, `/../resources/dummy.ts`)
    })

    // HttpApi Gateway
    const httpApi = new HttpApi(this, "HttpApi", {
      apiName: 'http-api'
    })
    httpApi.addRoutes({
      path: '/',
      methods: [ HttpMethod.GET ],
      integration: new HttpLambdaIntegration('DummyIntegration', dummyFn),
    })

    // Outputs
    new CfnOutput(this, "HttpApi URL", {
      value: httpApi.url ?? "Error: can't get the HTTP API URL!",
    });

  }
}
