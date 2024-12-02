import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as ec2 from 'aws-cdk-lib/aws-ec2';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as logs from 'aws-cdk-lib/aws-logs';
import { RetentionDays } from 'aws-cdk-lib/aws-logs';
import * as ecs from 'aws-cdk-lib/aws-ecs';
import * as events from 'aws-cdk-lib/aws-events';
import * as targets from "aws-cdk-lib/aws-events-targets";
import * as path from "node:path";
import { DockerImageAsset } from "aws-cdk-lib/aws-ecr-assets";
import { CfnOutput, Duration } from "aws-cdk-lib";

export class S3TriggerFargateTaskStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Ingestion bucket
    const bucket = new s3.Bucket(this, 'IngestionBucket', {
      eventBridgeEnabled: true,
      blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      autoDeleteObjects: true,
      enforceSSL: true,
      publicReadAccess: false
    });

    // VPC for the ECS Cluster
    const vpc = new ec2.Vpc(this, "VPC", {
      maxAzs: 2,
      natGateways: 1,
      subnetConfiguration: [
        {
          cidrMask: 24,
          name: "public",
          subnetType: ec2.SubnetType.PUBLIC,
        },
        {
          cidrMask: 24,
          name: "private",
          subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS,
        },
      ],
    });

    // S3 Gateway Endpoint to avoid accessing S3 from Internet
    const s3GatewayEndpoint = vpc.addGatewayEndpoint('S3GatewayEndpoint', {
      service: ec2.GatewayVpcEndpointAwsService.S3
    });

    // IAM policy to only enable access to S3 through vpc endpoint (OPTIONAL)
    const bucketDenyPolicy = new iam.PolicyStatement({
      effect: iam.Effect.DENY,
      principals: [new iam.AnyPrincipal()],
      actions: ['s3:GetObject'], // adapt to your security requirements
      resources: [
        `arn:aws:s3:::${bucket.bucketName}`,
        `arn:aws:s3:::${bucket.bucketName}/*`,
      ],
      conditions: {
        'StringNotEquals': {
          'aws:SourceVpce': s3GatewayEndpoint.vpcEndpointId,
        },
      },
    });
    bucket.addToResourcePolicy(bucketDenyPolicy);

    const cluster = new ecs.Cluster(this, "Cluster", {
      vpc: vpc,
    });

    // ECS Task definition
    const taskDefinition = new ecs.FargateTaskDefinition(this, "TaskDefinition", {
      cpu: 512,
      memoryLimitMiB: 2048,
      runtimePlatform: {
        cpuArchitecture: ecs.CpuArchitecture.X86_64,
        operatingSystemFamily: ecs.OperatingSystemFamily.LINUX
      },
    });

    // Container logs
    const ecsLogGroup = new logs.LogGroup(this, 'ContainerLogGroup', {
      logGroupName: '/ecs/doc-ingestion',
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      retention: RetentionDays.FIVE_DAYS
    });

    // Container image
    const container = taskDefinition.addContainer('DocIngestion', {
      image: ecs.ContainerImage.fromDockerImageAsset(new DockerImageAsset(this, 'DocIngestionImage', {
        directory: path.join(__dirname, '../docker/doc-ingestion'),
      })),
      logging: new ecs.AwsLogDriver({ streamPrefix: 'doc-ingestion-logs', logGroup: ecsLogGroup}),
    });

    // Define the ECS Task as a target for the EventBridge rule
    // We extract information from the event and store them in environment variables
    const ecsTask = new targets.EcsTask({
      taskDefinition,
      cluster,
      containerOverrides: [
        {
          containerName: container.containerName,
          environment: [
            {
              name: 'S3_BUCKET',
              value: events.EventField.fromPath("$.detail.bucket.name"),
            },
            {
              name: 'S3_OBJECT_KEY',
              value:events. EventField.fromPath("$.detail.object.key"),
            }
          ]
        }
      ],
      maxEventAge: Duration.hours(2),
      retryAttempts: 3
    });

    // EventBridge rule definition
    const rule = new events.Rule(this, 'rule', {
      eventPattern: {
        source: ['aws.s3'],
        detailType: [
          'Object Created'
        ],
        detail: {
          bucket: {
            name: [
              bucket.bucketName
            ]
          },
          // OPTIONAL: if there is a specific prefix to watch for
          // object: {
          //   key: [{
          //     prefix: "prefix"
          //   }]
          // }
        }
      },
      targets: [
          ecsTask,
          // just for debugging purpose, log events in cloudwatch
          // new targets.CloudWatchLogGroup(new logs.LogGroup(this, 'RuleLogs', {
          //   logGroupName: '/aws/events/doc-ingestion',
          //   removalPolicy: cdk.RemovalPolicy.DESTROY,
          //   retention: RetentionDays.FIVE_DAYS
          // }))
      ]
    });

    // Allow ECS task to access the bucket
    bucket.grantRead(taskDefinition.taskRole);

    new CfnOutput(this, 'IngestionBucketOut', {
      key: 'IngestionBucket',
      value: bucket.bucketName
    });

    new CfnOutput(this, 'ECSLogsOut', {
      key: 'ECSLogs',
      value: ecsLogGroup.logGroupName
    });
  }
}
