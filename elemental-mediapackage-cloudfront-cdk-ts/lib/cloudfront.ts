import { Aws, aws_mediapackage as mediapackage, CfnOutput,   aws_cloudfront as cloudfront, Fn } from "aws-cdk-lib";
import { HttpOrigin } from "aws-cdk-lib/aws-cloudfront-origins";

import { Construct } from "constructs";
export class CloudFront extends Construct {
  public readonly channel: mediapackage.CfnChannel;

  constructor(scope: Construct, id: string, hlsEndpoint: string, dashEndpoint: string, mssEndpoint: string) {
    super(scope, id);

    const mediaPackageHostname = Fn.select(2, Fn.split("/", hlsEndpoint));


    const origin = new HttpOrigin(mediaPackageHostname);


    const distribution = new cloudfront.Distribution(this, "Distribution", {
        comment: Aws.STACK_NAME + " - Demo website Secure Media Delivery",
        defaultRootObject: "index.html",
        minimumProtocolVersion: cloudfront.SecurityPolicyProtocol.TLS_V1_2016,
        defaultBehavior: {
          origin: origin,
          cachePolicy: cloudfront.CachePolicy.CACHING_OPTIMIZED,
          allowedMethods: cloudfront.AllowedMethods.ALLOW_GET_HEAD,
          viewerProtocolPolicy: cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
        },
        additionalBehaviors: {
          "*.m3u8": {
            origin: origin,
            viewerProtocolPolicy:
              cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
            cachePolicy: cloudfront.CachePolicy.ELEMENTAL_MEDIA_PACKAGE,

          },
          "*.ts": {
            origin: origin,
            viewerProtocolPolicy:
              cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
            cachePolicy: cloudfront.CachePolicy.ELEMENTAL_MEDIA_PACKAGE,
          }
        },
      });


      const hlsPath = Fn.select(1, Fn.split("/out/", hlsEndpoint));
      const dashPath = Fn.select(1, Fn.split("/out/", dashEndpoint));
      const mssPath = Fn.select(1, Fn.split("/out/", mssEndpoint));

      new CfnOutput(this, "HlsEndpoint", {
        exportName: Aws.STACK_NAME + "-HLS-CF",
        value: "https://" + distribution.domainName + '/out/' + hlsPath,
      });

      new CfnOutput(this, "DashEndpoint", {
        exportName: Aws.STACK_NAME + "-DASH-CF",
        value: "https://" + distribution.domainName + '/out/' + dashPath,
      });

      new CfnOutput(this, "MssEndpoint", {
        exportName: Aws.STACK_NAME + "-MSS-CF",
        value: "https://" + distribution.domainName + '/out/' + mssPath,
      });

  }

}