import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as ec2 from 'aws-cdk-lib/aws-ec2';
import * as ecs from 'aws-cdk-lib/aws-ecs';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as logs from 'aws-cdk-lib/aws-logs';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as wafv2 from 'aws-cdk-lib/aws-wafv2';

const CONTAINER_PORT = 8080;
const LOG_PREFIX = 'alb';
const RATE_LIMIT = 50; // requests per client IP in the 60 second WAF window

export class EcsGatewayStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // ---- Who can reach the gateway: an explicit input, no default. Use a single address, for example
    // `cdk deploy -c allowedCidr=203.0.113.7/32`. Use `-c scheme=internal` for an internal load balancer.
    const allowedCidr = String(this.node.tryGetContext('allowedCidr') ?? '');
    const cidrParts = /^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})\/(\d{1,2})$/.exec(allowedCidr);
    if (!cidrParts || cidrParts.slice(1, 5).some((o) => Number(o) > 255) || Number(cidrParts[5]) > 32) {
      throw new Error('Set the client range with -c allowedCidr=<IPv4 CIDR>, for example -c allowedCidr=203.0.113.7/32');
    }
    // A prefix shorter than /8 (including every /0) is treated as "anyone", whatever the address part says.
    if (Number(cidrParts[5]) < 8 && this.node.tryGetContext('allowAnyone') !== 'true') {
      throw new Error(`${allowedCidr} opens the gateway to a very large part of the internet. Add -c allowAnyone=true if you really want that.`);
    }
    const internal = this.node.tryGetContext('scheme') === 'internal';

    // ---- Network: the gateway load balancers sit in the public (or, if internal, private) subnets of both
    // Availability Zones. The tasks sit in private subnets of the same two zones, as the gateway must cover
    // every zone the service uses. One NAT gateway lets the tasks pull the public image.
    const vpc = new ec2.Vpc(this, 'Vpc', { maxAzs: 2, natGateways: 1 });
    const gatewaySubnets = internal ? vpc.privateSubnets : vpc.publicSubnets;

    // Inbound security group of the gateway load balancers. Supplying it makes ECS stop managing inbound rules.
    const gatewaySg = new ec2.SecurityGroup(this, 'GatewaySg', { vpc, allowAllOutbound: false, description: 'ECS Gateway load balancers' });
    gatewaySg.addIngressRule(ec2.Peer.ipv4(allowedCidr), ec2.Port.tcp(443), 'HTTPS from the allowed client range');
    const taskSg = new ec2.SecurityGroup(this, 'TaskSg', { vpc, description: 'Fargate tasks' });
    taskSg.addIngressRule(gatewaySg, ec2.Port.tcp(CONTAINER_PORT), 'Gateway load balancers to tasks');
    gatewaySg.addEgressRule(taskSg, ec2.Port.tcp(CONTAINER_PORT), 'Gateway load balancers to tasks');

    // ---- AWS WAF: a regional web ACL in the same Region as the gateway, shared by every service behind it.
    const webAclName = `${this.stackName}-web-acl`;
    const webAcl = new wafv2.CfnWebACL(this, 'WebAcl', {
      name: webAclName,
      scope: 'REGIONAL',
      defaultAction: { allow: {} },
      visibilityConfig: { cloudWatchMetricsEnabled: true, sampledRequestsEnabled: true, metricName: 'ecs-gateway' },
      rules: [{
        name: 'RateLimitPerIp',
        priority: 0,
        action: { block: {} },
        statement: { rateBasedStatement: { limit: RATE_LIMIT, evaluationWindowSec: 60, aggregateKeyType: 'IP' } },
        visibilityConfig: { cloudWatchMetricsEnabled: true, sampledRequestsEnabled: true, metricName: 'rate-limit-per-ip' },
      }],
    });

    // ---- Access log bucket in the gateway's Region. ELB supports only SSE-S3 for log buckets.
    // autoDeleteObjects empties the bucket on `cdk destroy` (a CDK helper function, not in the request path).
    const logBucket = new s3.Bucket(this, 'GatewayLogs', {
      encryption: s3.BucketEncryption.S3_MANAGED,
      blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
      enforceSSL: true,
      lifecycleRules: [{ expiration: cdk.Duration.days(7) }],
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      autoDeleteObjects: true,
    });
    logBucket.addToResourcePolicy(new iam.PolicyStatement({
      principals: [new iam.ServicePrincipal('logdelivery.elasticloadbalancing.amazonaws.com')],
      actions: ['s3:PutObject'],
      resources: [logBucket.arnForObjects(`${LOG_PREFIX}/AWSLogs/${this.account}/*`)],
      conditions: {
        StringEquals: { 'aws:SourceAccount': this.account },
        // The load balancer is created later by ECS, so its name is not known here.
        ArnLike: { 'aws:SourceArn': `arn:${this.partition}:elasticloadbalancing:${this.region}:${this.account}:loadbalancer/*` },
      },
    }));

    // ---- Infrastructure role that ECS assumes to create load balancers, listeners, security groups and certificates.
    const infrastructureRole = new iam.Role(this, 'GatewayInfrastructureRole', {
      assumedBy: new iam.ServicePrincipal('ecs.amazonaws.com'),
      managedPolicies: [iam.ManagedPolicy.fromAwsManagedPolicyName('AmazonECSInfrastructureRoleForGatewayHostSharedALB')],
    });

    // ---- ECS Gateway (platform team). aws-cdk-lib has no construct for it yet, so it is a CfnResource.
    // DeletionProtection defaults to true; it is off here so that `cdk destroy` works.
    const gatewayName = `${this.stackName}-gateway`;
    const gateway = new cdk.CfnResource(this, 'Gateway', {
      type: 'AWS::ECS::Gateway',
      properties: {
        GatewayName: gatewayName,
        InfrastructureRoleArn: infrastructureRole.roleArn,
        DeletionProtection: false,
        // With the default (GATEWAY) the gateway's tags are copied to the certificates ECS requests for each
        // service. CloudFormation adds aws:cloudformation:* tags to the gateway, and AWS Certificate Manager
        // rejects tag keys that start with aws:, so every certificate request fails and the services never
        // finish creating. NONE avoids that.
        PropagateTags: 'NONE',
        Configuration: {
          HostSharedAlb: {
            Scheme: internal ? 'internal' : 'internet-facing',
            NetworkConfiguration: {
              Subnets: gatewaySubnets.map((s) => s.subnetId),
              IpAddressType: 'ipv4',
              InboundSecurityGroup: gatewaySg.securityGroupId,
            },
            WebACLArn: webAcl.attrArn,
            AccessLogs: { Destination: { S3: { Bucket: logBucket.bucketName, Prefix: LOG_PREFIX } } },
            MaxAlbCount: 2,
          },
        },
      },
    });
    gateway.node.addDependency(logBucket); // the bucket policy must exist before the first load balancer is created

    const cluster = new ecs.Cluster(this, 'Cluster', { vpc });
    const association = new cdk.CfnResource(this, 'GatewayAssociation', {
      type: 'AWS::ECS::GatewayClusterAssociations',
      properties: { Gateway: gateway.getAtt('Arn'), Cluster: cluster.clusterName },
    });

    // ---- Two services (application teams). Each opts in with one gatewayConnector and gets its own HTTPS hostname.
    const serviceNames = ['orders', 'catalog'].map((name) => {
      const taskDefinition = new ecs.FargateTaskDefinition(this, `${name}-task`, { cpu: 256, memoryLimitMiB: 512 });
      taskDefinition.addContainer('web', {
        image: ecs.ContainerImage.fromRegistry('public.ecr.aws/docker/library/busybox:stable'),
        command: ['sh', '-c', `mkdir -p /www && echo "hello from ${name}" > /www/index.html && exec httpd -f -p ${CONTAINER_PORT} -h /www`],
        logging: ecs.LogDrivers.awsLogs({
          streamPrefix: name,
          logGroup: new logs.LogGroup(this, `${name}-logs`, { retention: logs.RetentionDays.ONE_WEEK, removalPolicy: cdk.RemovalPolicy.DESTROY }),
        }),
        // The connector refers to this port by name.
        portMappings: [{ containerPort: CONTAINER_PORT, name: 'web' }],
      });
      const service = new ecs.FargateService(this, `${name}-service`, {
        cluster,
        taskDefinition,
        desiredCount: 1,
        minHealthyPercent: 100, // start the replacement task before the old one stops
        securityGroups: [taskSg],
        vpcSubnets: { subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS },
        circuitBreaker: { rollback: true },
      });
      // No L2 property for gateway connectors yet: set it on the L1 service.
      (service.node.defaultChild as ecs.CfnService).addPropertyOverride('GatewayConnectors', [{
        PortName: 'web',
        // The health check port defaults to 80, not to the container port. With the container on 8080 the
        // health checks time out (Target.Timeout) and the targets keep flapping, so it is set here.
        HealthCheck: { HealthCheckPath: '/', HealthCheckPort: CONTAINER_PORT },
        Filters: { AccessTypes: [internal ? 'PRIVATE' : 'PUBLIC'] },
      }]);
      // Deploy after the association is ACTIVE; on delete, the services go first so that their routes are removed.
      service.node.addDependency(association);
      return service.serviceName;
    });

    new cdk.CfnOutput(this, 'GatewayName', { value: gatewayName });
    new cdk.CfnOutput(this, 'ClusterName', { value: cluster.clusterName });
    new cdk.CfnOutput(this, 'ServiceNames', { value: cdk.Fn.join(',', serviceNames) });
    new cdk.CfnOutput(this, 'WebAclName', { value: webAclName });
    new cdk.CfnOutput(this, 'LogBucketName', { value: logBucket.bucketName });
    new cdk.CfnOutput(this, 'AllowedCidr', { value: allowedCidr });
  }
}
