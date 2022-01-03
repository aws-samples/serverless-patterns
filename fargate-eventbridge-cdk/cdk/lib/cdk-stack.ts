import { CfnOutput, Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { Vpc } from 'aws-cdk-lib/aws-ec2';
import { Cluster, ContainerImage } from 'aws-cdk-lib/aws-ecs';
import { ApplicationLoadBalancedFargateService } from 'aws-cdk-lib/aws-ecs-patterns';
import { EventBus } from 'aws-cdk-lib/aws-events';
import path = require('path');

export class CdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const bus = new EventBus(this, 'bus', {
      eventBusName: 'DemoEventBus'
    });

    const vpc = new Vpc(this, 'Vpc', {
      maxAzs: 3,
    });

    const cluster = new Cluster(this, 'Cluster', {
      vpc: vpc,
    });

    const fargate = new ApplicationLoadBalancedFargateService(this, 'FargateService', {
      cluster: cluster,
      cpu: 512,
      desiredCount: 1,
      taskImageOptions: {
        image: ContainerImage.fromAsset(path.join(__dirname, '../src/')),
        environment: {
          eventBusName: bus.eventBusName,
          region: process.env.CDK_DEFAULT_REGION!,
        },
      },
      assignPublicIp: false,
      memoryLimitMiB: 2048,
    });

    bus.grantPutEventsTo(fargate.taskDefinition.taskRole);

    new CfnOutput(this, 'EventBusName', { value: bus.eventBusName });
  }
}
