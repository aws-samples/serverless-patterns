import { Construct } from 'constructs';
import {
  App,
  Stack,
  StackProps,
  Duration,
  CfnOutput,
  RemovalPolicy,
  aws_ec2 as ec2,
  aws_rds as rds,
  aws_iam as iam,
  custom_resources as cr,
  aws_lambda as lambda,
  aws_lambda_nodejs as nodejs,
  aws_events as events,
  aws_docdb as docdb,
  aws_secretsmanager as secrets,
} from 'aws-cdk-lib';

export interface DocumentDbStreamLambdaEventBridgeStackProps extends StackProps {}
export class DocumentDbStreamLambdaEventBridgeStack extends Stack {
  constructor(scope: Construct, id: string, props?: DocumentDbStreamLambdaEventBridgeStackProps) {
    super(scope, id, props);

    // The code that defines your stack goes here

    // default event bus
    const defaultEventBus = events.EventBus.fromEventBusName(this, 'Default-Event-Bus', 'default');

    const vpc = ec2.Vpc.fromLookup(this, 'default-vpc-id', {
      isDefault: true,
    });

    const docDbSg = new ec2.SecurityGroup(this, 'DocDB-SG', {
      vpc: vpc,
    });

    docDbSg.addIngressRule(ec2.Peer.anyIpv4(), ec2.Port.tcp(27017));

    const cluster = new docdb.DatabaseCluster(this, 'Database', {
      masterUser: {
        username: 'myuser', // NOTE: 'admin' is reserved by DocumentDB
        excludeCharacters: '"@/:', // optional, defaults to the set "\"@/" and is also used for eventually created rotations
        secretName: 'DocumentDBSecret', // optional, if you prefer to specify the secret name
      },
      dbClusterName: 'DocDbCluster',
      securityGroup: docDbSg,
      instanceType: ec2.InstanceType.of(ec2.InstanceClass.T3, ec2.InstanceSize.MEDIUM),
      engineVersion: '4.0.0',
      instances: 1,
      vpc,
    });

    new ec2.InterfaceVpcEndpoint(this, 'VPC Endpoint for Secrets', {
      vpc,
      service: ec2.InterfaceVpcEndpointAwsService.SECRETS_MANAGER,
      subnets: {
        subnets: vpc.publicSubnets,
      },
      securityGroups: [docDbSg],
    });

    const lambdaVpcEndpoint = new ec2.InterfaceVpcEndpoint(this, 'VPC Endpoint for Lambda to enable CDC', {
      vpc,
      service: ec2.InterfaceVpcEndpointAwsService.LAMBDA,
      subnets: {
        subnets: vpc.publicSubnets,
      },
      securityGroups: [docDbSg],
    });

    const userCreatedLambda = new nodejs.NodejsFunction(this, 'UserCreatedLambda', {
      runtime: lambda.Runtime.NODEJS_18_X,
      handler: 'main',
      entry: 'src/lambdas/user-created.ts',
      timeout: Duration.seconds(60),
      vpc,
      securityGroups: [docDbSg],
      environment: {
        DEFAULT_EVENT_BUS: defaultEventBus.eventBusName,
      },
    });
    const usersCdcLambda = new nodejs.NodejsFunction(this, 'UsersCdcLambda', {
      runtime: lambda.Runtime.NODEJS_18_X,
      handler: 'main',
      entry: 'src/lambdas/users-cdc.ts',
      timeout: Duration.seconds(60),
      vpc,
      securityGroups: [docDbSg],
      environment: {
        DEFAULT_EVENT_BUS: defaultEventBus.eventBusName,
      },
    });

    defaultEventBus.grantPutEventsTo(usersCdcLambda);

    usersCdcLambda.addToRolePolicy(
      new iam.PolicyStatement({
        sid: 'LambdaESMNetworkingAccess',
        effect: iam.Effect.ALLOW,
        actions: [
          'ec2:CreateNetworkInterface',
          'ec2:DescribeNetworkInterfaces',
          'ec2:DescribeVpcs',
          'ec2:DeleteNetworkInterface',
          'ec2:DescribeSubnets',
          'ec2:DescribeSecurityGroups',
          'kms:Decrypt',
        ],
        resources: ['*'],
      })
    );
    usersCdcLambda.addToRolePolicy(
      new iam.PolicyStatement({
        sid: 'LambdaDocDBESMAccess',
        effect: iam.Effect.ALLOW,
        actions: ['rds:DescribeDBClusters', 'rds:DescribeDBClusterParameters', 'rds:DescribeDBSubnetGroups'],
        resources: ['*'],
      })
    );
    usersCdcLambda.addToRolePolicy(
      new iam.PolicyStatement({
        sid: 'LambdaDocDBESMGetSecretValueAccess',
        effect: iam.Effect.ALLOW,
        actions: ['secretsmanager:GetSecretValue'],
        resources: [`arn:aws:secretsmanager:${this.region}:${this.account}:secret:DocumentDBSecret`],
      })
    );

    const enableCdcLambda = new nodejs.NodejsFunction(this, 'EnableCdcLambdaCustomResource', {
      runtime: lambda.Runtime.NODEJS_18_X,
      handler: 'main',
      entry: 'cdk/lambdas/enable-cdc-cr.ts',
      vpc,
      securityGroups: [docDbSg],
    });

    enableCdcLambda.addToRolePolicy(
      new iam.PolicyStatement({
        effect: iam.Effect.ALLOW,
        actions: [
          'lambda:CreateEventSourceMapping',
          'lambda:UpdateEventSourceMapping',
          'lambda:DeleteEventSourceMapping',
        ],
        resources: ['arn:aws:lambda:*'],
      })
    );

    const awsSDKCall: cr.AwsSdkCall = {
      service: 'Lambda',
      action: 'invoke',
      parameters: {
        FunctionName: enableCdcLambda.functionName,
        Payload: JSON.stringify({
          cdcStreams: [
            {
              cdcFunctionName: userCreatedLambda.functionName,
              collectionName: 'users',
            },
          ],
          databaseName: 'docdb',
          clusterArn: cluster.clusterIdentifier,
          authUri: cluster.secret?.secretValue,
          date: new Date(),
        }),
      },
      physicalResourceId: cr.PhysicalResourceId.of(`batchJobsCdc`),
    };
    const customResource = new cr.AwsCustomResource(this, 'InvokeBatchJobsCdc', {
      onCreate: awsSDKCall,
      onUpdate: awsSDKCall,
      policy: cr.AwsCustomResourcePolicy.fromSdkCalls({
        resources: cr.AwsCustomResourcePolicy.ANY_RESOURCE,
      }),
    });

    enableCdcLambda.grantInvoke(customResource);

    new CfnOutput(this, 'Docdb-endpoint', {
      value: `${cluster.clusterEndpoint.hostname}`,
    });
  }
}
