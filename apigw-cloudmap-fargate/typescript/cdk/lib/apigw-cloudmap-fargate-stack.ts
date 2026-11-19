import { CfnOutput, Duration, Names, RemovalPolicy, Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as apigwv2 from 'aws-cdk-lib/aws-apigatewayv2';
import { HttpIamAuthorizer } from 'aws-cdk-lib/aws-apigatewayv2-authorizers';
import { HttpServiceDiscoveryIntegration } from 'aws-cdk-lib/aws-apigatewayv2-integrations';
import * as ec2 from 'aws-cdk-lib/aws-ec2';
import * as ecs from 'aws-cdk-lib/aws-ecs';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as logs from 'aws-cdk-lib/aws-logs';
import * as servicediscovery from 'aws-cdk-lib/aws-servicediscovery';

const CONTAINER_PORT = 80;

export class ApigwCloudMapFargateStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    // Two AZs, tasks in private subnets, one NAT gateway so the tasks can pull the public image.
    const vpc = new ec2.Vpc(this, 'Vpc', { maxAzs: 2, natGateways: 1 });
    const cluster = new ecs.Cluster(this, 'Cluster', { vpc });

    // The Cloud Map namespace must be a private DNS namespace. Its name is derived from the stack name.
    const namespace = new servicediscovery.PrivateDnsNamespace(this, 'Namespace', {
      vpc,
      name: `${Names.uniqueResourceName(this, { maxLength: 40, separator: '-', allowedSpecialCharacters: '-' }).toLowerCase()}.internal`,
    });

    // Container logs: explicit log group with retention, deleted by cdk destroy.
    const logGroup = new logs.LogGroup(this, 'ContainerLogs', {
      retention: logs.RetentionDays.ONE_WEEK,
      removalPolicy: RemovalPolicy.DESTROY,
    });
    // Both task roles trust Amazon ECS only for tasks of this account and Region (confused deputy protection). The task role has no permissions: the container calls no AWS API.
    const ecsTasks = new iam.ServicePrincipal('ecs-tasks.amazonaws.com', {
      conditions: {
        ArnLike: { 'aws:SourceArn': `arn:${this.partition}:ecs:${this.region}:${this.account}:*` },
        StringEquals: { 'aws:SourceAccount': this.account },
      },
    });
    const taskDefinition = new ecs.FargateTaskDefinition(this, 'TaskDef', {
      cpu: 256,
      memoryLimitMiB: 512,
      taskRole: new iam.Role(this, 'TaskRole', { assumedBy: ecsTasks }),
      executionRole: new iam.Role(this, 'ExecutionRole', { assumedBy: ecsTasks }),
    });
    // Stock nginx image, pinned tag, no image build. The command writes a page that names the serving task.
    const container = taskDefinition.addContainer('web', {
      image: ecs.ContainerImage.fromRegistry('public.ecr.aws/nginx/nginx:1.31.7-alpine3.24'),
      portMappings: [{ containerPort: CONTAINER_PORT }],
      command: ['sh', '-c', 'echo "served by task $(hostname)" > /usr/share/nginx/html/index.html && exec nginx -g "daemon off;"'],
      logging: ecs.LogDrivers.awsLogs({ streamPrefix: 'web', logGroup }),
      healthCheck: { command: ['CMD-SHELL', `wget -q -O /dev/null http://127.0.0.1:${CONTAINER_PORT}/ || exit 1`], startPeriod: Duration.seconds(10) },
    });

    // The VPC link has its own security group: no inbound rules, outbound only to the container port inside the VPC.
    // The task security group accepts the container port only from the VPC link security group.
    const vpcLinkSg = new ec2.SecurityGroup(this, 'VpcLinkSg', { vpc, allowAllOutbound: false });
    vpcLinkSg.addEgressRule(ec2.Peer.ipv4(vpc.vpcCidrBlock), ec2.Port.tcp(CONTAINER_PORT), 'Container port inside the VPC');
    const taskSg = new ec2.SecurityGroup(this, 'TaskSg', { vpc });
    taskSg.addIngressRule(vpcLinkSg, ec2.Port.tcp(CONTAINER_PORT), 'VPC link to task');

    // SRV records carry the IP address and the port that API Gateway needs. The default for awsvpc is an A record.
    const service = new ecs.FargateService(this, 'Service', {
      cluster,
      taskDefinition,
      desiredCount: 1,
      minHealthyPercent: 100,
      circuitBreaker: { rollback: true },
      securityGroups: [taskSg],
      cloudMapOptions: {
        cloudMapNamespace: namespace,
        dnsRecordType: servicediscovery.DnsRecordType.SRV,
        container,
        containerPort: CONTAINER_PORT,
      },
    });

    // The tasks pull the public image through the NAT gateway, so create the service only after the private routes exist.
    for (const subnet of vpc.privateSubnets) service.node.addDependency(subnet.internetConnectivityEstablished);

    // HTTP API with a VPC link V2. The integration target is the Cloud Map service, and callers must sign requests with IAM (SigV4).
    // The default $default stage keeps the stage name out of the backend path.
    const vpcLink = new apigwv2.VpcLink(this, 'VpcLink', { vpc, securityGroups: [vpcLinkSg] });
    const api = new apigwv2.HttpApi(this, 'HttpApi', { description: 'HTTP API to Amazon ECS on AWS Fargate through AWS Cloud Map' });
    const cloudMapService = service.cloudMapService;
    if (!cloudMapService) throw new Error('cloudMapOptions did not create a Cloud Map service');
    const integration = new HttpServiceDiscoveryIntegration('CloudMapIntegration', cloudMapService, { vpcLink });
    const authorizer = new HttpIamAuthorizer();
    for (const path of ['/', '/{proxy+}']) {
      api.addRoutes({ path, methods: [apigwv2.HttpMethod.GET], integration, authorizer });
    }

    new CfnOutput(this, 'ApiUrl', { value: api.apiEndpoint, description: 'Invoke URL of the HTTP API (no trailing slash)' });
    new CfnOutput(this, 'ClusterName', { value: cluster.clusterName });
    new CfnOutput(this, 'EcsServiceName', { value: service.serviceName });
    new CfnOutput(this, 'CloudMapNamespaceName', { value: namespace.namespaceName });
    new CfnOutput(this, 'CloudMapServiceName', { value: cloudMapService.serviceName });
    new CfnOutput(this, 'CloudMapServiceId', { value: cloudMapService.serviceId });
    new CfnOutput(this, 'VpcLinkId', { value: vpcLink.vpcLinkId });
    new CfnOutput(this, 'ContainerLogGroupName', { value: logGroup.logGroupName });
  }
}
