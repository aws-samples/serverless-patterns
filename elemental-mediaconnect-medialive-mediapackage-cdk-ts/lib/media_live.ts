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

  constructor(
    scope: Construct,
    id: string,
    mediaPackageChannelId: string,
    mediaConnectFlowA: string,
    mediaConnectFlowB: string
  ) {
    super(scope, id);

    const config = loadMediaLiveConfig();

    const policy = {
      Version: "2012-10-17",
      Statement: [
        {
          Effect: "Allow",
          Action: [
            "mediaconnect:ManagedDescribeFlow",
            "mediaconnect:ManagedAddOutput",
            "mediaconnect:ManagedRemoveOutput",
            "mediaconnect:AddFlowMediaStreams",
            "mediaconnect:AddFlowOutputs",
            "mediaconnect:AddFlowSources",
            "mediaconnect:CreateFlow",
            "mediaconnect:DeleteFlow",
          ],
          Resource: [`arn:aws:mediaconnect:${Aws.REGION}:${Aws.ACCOUNT_ID}:*`]
        }
      ],
    };

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
      inlinePolicies: {
        medialivecustom: iam.PolicyDocument.fromJson(policy),
      },
      assumedBy: new iam.ServicePrincipal("medialive.amazonaws.com"),
    });

    //1. Create Input

    const cfnInputProps: medialive.CfnInputProps = {
      name: Aws.STACK_NAME + "_MyInput",
      type: "MEDIACONNECT",
      roleArn: role.roleArn,
      mediaConnectFlows: [
        {
          flowArn: mediaConnectFlowA,
        },
        {
          flowArn: mediaConnectFlowB,
        },
      ],
    };

    const medialive_input = new medialive.CfnInput(
      this,
      "MediaInputChannel",
      cfnInputProps
    );

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


    this.channelLive = channelLive;
  }
}
