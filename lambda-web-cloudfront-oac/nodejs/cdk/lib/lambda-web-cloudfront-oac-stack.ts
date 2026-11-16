import * as path from 'node:path';
import * as cdk from 'aws-cdk-lib';
import * as cloudfront from 'aws-cdk-lib/aws-cloudfront';
import * as origins from 'aws-cdk-lib/aws-cloudfront-origins';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as logs from 'aws-cdk-lib/aws-logs';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as s3deploy from 'aws-cdk-lib/aws-s3-deployment';
import { Construct } from 'constructs';

/**
 * A Lambda Web Function that is reachable only through one CloudFront distribution.
 *
 * - The endpoint uses AuthType IamAuth from creation, so Lambda rejects every
 *   request that is not SigV4-signed (403) before the application runs.
 * - CloudFront signs each origin request through an Origin Access Control of
 *   type `lambda` (SigningBehavior `always-amz-auth`).
 * - A resource policy on the function allows lambda:InvokeWebFunctionEndpoint
 *   for the CloudFront service principal only when AWS:SourceArn is this
 *   distribution.
 *
 * There are no L2 constructs for Web Functions yet, so the function, revision,
 * endpoint and resource policy use the generated L1 (Cfn*) classes.
 */
export class LambdaWebCloudFrontOacStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const functionName = cdk.Stack.of(this).stackName;
    const endpointName = 'dev';

    // --- Code bucket -------------------------------------------------------
    // AWS::Lambda::WebFunctionRevision loads the zip from S3. The bucket must
    // have versioning enabled and allow the Lambda service to read objects.
    const codeBucket = new s3.Bucket(this, 'CodeBucket', {
      versioned: true,
      blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
      encryption: s3.BucketEncryption.S3_MANAGED,
      enforceSSL: true,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      autoDeleteObjects: true,
    });
    codeBucket.addToResourcePolicy(
      new iam.PolicyStatement({
        sid: 'LambdaWebFunctionsReadCode',
        principals: [new iam.ServicePrincipal('lambda.amazonaws.com')],
        actions: ['s3:GetObject', 's3:GetObjectVersion'],
        resources: [codeBucket.arnForObjects('*')],
        conditions: { StringEquals: { 'aws:SourceAccount': this.account } },
      }),
    );

    // Upload src/ as ONE zip object (extract: false). The object key is derived
    // from the asset hash, so a code change produces a new key, which in turn
    // replaces the immutable revision below. prune is off so that the zip of a
    // revision that is being replaced stays readable until the swap completes.
    // No destinationKeyPrefix: `objectKeys` reports the source key (no prefix),
    // and the bucket holds nothing but this function's code.
    const code = new s3deploy.BucketDeployment(this, 'Code', {
      destinationBucket: codeBucket,
      sources: [s3deploy.Source.asset(path.join(__dirname, '..', 'src'))],
      extract: false,
      prune: false,
    });
    const codeKey = cdk.Fn.select(0, code.objectKeys);
    const codeVersionId = cdk.Fn.select(0, code.objectVersionIds);

    // --- Execution role and log group ---------------------------------------
    const executionRole = new iam.Role(this, 'ExecutionRole', {
      assumedBy: new iam.ServicePrincipal('lambda.amazonaws.com'),
      description: `Execution role for the ${functionName} Lambda Web Function (logs only)`,
      managedPolicies: [
        iam.ManagedPolicy.fromAwsManagedPolicyName('service-role/AWSLambdaBasicExecutionRole'),
      ],
    });

    const logGroup = new logs.LogGroup(this, 'LogGroup', {
      logGroupName: `/aws/lambda/web/${functionName}`,
      retention: logs.RetentionDays.ONE_WEEK,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    // --- Web Function: function + revision + endpoint ------------------------
    const webFunction = new lambda.CfnWebFunction(this, 'WebFunction', { functionName });

    const revision = new lambda.CfnWebFunctionRevision(this, 'WebFunctionRevision', {
      functionName: webFunction.ref,
      description: 'Deployed by CDK',
      buildConfig: {
        runtimeConfig: { runtime: 'nodejs24.x' },
        codeConfig: {
          s3Object: { bucket: codeBucket.bucketName, key: codeKey, versionId: codeVersionId },
        },
      },
      serviceConfig: {
        executionRoleArn: executionRole.roleArn,
        // Request timeout in seconds (3-900).
        timeoutSeconds: 30,
        telemetryConfig: { loggingConfig: { logGroup: logGroup.logGroupName } },
      },
    });
    revision.node.addDependency(code);
    revision.node.addDependency(logGroup);

    const endpoint = new lambda.CfnWebFunctionEndpoint(this, 'WebFunctionEndpoint', {
      functionName: webFunction.ref,
      endpointName,
      // IamAuth from the first deployment: the endpoint is never public.
      authType: 'IamAuth',
      // One regional endpoint. The type and Regions cannot be changed later.
      endpointType: 'HomeRegion',
      revisionWeights: [{ revisionId: revision.attrRevisionId, weight: 100 }],
    });

    // --- CloudFront: OAC + distribution ------------------------------------
    // OriginAccessControlOriginType must be `lambda` and SigningBehavior
    // `always-amz-auth` for Web Function origins (`always` is rejected).
    const oac = new cloudfront.CfnOriginAccessControl(this, 'OriginAccessControl', {
      originAccessControlConfig: {
        name: functionName,
        description: `Signs CloudFront requests to the ${functionName} Web Function`,
        originAccessControlOriginType: 'lambda',
        signingProtocol: 'sigv4',
        signingBehavior: 'always-amz-auth',
      },
    });

    // Cache key = path + query string + the viewer's Authorization header.
    // The managed CachingOptimized policy leaves query strings and
    // Authorization out of the key, and CloudFront forwards Authorization to
    // the origin only when the cache policy includes it. This policy keeps
    // CachingOptimized's TTLs and compression and adds both, so each
    // signed-in viewer gets their own cache entries.
    const cachePolicy = new cloudfront.CachePolicy(this, 'CachePolicy', {
      cachePolicyName: functionName,
      comment: 'Path, query string and Authorization header in the cache key',
      minTtl: cdk.Duration.seconds(1),
      defaultTtl: cdk.Duration.days(1),
      maxTtl: cdk.Duration.days(365),
      enableAcceptEncodingGzip: true,
      enableAcceptEncodingBrotli: true,
      headerBehavior: cloudfront.CacheHeaderBehavior.allowList('Authorization'),
      cookieBehavior: cloudfront.CacheCookieBehavior.none(),
      queryStringBehavior: cloudfront.CacheQueryStringBehavior.all(),
    });

    const distribution = new cloudfront.Distribution(this, 'Distribution', {
      comment: functionName,
      priceClass: cloudfront.PriceClass.PRICE_CLASS_100,
      defaultBehavior: {
        origin: new origins.HttpOrigin(endpoint.attrDomainName, {
          protocolPolicy: cloudfront.OriginProtocolPolicy.HTTPS_ONLY,
          originSslProtocols: [cloudfront.OriginSslPolicy.TLS_V1_2],
          originAccessControlId: oac.attrId,
        }),
        viewerProtocolPolicy: cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
        allowedMethods: cloudfront.AllowedMethods.ALLOW_ALL,
        cachedMethods: cloudfront.CachedMethods.CACHE_GET_HEAD,
        compress: true,
        cachePolicy,
        // Forward viewer headers and query string, but not Host: Lambda routes
        // on Host, so the origin request must carry the endpoint domain.
        originRequestPolicy: cloudfront.OriginRequestPolicy.ALL_VIEWER_EXCEPT_HOST_HEADER,
      },
    });

    // --- Resource policy: only this distribution may invoke the endpoint -----
    const distributionArn = this.formatArn({
      service: 'cloudfront',
      region: '',
      resource: 'distribution',
      resourceName: distribution.distributionId,
    });

    new lambda.CfnResourcePolicy(this, 'ResourcePolicy', {
      resourceArn: webFunction.attrFunctionArn,
      policyDocument: {
        Version: '2012-10-17',
        Statement: [
          {
            Sid: 'AllowCloudFrontDistribution',
            Effect: 'Allow',
            Principal: { Service: 'cloudfront.amazonaws.com' },
            Action: 'lambda:InvokeWebFunctionEndpoint',
            Resource: `${webFunction.attrFunctionArn}/endpoint/${endpointName}`,
            Condition: { StringEquals: { 'AWS:SourceArn': distributionArn } },
          },
        ],
      },
    });

    // --- Outputs -------------------------------------------------------------
    new cdk.CfnOutput(this, 'CloudFrontUrl', {
      description: 'Request the application through here',
      value: `https://${distribution.distributionDomainName}`,
    });
    new cdk.CfnOutput(this, 'OriginUrl', {
      description: 'The Web Function endpoint; returns 403 when called directly',
      value: `https://${endpoint.attrDomainName}`,
    });
    new cdk.CfnOutput(this, 'DistributionId', { value: distribution.distributionId });
    new cdk.CfnOutput(this, 'FunctionArn', { value: webFunction.attrFunctionArn });
    new cdk.CfnOutput(this, 'CodeBucketName', { value: codeBucket.bucketName });
  }
}
