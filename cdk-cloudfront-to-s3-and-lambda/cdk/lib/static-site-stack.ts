import * as cdk from "@aws-cdk/core";
import * as lambda from "@aws-cdk/aws-lambda";
import * as lambdaNode from "@aws-cdk/aws-lambda-nodejs";
import * as path from "path";
import * as apigw from "@aws-cdk/aws-apigateway";
import * as s3 from "@aws-cdk/aws-s3";
import * as s3Deployment from "@aws-cdk/aws-s3-deployment";
import * as cloudfront from "@aws-cdk/aws-cloudfront";
import * as iam from "@aws-cdk/aws-iam";
import {Duration} from "@aws-cdk/core";

export class StaticSiteStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const apiDefaultHandler = new lambdaNode.NodejsFunction(
      this,
      "apiDefaultHandler",
      {
        runtime: lambda.Runtime.NODEJS_12_X,
        handler: "get",
        entry: path.join(__dirname, "../../api/default/index.ts"),
        memorySize: 1024,
      }
    );
    const apiHelloGetHandler = new lambdaNode.NodejsFunction(
      this,
      "apiHelloGetHandler",
      {
        runtime: lambda.Runtime.NODEJS_12_X,
        handler: "get",
        entry: path.join(__dirname, "../../api/hello/index.ts"),
        memorySize: 1024,
      }
    );
    const apiWorldGetHandler = new lambdaNode.NodejsFunction(
      this,
      "apiWorldGetHandler",
      {
        runtime: lambda.Runtime.NODEJS_12_X,
        handler: "get",
        entry: path.join(__dirname, "../../api/world/index.ts"),
        memorySize: 1024,
      }
    );
    const apiGateway = new apigw.LambdaRestApi(this, "apiGateway", {
      handler: apiDefaultHandler,
      proxy: false,
    });

    // /api
    const apiRoute = apiGateway.root.addResource("api")

    // /api/hello
    const apiHelloRoute = apiRoute.addResource("hello");
    // GET
    apiHelloRoute.addMethod(
      "GET",
      new apigw.LambdaIntegration(apiHelloGetHandler)
    );

    // /api/world
    const apiWorldRoute = apiRoute.addResource("world");
    // GET
    apiWorldRoute.addMethod(
      "GET",
      new apigw.LambdaIntegration(apiWorldGetHandler)
    );

    // Create a bucket for static content.
    const staticBucket = new s3.Bucket(this, "staticBucket", {
      encryption: s3.BucketEncryption.S3_MANAGED,
      lifecycleRules: [
        { abortIncompleteMultipartUploadAfter: cdk.Duration.days(7) },
        { noncurrentVersionExpiration: cdk.Duration.days(7) },
      ],
      blockPublicAccess: {
        blockPublicAcls: true,
        blockPublicPolicy: true,
        ignorePublicAcls: true,
        restrictPublicBuckets: true,
      },
      versioned: true,
    });

    // Deploy the static content.
    // Depending on your process, you might want to deploy the static content yourself
    // using an s3 sync command instead.
    new s3Deployment.BucketDeployment(this, "staticBucketDeployment", {
      sources: [s3Deployment.Source.asset(path.join(__dirname, "../../web"))],
      destinationKeyPrefix: "/",
      destinationBucket: staticBucket,
    });

    // Create a CloudFront distribution connected to the Lambda and the static content.
    const cfOriginAccessIdentity = new cloudfront.OriginAccessIdentity(
      this,
      "cfOriginAccessIdentity",
      {}
    );
    const cloudfrontS3Access = new iam.PolicyStatement();
    cloudfrontS3Access.addActions("s3:GetBucket*");
    cloudfrontS3Access.addActions("s3:GetObject*");
    cloudfrontS3Access.addActions("s3:List*");
    cloudfrontS3Access.addResources(staticBucket.bucketArn);
    cloudfrontS3Access.addResources(`${staticBucket.bucketArn}/*`);
    cloudfrontS3Access.addCanonicalUserPrincipal(
      cfOriginAccessIdentity.cloudFrontOriginAccessIdentityS3CanonicalUserId
    );
    staticBucket.addToResourcePolicy(cloudfrontS3Access);

    // Add a Lambda@Edge to add CORS headers to the API.
    const apiCorsLambda = new cloudfront.experimental.EdgeFunction(
      this,
      "apiCors",
      {
        code: lambda.Code.fromAsset(path.join(__dirname, "./cloudfront")),
        handler: "cors.onOriginResponse",
        runtime: lambda.Runtime.NODEJS_12_X,
      }
    );

    // Add a Lambda@Edge to rewrite paths and add redirects headers to the static site.
    const staticRewriteLambda = new cloudfront.experimental.EdgeFunction(
      this,
      "staticRewrite",
      {
        code: lambda.Code.fromAsset(path.join(__dirname, "./cloudfront")),
        handler: "rewrite.onViewerRequest",
        runtime: lambda.Runtime.NODEJS_12_X,
      }
    );

    // Create distribution.
    const distribution = new cloudfront.CloudFrontWebDistribution(this, "webDistribution", {
      originConfigs: [
        {
          customOriginSource: {
            domainName: `${apiGateway.restApiId}.execute-api.${this.region}.${this.urlSuffix}`,
          },
          originPath: `/${apiGateway.deploymentStage.stageName}`,
          behaviors: [
            {
              lambdaFunctionAssociations: [
                {
                  lambdaFunction: apiCorsLambda,
                  eventType: cloudfront.LambdaEdgeEventType.ORIGIN_RESPONSE,
                },
              ],
              allowedMethods: cloudfront.CloudFrontAllowedMethods.ALL,
              pathPattern: "api/*",
              maxTtl: Duration.millis(0),
            },
          ],
        },
        {
          s3OriginSource: {
            s3BucketSource: staticBucket,
            originAccessIdentity: cfOriginAccessIdentity,
          },
          behaviors: [
            {
              lambdaFunctionAssociations: [
                {
                  lambdaFunction: staticRewriteLambda,
                  eventType: cloudfront.LambdaEdgeEventType.VIEWER_REQUEST,
                },
              ],
              isDefaultBehavior: true,
            },
          ],
        },
      ],
    });
    new cdk.CfnOutput(this, "distributionDomainName", { value: distribution.distributionDomainName });
  }
}
