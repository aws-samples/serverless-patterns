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
  aws_events_targets as targets,
  aws_secretsmanager as secrets,
  SecretValue,
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
        // excludeCharacters: '[!@#$%^&*()_+-=\\[]{}|;\':",./<>?`~]', // optional, defaults to the set "\"@/" and is also used for eventually created rotations
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
      allowPublicSubnet: true,
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
      allowPublicSubnet: true,
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

    const enableCdcLambdaCR = new nodejs.NodejsFunction(this, 'EnableCdcLambdaCustomResource', {
      runtime: lambda.Runtime.NODEJS_18_X,
      handler: 'main',
      entry: 'src/lambdas/enable-cdc-cr.ts',
      vpc,
      securityGroups: [docDbSg],
      allowPublicSubnet: true,
    });

    enableCdcLambdaCR.addToRolePolicy(
      new iam.PolicyStatement({
        effect: iam.Effect.ALLOW,
        actions: ['lambda:CreateEventSourceMapping', 'lambda:UpdateEventSourceMapping', 'lambda:DeleteEventSourceMapping'],
        resources: ['*'],
      })
    );

    const awsSDKCall: cr.AwsSdkCall = {
      service: 'Lambda',
      action: 'invoke',
      parameters: {
        FunctionName: enableCdcLambdaCR.functionName,
        Payload: JSON.stringify({
          cdcStreams: [
            {
              cdcFunctionName: usersCdcLambda.functionName,
              collectionName: 'users',
            },
          ],
          databaseName: 'docdb',
          clusterArn: `arn:aws:rds:${this.region}:${this.account}:cluster:${cluster.clusterIdentifier}`,
          authUri: cluster.secret?.secretArn,
          date: new Date(),
        }),
      },
      physicalResourceId: cr.PhysicalResourceId.of(`enableCdcLambda`),
    };
    const customResource = new cr.AwsCustomResource(this, 'InvokeEnableCdcLambda', {
      onCreate: awsSDKCall,
      onUpdate: awsSDKCall,
      policy: cr.AwsCustomResourcePolicy.fromSdkCalls({
        resources: cr.AwsCustomResourcePolicy.ANY_RESOURCE,
      }),
    });

    enableCdcLambdaCR.grantInvoke(customResource);

    const userCreatedRule = new events.Rule(this, 'UserCreatedRule', {
      eventBus: defaultEventBus,
      eventPattern: {
        source: ['docdb.cdc'],
        detailType: ['userCreated'],
      },
      targets: [new targets.LambdaFunction(userCreatedLambda)],
    });

    new CfnOutput(this, 'Docdb-endpoint-hostname', {
      value: `${cluster.clusterEndpoint.hostname}`,
    });
    new CfnOutput(this, 'Docdb-endpoint-port', {
      value: `${cluster.clusterEndpoint.port}`,
    });
    new CfnOutput(this, 'Docdb-cluster-identifier', {
      value: `${cluster.clusterIdentifier}`,
    });
    new CfnOutput(this, 'Docdb-cluster-resource-identifier', {
      value: `${cluster.clusterResourceIdentifier}`,
    });
    new CfnOutput(this, 'Docdb-cluster-secret-arn', {
      value: `${cluster.secret?.secretArn}`,
    });
  }
}
