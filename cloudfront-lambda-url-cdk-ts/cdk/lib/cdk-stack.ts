import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as cloudfront from 'aws-cdk-lib/aws-cloudfront';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as lambdaNode from 'aws-cdk-lib/aws-lambda-nodejs';

export class CdkStack extends cdk.Stack {
    constructor(scope: Construct, id: string, props?: cdk.StackProps) {
        super(scope, id, props);

        // Create the Lambda
        const simpleLambda = new lambdaNode.NodejsFunction(this, 'simpleLambda', {
            entry: 'lambda/handler.ts',
            handler: 'handler',
            runtime: lambda.Runtime.NODEJS_18_X
        });

        // Configure the Lambda URL
        const lambdaUrl = simpleLambda.addFunctionUrl({
            authType: lambda.FunctionUrlAuthType.NONE,
        });

        // Create the CloudFront distribution redirecting calls to the Lambda URL
        const cfDistribution = new cloudfront.CloudFrontWebDistribution(this, 'CFDistribution', {
            originConfigs: [
                {
                    customOriginSource: {
                        domainName: this.getURLDomain(lambdaUrl),
                    },
                    behaviors: [{
                        isDefaultBehavior: true
                    }],
                },
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
}
