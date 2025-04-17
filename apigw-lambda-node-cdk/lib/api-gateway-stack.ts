// lib/api-gateway-stack.ts
import * as cdk from 'aws-cdk-lib';
import * as apigateway from 'aws-cdk-lib/aws-apigateway';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import { Construct } from 'constructs';
import path = require('path');
import * as fs from 'fs';

interface ApiGatewayStackProps extends cdk.NestedStackProps {
  handleLambda: lambda.Function;
  searchLambda: lambda.Function;
  stageName: string;
}

export class ApiGatewayStack extends cdk.NestedStack {
  public readonly api: apigateway.SpecRestApi;

  constructor(scope: Construct, id: string, props: ApiGatewayStackProps) {
    super(scope, id, props);

    const openApiSpecPath = path.join(__dirname, 'openapi/openapi.json');
    const openApiSpecContent= fs.readFileSync(openApiSpecPath, 'utf8');

     // Parse JSON and replace placeholders
    const openApiSpec = JSON.parse(
        openApiSpecContent.replaceAll(
            '${lambdaArn}', props.handleLambda.functionArn
        ).replaceAll(
            '${region}', cdk.Stack.of(this).region
        ).replaceAll(     
            '${searchLambdaArn}', props.searchLambda.functionArn,
        )
    );

    this.api = new apigateway.SpecRestApi(this, 'SampleApiGatewayLambda2Api', {
      restApiName: 'OrdersAPI',
      description: 'API Gateway with Lambda integration',
      apiDefinition: apigateway.ApiDefinition.fromInline(openApiSpec),
      deployOptions: {
        tracingEnabled: true,
        dataTraceEnabled: true,
        stageName: props.stageName,
      },
      cloudWatchRole: false,
    });

    // TODO: is it too permissive? Should we define method and stage instead of **?
    new lambda.CfnPermission(this, 'LambdaHandlerPermission', {
        action: 'lambda:InvokeFunction',
        functionName: props.handleLambda.functionName,
        principal: 'apigateway.amazonaws.com',
        sourceArn: `arn:aws:execute-api:${this.region}:${this.account}:${this.api.restApiId}/*/*/order*`,
    });  

    new lambda.CfnPermission(this, 'LambdaSearchPermission', {
        action: 'lambda:InvokeFunction',
        functionName: props.searchLambda.functionName,
        principal: 'apigateway.amazonaws.com',
        sourceArn: `arn:aws:execute-api:${this.region}:${this.account}:${this.api.restApiId}/*/*/orders/search*`,
    }); 

    // Output the API URL
    new cdk.CfnOutput(this, 'ApiUrl', {
        value: this.api.url,
        description: 'API Gateway URL',
    });
      
  }
}
