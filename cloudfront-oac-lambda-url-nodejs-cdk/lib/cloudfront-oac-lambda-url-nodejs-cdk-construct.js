const {Construct} = require('constructs');
const cdk = require('aws-cdk-lib');
const iam = require('aws-cdk-lib/aws-iam');
const lambda = require('aws-cdk-lib/aws-lambda');
const cloudfront = require('aws-cdk-lib/aws-cloudfront');
const origins = require('aws-cdk-lib/aws-cloudfront-origins');

const NAME = 'cloudfront-oac-lambda-url';

class CloudfrontOacLambdaUrlNodejsCdkConstruct extends Construct {
    /**
     * @param {cdk.App} scope
     * @param {string} id
     * @param {cdk.StackProps=} props
     */
    constructor(scope, id, props) {
        super(scope, id);

        const lambdaFunction = new lambda.Function(this, 'lambdaFunction', {
            code: lambda.Code.fromAsset('lambda'),
            handler: 'index.handler',
            functionName: NAME,
            architecture: lambda.Architecture.ARM_64,
            runtime: lambda.Runtime.NODEJS_20_X
        });

        const functionUrl = lambdaFunction.addFunctionUrl({
            authType: lambda.FunctionUrlAuthType.AWS_IAM
        });

        const functionOrigin = new origins.FunctionUrlOrigin(functionUrl);

        const cfDistribution = new cloudfront.Distribution(this, 'Distribution', {
            comment: NAME,
            defaultBehavior: {origin: functionOrigin}
        });

        const cfnOriginAccessControl = new cloudfront.CfnOriginAccessControl(this, 'MyCfnOriginAccessControl', {
            originAccessControlConfig: {
                name: NAME,
                originAccessControlOriginType: 'lambda',
                signingBehavior: 'always',
                signingProtocol: 'sigv4'
            }
        });

        const distributionResource = cfDistribution.node.defaultChild;
        distributionResource.addPropertyOverride('DistributionConfig.Origins.0.OriginAccessControlId', cfnOriginAccessControl.attrId);


        lambdaFunction.addPermission('cfn-permission', {
            principal: new iam.ServicePrincipal('cloudfront.amazonaws.com'),
            action: 'lambda:InvokeFunctionUrl',
            sourceArn: `arn:aws:cloudfront::${scope.account}:distribution/${cfDistribution.distributionId}`
        });


        new cdk.CfnOutput(this, 'lambdaUrl', {
            key: 'lambdaUrl',
            value: functionUrl.url
        });

        new cdk.CfnOutput(this, 'cloudfrontUrl', {
            key: 'cloudfrontUrl',
            value: `https://${cfDistribution.domainName}`
        });
    }
}

module.exports = {CloudfrontOacLambdaUrlNodejsCdkConstruct: CloudfrontOacLambdaUrlNodejsCdkConstruct}
