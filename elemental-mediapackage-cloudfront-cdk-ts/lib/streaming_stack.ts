import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { CloudFront } from './cloudfront';
import { MediaPackage } from './media_package';
// import * as sqs from 'aws-cdk-lib/aws-sqs';

export class StreamingStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    //1. Create MediaPackage Channel
    const mediaPackageChannel = new MediaPackage(
      this,
      "MediaPackage"
    );

    //2. Create CloudFront distribution
    const cloudfront = new CloudFront(this, "MyCloudFront", mediaPackageChannel.hlsEndpoint, mediaPackageChannel.dashEndpoint, mediaPackageChannel.mssEndpoint);
  }

}
