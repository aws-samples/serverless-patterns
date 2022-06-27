import { Aws, aws_mediapackage as mediapackage, CfnOutput } from "aws-cdk-lib";

import { Construct } from "constructs";
import { loadMediaPackageConfig } from "../helpers/configuration";
export class MediaPackage extends Construct {
  public readonly hlsEndpoint: string;
  public readonly dashEndpoint: string;
  public readonly mssEndpoint: string;

  constructor(scope: Construct, id: string) {
    super(scope, id);

    const myChannel = new mediapackage.CfnChannel(this, "MyCfnChannel", {
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

    const hlsEndpoint = new mediapackage.CfnOriginEndpoint(
      this,
      "HlsEndpoint",
      {
        channelId: myChannel.id,
        id: Aws.STACK_NAME + "-hls-" + myChannel.id,
        hlsPackage,
      }
    );

    this.hlsEndpoint = hlsEndpoint.attrUrl;

    hlsEndpoint.node.addDependency(myChannel);

    const dashPackage: mediapackage.CfnOriginEndpoint.DashPackageProperty = {
      segmentDurationSeconds: config.dash_segment_duration_seconds,
      manifestWindowSeconds: config.dash_manifest_window_seconds,
      streamSelection: {
        minVideoBitsPerSecond: config.dash_min_video_bits_per_second,
        maxVideoBitsPerSecond: config.dash_max_video_bits_per_second,
        streamOrder: config.dash_stream_order,
      },
    };

    const dashEndpoint = new mediapackage.CfnOriginEndpoint(
      this,
      "DashEndpoint",
      {
        channelId: myChannel.id,
        id: Aws.STACK_NAME + "-dash-" + myChannel.id,
        dashPackage,
      }
    );

    this.dashEndpoint = dashEndpoint.attrUrl;

    dashEndpoint.node.addDependency(myChannel);

    const mssPackage: mediapackage.CfnOriginEndpoint.MssPackageProperty = {
      segmentDurationSeconds: config.mss_segment_duration_seconds,
      manifestWindowSeconds: config.mss_manifest_window_seconds,
      streamSelection: {
        minVideoBitsPerSecond: config.mss_min_video_bits_per_second,
        maxVideoBitsPerSecond: config.mss_max_video_bits_per_second,
        streamOrder: config.mss_stream_order,
      },
    };

    const mssEndpoint = new mediapackage.CfnOriginEndpoint(
      this,
      "MssEndpoint",
      {
        channelId: myChannel.id,
        id: Aws.STACK_NAME + "-mss-" + myChannel.id,
        mssPackage,
      }
    );

    this.mssEndpoint = mssEndpoint.attrUrl;

    mssEndpoint.node.addDependency(myChannel);

    new CfnOutput(this, "HlsUrlStream", {
      exportName: Aws.STACK_NAME + "-HLS-URL",
      value: hlsEndpoint.attrUrl,
    });

    new CfnOutput(this, "DashUrlStream", {
      exportName: Aws.STACK_NAME + "-DASH-URL",
      value: dashEndpoint.attrUrl,
    });

    new CfnOutput(this, "MssUrlStream", {
      exportName: Aws.STACK_NAME + "-MSS-URL",
      value: mssEndpoint.attrUrl,
    });
  }
}
