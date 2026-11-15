import * as path from 'path';
import { CfnOutput, Stack, StackProps } from 'aws-cdk-lib';
import * as ecrAssets from 'aws-cdk-lib/aws-ecr-assets';
import * as ecs from 'aws-cdk-lib/aws-ecs';
import * as iam from 'aws-cdk-lib/aws-iam';
import { Construct } from 'constructs';

export class CdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    // Build the image from ../src and push it to the CDK bootstrap ECR repository
    const image = new ecrAssets.DockerImageAsset(this, 'DockerImageAsset', {
      directory: path.join(__dirname, '../src/'),
      platform: ecrAssets.Platform.LINUX_AMD64,
    });

    // Lets ECS pull the image and write container logs
    const executionRole = new iam.Role(this, 'TaskExecutionRole', {
      assumedBy: new iam.ServicePrincipal('ecs-tasks.amazonaws.com'),
      managedPolicies: [
        iam.ManagedPolicy.fromAwsManagedPolicyName('service-role/AmazonECSTaskExecutionRolePolicy'),
      ],
    });

    // Lets ECS create and manage the load balancer, security groups, certificate and scaling
    const infrastructureRole = new iam.Role(this, 'InfrastructureRole', {
      assumedBy: new iam.ServicePrincipal('ecs.amazonaws.com'),
      managedPolicies: [
        iam.ManagedPolicy.fromAwsManagedPolicyName('service-role/AmazonECSInfrastructureRoleforExpressGatewayServices'),
      ],
    });

    const cluster = new ecs.CfnCluster(this, 'Cluster');

    // Amazon ECS Express Mode service. With no network configuration, ECS uses the
    // default VPC and creates an internet-facing Application Load Balancer with HTTPS.
    const service = new ecs.CfnExpressGatewayService(this, 'Service', {
      cluster: cluster.ref,
      executionRoleArn: executionRole.roleArn,
      infrastructureRoleArn: infrastructureRole.roleArn,
      cpu: '1024',
      memory: '2048',
      healthCheckPath: '/',
      primaryContainer: {
        image: image.imageUri,
        containerPort: 80,
        environment: [{ name: 'region', value: this.region }],
      },
    });

    new CfnOutput(this, 'ExpressServiceARN', { value: service.attrServiceArn });
    new CfnOutput(this, 'ExpressServiceEndpoint', { value: service.attrEndpoint });
  }
}
