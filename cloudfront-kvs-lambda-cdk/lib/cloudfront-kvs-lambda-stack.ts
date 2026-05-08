import * as cdk from 'aws-cdk-lib';
import * as cloudfront from 'aws-cdk-lib/aws-cloudfront';
import * as origins from 'aws-cdk-lib/aws-cloudfront-origins';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as s3 from 'aws-cdk-lib/aws-s3';
import { Construct } from 'constructs';

export class CloudfrontKvsLambdaStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // KeyValueStore for edge configuration (feature flags, redirects, A/B test config)
    const kvs = new cloudfront.KeyValueStore(this, 'ConfigStore', {
      keyValueStoreName: 'edge-config-store',
      comment: 'Feature flags and routing config at the edge'
    });

    // CloudFront Function that reads from KVS
    const cfFunction = new cloudfront.Function(this, 'RouterFn', {
      code: cloudfront.FunctionCode.fromInline(`
        import cf from 'cloudfront';
        const kvsHandle = cf.kvs();

        async function handler(event) {
          const request = event.request;
          const uri = request.uri;

          try {
            // Check if there's a redirect rule for this path
            const redirect = await kvsHandle.get(uri);
            if (redirect) {
              return { statusCode: 302, statusDescription: 'Found', headers: { location: { value: redirect } } };
            }
          } catch (e) {
            // Key not found - continue to origin
          }

          // Check feature flag for A/B testing
          try {
            const abConfig = await kvsHandle.get('ab-test-enabled');
            if (abConfig === 'true') {
              request.headers['x-ab-variant'] = { value: Math.random() > 0.5 ? 'A' : 'B' };
            }
          } catch (e) {}

          return request;
        }
      `),
      functionName: 'kvs-edge-router',
      runtime: cloudfront.FunctionRuntime.JS_2_0,
      keyValueStore: kvs
    });

    // Origin bucket
    const bucket = new s3.Bucket(this, 'OriginBucket', {
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      autoDeleteObjects: true
    });

    // CloudFront distribution
    const distribution = new cloudfront.Distribution(this, 'Distribution', {
      defaultBehavior: {
        origin: origins.S3BucketOrigin.withOriginAccessControl(bucket),
        functionAssociations: [{
          function: cfFunction,
          eventType: cloudfront.FunctionEventType.VIEWER_REQUEST
        }]
      }
    });

    new cdk.CfnOutput(this, 'DistributionUrl', { value: `https://${distribution.distributionDomainName}` });
    new cdk.CfnOutput(this, 'KeyValueStoreArn', { value: kvs.keyValueStoreArn });
    new cdk.CfnOutput(this, 'BucketName', { value: bucket.bucketName });
  }
}
