import { RemovalPolicy, Stack, StackProps} from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { BlockPublicAccess, Bucket, BucketEncryption, } from 'aws-cdk-lib/aws-s3';
import { GatewayVpcEndpointAwsService, Vpc } from 'aws-cdk-lib/aws-ec2';
import { Cluster, ContainerImage } from 'aws-cdk-lib/aws-ecs';
import { ApplicationLoadBalancedFargateService } from 'aws-cdk-lib/aws-ecs-patterns';
import { AnyPrincipal, Effect, PolicyStatement } from 'aws-cdk-lib/aws-iam';
import path = require('path');

export class CdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const BUCKET_NAME = 'demo-bucket-serverless-patterns'

    const demoBucket = new Bucket(this, 'demoBucket', {
      blockPublicAccess: BlockPublicAccess.BLOCK_ALL,
      bucketName: BUCKET_NAME,
      encryption: BucketEncryption.KMS_MANAGED,
      enforceSSL: true,
      publicReadAccess: false,
      removalPolicy: RemovalPolicy.DESTROY,
      versioned: false,
      autoDeleteObjects: true
    });

    const vpc = new Vpc(this, 'MyVpc', {
      maxAzs: 3
    });

    const s3GatewayEndpoint = vpc.addGatewayEndpoint('s3GatewayEndpoint', {
      service: GatewayVpcEndpointAwsService.S3
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

    const cluster = new Cluster(this, 'MyCluster', {
      vpc: vpc
    });

    const fargate = new ApplicationLoadBalancedFargateService(this, 'MyFargateService', {
      cluster: cluster,
      cpu: 512,
      desiredCount: 1,
      taskImageOptions: {
        image: ContainerImage.fromAsset(path.join(__dirname, '../src/')),
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
