import * as cdk from 'aws-cdk-lib';
import * as logs from 'aws-cdk-lib/aws-logs';
import * as sqs from 'aws-cdk-lib/aws-sqs';
import * as pipes from 'aws-cdk-lib/aws-pipes';
import * as iam from 'aws-cdk-lib/aws-iam';
import { Construct } from 'constructs';
import { Queue } from 'aws-cdk-lib/aws-sqs';
import { Cluster, ContainerImage, FargateTaskDefinition, LogDriver } from 'aws-cdk-lib/aws-ecs';
import { RetentionDays } from 'aws-cdk-lib/aws-logs';
import { JsonPath } from "aws-cdk-lib/aws-stepfunctions";
import { SubnetType } from 'aws-cdk-lib/aws-ec2';

export class EventbridgePipesSqsToEcsTaskCdkTypescriptStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);


    const sqsDLQ = new Queue(this, 'SQSDLQ', {
      queueName: 'sqs-dlq',
    });

    const sqsQueue = new sqs.Queue(this, 'SQSQueue', {
      queueName: 'sqs-queue',
      retentionPeriod: cdk.Duration.minutes(15),
      deadLetterQueue: {
        queue: sqsDLQ,
        maxReceiveCount: 2
      }
    });


    // create a cloudwatch log group called EventBridgePipeTraceLogGroup and add a retention time of 1 day
    const eventBridgePipeTraceLogGroup = new logs.LogGroup(this, 'EventBridgePipeTraceLogGroup', {
      retention: logs.RetentionDays.ONE_DAY,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    // create a cloudwatch log group called SQSEventBridgePipeTargetLogGroup and add a retention time of 1 day
    const sqsEventBridgePipeTargetLogGroup = new logs.LogGroup(this, 'SQSEventBridgePipeTargetLogGroup', {
      logGroupName: 'SQSEventBridgePipeTargetLogGroup',
      retention: logs.RetentionDays.ONE_DAY,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    const testVPC = new cdk.aws_ec2.Vpc(this, 'TestVPC', {
      maxAzs: 2,
    });

    // create a security group in testVPC egress only
    const ecsTaskSecurityGroup = new cdk.aws_ec2.SecurityGroup(this, 'ECSTaskSecurityGroup', {
      vpc: testVPC,
      allowAllOutbound: true,
      securityGroupName: 'ecs-task-security-group',
    });

    const testECSCluster = new Cluster(this, 'TestECSCluster', {
      clusterName: 'test-ecs-cluster',
      enableFargateCapacityProviders: true,
      vpc: testVPC
    });

    const testfargateTaskDefinition = new FargateTaskDefinition(this, 'TestfargateTaskDefinition', {
      memoryLimitMiB: 512,
      cpu: 256,
    });

    testfargateTaskDefinition.addContainer('TestContainer', {
      image: ContainerImage.fromRegistry('public.ecr.aws/docker/library/alpine:edge'),
      logging: LogDriver.awsLogs({
        streamPrefix: '/ecstask',
        logGroup: sqsEventBridgePipeTargetLogGroup,
      }),
    });


    // create a IAM role for EventBridge pipe
    const pipeRole = new iam.Role(this, 'PipeRole', {
      assumedBy: new iam.ServicePrincipal('pipes.amazonaws.com'),
    });

    // Give pipeRole permissions to consume from the SQS queue and run the ECS task
    sqsQueue.grantConsumeMessages(pipeRole);
    testfargateTaskDefinition.grantRun(pipeRole);
    eventBridgePipeTraceLogGroup.grantWrite(pipeRole);

    // create a EventBridge pipe which consumes events from SQS with batch size 1 and runs a ECS task for events which match the filter criteria
    const pipe = new pipes.CfnPipe(this, 'SQSEventBridgePipe', {
      roleArn: pipeRole.roleArn,
      description: 'SQS EventBridge Pipe to execute ECS tasks for matched events',
      name: 'SQSEventBridgePipe',
      source: sqsQueue.queueArn,
      sourceParameters: {
        filterCriteria: {
          filters: [
            {
              "pattern": "{\"body\": {\"partnerId\": [\"1234\"]}}"
            }
          ]
        },
        sqsQueueParameters: {
          batchSize: 1
        }
      },
      target: testECSCluster.clusterArn,
      targetParameters: {
        ecsTaskParameters: {
          capacityProviderStrategy: [{
            capacityProvider: 'FARGATE',
            base: 1
          }],
          taskDefinitionArn: testfargateTaskDefinition.taskDefinitionArn,
          taskCount: 1,
          networkConfiguration: {
            awsvpcConfiguration: {
              securityGroups: [ecsTaskSecurityGroup.securityGroupId],
              subnets: testVPC.selectSubnets({
                subnetType: SubnetType.PRIVATE_WITH_EGRESS
              }).subnets.map(subnet => subnet.subnetId),
            },
          },
          overrides: {
            containerOverrides: [
              {
                name: testfargateTaskDefinition.defaultContainer?.containerName,
                command: ['/bin/echo', JsonPath.stringAt('$.body.partnerId')],
              },
            ],
          }
        }
      }
    });


    new cdk.CfnOutput(this, 'SqsUrl', {
      value: sqsQueue.queueUrl
    })

  }
}