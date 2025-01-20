import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as cloudfront from 'aws-cdk-lib/aws-cloudfront';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as lambdaNode from 'aws-cdk-lib/aws-lambda-nodejs';
import path = require('path');
import { Effect, PolicyStatement } from 'aws-cdk-lib/aws-iam';

export class CdkStack extends cdk.Stack {
    constructor(scope: Construct, id: string, props?: cdk.StackProps) {
        super(scope, id, props);

        // Create the Lambda
        const simpleLambda = new lambdaNode.NodejsFunction(this, 'simpleLambda', {
            entry: 'lambda/handler.ts',
            handler: 'handler',
            runtime: lambda.Runtime.NODEJS_18_X,
            functionName: 'simpleLambda'
        });

        const authFunction = this.createAuthEdgeFunction(simpleLambda.functionArn);

        // Configure the Lambda URL
        const lambdaUrl = simpleLambda.addFunctionUrl({
            authType: lambda.FunctionUrlAuthType.AWS_IAM,
        });

        // Create the CloudFront distribution redirecting calls to the Lambda URL
        const cfDistribution = new cloudfront.CloudFrontWebDistribution(this, 'CFDistribution', {
            originConfigs: [
                {
                    customOriginSource: {
                        domainName: this.getURLDomain(lambdaUrl),
                        originProtocolPolicy: cloudfront.OriginProtocolPolicy.HTTPS_ONLY,
                    },
                    behaviors: [{
                        isDefaultBehavior: true,
                        allowedMethods: cloudfront.CloudFrontAllowedMethods.ALL,
                        lambdaFunctionAssociations: [{
                            eventType: cloudfront.LambdaEdgeEventType.ORIGIN_REQUEST,
                            lambdaFunction: authFunction.currentVersion,
                            includeBody: true
                        }],
                    }],
                }
            ],
        });

        new cdk.CfnOutput(this, 'CloudFrontDistributionURL', {
            value: cfDistribution.distributionDomainName,
        });

    }

    /**
     * Extracts the domain from a Lambda URL
     * 
     * Example: https://my-lambda.execute-api.us-east-1.amazonaws.com/ -> my-lambda.execute-api.us-east-1.amazonaws.com
     */
    getURLDomain(lambdaUrl: lambda.FunctionUrl) {
        return cdk.Fn.select(2, cdk.Fn.split('/', lambdaUrl.url));
    }

    private createAuthEdgeFunction(functionArn: string) {
        const authFunction = new cloudfront.experimental.EdgeFunction(this, 'AuthLambdaEdge', {
            handler: 'authEdge.handler',
            runtime: lambda.Runtime.NODEJS_16_X,
            code: lambda.Code.fromAsset(path.join(__dirname, '../lambda-edge'), {
                bundling: {
                    command: [
                        "bash",
                        "-c",
                        "npm install && cp -rT /asset-input/ /asset-output/",
                    ],
                    image: lambda.Runtime.NODEJS_16_X.bundlingImage,
                    user: "root",
                },
            }),
            currentVersionOptions: {
                removalPolicy: cdk.RemovalPolicy.DESTROY
            },
            timeout: cdk.Duration.seconds(7),
        });

        authFunction.addToRolePolicy(new PolicyStatement({
            sid: 'AllowInvokeFunctionUrl',
            effect: Effect.ALLOW,
            actions: ['lambda:InvokeFunctionUrl'],
            resources: [functionArn],
            conditions: {
                "StringEquals": { "lambda:FunctionUrlAuthType": "AWS_IAM" }
            }
        }));
        return authFunction;
    }
}
