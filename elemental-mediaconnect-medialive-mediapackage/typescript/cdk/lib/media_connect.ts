import { Aws, aws_mediaconnect as mediaconnect, CfnOutput } from "aws-cdk-lib";

import { Construct } from "constructs";
import { loadMediaConnectConfig } from "../helpers/configuration";

export class MediaConnect extends Construct {
  public readonly flowArnA: string;
  public readonly flowArnB: string;

  private readonly protocol = "srt-listener";

  constructor(scope: Construct, id: string) {
    super(scope, id);

    const config = loadMediaConnectConfig();

    const cfnFlowA = new mediaconnect.CfnFlow(this, "MyCfnFlowA", {
      name: Aws.STACK_NAME + "_" + "FlowA",
      source: {
        description: Aws.STACK_NAME + "_" + "FlowA",
        ingestPort: config.ingestPort,
        minLatency: config.minLatency,
        name: Aws.STACK_NAME + "_" + "FlowA",
        protocol: this.protocol,
        whitelistCidr: config.whitelistCidr,
      },
      availabilityZone: config.availabilityZone.a,
    });

    const cfnFlowB = new mediaconnect.CfnFlow(this, "MyCfnFlowB", {
      name: Aws.STACK_NAME + "_" + "FlowB",
      source: {
        description: Aws.STACK_NAME + "_" + "FlowB",
        ingestPort: config.ingestPort,
        minLatency: config.minLatency,
        name: Aws.STACK_NAME + "_" + "FlowB",
        protocol: this.protocol,
        whitelistCidr: config.whitelistCidr,
      },
      availabilityZone: config.availabilityZone.b,
    });

    this.flowArnA = cfnFlowA.attrFlowArn;
    this.flowArnB = cfnFlowB.attrFlowArn;

    new CfnOutput(this, "MediaConnectFlowA", {
      value:
        cfnFlowA.attrSourceIngestIp + ":" + cfnFlowA.attrSourceSourceIngestPort,
    });

    new CfnOutput(this, "MediaConnectFlowB", {
      value:
        cfnFlowB.attrSourceIngestIp + ":" + cfnFlowB.attrSourceSourceIngestPort,
    });

    new CfnOutput(this, "flowAArn", {
      value: cfnFlowA.attrFlowArn,
    });

    new CfnOutput(this, "flowBArn", {
      value: cfnFlowB.attrFlowArn,
    });
  }
}
