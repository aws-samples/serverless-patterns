import { Aws, aws_mediapackage as mediapackage, CfnOutput } from "aws-cdk-lib";

import { Construct } from "constructs";
import { loadMediaPackageConfig } from "../helpers/configuration";
export class MediaPackage extends Construct {
  public readonly channel: mediapackage.CfnChannel;

  constructor(scope: Construct, id: string) {
    super(scope, id);

    this.channel = new mediapackage.CfnChannel(this, "MyCfnChannel", {
      id: "myMediaPackageChannel",
      description: "Channel for " + Aws.STACK_NAME,
    });

    const config = loadMediaPackageConfig();

    const hlsPackage: mediapackage.CfnOriginEndpoint.HlsPackageProperty = {
      segmentDurationSeconds: config.hls_segment_duration_seconds,
      playlistWindowSeconds: config.hls_playlist_window_seconds,
      streamSelection: {
        minVideoBitsPerSecond: config.hls_min_video_bits_per_second,
        maxVideoBitsPerSecond: config.hls_max_video_bits_per_second,
        streamOrder: config.hls_stream_order,
      },
    };

    const hls_endpoint = new mediapackage.CfnOriginEndpoint(
      this,
      "HlsEndpoint",
      {
        channelId: this.channel.id,
        id: Aws.STACK_NAME + "-hls-" + this.channel.id,
        hlsPackage,
      }
    );

    hls_endpoint.node.addDependency(this.channel);

    // Output the url stream to player
    new CfnOutput(this, "HlsUrlStream", {
      exportName: Aws.STACK_NAME + "-HLS-URL",
      value: hls_endpoint.attrUrl,
    });

    const dashPackage: mediapackage.CfnOriginEndpoint.DashPackageProperty = {
      segmentDurationSeconds: config.dash_segment_duration_seconds,
      manifestWindowSeconds: config.dash_manifest_window_seconds,
      streamSelection: {
        minVideoBitsPerSecond: config.dash_min_video_bits_per_second,
        maxVideoBitsPerSecond: config.dash_max_video_bits_per_second,
        streamOrder: config.dash_stream_order,
      },
    };

    const dash_endpoint = new mediapackage.CfnOriginEndpoint(
      this,
      "DashEndpoint",
      {
        channelId: this.channel.id,
        id: Aws.STACK_NAME + "-dash-" + this.channel.id,
        dashPackage,
      }
    );

    dash_endpoint.node.addDependency(this.channel);

    // Output the url stream to player
    new CfnOutput(this, "DashUrlStream", {
      exportName: Aws.STACK_NAME + "-DASH-URL",
      value: dash_endpoint.attrUrl,
    });
    const mssPackage: mediapackage.CfnOriginEndpoint.MssPackageProperty = {
      segmentDurationSeconds: config.mss_segment_duration_seconds,
      manifestWindowSeconds: config.mss_manifest_window_seconds,
      streamSelection: {
        minVideoBitsPerSecond: config.mss_min_video_bits_per_second,
        maxVideoBitsPerSecond: config.mss_max_video_bits_per_second,
        streamOrder: config.mss_stream_order,
      },
    };

    const mss_endpoint = new mediapackage.CfnOriginEndpoint(
      this,
      "MssEndpoint",
      {
        channelId: this.channel.id,
        id: Aws.STACK_NAME + "-mss-" + this.channel.id,
        mssPackage,
      }
    );

    mss_endpoint.node.addDependency(this.channel);

    // Output the url stream to player
    new CfnOutput(this, "MssUrlStream", {
      exportName: Aws.STACK_NAME + "-MSS-URL",
      value: mss_endpoint.attrUrl,
    });
  }
}
