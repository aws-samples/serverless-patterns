import {
  Stack,
  StackProps,
  RemovalPolicy,
  CfnOutput,
  Aws,
  aws_cloudfront_origins as origins,
  aws_cloudfront as cloudfront,
  aws_lambda as lambda,
  aws_iam as iam,
  aws_logs as logs,
  } from 'aws-cdk-lib';

  import { Construct } from 'constructs';
  import { HttpLambdaIntegration } from "@aws-cdk/aws-apigatewayv2-integrations-alpha";
  import { HttpIamAuthorizer } from '@aws-cdk/aws-apigatewayv2-authorizers-alpha';
  import * as apigwv2 from "@aws-cdk/aws-apigatewayv2-alpha";

export class CloudfrontLeApigwCdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const helloWorld = new lambda.Function(this, "HelloWorld", {
      runtime:  lambda.Runtime.PYTHON_3_7,
      code: lambda.Code.fromAsset("lambda"),
      handler: "index.handler",
    });

    // Set Lambda Logs Retention and Removal Policy
    new logs.LogGroup(this, "HelloWorldLogs", {
      logGroupName: "/aws/lambda/" + helloWorld.functionName,
      removalPolicy: RemovalPolicy.DESTROY,
      retention: logs.RetentionDays.ONE_MONTH,
    });

    const lambdaEdge = new lambda.Function(this, 'LambdaEdge', {
      runtime: lambda.Runtime.NODEJS_12_X,
      handler: 'index.handler',
      code: lambda.Code.fromAsset('lambda_edge'),
    });

    const authorizer = new HttpIamAuthorizer();

    // Creates a distribution from an S3 bucket.
    const httpApi = new apigwv2.HttpApi(this, "HttpApi", {
      apiName: 'TestSig4',
      description: 'Testing sig4 signature',
      defaultAuthorizer: authorizer
    });

    httpApi.addRoutes({
      path: "/",
      methods: [apigwv2.HttpMethod.GET],
      integration: new HttpLambdaIntegration(
        "HelloWorldIntegration",
        helloWorld
      ),
    });

    const region = Stack.of(this).region;

    // create a policy statement
    const invokeApiPolicy = new iam.PolicyStatement({
      actions: ['execute-api:Invoke'],
      resources: [`arn:aws:execute-api:${region}:*:${httpApi.apiId}/*`],
    });

    // add the policy to the Function's role
    lambdaEdge.role?.attachInlinePolicy(
      new iam.Policy(this, 'invoke-http-api-policy', {
        statements: [invokeApiPolicy],
      }),
    );

    const distribution = new cloudfront.Distribution(this, 'myDistribution', {
      comment: 'Test sig4 signature',
      defaultBehavior: {
        origin: new origins.HttpOrigin(
          `${httpApi.apiId}.execute-api.${region}.amazonaws.com`
        ),
        cachePolicy: cloudfront.CachePolicy.CACHING_DISABLED,
        viewerProtocolPolicy: cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
          edgeLambdas: [
            {
              functionVersion: lambdaEdge.currentVersion,
              eventType: cloudfront.LambdaEdgeEventType.ORIGIN_REQUEST,
            }
          ],
      }
    });

    new CfnOutput(this, "ApiEndpoint", {
      value: `https://${httpApi.apiId}.execute-api.${region}.amazonaws.com`,
      exportName: Aws.STACK_NAME + "ApiEndpoint",
      description: "Endpoint",
    });

    new CfnOutput(this, "DistributionDomainName", {
      value: "https://" + distribution.domainName,
      exportName: Aws.STACK_NAME + "DomainName",
      description: "Demo Website",
    });


  }
}
