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
  Stack,
  StackProps,
  Duration,
  CfnOutput,
  aws_iam as iam,
} from "aws-cdk-lib";
import { Construct, DependencyGroup } from 'constructs';
import { MediaLive } from './media_live';
import { MediaPackage } from './media_package';
import { MediaPackageCdnAuth } from './media_package_cdn_auth';
import { Secrets } from "./secrets";
import { loadMediaPackageConfig } from "../helpers/configuration";


export class StreamingStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);
       
      const configMediaPackage = loadMediaPackageConfig();
      var mediaPackageChannel: MediaPackageCdnAuth;
      var mediaLiveChannel: MediaLive;

       //👇Checking if using CDN Authorization for each MediaPackage Endpoints
       if (configMediaPackage.cdn_authorization) {

        const secrets = new Secrets(this, "Secrets");
        //Policy to be used by MediaPackage for CDN Authorization
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

        //Create MediaPackage Channel using CDN Authorization
        mediaPackageChannel = new MediaPackageCdnAuth(
          this,
          "MyMediaPackageChannel",
          role4mediapackage.roleArn,
          secrets,
        );


      } else {
          //Create MediaPackage Channel without CDN Authorization
          mediaPackageChannel = new MediaPackage(
            this,
            "MyMediaPackageChannel"
          );
      }
   

      //Create Media Live Channel
      mediaLiveChannel = new MediaLive(
        this,
        "MyMediaLiveChannel",
        mediaPackageChannel.myChannel.id
      );

      //👇Add dependencyto wait for MediaPackage channel to be ready before deploying MediaLive & MediaTailor
      mediaLiveChannel.node.addDependency(mediaPackageChannel);
  


    //👇 Generating Cfn output (TbD CMAF output is not displaying)
    new CfnOutput(this, "MediaLiveChannelName", {
      value: mediaLiveChannel.myChannelName,
    });
    new CfnOutput(this, "MediaLiveChannelArn", {
      value: mediaLiveChannel.myChannelArn,
    });
    new CfnOutput(this, "MediaLiveChannelInputName", {
      value: mediaLiveChannel.myChannelInput,
    });

    new CfnOutput(this, "MediaPackageChannelName", {
      value: mediaPackageChannel.myChannelName,
    });
    new CfnOutput(this, "MediaPackageChannelArn", {
      value: mediaPackageChannel.myChannelArn,
    });
    new CfnOutput(this, "MediaPackageChannelUrl-HLS", {
      value: mediaPackageChannel.hlsEndpoint,
    });
    new CfnOutput(this, "MediaPackageChannelUrl-DASH", {
      value: mediaPackageChannel.dashEndpoint,
    });
    new CfnOutput(this, "MediaPackageChannelUrl-CMAF", {
      value: mediaPackageChannel.cmafEndpoint,
    });
    new CfnOutput(this, "MediaPackageChannelUrl-MSS", {
      value: mediaPackageChannel.mssEndpoint,
    });

  }
}
