import * as path from 'path';
import { CfnOutput, Stack, StackProps } from '@aws-cdk/core';
import * as apprunner from '@aws-cdk/aws-apprunner';
import * as ecrAssests from '@aws-cdk/aws-ecr-assets';
import { Construct } from 'constructs';
import { Cpu, Memory } from '@aws-cdk/aws-apprunner';

export class CdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const appRunnerService = new apprunner.Service(this, 'Service', {
      serviceName: 'sample-apprunner-service-cdk',
      source: apprunner.Source.fromAsset({
        imageConfiguration: {
          port: 80,
          environment: {
            region: process.env.CDK_DEFAULT_REGION!,
          },
        },
        asset: new ecrAssests.DockerImageAsset(this, 'DockerImageAsset', {
          directory: path.join(__dirname, '../src/')
        })
      }),
      cpu: Cpu.ONE_VCPU,
      memory: Memory.TWO_GB
    });    

    new CfnOutput(this, 'AppRunnerServiceARN', { value: appRunnerService.serviceArn });
    new CfnOutput(this, 'AppRunnerServiceURL', { value: `https://${appRunnerService.serviceUrl}`});
  }
}
