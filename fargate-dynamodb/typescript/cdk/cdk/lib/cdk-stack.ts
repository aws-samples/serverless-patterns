import { Stack, StackProps, CfnOutput, RemovalPolicy } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { Table, BillingMode, AttributeType } from 'aws-cdk-lib/aws-dynamodb';
import { GatewayVpcEndpointAwsService, Vpc } from 'aws-cdk-lib/aws-ec2';
import { Cluster, ContainerImage } from 'aws-cdk-lib/aws-ecs';
import { ApplicationLoadBalancedFargateService } from 'aws-cdk-lib/aws-ecs-patterns';
import { AnyPrincipal, Effect, PolicyStatement } from 'aws-cdk-lib/aws-iam';
import path = require('path');

export class CdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const dynamoTable = new Table(this, 'DynamoTable', {
      partitionKey: {name:'ID', type: AttributeType.STRING},
      billingMode: BillingMode.PAY_PER_REQUEST,
      removalPolicy: RemovalPolicy.DESTROY
    });

    const vpc = new Vpc(this, 'MyVpc', {
      maxAzs: 3
    });

    const dynamoGatewayEndpoint = vpc.addGatewayEndpoint('dynamoGatewayEndpoint', {
      service: GatewayVpcEndpointAwsService.DYNAMODB
    });

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
      })
    );

    // Write permissions for Fargate
    dynamoTable.grantWriteData(fargate.taskDefinition.taskRole);

    // Outputs
    new CfnOutput(this, 'DynamoDbTableName', { value: dynamoTable.tableName });
  }
}
