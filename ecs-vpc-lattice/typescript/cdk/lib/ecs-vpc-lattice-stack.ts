import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as ec2 from 'aws-cdk-lib/aws-ec2';
import * as ecs from 'aws-cdk-lib/aws-ecs';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as logs from 'aws-cdk-lib/aws-logs';
import * as cw from 'aws-cdk-lib/aws-cloudwatch';
import * as lattice from 'aws-cdk-lib/aws-vpclattice';
import * as path from 'path';

const CONTAINER_PORT = 8080;

export class EcsVpcLatticeStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // The version the app reports. Deploy again with `-c appVersion=v2` to start a blue/green deployment.
    const appVersion: string = String(this.node.tryGetContext('appVersion') ?? 'v1');

    // ---- Network: public subnets for the Fargate tasks (public image pull, no NAT gateway) and
    // isolated subnets for the hook Lambda, which only talks to VPC Lattice.
    const vpc = new ec2.Vpc(this, 'Vpc', {
      maxAzs: 2,
      natGateways: 0,
      subnetConfiguration: [
        { name: 'public', subnetType: ec2.SubnetType.PUBLIC, cidrMask: 24 },
        { name: 'isolated', subnetType: ec2.SubnetType.PRIVATE_ISOLATED, cidrMask: 24 },
      ],
    });

    const taskSg = new ec2.SecurityGroup(this, 'TaskSg', { vpc, description: 'Fargate tasks: only VPC Lattice may connect' });
    const hookSg = new ec2.SecurityGroup(this, 'HookSg', { vpc, description: 'Hook Lambda' });
    const assocSg = new ec2.SecurityGroup(this, 'AssocSg', { vpc, description: 'VPC association: clients in the VPC may call listeners' });
    assocSg.addIngressRule(ec2.Peer.ipv4(vpc.vpcCidrBlock), ec2.Port.tcp(80), 'Clients in the VPC to the Lattice listener');

    // VPC Lattice reaches targets, and runs its health checks, from the addresses in its managed prefix list
    // (com.amazonaws.<region>.vpc-lattice). The prefix list ID is different in every Region, so it is a stack
    // parameter: `cdk deploy --parameters LatticePrefixListId=pl-...` (the README shows the command that looks it up).
    const prefixListId = new cdk.CfnParameter(this, 'LatticePrefixListId', {
      type: 'String',
      description: 'ID of the AWS managed prefix list com.amazonaws.<region>.vpc-lattice in this Region',
      allowedPattern: '^pl-[0-9a-f]+$',
      constraintDescription: 'Must be a prefix list ID such as pl-0123456789abcdef0',
    });
    taskSg.addIngressRule(ec2.Peer.prefixList(prefixListId.valueAsString), ec2.Port.tcp(CONTAINER_PORT), 'VPC Lattice to tasks and health checks');

    // ---- VPC Lattice: service network, VPC association, two IP target groups (blue and green), service, listener, rules.
    const serviceNetwork = new lattice.CfnServiceNetwork(this, 'ServiceNetwork', { authType: 'NONE' });
    const vpcAssociation = new lattice.CfnServiceNetworkVpcAssociation(this, 'VpcAssociation', {
      serviceNetworkIdentifier: serviceNetwork.attrId,
      vpcIdentifier: vpc.vpcId,
      securityGroupIds: [assocSg.securityGroupId],
    });

    const targetGroup = (tgId: string) =>
      new lattice.CfnTargetGroup(this, tgId, {
        type: 'IP',
        config: {
          port: CONTAINER_PORT,
          protocol: 'HTTP',
          protocolVersion: 'HTTP1',
          ipAddressType: 'IPV4',
          vpcIdentifier: vpc.vpcId,
          healthCheck: {
            enabled: true,
            protocol: 'HTTP',
            path: '/',
            healthCheckIntervalSeconds: 10,
            healthCheckTimeoutSeconds: 5,
            healthyThresholdCount: 2,
            unhealthyThresholdCount: 2,
            matcher: { httpCode: '200' },
          },
        },
      });
    const blueTargetGroup = targetGroup('BlueTargetGroup');
    const greenTargetGroup = targetGroup('GreenTargetGroup');

    const latticeService = new lattice.CfnService(this, 'LatticeService', { authType: 'NONE' });
    const listener = new lattice.CfnListener(this, 'Listener', {
      serviceIdentifier: latticeService.attrId,
      protocol: 'HTTP',
      port: 80,
      defaultAction: { fixedResponse: { statusCode: 404 } },
    });

    // Both rules start at blue 100 / green 0. During a deployment ECS edits these weights.
    const initialWeights = [
      { targetGroupIdentifier: blueTargetGroup.attrId, weight: 100 },
      { targetGroupIdentifier: greenTargetGroup.attrId, weight: 0 },
    ];
    // Test rule: only requests with the header "x-environment: test" (used by the hook Lambda).
    const testRule = new lattice.CfnRule(this, 'TestRule', {
      serviceIdentifier: latticeService.attrId,
      listenerIdentifier: listener.attrId,
      priority: 10,
      match: { httpMatch: { headerMatches: [{ name: 'x-environment', match: { exact: 'test' } }] } },
      action: { forward: { targetGroups: initialWeights } },
    });
    // Production rule: everything else.
    const productionRule = new lattice.CfnRule(this, 'ProductionRule', {
      serviceIdentifier: latticeService.attrId,
      listenerIdentifier: listener.attrId,
      priority: 100,
      match: { httpMatch: { pathMatch: { match: { prefix: '/' } } } },
      action: { forward: { targetGroups: initialWeights } },
    });
    const serviceAssociation = new lattice.CfnServiceNetworkServiceAssociation(this, 'ServiceAssociation', {
      serviceIdentifier: latticeService.attrId,
      serviceNetworkIdentifier: serviceNetwork.attrId,
    });

    // ---- ECS infrastructure role: lets ECS register tasks and change listener rule weights in VPC Lattice.
    const infrastructureRole = new iam.Role(this, 'EcsInfrastructureRole', {
      assumedBy: new iam.ServicePrincipal('ecs.amazonaws.com'),
      managedPolicies: [iam.ManagedPolicy.fromAwsManagedPolicyName('AmazonECSInfrastructureRolePolicyForVpcLattice')],
    });

    // ---- Lifecycle hook Lambda: runs inside the VPC and calls the Lattice service DNS name through the VPC association.
    const hookFunction = new lambda.Function(this, 'HookFunction', {
      runtime: lambda.Runtime.NODEJS_24_X,
      handler: 'hook.handler',
      code: lambda.Code.fromAsset(path.join(__dirname, '..', 'lambda'), { exclude: ['*.test.js'] }),
      vpc,
      vpcSubnets: { subnetType: ec2.SubnetType.PRIVATE_ISOLATED },
      securityGroups: [hookSg],
      timeout: cdk.Duration.seconds(90),
      logGroup: new logs.LogGroup(this, 'HookLogGroup', {
        retention: logs.RetentionDays.ONE_WEEK,
        removalPolicy: cdk.RemovalPolicy.DESTROY,
      }),
    });

    // ---- CloudWatch alarms: any 5xx from the VPC Lattice service during the deployment triggers a rollback.
    // VPC Lattice publishes the service metrics per Availability Zone (dimensions AvailabilityZone and Service),
    // and a CloudWatch alarm only matches the exact dimension set, so there is one alarm per AZ of the VPC.
    // HTTPCode_5XX_Count only exists after the first 5xx, hence treatMissingData NOT_BREACHING.
    const alarms = vpc.availabilityZones.map((az, i) => new cw.Alarm(this, `Lattice5xxAlarm${i}`, {
      alarmDescription: 'HTTP 5xx responses from the VPC Lattice service in one Availability Zone',
      metric: new cw.Metric({
        namespace: 'AWS/VpcLattice',
        metricName: 'HTTPCode_5XX_Count',
        dimensionsMap: { Service: latticeService.attrId, AvailabilityZone: az },
        statistic: 'Sum',
        period: cdk.Duration.minutes(1),
      }),
      threshold: 1,
      evaluationPeriods: 1,
      comparisonOperator: cw.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
      treatMissingData: cw.TreatMissingData.NOT_BREACHING,
    }));

    // ---- ECS: Fargate service with the BLUE_GREEN strategy. The app is a public busybox image that serves {"version": ...}.
    const cluster = new ecs.Cluster(this, 'Cluster', { vpc });
    const taskDefinition = new ecs.FargateTaskDefinition(this, 'TaskDef', { cpu: 256, memoryLimitMiB: 512 });
    const container = taskDefinition.addContainer('web', {
      image: ecs.ContainerImage.fromRegistry('public.ecr.aws/docker/library/busybox:stable'),
      command: [
        'sh', '-c',
        `mkdir -p /www && echo "{\\"version\\":\\"$APP_VERSION\\"}" > /www/index.html && exec httpd -f -p ${CONTAINER_PORT} -h /www`,
      ],
      environment: { APP_VERSION: appVersion },
      logging: ecs.LogDrivers.awsLogs({
        streamPrefix: 'web',
        logGroup: new logs.LogGroup(this, 'WebLogGroup', {
          retention: logs.RetentionDays.ONE_WEEK,
          removalPolicy: cdk.RemovalPolicy.DESTROY,
        }),
      }),
    });
    // The port mapping name is what ECS registers with the Lattice target groups.
    container.addPortMappings({ containerPort: CONTAINER_PORT, name: 'web', protocol: ecs.Protocol.TCP });

    const service = new ecs.FargateService(this, 'Service', {
      cluster,
      taskDefinition,
      desiredCount: 1,
      assignPublicIp: true,
      vpcSubnets: { subnetType: ec2.SubnetType.PUBLIC },
      securityGroups: [taskSg],
      deploymentStrategy: ecs.DeploymentStrategy.BLUE_GREEN,
      bakeTime: cdk.Duration.minutes(2),
      minHealthyPercent: 100,
      maxHealthyPercent: 200,
      circuitBreaker: { rollback: true },
      lifecycleHooks: [
        // Runs after ECS moved TEST traffic to the green revision and before production traffic moves.
        new ecs.DeploymentLifecycleLambdaTarget(hookFunction, 'TestGreenHook', {
          lifecycleStages: [ecs.DeploymentLifecycleStage.POST_TEST_TRAFFIC_SHIFT],
        }),
      ],
    });
    service.enableDeploymentAlarms(alarms.map((a) => a.alarmName), { behavior: ecs.AlarmBehavior.ROLLBACK_ON_ALARM });

    // The L2 construct has no VPC Lattice support yet, so the typed L1 property is set directly.
    const cfnService = service.node.defaultChild as ecs.CfnService;
    cfnService.vpcLatticeConfigurations = [
      {
        roleArn: infrastructureRole.roleArn,
        targetGroupArn: blueTargetGroup.attrArn,
        portName: 'web',
        advancedConfiguration: {
          alternateTargetGroupArn: greenTargetGroup.attrArn,
          productionListenerRule: productionRule.attrArn,
          testListenerRule: testRule.attrArn,
        },
      },
    ];
    // The L2 hook target also lacks HookDetails and the timeout. HookDetails must be a JSON object as a string
    // (CloudFormation rejects a plain object); ECS passes it to the Lambda as event.hookDetails.
    cfnService.addPropertyOverride(
      'DeploymentConfiguration.LifecycleHooks.0.HookDetails',
      cdk.Fn.join('', [
        '{"url":"http://', latticeService.attrDnsEntryDomainName, '/","expectedVersion":', JSON.stringify(appVersion), '}',
      ]),
    );
    cfnService.addPropertyOverride('DeploymentConfiguration.LifecycleHooks.0.TimeoutConfiguration', {
      TimeoutInMinutes: 10,
      Action: 'ROLLBACK',
    });
    // The Lattice service must be reachable from the VPC before the first deployment runs the hook.
    cfnService.node.addDependency(serviceAssociation, vpcAssociation, infrastructureRole);

    new cdk.CfnOutput(this, 'ClusterName', { value: cluster.clusterName });
    new cdk.CfnOutput(this, 'ServiceName', { value: service.serviceName });
    new cdk.CfnOutput(this, 'HookFunctionName', { value: hookFunction.functionName });
    new cdk.CfnOutput(this, 'HookLogGroupName', { value: hookFunction.logGroup.logGroupName });
    new cdk.CfnOutput(this, 'LatticeServiceId', { value: latticeService.attrId });
    new cdk.CfnOutput(this, 'LatticeListenerId', { value: listener.attrId });
    new cdk.CfnOutput(this, 'ProductionRuleId', { value: productionRule.attrId });
    new cdk.CfnOutput(this, 'TestRuleId', { value: testRule.attrId });
    new cdk.CfnOutput(this, 'LatticeServiceDnsName', { value: latticeService.attrDnsEntryDomainName });
  }
}
