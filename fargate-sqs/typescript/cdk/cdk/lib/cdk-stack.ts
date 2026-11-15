import { CfnOutput, Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { Queue, QueueEncryption } from 'aws-cdk-lib/aws-sqs';
import { InterfaceVpcEndpointAwsService, Vpc } from 'aws-cdk-lib/aws-ec2';
import { Cluster, ContainerImage } from 'aws-cdk-lib/aws-ecs';
import { ApplicationLoadBalancedFargateService } from 'aws-cdk-lib/aws-ecs-patterns';
import { AnyPrincipal, Effect, PolicyStatement } from 'aws-cdk-lib/aws-iam';
import path = require('path');

export class CdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const vpc = new Vpc(this, 'Vpc', {
      maxAzs: 3,
    });

    const sqsQueue = new Queue(this, 'Queue', {
      encryption: QueueEncryption.KMS_MANAGED,
    });

    const sqsEndpoint = vpc.addInterfaceEndpoint('SqsInterfaceEndpoint', {
      service: InterfaceVpcEndpointAwsService.SQS,
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
          queueUrl: sqsQueue.queueUrl,
          region: process.env.CDK_DEFAULT_REGION!,
        },
      },
      assignPublicIp: false,
      memoryLimitMiB: 2048,
    });

    // Allow read and write actions from the Fargate Task Definition only
    sqsEndpoint.addToPolicy(
      new PolicyStatement({
        effect: Effect.ALLOW,
        principals: [new AnyPrincipal()],
        actions: ['sqs:SendMessage', 'sqs:ReceiveMessage'],
        resources: [sqsQueue.queueArn],
        conditions: {
          ArnEquals: {
            'aws:PrincipalArn': `${fargate.taskDefinition.taskRole.roleArn}`,
          },
        },
      })
    );

    // Read and Write permissions to SQS queue for Fargate
    sqsQueue.grantSendMessages(fargate.taskDefinition.taskRole);
    sqsQueue.grantConsumeMessages(fargate.taskDefinition.taskRole);

    // SQS policy to deny access if it isn't from a VPC endpoint
    sqsQueue.addToResourcePolicy(
      new PolicyStatement({
        effect: Effect.DENY,
        resources: [sqsQueue.queueArn],
        actions: ['sqs:SendMessage', 'sqs:ReceiveMessage'],
        principals: [new AnyPrincipal()],
        conditions: {
          StringNotEquals: {
            'aws:sourceVpce': [sqsEndpoint.vpcEndpointId],
          },
        },
      })
    );

    new CfnOutput(this, 'SqsQueueUrl', { value: sqsQueue.queueUrl });
  }
}
