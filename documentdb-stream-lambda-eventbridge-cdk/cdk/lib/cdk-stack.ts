import { Construct } from 'constructs';
import {
  Stack,
  StackProps,
  Duration,
  aws_ec2 as ec2,
  aws_iam as iam,
  custom_resources as cr,
  aws_lambda as lambda,
  aws_lambda_nodejs as nodejs,
  aws_events as events,
  aws_events_targets as targets,
} from 'aws-cdk-lib';

export interface DocumentDbStreamLambdaEventBridgeStackProps extends StackProps {
  databaseName: string;
  collectionName: string;
  docDbClusterId: string;
  docDbClusterSecretArn: string;
  vpcId?: string;
  securityGroupId: string;
}
export class DocumentDbStreamLambdaEventBridgeStack extends Stack {
  constructor(scope: Construct, id: string, props: DocumentDbStreamLambdaEventBridgeStackProps) {
    super(scope, id, props);

    // The code that defines your stack goes here

    // default event bus
    const defaultEventBus = events.EventBus.fromEventBusName(this, 'Default-Event-Bus', 'default');

    const vpc = !!props.vpcId
      ? ec2.Vpc.fromLookup(this, 'custom-vpc', {
          vpcId: props.vpcId,
        })
      : ec2.Vpc.fromLookup(this, 'default-vpc', {
          isDefault: true,
        });

    const docDbSg = ec2.SecurityGroup.fromLookupById(this, 'DocDB-SG', props.securityGroupId);

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

    const productsCdcLambda = new nodejs.NodejsFunction(this, 'ProductsCdcLambda', {
      runtime: lambda.Runtime.NODEJS_18_X,
      handler: 'main',
      entry: 'src/lambdas/products-cdc.ts',
      timeout: Duration.seconds(60),
      vpc,
      securityGroups: [docDbSg],
      allowPublicSubnet: true,
      environment: {
        DEFAULT_EVENT_BUS: defaultEventBus.eventBusName,
      },
    });

    defaultEventBus.grantPutEventsTo(productsCdcLambda);

    productsCdcLambda.addToRolePolicy(
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
    productsCdcLambda.addToRolePolicy(
      new iam.PolicyStatement({
        sid: 'LambdaDocDBESMAccess',
        effect: iam.Effect.ALLOW,
        actions: ['rds:DescribeDBClusters', 'rds:DescribeDBClusterParameters', 'rds:DescribeDBSubnetGroups'],
        resources: ['*'],
      })
    );
    productsCdcLambda.addToRolePolicy(
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
              cdcFunctionName: productsCdcLambda.functionName,
              collectionName: 'products',
            },
          ],
          databaseName: 'docdb',
          clusterArn: `arn:aws:rds:${this.region}:${this.account}:cluster:${props.docDbClusterId}`,
          authUri: props.docDbClusterSecretArn,
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

    const productCreatedLambda = new nodejs.NodejsFunction(this, 'ProductCreatedLambda', {
      runtime: lambda.Runtime.NODEJS_18_X,
      handler: 'main',
      entry: 'src/lambdas/product-created.ts',
      timeout: Duration.seconds(60),
      vpc,
      securityGroups: [docDbSg],
      allowPublicSubnet: true,
      environment: {
        DEFAULT_EVENT_BUS: defaultEventBus.eventBusName,
      },
    });
    const productCreatedRule = new events.Rule(this, 'ProductCreatedRule', {
      eventBus: defaultEventBus,
      eventPattern: {
        source: ['docdb.cdc'],
        detailType: ['productCreated'],
      },
      targets: [new targets.LambdaFunction(productCreatedLambda)],
    });
  }
}
