/**
 *  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 *  Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance
 *  with the License. A copy of the License is located at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  or in the 'license' file accompanying this file. This file is distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES
 *  OR CONDITIONS OF ANY KIND, express or implied. See the License for the specific language governing permissions
 *  and limitations under the License.
 */

 import { 
  Aws, 
  aws_mediapackage as mediapackage, 
  aws_cloudfront as cloudfront,
  aws_cloudfront_origins as origins,
  Fn} from "aws-cdk-lib";
import { Construct } from "constructs";
import { Secrets } from "./secrets";

export class CloudFront extends Construct {
  //👇 Defining public variables to export on CloudFormation 
  public readonly channel: mediapackage.CfnChannel;
  public readonly hlsPlayback: string;
  public readonly dashPlayback: string;
  public readonly myChannelArn: string;
  public readonly myDistribId: string;
  public readonly myDistribHostname: string;

  //Defining private Variable
  private readonly CDNHEADER="MediaPackageCDNIdentifier"

  constructor(scope: Construct, 
    id: string, 
    hlsEndpoint: string, 
    dashEndpoint: string,
    props: Secrets){
    super(scope, id);

    //👇 Defining Origin Hostname variables for EMP
    const mediaPackageHostname = Fn.select(2, Fn.split("/", hlsEndpoint));

    //👇 Creating generic Viewer/Country/City Origin Request Policy with CloudFront Header
    const myOriginRequestPolicy = new cloudfront.OriginRequestPolicy(this, 'OriginRequestPolicy',
        {
          originRequestPolicyName: Aws.STACK_NAME + "Viewer-Country-City",
          comment: "Policy to FWD CloudFront headers",
          headerBehavior: cloudfront.OriginRequestHeaderBehavior.allowList(
            "CloudFront-Viewer-Address",
            "CloudFront-Viewer-Country",
            "CloudFront-Viewer-City",
            "Referer",
            "User-Agent",
            "Access-Control-Request-Method",
            "Access-Control-Request-Headers"
          ),
          queryStringBehavior: cloudfront.OriginRequestQueryStringBehavior.all(),
        }
      );

    //👇 Creating EMP origin with green header
    const mediaPackageOrigin = new origins.HttpOrigin(
        mediaPackageHostname,
        {
          customHeaders: {
          'X-MediaPackage-CDNIdentifier': props.cdnSecret.secretValueFromJson(this.CDNHEADER).unsafeUnwrap().toString(),
          },
          originSslProtocols: [cloudfront.OriginSslPolicy.SSL_V3],
          protocolPolicy: cloudfront.OriginProtocolPolicy.HTTPS_ONLY,
        }
    );

    //👇 Creating the CloudFront Distribution
    const distribution = new cloudfront.Distribution(this, "Distribution", {
        comment: Aws.STACK_NAME + " - CDK deployment Secure Media Delivery",
        defaultRootObject: "",
        minimumProtocolVersion: cloudfront.SecurityPolicyProtocol.TLS_V1_2016,
        defaultBehavior: {
          origin: mediaPackageOrigin,
          cachePolicy: cloudfront.CachePolicy.CACHING_OPTIMIZED,
          allowedMethods: cloudfront.AllowedMethods.ALLOW_GET_HEAD,
          viewerProtocolPolicy: cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
          originRequestPolicy : myOriginRequestPolicy,
        },
        additionalBehaviors: {
          "*.m3u8": {
            origin: mediaPackageOrigin,
            viewerProtocolPolicy: cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
            allowedMethods: cloudfront.AllowedMethods.ALLOW_ALL,
            cachePolicy: cloudfront.CachePolicy.ELEMENTAL_MEDIA_PACKAGE,
            originRequestPolicy : myOriginRequestPolicy,
          },
          "*.ts": {
            origin: mediaPackageOrigin,
            viewerProtocolPolicy: cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
            cachePolicy: cloudfront.CachePolicy.ELEMENTAL_MEDIA_PACKAGE,
            originRequestPolicy : myOriginRequestPolicy,

          },
          "*.mpd": {
            origin: mediaPackageOrigin,
            viewerProtocolPolicy: cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
            cachePolicy: cloudfront.CachePolicy.ELEMENTAL_MEDIA_PACKAGE,
            originRequestPolicy : myOriginRequestPolicy,

          }
        },
    });

    //👇 Getting the path from EMP (/out/v1/<hashed-id-EMP>) & EMT (/v1/master/<hashed-id-EMT>/<config-EMT>) endpoints
    const hlsPath = Fn.select(1, Fn.split("/out/", hlsEndpoint));
    const dashPath = Fn.select(1, Fn.split("/out/", dashEndpoint));


    this.hlsPlayback="https://" + distribution.domainName + '/out/' + hlsPath
    this.dashPlayback="https://" + distribution.domainName + '/out/' + dashPath

    this.myDistribId=distribution.distributionId
    this.myDistribHostname=distribution.distributionDomainName

}

}