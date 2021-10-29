import * as cdk from '@aws-cdk/core';
import * as s3 from '@aws-cdk/aws-s3';
import * as ec2 from '@aws-cdk/aws-ec2';
import * as ecs from '@aws-cdk/aws-ecs';
import * as ecs_patterns from '@aws-cdk/aws-ecs-patterns';
import { AnyPrincipal, Effect, PolicyStatement } from '@aws-cdk/aws-iam';
import path = require('path');

export class CdkStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const BUCKET_NAME = 'demo-bucket-serverless-patterns'

    const demoBucket = new s3.Bucket(this, 'demoBucket', {
      blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
      bucketName: BUCKET_NAME,
      encryption: s3.BucketEncryption.KMS_MANAGED,
      enforceSSL: true,
      publicReadAccess: false,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      versioned: false,  // turn off versioning to make cdk destroy easier
    });

    const vpc = new ec2.Vpc(this, 'MyVpc', {
      maxAzs: 3
    });

    const s3GatewayEndpoint = vpc.addGatewayEndpoint('s3GatewayEndpoint', {
      service: ec2.GatewayVpcEndpointAwsService.S3
    });

    // Add bucket policy to restrict access to VPCE
    demoBucket.addToResourcePolicy(
      new PolicyStatement({
        effect: Effect.DENY,
        resources: [
          demoBucket.bucketArn,
        ],
        actions: [
          's3:ListBucket'
        ],
        principals: [new AnyPrincipal()],
        conditions: {
          "StringNotEquals": {
            "aws:sourceVpce": [s3GatewayEndpoint.vpcEndpointId]
          }
        }
      })
    );

    demoBucket.addToResourcePolicy(
      new PolicyStatement({
        effect: Effect.DENY,
        resources: [
          demoBucket.arnForObjects('*')
        ],
        actions: [
          's3:PutObject',
          's3:GetObject'
        ],
        principals: [new AnyPrincipal()],
        conditions: {
          "StringNotEquals": {
            "aws:sourceVpce": [s3GatewayEndpoint.vpcEndpointId]
          }
        }
      })
    );

    const cluster = new ecs.Cluster(this, 'MyCluster', {
      vpc: vpc
    });

    const fargate = new ecs_patterns.ApplicationLoadBalancedFargateService(this, 'MyFargateService', {
      cluster: cluster,
      cpu: 512,
      desiredCount: 1,
      taskImageOptions: {
        image: ecs.ContainerImage.fromAsset(path.join(__dirname, '../src/')),
        environment: {
          bucketName: demoBucket.bucketName,
          region: process.env.CDK_DEFAULT_REGION!
        },
      },
      assignPublicIp: false,
      memoryLimitMiB: 2048,
    });

    // Read and Write permissions for Fargate
    demoBucket.grantReadWrite(fargate.taskDefinition.taskRole);
  }
}
