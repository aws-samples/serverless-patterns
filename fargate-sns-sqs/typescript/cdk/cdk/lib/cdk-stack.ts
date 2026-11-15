import { CfnOutput, Stack, StackProps, RemovalPolicy } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { Topic } from 'aws-cdk-lib/aws-sns';
import { SqsSubscription } from 'aws-cdk-lib/aws-sns-subscriptions';
import { Queue, QueueEncryption } from 'aws-cdk-lib/aws-sqs';
import { InterfaceVpcEndpointAwsService, Vpc } from 'aws-cdk-lib/aws-ec2';
import { Cluster, ContainerImage } from 'aws-cdk-lib/aws-ecs';
import { ApplicationLoadBalancedFargateService } from 'aws-cdk-lib/aws-ecs-patterns';
import { AnyPrincipal, Effect, PolicyStatement, ServicePrincipal } from 'aws-cdk-lib/aws-iam';
import { Key } from 'aws-cdk-lib/aws-kms';
import path = require('path');

export class CdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const vpc = new Vpc(this, 'Vpc', {
      maxAzs: 3,
    });

    const kmsKey = new Key(this, 'SnsSqsKmsKey', {
      description: 'KMS Key used for SNS and SQS',
      alias: 'alias/SnsSqsKmsKey',
      enableKeyRotation: true,
      enabled: true,
      removalPolicy: RemovalPolicy.DESTROY
    });

    const snsTopic = new Topic(this, 'SnsTopic', {
      masterKey: kmsKey
    });

    const snsEndpoint = vpc.addInterfaceEndpoint('SnsInterfaceEndpoint', {
      service: InterfaceVpcEndpointAwsService.SNS,
    });

    const sqsQueue = new Queue(this, 'Queue', {
      encryption: QueueEncryption.KMS,
      encryptionMasterKey: kmsKey
    });

    const sqsEndpoint = vpc.addInterfaceEndpoint('SqsInterfaceEndpoint', {
      service: InterfaceVpcEndpointAwsService.SQS,
    });

    const sqsSubs = new SqsSubscription(sqsQueue);

    snsTopic.addSubscription(sqsSubs);

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
          snsTopicArn: snsTopic.topicArn,
          queueUrl: sqsQueue.queueUrl,
          region: process.env.CDK_DEFAULT_REGION!,
        },
      },
      assignPublicIp: false,
      memoryLimitMiB: 2048,
    });

    fargate.taskDefinition.taskRole.addToPrincipalPolicy(
      new PolicyStatement({
        effect: Effect.ALLOW,
        actions: ['kms:Decrypt','kms:DescribeKey','kms:Encrypt','kms:GenerateDataKey*'],
        resources: [`${kmsKey.keyArn}`]
      })
    )

    // Allow publish action from the Fargate Task Definition only
    snsEndpoint.addToPolicy(
      new PolicyStatement({
        effect: Effect.ALLOW,
        principals: [new AnyPrincipal()],
        actions: ['sns:Publish'],
        resources: [snsTopic.topicArn],
        conditions: {
          ArnEquals: {
            'aws:PrincipalArn': `${fargate.taskDefinition.taskRole.roleArn}`,
          },
        },
      })
    );

    // Publish permissions to SNS topic for Fargate
    snsTopic.grantPublish(fargate.taskDefinition.taskRole);

    // SNS policy to deny access if it isn't from a VPC endpoint
    snsTopic.addToResourcePolicy(
      new PolicyStatement({
        effect: Effect.DENY,
        resources: [snsTopic.topicArn],
        actions: ['sns:Publish'],
        principals: [new AnyPrincipal()],
        conditions: {
          StringNotEquals: {
            'aws:sourceVpce': [snsEndpoint.vpcEndpointId],
          },
        },
      })
    );

    // Allow read action from the Fargate Task Definition only
    sqsEndpoint.addToPolicy(
      new PolicyStatement({
        effect: Effect.ALLOW,
        principals: [new AnyPrincipal()],
        actions: ['sqs:ReceiveMessage'],
        resources: [sqsQueue.queueArn],
        conditions: {
          ArnEquals: {
            'aws:PrincipalArn': `${fargate.taskDefinition.taskRole.roleArn}`,
          },
        },
      })
    );

    // Read permission to SQS queue for Fargate
    sqsQueue.grantConsumeMessages(fargate.taskDefinition.taskRole);

    // SQS policy to deny access if it isn't from a VPC endpoint
    sqsQueue.addToResourcePolicy(
      new PolicyStatement({
        effect: Effect.DENY,
        resources: [sqsQueue.queueArn],
        actions: ['sqs:ReceiveMessage'],
        principals: [new AnyPrincipal()],
        conditions: {
          StringNotEquals: {
            'aws:sourceVpce': [sqsEndpoint.vpcEndpointId],
          },
        },
      })
    );

    new CfnOutput(this, 'SqsQueueUrl', { value: sqsQueue.queueUrl });
    new CfnOutput(this, 'SnsTopicARN', { value: snsTopic.topicArn });
  }
}
