import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as ec2 from 'aws-cdk-lib/aws-ec2';
import * as elbv2 from 'aws-cdk-lib/aws-elasticloadbalancingv2';
import * as elbv2t from 'aws-cdk-lib/aws-elasticloadbalancingv2-targets';
import * as acm from 'aws-cdk-lib/aws-certificatemanager';
import * as route53 from 'aws-cdk-lib/aws-route53';
import * as targets from 'aws-cdk-lib/aws-route53-targets';
import * as cr from 'aws-cdk-lib/custom-resources';
import * as iam from 'aws-cdk-lib/aws-iam';

export interface MicroVmCustomDomainsConfig {
  /** ID of an existing Route 53 public hosted zone that will hold the wildcard record. */
  readonly hostedZoneId: string;
  /** Name of that hosted zone, e.g. "example.com". */
  readonly hostedZoneName: string;
  /**
   * The wildcard base under which each custom domain is served, e.g.
   * "microvms.example.com". Customers reach
   * "<uuid>.microvms.example.com".
   */
  readonly customDomainBase: string;
  /**
   * The MicroVM endpoint base the Host header is rewritten TO, e.g.
   * "lambda-microvm.us-east-2.on.aws". The per-request prefix is preserved,
   * producing "<uuid>.lambda-microvm.us-east-2.on.aws".
   */
  readonly microvmEndpointBase: string;
  /**
   * AWS-managed PrivateLink service used to reach MicroVMs privately, e.g.
   * "com.amazonaws.us-east-2.lambda-microvm".
   */
  readonly microvmVpceServiceName: string;
  /** Origin allowed on the CORS response headers the ALB inserts. */
  readonly corsAllowOrigin: string;
}

export interface MicroVmCustomDomainsStackProps extends cdk.StackProps {
  readonly config: MicroVmCustomDomainsConfig;
}

/**
 * Fronts AWS Lambda MicroVMs with customer-owned wildcard custom domains.
 *
 * This is the core, reusable networking pattern described in the blog post:
 * everything in the hot request path and nothing else. The optional demo layer
 * (single-page app + provisioning API) lives in a separate construct,
 * {@link MicroVmDemoApp}, and attaches to the {@link httpsListener} exposed here.
 *
 * Request flow:
 *   <uuid>.microvms.example.com
 *     -> Route 53 A/AAAA alias (wildcard) -> ALB (TLS, *.customDomainBase cert)
 *     -> HTTPS listener rule: regex host match + Host-header rewrite Transform
 *          <uuid>.customDomainBase  =>  <uuid>.microvmEndpointBase
 *     -> IP target group (private ENI IPs of the MicroVM interface endpoint), HTTPS:443
 *   MicroVM front-end routes on the (rewritten) Host header and enforces the JWE
 *   auth token the client still supplies in X-aws-proxy-auth.
 *
 * No CloudFront, and no compute in the request path. The only Lambda is a
 * deploy-time custom resource that discovers the endpoint ENI IPs.
 */
export class MicroVmCustomDomainsStack extends cdk.Stack {
  /**
   * The public HTTPS:443 listener on the ALB. Exposed so the optional demo
   * construct can attach its own (higher-priority) host rule without the core
   * stack needing to know anything about the demo.
   */
  public readonly httpsListener: elbv2.ApplicationListener;

  constructor(scope: Construct, id: string, props: MicroVmCustomDomainsStackProps) {
    super(scope, id, props);
    const cfg = props.config;

    const wildcardDomain = `*.${cfg.customDomainBase}`;

    // --- Networking -------------------------------------------------------
    // A small VPC to host the ALB and the MicroVM interface endpoint. 2 AZs is
    // the minimum for an internet-facing ALB. NAT gateways are unnecessary
    // (nothing here needs egress), so we omit them to stay lean and cheap.
    const vpc = new ec2.Vpc(this, 'Vpc', {
      maxAzs: 2,
      natGateways: 0,
      subnetConfiguration: [
        { name: 'public', subnetType: ec2.SubnetType.PUBLIC, cidrMask: 24 },
        { name: 'private', subnetType: ec2.SubnetType.PRIVATE_ISOLATED, cidrMask: 24 },
      ],
    });

    // Security group for the interface endpoint: allow HTTPS from within the VPC
    // (the ALB nodes) only.
    const endpointSg = new ec2.SecurityGroup(this, 'EndpointSg', {
      vpc,
      description: 'Ingress to MicroVM interface endpoint from ALB',
      allowAllOutbound: true,
    });
    endpointSg.addIngressRule(
      ec2.Peer.ipv4(vpc.vpcCidrBlock),
      ec2.Port.tcp(443),
      'HTTPS from ALB within VPC',
    );

    // Interface (PrivateLink) endpoint to the AWS-managed MicroVM service.
    const endpoint = new ec2.InterfaceVpcEndpoint(this, 'MicroVmEndpoint', {
      vpc,
      service: new ec2.InterfaceVpcEndpointService(cfg.microvmVpceServiceName, 443),
      subnets: { subnetType: ec2.SubnetType.PRIVATE_ISOLATED },
      securityGroups: [endpointSg],
      // We rewrite Host ourselves at the ALB; keep the service's own private DNS
      // off so the ALB reaches the endpoint by its ENI IPs, not by the MicroVM name.
      privateDnsEnabled: false,
      open: false,
    });

    // --- Resolve the endpoint's private ENI IPs --------------------------
    // CloudFormation does not surface interface-endpoint ENI IPs as attributes,
    // so discover them at deploy time with a custom resource (deploy-time only,
    // never in the request path).
    const targetIps = this.discoverEndpointIps(endpoint, vpc.availabilityZones.length);

    // --- TLS certificate for the wildcard custom domain -------------------
    const hostedZone = route53.HostedZone.fromHostedZoneAttributes(this, 'Zone', {
      hostedZoneId: cfg.hostedZoneId,
      zoneName: cfg.hostedZoneName,
    });

    const certificate = new acm.Certificate(this, 'WildcardCert', {
      domainName: wildcardDomain,
      validation: acm.CertificateValidation.fromDns(hostedZone),
    });

    // --- Application Load Balancer ---------------------------------------
    const albSg = new ec2.SecurityGroup(this, 'AlbSg', {
      vpc,
      description: 'Public HTTPS ingress to MicroVM custom-domain ALB',
      allowAllOutbound: true,
    });
    albSg.addIngressRule(ec2.Peer.anyIpv4(), ec2.Port.tcp(443), 'HTTPS from internet');

    const alb = new elbv2.ApplicationLoadBalancer(this, 'Alb', {
      vpc,
      internetFacing: true,
      securityGroup: albSg,
      vpcSubnets: { subnetType: ec2.SubnetType.PUBLIC },
    });

    // Target group of the endpoint ENI IPs, spoken to over HTTPS. The MicroVM
    // service presents its own certificate; ALB does not validate target certs,
    // so re-origination succeeds regardless of the name mismatch. Health checks
    // use a permissive matcher because an unauthenticated probe returns 403.
    const targetGroup = new elbv2.ApplicationTargetGroup(this, 'MicroVmTargets', {
      vpc,
      protocol: elbv2.ApplicationProtocol.HTTPS,
      port: 443,
      targetType: elbv2.TargetType.IP,
      targets: targetIps.map((ip) => new elbv2t.IpTarget(ip, 443)),
      healthCheck: {
        protocol: elbv2.Protocol.HTTPS,
        path: '/',
        healthyHttpCodes: '200,403,404',
      },
    });

    const listener = alb.addListener('Https', {
      port: 443,
      protocol: elbv2.ApplicationProtocol.HTTPS,
      certificates: [certificate],
      // Default action for anything that doesn't match our host regex.
      defaultAction: elbv2.ListenerAction.fixedResponse(404, {
        contentType: 'text/plain',
        messageBody: 'Unknown custom domain',
      }),
    });
    this.httpsListener = listener;

    // --- CORS response headers, inserted by the ALB on EVERY response --------
    // The ALB header-modification feature adds these Access-Control-* headers to
    // all responses on this listener -- both our OPTIONS preflight 204 AND the
    // forwarded MicroVM response. That satisfies the browser without any change
    // to the MicroVM application. (These are listener attributes; the L2 does
    // not model them yet, so we set them on the underlying CfnListener.)
    const cfnListener = listener.node.defaultChild as elbv2.CfnListener;
    cfnListener.addPropertyOverride('ListenerAttributes', [
      { Key: 'routing.http.response.access_control_allow_origin.header_value', Value: cfg.corsAllowOrigin },
      { Key: 'routing.http.response.access_control_allow_methods.header_value', Value: 'GET,POST,PUT,DELETE,OPTIONS,PATCH,HEAD' },
      { Key: 'routing.http.response.access_control_allow_headers.header_value', Value: 'x-aws-proxy-auth,x-aws-proxy-port,content-type,authorization' },
      { Key: 'routing.http.response.access_control_expose_headers.header_value', Value: 'content-type,content-length' },
      { Key: 'routing.http.response.access_control_max_age.header_value', Value: '86400' },
    ]);

    // --- CORS preflight: answer OPTIONS at the edge --------------------------
    // Priority ahead of the forwarding rule so preflights never reach the origin
    // (they would 403 there without a JWE token anyway). See the README "CORS"
    // section for the important limitation on Access-Control-* response headers.
    new elbv2.ApplicationListenerRule(this, 'CorsPreflightRule', {
      listener,
      priority: 10,
      conditions: [elbv2.ListenerCondition.httpRequestMethods(['OPTIONS'])],
      action: elbv2.ListenerAction.fixedResponse(204, {
        contentType: 'text/plain',
        messageBody: '',
      }),
    });

    // --- Host-header rewrite forwarding rule ------------------------------
    // Match "<uuid>.customDomainBase" with a regex condition, forward to the
    // target group, and rewrite the Host header to "<uuid>.microvmEndpointBase"
    // using the new ALB Transforms feature (L1 escape hatch; not yet in the L2).
    const forwardingRule = new elbv2.ApplicationListenerRule(this, 'HostRewriteRule', {
      listener,
      priority: 20,
      // The L2 requires at least one condition/action; we replace both on the L1
      // below to express the regex match + transform that the L2 can't model yet.
      conditions: [elbv2.ListenerCondition.hostHeaders([`*.${cfg.customDomainBase}`])],
      action: elbv2.ListenerAction.forward([targetGroup]),
    });

    this.applyHostRewrite(forwardingRule, cfg.customDomainBase, cfg.microvmEndpointBase);

    // --- Route 53: wildcard alias to the ALB -------------------------------
    // customDomainBase is always within the hosted zone, so we use the fully
    // qualified wildcard name directly (CDK accepts absolute names that end in
    // the zone name). This is robust to any number of subdomain labels between
    // the base and the zone apex.
    const albAlias = route53.RecordTarget.fromAlias(new targets.LoadBalancerTarget(alb));
    new route53.ARecord(this, 'WildcardAlias', {
      zone: hostedZone,
      recordName: wildcardDomain,
      target: albAlias,
    });
    new route53.AaaaRecord(this, 'WildcardAliasV6', {
      zone: hostedZone,
      recordName: wildcardDomain,
      target: albAlias,
    });

    // --- Outputs ----------------------------------------------------------
    new cdk.CfnOutput(this, 'AlbDnsName', { value: alb.loadBalancerDnsName });
    new cdk.CfnOutput(this, 'WildcardDomain', { value: wildcardDomain });
    new cdk.CfnOutput(this, 'CertificateArn', { value: certificate.certificateArn });
    new cdk.CfnOutput(this, 'ResolvedTargetIps', { value: cdk.Fn.join(',', targetIps) });
    new cdk.CfnOutput(this, 'CorsAllowOrigin', {
      value: cfg.corsAllowOrigin,
      description: 'Origin the OPTIONS preflight advertises. See README CORS caveat.',
    });
  }

  /**
   * Discovers the private IPv4 addresses of the interface endpoint's ENIs at
   * deploy time. This is the ONLY compute in the package, it runs only during
   * `cdk deploy`, and it is never in the request path.
   */
  private discoverEndpointIps(endpoint: ec2.InterfaceVpcEndpoint, count: number): string[] {
    // Query the endpoint's OWN ENIs by ID (exposed as a CloudFormation attribute),
    // rather than by a filter. This avoids guessing filter keys and guarantees we
    // only ever read IPs that belong to this endpoint — so ordering of the results
    // is irrelevant (every returned private IP is a valid target).
    const lookup = new cr.AwsCustomResource(this, 'EndpointIpLookup', {
      onUpdate: {
        service: 'EC2',
        action: 'describeNetworkInterfaces',
        parameters: {
          NetworkInterfaceIds: endpoint.vpcEndpointNetworkInterfaceIds,
        },
        physicalResourceId: cr.PhysicalResourceId.of(endpoint.vpcEndpointId),
      },
      policy: cr.AwsCustomResourcePolicy.fromStatements([
        new iam.PolicyStatement({
          actions: ['ec2:DescribeNetworkInterfaces'],
          resources: ['*'], // DescribeNetworkInterfaces does not support resource-level scoping.
        }),
      ]),
      installLatestAwsSdk: false,
    });
    lookup.node.addDependency(endpoint);

    // One ENI per AZ; pull the private IP out of each response entry.
    const ips: string[] = [];
    for (let i = 0; i < count; i++) {
      ips.push(lookup.getResponseField(`NetworkInterfaces.${i}.PrivateIpAddress`));
    }
    return ips;
  }

  /**
   * Injects the ALB Transforms `host-header-rewrite` onto a listener rule, and
   * swaps the plain host-header condition for a regex condition that captures the
   * prefix ahead of the base. The L2 ApplicationListenerRule can't model either
   * yet, so we reach the underlying CfnListenerRule and override its properties
   * directly.
   *
   * Verified against the CloudFormation reference for
   * AWS::ElasticLoadBalancingV2::ListenerRule (Transforms / RewriteConfig).
   */
  private applyHostRewrite(
    rule: elbv2.ApplicationListenerRule,
    customDomainBase: string,
    microvmEndpointBase: string,
  ): void {
    const cfnRule = rule.node.defaultChild as elbv2.CfnListenerRule;

    // Escape regex metacharacters in the (dotted) domain literals.
    const escapedBase = customDomainBase.replace(/[.]/g, '\\.');
    // Capture everything ahead of the base (the MicroVM prefix) and reuse it.
    const matchRegex = `^(.+)\\.${escapedBase}$`;
    const replaceWith = `$1.${microvmEndpointBase}`;

    // Regex host-header condition. ELBv2 requires EXACTLY ONE of Values /
    // RegexValues / HostHeaderConfig on a host-header condition, so we set only
    // RegexValues (the GA field for regex matching) — no HostHeaderConfig.
    cfnRule.conditions = [
      {
        field: 'host-header',
        regexValues: [matchRegex],
      },
    ];

    // Host-header rewrite transform.
    cfnRule.addPropertyOverride('Transforms', [
      {
        Type: 'host-header-rewrite',
        HostHeaderRewriteConfig: {
          Rewrites: [{ Regex: matchRegex, Replace: replaceWith }],
        },
      },
    ]);
  }
}
