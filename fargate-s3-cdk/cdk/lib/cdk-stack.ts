import * as cdk from '@aws-cdk/core';
import * as s3 from '@aws-cdk/aws-s3';
import * as ec2 from '@aws-cdk/aws-ec2';
import * as ecs from '@aws-cdk/aws-ecs';
import * as ecs_patterns from '@aws-cdk/aws-ecs-patterns';
import path = require('path');

export class CdkStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const demoBucket = new s3.Bucket(this, 'demoBucket', {
      blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
      bucketName: 'demo-bucket-serverless-patterns',
      encryption: s3.BucketEncryption.KMS_MANAGED,
      enforceSSL: true,
      publicReadAccess: false,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      versioned: false,  // turn off versioning to make cdk destroy easier
    });

    const vpc = new ec2.Vpc(this, 'MyVpc', {
      maxAzs: 3
    });

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
      memoryLimitMiB: 2048,
    });

    // Read and Write permissions for Fargate
    demoBucket.grantReadWrite(fargate.taskDefinition.taskRole);
  }
}
