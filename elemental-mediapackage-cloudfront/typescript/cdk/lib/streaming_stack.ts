import {
  Stack,
  StackProps,
  Duration,
  CfnOutput,
  aws_iam as iam,
} from "aws-cdk-lib";
import { Construct } from 'constructs';
import { MediaPackageCdnAuth } from './media_package';
import { CloudFront } from './cloudfront';

import { Secrets } from "./secrets";


export class StreamingStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    //1. Create Secrets, Policy and Role to be used by MediaPackage for CDN Authorization
    const secrets = new Secrets(this, "Secrets");

    const customPolicy = new iam.PolicyDocument({
        statements: [
          new iam.PolicyStatement({
            resources: [
              secrets.cdnSecret.secretArn,
            ],
            actions: [
              "secretsmanager:GetSecretValue",
              "secretsmanager:DescribeSecret",
              "secretsmanager:ListSecrets",
              "secretsmanager:ListSecretVersionIds",
            ],
          }),
        ],
    });

    //Role to be used by MediaPackage for CDN Authorization
    const role4mediapackage = new iam.Role(this, "MyMediaPackageRole", {
        description: "A role to be assumed by MediaPackage",
        assumedBy: new iam.ServicePrincipal('mediapackage.amazonaws.com'),
        inlinePolicies: {
          policy: customPolicy,
        },
        maxSessionDuration: Duration.hours(1),
    });

    //2. Create MediaPackage Channel using CDN Authorization
    const mediaPackageChannel = new MediaPackageCdnAuth(
      this,
      "MyMediaPackageChannel",
      role4mediapackage.roleArn,
      secrets,
    );


   //3. Create CloudFront distribution
   const cloudfront = new CloudFront(
    this,
    "MyCloudFrontDistribution", 
    mediaPackageChannel.hlsEndpoint, 
    mediaPackageChannel.dashEndpoint,
    secrets
  );
  

  //👇 Generating Cfn output
  new CfnOutput(this, "MediaPackageChannelName", {
    value: mediaPackageChannel.myChannelName,
  });
  new CfnOutput(this, "MediaPackageChannelArn", {
    value: mediaPackageChannel.myChannelArn,
  });


  new CfnOutput(this, "CloudFrontDistributionId", {
    value: cloudfront.myDistribId,
  });
  new CfnOutput(this, "CloudFrontDistribution-HLS", {
    value: cloudfront.hlsPlayback,
  });
  new CfnOutput(this, "CloudFrontDistribution-DASH", {
    value: cloudfront.dashPlayback,
  });
  }
}
