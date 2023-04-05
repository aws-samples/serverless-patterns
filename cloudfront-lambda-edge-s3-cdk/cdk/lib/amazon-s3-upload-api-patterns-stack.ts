import * as cdk from "aws-cdk-lib";
import {
  AllowedMethods,
  CachePolicy,
  Distribution,
  LambdaEdgeEventType,
  OriginAccessIdentity,
} from "aws-cdk-lib/aws-cloudfront";
import { S3Origin } from "aws-cdk-lib/aws-cloudfront-origins";
import { Runtime } from "aws-cdk-lib/aws-lambda";
import { BlockPublicAccess, Bucket, CfnBucket } from "aws-cdk-lib/aws-s3";
import { Construct } from "constructs";
import { NodejsFunction } from "aws-cdk-lib/aws-lambda-nodejs";
import { UserPool } from "aws-cdk-lib/aws-cognito";
import { StringParameter } from "aws-cdk-lib/aws-ssm";
import { CanonicalUserPrincipal, PolicyStatement } from "aws-cdk-lib/aws-iam";
import { CfnOutput } from "aws-cdk-lib";

export class AmazonS3UploadApiPatternsStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const pool = new UserPool(this, "cognitoUserPool", {
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });
    const client = pool.addClient("cognitoAppClient", {
      authFlows: {
        adminUserPassword: true,
      },
    });

    new CfnOutput(this, 'CognitoUserPoolId', { value: pool.userPoolId });
    new CfnOutput(this, 'CognitoAppClientId', { value: client.userPoolClientId });

    const userPoolParam = new StringParameter(this, "cognitoAuthUserPoolId", {
      parameterName: "cognitoAuthUserPoolId",
      stringValue: pool.userPoolId,
    });

    const appClientParam = new StringParameter(this, "cognitoAuthAppClientId", {
      parameterName: "cognitoAuthAppClientId",
      stringValue: client.userPoolClientId,
    });

    const authFunction = new NodejsFunction(this, "authFunction", {
      runtime: Runtime.NODEJS_14_X,
      handler: "handler",
      entry: "./authorizer/app.js",
      timeout: cdk.Duration.seconds(5),
    });
    userPoolParam.grantRead(authFunction);
    appClientParam.grantRead(authFunction);

    const originAccessIdentity = new OriginAccessIdentity(
      this,
      "originAccessIdentity",
      {
        comment: "Only allow CloudFront to access S3 bucket directly",
      }
    );

    const bucket = new Bucket(this, "originBucket", {
      blockPublicAccess: BlockPublicAccess.BLOCK_ALL,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    new CfnOutput(this, 'S3BucketName', { value: bucket.bucketName })

    const cfdistribution = new Distribution(this, "cloudfrontDistribution", {
      defaultBehavior: {
        origin: new S3Origin(bucket, {
          originAccessIdentity,
        }),
        allowedMethods: AllowedMethods.ALLOW_ALL,
        cachePolicy: CachePolicy.CACHING_DISABLED,
        edgeLambdas: [
          {
            functionVersion: authFunction.currentVersion,
            eventType: LambdaEdgeEventType.VIEWER_REQUEST,
          },
        ],
      },
    });

    const policyOverride = bucket.node.findChild("Policy").node
      .defaultChild as CfnBucket;
    policyOverride.addOverride(
      "Properties.PolicyDocument.Statement.0.Action",
      "s3:PutObject"
    );

    new CfnOutput(this, 'CloudFrontDistributionUrl', { value: cfdistribution.distributionDomainName });

  }
}
