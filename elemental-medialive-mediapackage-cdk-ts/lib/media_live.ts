import {
  aws_medialive as medialive,
  aws_iam as iam,
  Aws,
  CfnOutput,
  Fn,
} from "aws-cdk-lib";
import { Construct } from "constructs";
import { loadMediaLiveConfig } from "../helpers/configuration";

export class MediaLive extends Construct {
  public readonly channelLive: medialive.CfnChannel;

  constructor(scope: Construct, id: string, mediaPackageChannelId: string) {
    super(scope, id);

    const config = loadMediaLiveConfig();

    const role = new iam.Role(this, "MediaLiveAccessRole", {
      managedPolicies: [
        {
          managedPolicyArn:
            "arn:aws:iam::aws:policy/AWSElementalMediaPackageFullAccess",
        },
        {
          managedPolicyArn: "arn:aws:iam::aws:policy/CloudWatchLogsFullAccess",
        },
      ],
      assumedBy: new iam.ServicePrincipal("medialive.amazonaws.com"),
    });

    const mediaLiveSG = new medialive.CfnInputSecurityGroup(
      this,
      "MediaLiveInputSecurityGroup",
      {
        whitelistRules: [
          {
            cidr: config.inputCidr,
          },
        ],
      }
    );

    //1. Create Input

    var cfnInputProps: medialive.CfnInputProps = {
      name: '',
      type: '',
      inputSecurityGroups: [],
    };

    switch (config.type) {

      case "RTP_PUSH":
        cfnInputProps = {
          name: Aws.STACK_NAME + "_MyChannel",
          type: config.type,
          inputSecurityGroups: [mediaLiveSG.ref],
        };
        break;
      case "RTMP_PUSH":
        cfnInputProps = {
          name: Aws.STACK_NAME + "_MyChannel",
          type: config.type,
          inputSecurityGroups: [mediaLiveSG.ref],
          destinations: [
            {
              streamName: config.streamName + "/primary",
            },
            {
              streamName: config.streamName + "/secondary",
            },
          ],
        };
        break;
      case "RTMP_PULL":
      case "URL_PULL":
        cfnInputProps = {
          name: Aws.STACK_NAME + "_MyInput",
          type: config.type,
          sources: [
            {
              url: config.priUrl,
            },
            {
              url: config.secUrl,
            },
          ],
        };
        break;
    }

    const medialive_input = new medialive.CfnInput(this, "MediaInputChannel", cfnInputProps);

    //2. Create Channel
    var params = {
      resolution: "",
      maximumBitrate: "",
      encoderSettings: "",
    };

    switch (config.encodingProfile) {
      case "HD-1080p":
        params.resolution = "HD";
        params.maximumBitrate = "MAX_20_MBPS";
        params.encoderSettings = require("../config/encoding-profiles/hd-1080p");
        break;
      case "HD-720p":
        params.resolution = "HD";
        params.maximumBitrate = "MAX_10_MBPS";
        params.encoderSettings = require("../config/encoding-profiles/hd-720p");
        break;
      case "SD-540p":
        params.resolution = "SD";
        params.maximumBitrate = "MAX_10_MBPS";
        params.encoderSettings = require("../config/encoding-profiles/sd-540p");
        break;
      default:
        throw new Error(
          `EncodingProfile is invalid or undefined: ${config.encodingProfile}`
        );
    }

    const channelLive = new medialive.CfnChannel(this, "MediaLiveChannel", {
      channelClass: "SINGLE_PIPELINE",
      destinations: [
        {
          id: "media-destination",
          mediaPackageSettings: [
            {
              channelId: mediaPackageChannelId,
            },
          ],
        },
      ],
      inputSpecification: {
        codec: config.codec,
        resolution: params.resolution,
        maximumBitrate: params.maximumBitrate,
      },
      name: "MyMediaLiveChannel",
      roleArn: role.roleArn,
      inputAttachments: [
        {
          inputId: medialive_input.ref,
          inputAttachmentName: "media-package-input",
        },
      ],
      encoderSettings:
        params.encoderSettings as medialive.CfnChannel.EncoderSettingsProperty,
    });

    new CfnOutput(this, "MediaLiveChannelArn", {
      value: channelLive.attrArn,
    });


    new CfnOutput(this, "MediaLiveEndpoint", {
      value: Fn.join("", [Fn.select(0, medialive_input.attrDestinations)]),
    });

    this.channelLive = channelLive;


  }
}
