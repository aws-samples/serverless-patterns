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
  aws_mediapackage as mediapackage } from "aws-cdk-lib";
import { Construct } from "constructs";
import { loadMediaPackageConfig } from "../helpers/configuration";
import { Secrets } from "./secrets";

export class MediaPackageCdnAuth extends Construct {
  public readonly myChannel: mediapackage.CfnChannel;
  public readonly hlsEndpoint: string;
  public readonly dashEndpoint: string;
  public readonly cmafEndpoint: string;
  public readonly mssEndpoint: string;
  public readonly myChannelArn: string;
  public readonly myChannelName: string;
  

  constructor(scope: Construct, 
    id: string, 
    roleEMP: string, 
    props: Secrets){
    super(scope, id);
    const myMediaPackageChannelName=Aws.STACK_NAME + "_MediaPackageChannel"
    const config = loadMediaPackageConfig();
  
    //👇 Creating EMP channel
    this.myChannel = new mediapackage.CfnChannel(this, "MyCfnChannel", {
      id: myMediaPackageChannelName,
      description: "Channel for " + Aws.STACK_NAME,
    });


    //👇 HLS Packaging & endpoint with CDN authorization
    const hlsPackage: mediapackage.CfnOriginEndpoint.HlsPackageProperty = { 
      adMarkers: config.ad_markers,
      adTriggers: ['BREAK',
        'DISTRIBUTOR_ADVERTISEMENT',
        'DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY',
        'DISTRIBUTOR_PLACEMENT_OPPORTUNITY',
        'PROVIDER_ADVERTISEMENT',
        'PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY',
        'PROVIDER_PLACEMENT_OPPORTUNITY',
        'SPLICE_INSERT'],
      segmentDurationSeconds: config.hls_segment_duration_seconds,
      programDateTimeIntervalSeconds: config.hls_program_date_interval,
      playlistWindowSeconds: config.hls_playlist_window_seconds,
      useAudioRenditionGroup:true,
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
        channelId: this.myChannel.id,
        id: Aws.STACK_NAME + "-hls-" + this.myChannel.id,
        hlsPackage,
        // the properties below are optional
        authorization: {
          cdnIdentifierSecret: props.cdnSecret.secretArn,
          secretsRoleArn: roleEMP,
        },
      }
    );
    this.hlsEndpoint = hlsEndpoint.attrUrl;
    hlsEndpoint.node.addDependency(this.myChannel);


    //👇 DASH Packaging & endpoint with CDN authorization
    const dashPackage: mediapackage.CfnOriginEndpoint.DashPackageProperty = {
      periodTriggers: [config.dash_period_triggers],
      adTriggers: ['BREAK',
      'DISTRIBUTOR_ADVERTISEMENT',
      'DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY',
      'DISTRIBUTOR_PLACEMENT_OPPORTUNITY',
      'PROVIDER_ADVERTISEMENT',
      'PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY',
      'PROVIDER_PLACEMENT_OPPORTUNITY',
      'SPLICE_INSERT'],
      segmentDurationSeconds: config.dash_segment_duration_seconds,
      segmentTemplateFormat: 'TIME_WITH_TIMELINE',
      profile: 'NONE',
      minBufferTimeSeconds: 10,
      minUpdatePeriodSeconds: config.dash_segment_duration_seconds,
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
        channelId: this.myChannel.id,
        id: Aws.STACK_NAME + "-dash-",
        dashPackage,
        // the properties below are optional
        authorization: {
          cdnIdentifierSecret: props.cdnSecret.secretArn,
          secretsRoleArn: roleEMP,
        },
      }
    );
    this.dashEndpoint = dashEndpoint.attrUrl;
    dashEndpoint.node.addDependency(this.myChannel);

   //👇 CMAF Packaging & endpoint with CDN authorization
   const cmafPackage: mediapackage.CfnOriginEndpoint.CmafPackageProperty = {
      
    hlsManifests: [{
      id: Aws.STACK_NAME + "-cmaf-",
      // the properties below are optional
      adMarkers: config.ad_markers,
      includeIframeOnlyStream: false,
      playlistWindowSeconds: config.cmaf_manifest_window_seconds,
      programDateTimeIntervalSeconds: config.cmaf_program_date_interval,
      url: 'url',
    }],
    segmentDurationSeconds: config.cmaf_segment_duration_seconds,
    segmentPrefix: 'segmentPrefix',
    streamSelection: {
      maxVideoBitsPerSecond: config.cmaf_max_video_bits_per_second,
      minVideoBitsPerSecond: config.cmaf_min_video_bits_per_second,
      streamOrder: config.cmaf_stream_order,
    },
  };

  const cmafEndpoint = new mediapackage.CfnOriginEndpoint(
    this,
    "cmafEndpoint",
    {
      channelId: this.myChannel.id,
      id: Aws.STACK_NAME + "-cmaf-",
      cmafPackage,
      // the properties below are optional
      authorization: {
        cdnIdentifierSecret: props.cdnSecret.secretArn,
        secretsRoleArn: roleEMP,
      },
    }
  );
  this.cmafEndpoint = cmafEndpoint.attrUrl;
  cmafEndpoint.node.addDependency(this.myChannel);


    //👇 MSS Packaging & endpoint with CDN authorization
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
        channelId: this.myChannel.id,
        id: Aws.STACK_NAME + "-mss-",
        mssPackage,
        // the properties below are optional
        authorization: {
          cdnIdentifierSecret: props.cdnSecret.secretArn,
          secretsRoleArn: roleEMP,
        },
      }
    );
    this.mssEndpoint = mssEndpoint.attrUrl;
    mssEndpoint.node.addDependency(this.myChannel);

    this.myChannelName=myMediaPackageChannelName;
    this.myChannelArn=this.myChannel.attrArn;
  }
}
