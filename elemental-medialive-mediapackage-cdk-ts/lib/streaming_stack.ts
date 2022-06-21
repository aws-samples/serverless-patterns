import { Stack, StackProps} from 'aws-cdk-lib';
import { Construct, DependencyGroup } from 'constructs';
import { MediaLive } from './media_live';
import { MediaPackage } from './media_package';

export class StreamingStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);


    //1. Create MediaPackage Channel
    const mediaPackageChannel = new MediaPackage(
      this,
      "MediaPackageChannel"
    );

    //3. Create Media Live Channel
    const mediaLiveChannel = new MediaLive(
      this,
      "MediaLive",
      mediaPackageChannel.channel.id
    );


    //Add dependencyto wait for MediaPackage channel to be ready before deploying MediaLive
    const mediadep = new DependencyGroup();
    mediadep.add(mediaPackageChannel.channel);

    mediaLiveChannel.channelLive.node.addDependency(mediadep);

  }
}
