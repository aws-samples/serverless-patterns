import * as cdk from '@aws-cdk/core';
import { Table, BillingMode, AttributeType } from '@aws-cdk/aws-dynamodb';
import * as ec2 from '@aws-cdk/aws-ec2';
import * as ecs from '@aws-cdk/aws-ecs';
import * as ecs_patterns from '@aws-cdk/aws-ecs-patterns';
import { AnyPrincipal, Effect, PolicyStatement } from '@aws-cdk/aws-iam';
import path = require('path');

export class CdkStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const dynamoTable = new Table(this, 'DynamoTable', {
      partitionKey: {name:'ID', type: AttributeType.STRING},
      billingMode: BillingMode.PAY_PER_REQUEST,
      removalPolicy: cdk.RemovalPolicy.DESTROY
    });

    const vpc = new ec2.Vpc(this, 'MyVpc', {
      maxAzs: 3
    });

    const dynamoGatewayEndpoint = vpc.addGatewayEndpoint('dynamoGatewayEndpoint', {
      service: ec2.GatewayVpcEndpointAwsService.DYNAMODB
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
          databaseTable: dynamoTable.tableName,
          region: process.env.CDK_DEFAULT_REGION!
        },
      },
      memoryLimitMiB: 2048,
    });

    // Allow PutItem action from the Fargate Task Definition only
    dynamoGatewayEndpoint.addToPolicy(
      new PolicyStatement({
        effect: Effect.ALLOW,
        principals: [new AnyPrincipal()],
        actions: [
          'dynamodb:PutItem',
        ],
        resources: [
          `${dynamoTable.tableArn}`
        ],
        conditions: {
          'ArnEquals': {
            'aws:PrincipalArn': `${fargate.taskDefinition.taskRole.roleArn}`
          }
        }
    }));

    // Write permissions for Fargate
    dynamoTable.grantWriteData(fargate.taskDefinition.taskRole);

    // Outputs
    new cdk.CfnOutput(this, 'DynamoDbTableName', { value: dynamoTable.tableName });
  }
}
