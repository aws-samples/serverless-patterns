import * as cdk from 'aws-cdk-lib';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as apigateway from 'aws-cdk-lib/aws-apigateway';
import { Construct } from 'constructs';

export class LambdaBedrockMantleStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const apiKey = new cdk.CfnParameter(this, 'BedrockApiKey', {
      type: 'String',
      description: 'Bedrock API key generated from the AWS console',
      noEcho: true,
    });

    const fn = new lambda.Function(this, 'ResponsesApiFn', {
      runtime: lambda.Runtime.PYTHON_3_12,
      handler: 'index.handler',
      code: lambda.Code.fromAsset('src', {
        bundling: {
          image: lambda.Runtime.PYTHON_3_12.bundlingImage,
          command: [
            'bash', '-c',
            'pip install -r requirements.txt -t /asset-output && cp -au . /asset-output',
          ],
        },
      }),
      timeout: cdk.Duration.seconds(60),
      memorySize: 256,
      environment: {
        OPENAI_BASE_URL: `https://bedrock-mantle.${this.region}.api.aws/v1`,
        OPENAI_API_KEY: apiKey.valueAsString,
      },
    });

    const api = new apigateway.RestApi(this, 'ResponsesApi', {
      restApiName: 'Bedrock Mantle Responses API',
    });

    api.root.addResource('ask').addMethod(
      'POST',
      new apigateway.LambdaIntegration(fn),
    );

    new cdk.CfnOutput(this, 'ApiEndpoint', {
      value: api.url + 'ask',
      description: 'API Gateway endpoint URL',
    });
  }
}
