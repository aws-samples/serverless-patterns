import * as cdk from "aws-cdk-lib";
import * as cloudfront from "aws-cdk-lib/aws-cloudfront";
import * as origins from "aws-cdk-lib/aws-cloudfront-origins";
import * as apigateway from "aws-cdk-lib/aws-apigateway";
import * as s3 from "aws-cdk-lib/aws-s3";
import { Construct } from "constructs";

export class PatternStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // create two Rest API GWs, both with a http status 200 mock response, but with individual payload
    const api1 = new apigateway.RestApi(this, "api1", {
      description: "API 1",
      endpointConfiguration: {
        types: [apigateway.EndpointType.REGIONAL],
      },
    });
    api1.root.addMethod(
      "GET",
      new apigateway.MockIntegration({
        integrationResponses: [
          {
            statusCode: "200",
            responseTemplates: {
              "application/json": `{"message": "Hello from API 1"}`,
            },
          },
        ],
        requestTemplates: {
          "application/json": '{"statusCode": 200}',
        },
      }),
      {
        methodResponses: [{ statusCode: "200" }],
      },
    );
    const api2 = new apigateway.RestApi(this, "api2", {
      description: "API 2",
      endpointConfiguration: {
        types: [apigateway.EndpointType.REGIONAL],
      },
    });
    api2.root.addMethod(
      "GET",
      new apigateway.MockIntegration({
        integrationResponses: [
          {
            statusCode: "200",
            responseTemplates: {
              "application/json": `{"message": "Hello from API 2"}`,
            },
          },
        ],
        requestTemplates: {
          "application/json": '{"statusCode": 200}',
        },
      }),
      {
        methodResponses: [{ statusCode: "200" }],
      },
    );

    const kvStore = new cloudfront.KeyValueStore(this, "KVStore", {});

    const bucket = new s3.Bucket(this, "DistributionBucket", {
      bucketName: `distribution-bucket-${this.account}`,
      enforceSSL: true,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    // 2. Create CloudFront Function for redirects
    const redirectFunction = new cloudfront.Function(this, "RedirectFunction", {
      code: cloudfront.FunctionCode.fromInline(`
        import cf from 'cloudfront';

        // This fails if there is no key value store associated with the function
        const kvsHandle = cf.kvs();

        async function handler(event) {
          const request = event.request;

          const kvKey = 'APIGW' + (Math.random() < 0.5 ? 1 : 2) + 'URL';

          const redirectUrl = await kvsHandle.get(kvKey);

          const response = {
              statusCode: 302,
              statusDescription: 'Found',
              headers:
                  { "location": { "value": redirectUrl } }
              }

          return response;
        }
      `),
      // Note that JS_2_0 must be used for Key Value Store support
      runtime: cloudfront.FunctionRuntime.JS_2_0,
      keyValueStore: kvStore,
    });

    // add cloudfront distribution with no behaviour
    const cloudFrontDistribution = new cloudfront.Distribution(this, "CloudFrontDistribution", {
      defaultBehavior: {
        origin: origins.S3BucketOrigin.withOriginAccessControl(bucket),
        functionAssociations: [
          {
            function: redirectFunction,
            eventType: cloudfront.FunctionEventType.VIEWER_REQUEST,
          },
        ],
      },
    });

    // Output Cloudfront URL as CloudFormation output
    new cdk.CfnOutput(this, "CLOUDFRONTDOMAINNAME", {
      value: cloudFrontDistribution.distributionDomainName,
    });

    new cdk.CfnOutput(this, "APIGATEWAY1URL", {
      value: api1.url,
    });

    new cdk.CfnOutput(this, "APIGATEWAY2URL", {
      value: api2.url,
    });

    // output kv arn
    new cdk.CfnOutput(this, "KVSTOREARN", {
      value: kvStore.keyValueStoreArn,
    });
  }
}
