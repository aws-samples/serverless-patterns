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
  aws_medialive as medialive,
  aws_iam as iam,
  Aws,
} from "aws-cdk-lib";
import { Construct } from "constructs";
import { loadMediaLiveConfig } from "../helpers/configuration";

export class MediaLive extends Construct {
  public readonly channelLive: medialive.CfnChannel;
  public readonly myChannelArn: string;
  public readonly myChannelName: string;
  public readonly myChannelInput: string;

  constructor(scope: Construct, id: string, mediaPackageChannelId: string) {
    super(scope, id);
    const myMediaLiveChannelName=Aws.STACK_NAME + "_MediaLiveChannel"

    const config = loadMediaLiveConfig();
    var destinationValue=[]
    var inputSettingsValue={}

    //👇Generate a Role for MediaLive to access MediaPackage, MediaConnect and S3. You can modify the role to restrict to specific S3 buckets
    const policyMediaConnect = {
      Version: "2012-10-17",
      Statement: [
        {
          Effect: "Allow",
          Action: [
            "mediaconnect:ManagedDescribeFlow",
            "mediaconnect:ManagedAddOutput",
            "mediaconnect:ManagedRemoveOutput",
            "mediaconnect:AddFlowOutputs",
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
        medialivecustom: iam.PolicyDocument.fromJson(policyMediaConnect),
      },
      assumedBy: new iam.ServicePrincipal("medialive.amazonaws.com"),
    });

   //👇Generate Security Groups for RTP and RTMP (Push) inputs 
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

    //👇 1. Create a MediaLive input
    const inputName = Aws.STACK_NAME + "_" + config.inputType + "_MediaLiveInput"
    var cfnInputProps: medialive.CfnInputProps = {
      name: '',
      roleArn: '',
      type: '',
      inputSecurityGroups: [],
      destinations: [{
        streamName: '',
      }],
      inputDevices: [{
        id: '',
      }],
      mediaConnectFlows: [{
        flowArn: '',
      }],
      sources: [{
        passwordParam: 'passwordParam',
        url: 'url',
        username: 'username',
      }],
      vpc: {
        securityGroupIds: [''],
        subnetIds: [''],
      },
    };
    

      //👇1.1 Testing the Input Type
      switch (config.inputType) {
        case "INPUT_DEVICE":
          //👇 Validating if STANDARD or SINGLE_PIPELINE Channel to provide 1 or 2 InputDevice
          if (config.channelClass == "STANDARD") {
            destinationValue=[{id: config.priLink},{id: config.secLink}]
          }else{
            destinationValue=[{id: config.priLink}]
          }
          cfnInputProps = {
            name: inputName,
            type: config.inputType,
            inputDevices: destinationValue ,
          };
        break;
  
        case "RTP_PUSH":
          cfnInputProps = {
            name: inputName,
            type: config.inputType,
            inputSecurityGroups: [mediaLiveSG.ref],
          };
          break;
        case "RTMP_PUSH":
          //👇 Validating if STANDARD or SINGLE_PIPELINE Channel to provide 1 or 2 URL
          if (config.channelClass == "STANDARD") {
            destinationValue=[{streamName: config.streamName + "/primary"},{streamName: config.streamName + "/secondary"}]
          }else{
            destinationValue=[{streamName: config.streamName + "/primary"}]
          }
          cfnInputProps = {
            name: inputName,
            type: config.inputType,
            inputSecurityGroups: [mediaLiveSG.ref],
            destinations: destinationValue,
          };
          break;
        case "MP4_FILE": case "RTMP_PULL": case "URL_PULL": case "TS_FILE":
          //👇 Validating if STANDARD or SINGLE_PIPELINE Channel to provide 1 or 2 URL
          if (config.channelClass == "STANDARD") {
            destinationValue=[{url: config.priUrl},{url: config.secUrl}]
          }else{
            destinationValue=[{url: config.priUrl}]
          }
          cfnInputProps = {
            name: inputName,
            type: config.inputType,
            sources: destinationValue,
          };
          inputSettingsValue={sourceEndBehavior: config.sourceEndBehavior}
          break;
        case "MEDIACONNECT":
          //👇 Validating if STANDARD or SINGLE_PIPELINE Channel to provide 1 or 2 URL
          if (config.channelClass == "STANDARD") {
            destinationValue=[{flowArn: config.priFlow,},{flowArn: config.secFlow,}]
          }else{
            destinationValue=[{flowArn: config.priFlow,}]
          }
          cfnInputProps = {
            name: inputName,
            type: config.inputType,
            roleArn: role.roleArn,
            mediaConnectFlows: destinationValue,
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
      channelClass: config.channelClass,
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
      name: myMediaLiveChannelName,
      roleArn: role.roleArn,
      inputAttachments: [
        {
          inputId: medialive_input.ref,
          inputAttachmentName: inputName,
          inputSettings: inputSettingsValue,
        },
      ],
      encoderSettings:
        params.encoderSettings as medialive.CfnChannel.EncoderSettingsProperty,
    });

    this.channelLive = channelLive;
    this.myChannelName=myMediaLiveChannelName;
    this.myChannelArn=this.channelLive.attrArn;
    this.myChannelInput=inputName;
    
  }
}
