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
  secretName: string;
  databaseName: string;
  collectionName: string;
  docDbClusterId: string;
  docDbClusterSecretArn: string;
  securityGroupId: string;
  vpcId?: string;
  vpcLambdaEndpointExist?: boolean;
  vpcEventBridgeEndpointExist?: boolean;
  vpcSecretManagerEndpointExist?: boolean;
}
export class DocumentDbStreamLambdaEventBridgeStack extends Stack {
  constructor(scope: Construct, id: string, props: DocumentDbStreamLambdaEventBridgeStackProps) {
    super(scope, id, props);

    // default event bus
    const defaultEventBus = events.EventBus.fromEventBusName(this, 'Default-Event-Bus', 'default');

    const { vpc, docDbSg } = this.validateProps(props);

    const productsCdcLambda = createProductsCdcLambda(this, {
      vpc,
      docDbSg,
      defaultEventBus,
      docDbClusterSecretArn: props.docDbClusterSecretArn,
    });

    createEnableCdcLambdaCustomResource(this, {
      vpc,
      docDbSg,
      productsCdcLambda,
      docDbClusterId: props.docDbClusterId,
      docDbClusterSecretArn: props.docDbClusterSecretArn,
      secretName: props.secretName,
      databaseName: props.databaseName,
      collectionName: props.collectionName,
    });

    createProductCreatedLambda(this, { vpc, docDbSg, defaultEventBus });
  }

  private validateProps(props: DocumentDbStreamLambdaEventBridgeStackProps) {
    const vpc = !!props.vpcId
      ? ec2.Vpc.fromLookup(this, 'custom-vpc', {
          vpcId: props.vpcId,
        })
      : ec2.Vpc.fromLookup(this, 'default-vpc', {
          isDefault: true,
        });

    const docDbSg = ec2.SecurityGroup.fromLookupById(this, 'DocDB-SG', props.securityGroupId);

    if (!props.vpcSecretManagerEndpointExist) {
      new ec2.InterfaceVpcEndpoint(this, 'VPC Endpoint for Secrets', {
        vpc,
        service: ec2.InterfaceVpcEndpointAwsService.SECRETS_MANAGER,
        subnets: {
          subnets: vpc.publicSubnets,
        },
        securityGroups: [docDbSg],
      });
    }

    if (!props.vpcLambdaEndpointExist) {
      const lambdaVpcEndpoint = new ec2.InterfaceVpcEndpoint(this, 'VPC Endpoint for Lambda to enable CDC', {
        vpc,
        service: ec2.InterfaceVpcEndpointAwsService.LAMBDA,
        subnets: {
          subnets: vpc.publicSubnets,
        },
        securityGroups: [docDbSg],
      });
    }
    if (!props.vpcEventBridgeEndpointExist) {
      const eventBridgeVpcEndpoint = new ec2.InterfaceVpcEndpoint(this, 'VPC Endpoint for EventBridge to enable CDC', {
        vpc,
        service: ec2.InterfaceVpcEndpointAwsService.EVENTBRIDGE,
        subnets: {
          subnets: vpc.publicSubnets,
        },
        securityGroups: [docDbSg],
      });
    }
    return { vpc, docDbSg };
  }
}

interface CreateProductsCdcLambdaProps {
  vpc: ec2.IVpc;
  docDbSg: ec2.ISecurityGroup;
  defaultEventBus: events.IEventBus;
  docDbClusterSecretArn: string;
}
function createProductsCdcLambda(scope: Construct, { defaultEventBus, docDbClusterSecretArn, docDbSg, vpc }: CreateProductsCdcLambdaProps) {
  const productsCdcLambda = new nodejs.NodejsFunction(scope, 'ProductsCdcLambda', {
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
      resources: [docDbClusterSecretArn],
    })
  );
  return productsCdcLambda;
}

interface CreateEnableCdcLambdaCustomResourceProps {
  vpc: ec2.IVpc;
  docDbSg: ec2.ISecurityGroup;
  productsCdcLambda: nodejs.NodejsFunction;
  secretName: string;
  docDbClusterId: string;
  docDbClusterSecretArn: string;
  databaseName: string;
  collectionName: string;
}
function createEnableCdcLambdaCustomResource(
  scope: Construct,
  {
    docDbSg,
    vpc,
    productsCdcLambda,
    docDbClusterId,
    docDbClusterSecretArn,
    secretName,
    databaseName,
    collectionName,
  }: CreateEnableCdcLambdaCustomResourceProps
) {
  const enableCdcLambdaCR = new nodejs.NodejsFunction(scope, 'EnableCdcLambdaCustomResource', {
    runtime: lambda.Runtime.NODEJS_18_X,
    handler: 'main',
    entry: 'src/lambdas/enable-cdc-cr.ts',
    vpc,
    timeout: Duration.seconds(30),
    securityGroups: [docDbSg],
    allowPublicSubnet: true,
    bundling: {
      sourceMap: true,
      minify: true,
      externalModules: [], // this is necessary because with NODEJS_18_X the bundled version of the sdk is not the recent one
    },
  });

  enableCdcLambdaCR.addToRolePolicy(
    new iam.PolicyStatement({
      effect: iam.Effect.ALLOW,
      actions: ['lambda:CreateEventSourceMapping', 'lambda:UpdateEventSourceMapping', 'lambda:DeleteEventSourceMapping'],
      resources: ['*'],
    })
  );

  enableCdcLambdaCR.addToRolePolicy(
    new iam.PolicyStatement({
      sid: 'LambdaGetSecretValueAccessForDocDB',
      effect: iam.Effect.ALLOW,
      actions: ['secretsmanager:GetSecretValue'],
      resources: [docDbClusterSecretArn],
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
            collectionName,
          },
        ],
        secretName,
        databaseName,
        authUri: docDbClusterSecretArn,
        clusterArn: `arn:aws:rds:${Stack.of(scope).region}:${Stack.of(scope).account}:cluster:${docDbClusterId}`,
        date: new Date(),
      }),
    },
    physicalResourceId: cr.PhysicalResourceId.of(`enableCdcLambda`),
  };
  const customResource = new cr.AwsCustomResource(scope, 'InvokeEnableCdcLambda', {
    onCreate: awsSDKCall,
    onUpdate: awsSDKCall,
    policy: cr.AwsCustomResourcePolicy.fromSdkCalls({
      resources: cr.AwsCustomResourcePolicy.ANY_RESOURCE,
    }),
  });

  enableCdcLambdaCR.grantInvoke(customResource);

  return { enableCdcLambdaCR, customResource };
}

interface CreateProductCreatedLambdaProps {
  vpc: ec2.IVpc;
  docDbSg: ec2.ISecurityGroup;
  defaultEventBus: events.IEventBus;
}
function createProductCreatedLambda(scope: Construct, { docDbSg, vpc, defaultEventBus }: CreateProductCreatedLambdaProps) {
  const productCreatedLambda = new nodejs.NodejsFunction(scope, 'ProductCreatedLambda', {
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
  const productCreatedRule = new events.Rule(scope, 'ProductCreatedRule', {
    eventBus: defaultEventBus,
    eventPattern: {
      source: ['products.cdc'],
      detailType: ['productCreated'],
    },
    targets: [new targets.LambdaFunction(productCreatedLambda)],
  });

  return { productCreatedLambda, productCreatedRule };
}
