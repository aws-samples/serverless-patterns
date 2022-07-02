import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct, DependencyGroup } from 'constructs';
import { MediaConnect } from './media_connect';
import { MediaLive } from './media_live';
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

    //2. Create the media connect
    const mediaConnect = new MediaConnect(this, "MyMediaConnect");


    //3. Create Media Live Channel
    const mediaLiveChannel = new MediaLive(
      this,
      "MediaLive",
      mediaPackageChannel.channel.id,
      mediaConnect.flowArnA,
      mediaConnect.flowArnB
    );

    mediaLiveChannel.node.addDependency(mediaConnect);


    //Add dependencyto wait for MediaPackage channel to be ready before deploying MediaLive
    const mediadep = new DependencyGroup();
    mediadep.add(mediaPackageChannel.channel);

    mediaLiveChannel.channelLive.node.addDependency(mediadep);




  }
}
