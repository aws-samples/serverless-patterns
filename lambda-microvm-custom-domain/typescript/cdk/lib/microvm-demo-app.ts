import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as elbv2 from 'aws-cdk-lib/aws-elasticloadbalancingv2';
import * as elbv2t from 'aws-cdk-lib/aws-elasticloadbalancingv2-targets';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';
import * as path from 'path';

export interface MicroVmDemoAppProps {
  /**
   * The core stack's public HTTPS listener. The demo attaches a higher-priority
   * host rule here; it does not create its own ALB, certificate, or DNS record
   * (the demo host is a label under the wildcard base, so the core stack's
   * wildcard cert and Route 53 record already cover it).
   */
  readonly listener: elbv2.IApplicationListener;
  /**
   * The single hostname (a label under the wildcard base) that serves the demo
   * app: the static page AND its /api/provision endpoint, both from one
   * ALB-invoked Lambda, e.g. "customdomain.microvms.example.com".
   * A higher-priority listener rule matches this exact host BEFORE the core
   * stack's wildcard host-rewrite rule, so it is never rewritten to a MicroVM
   * origin.
   */
  readonly appDomain: string;
  /**
   * ARN of the MicroVM image the provisioning Lambda launches when no running
   * MicroVM is available, e.g.
   * "arn:aws:lambda:us-east-2:111122223333:microvm-image:my-microvm-image".
   */
  readonly microvmImageArn: string;
  /** Wildcard base, passed to the Lambda so it can build custom-domain URLs. */
  readonly customDomainBase: string;
  /** MicroVM endpoint base, passed to the Lambda so it can map <uuid> endpoints. */
  readonly microvmEndpointBase: string;
}

/**
 * OPTIONAL demo layer for the MicroVM custom-domains pattern, deployed alongside
 * {@link MicroVmCustomDomainsStack} and attached to its {@link
 * MicroVmCustomDomainsStack.httpsListener}. NOTHING here is in the hot request
 * path to a MicroVM — the browser calls the MicroVM's own custom domain
 * directly. This construct only makes the pattern easy to try end to end.
 *
 * One control-plane Lambda, invoked directly by the ALB (no Function URL),
 * serves BOTH the static demo page (GET /) and the provisioning endpoint
 * (POST /api/provision) under a dedicated host in the same wildcard. It reuses a
 * RUNNING MicroVM from the configured image (or runs a new one) and mints a
 * short-lived auth token.
 *
 * Not production-safe as written: the provisioning path is intentionally open
 * for demonstration. Put authentication and rate limiting in front of it, pin
 * CORS to your origin, and scope IAM to the minimum before adapting it.
 */
export class MicroVmDemoApp extends Construct {
  constructor(scope: Construct, id: string, props: MicroVmDemoAppProps) {
    super(scope, id);

    // Bundled with esbuild because the @aws-sdk/client-lambda-microvms client is
    // not in the Lambda runtime, and the demo HTML is inlined via a text loader.
    const provisionFn = new NodejsFunction(this, 'ProvisionFn', {
      runtime: lambda.Runtime.NODEJS_22_X,
      entry: path.join(__dirname, '..', 'lambda', 'provision.ts'),
      handler: 'handler',
      timeout: cdk.Duration.seconds(60),
      memorySize: 256,
      environment: {
        MICROVM_IMAGE_ARN: props.microvmImageArn,
        CUSTOM_DOMAIN_BASE: props.customDomainBase,
        MICROVM_ENDPOINT_BASE: props.microvmEndpointBase,
        TOKEN_TTL_MINUTES: '30',
        DEFAULT_PORT: '8080',
      },
      bundling: {
        // The lambda-microvms client is NOT in the Node runtime, so bundle all
        // deps (empty externalModules overrides the default that treats the v3
        // SDK as external).
        externalModules: [],
        // Inline frontend/index.html as a string import in the handler.
        loader: { '.html': 'text' },
      },
    });

    // Least-privilege: only the MicroVM control-plane actions the handler calls.
    // (IAM prefix is "lambda"; verified via the SDK's defaultSigningName.)
    //
    // RunMicrovm, GetMicrovm and CreateMicrovmAuthToken are all authorized on the
    // MicroVM *image* resource -- there is no per-MicroVM ARN in Lambda's IAM
    // model -- so the single image ARN is the tightest grant possible. Because the
    // ARN carries both, this also pins these actions to this account and Region.
    provisionFn.addToRolePolicy(
      new iam.PolicyStatement({
        actions: [
          'lambda:RunMicrovm',
          'lambda:GetMicrovm',
          'lambda:CreateMicrovmAuthToken',
        ],
        resources: [props.microvmImageArn],
      }),
    );

    // ListMicrovms is defined with no resource ARN in Lambda's IAM authorization
    // model, so it can only be granted on "*" -- a narrower ARN would match nothing
    // and deny the call. It is already implicitly account-scoped (the role can only
    // list MicroVMs in its own account); the demo calls it only to find a reusable
    // RUNNING MicroVM before launching a new one.
    provisionFn.addToRolePolicy(
      new iam.PolicyStatement({
        actions: ['lambda:ListMicrovms'],
        resources: ['*'],
      }),
    );

    // RunMicrovm implicitly attaches the AWS-managed default ingress/egress
    // network connectors, which requires lambda:PassNetworkConnector on those
    // managed connector ARNs (partition-owned, "aws" account).
    provisionFn.addToRolePolicy(
      new iam.PolicyStatement({
        actions: ['lambda:PassNetworkConnector'],
        resources: [
          `arn:${cdk.Aws.PARTITION}:lambda:${cdk.Aws.REGION}:aws:network-connector:aws-network-connector:*`,
        ],
      }),
    );

    // Register the Lambda as an ALB target. The ALB invokes it directly for the
    // demo host; there is no Function URL and no public Lambda endpoint. Health
    // checks are disabled: a Lambda target group's health check would call the
    // handler with an ELB probe, and we would rather not spin the provisioning
    // logic on every probe -- the target is healthy as long as the function
    // exists.
    const appTargetGroup = new elbv2.ApplicationTargetGroup(this, 'AppTargets', {
      targetType: elbv2.TargetType.LAMBDA,
      targets: [new elbv2t.LambdaTarget(provisionFn)],
      healthCheck: { enabled: false },
    });

    // Highest-priority rule: the exact demo host, forwarded to the Lambda. It
    // sits ABOVE the core stack's wildcard host-rewrite rule (priority 20), so
    // requests to the demo host are served by the Lambda and never rewritten to
    // a MicroVM origin. appDomain is a label under customDomainBase, so the
    // wildcard cert and wildcard Route 53 record already cover it.
    new elbv2.ApplicationListenerRule(this, 'AppHostRule', {
      listener: props.listener,
      priority: 5,
      conditions: [elbv2.ListenerCondition.hostHeaders([props.appDomain])],
      action: elbv2.ListenerAction.forward([appTargetGroup]),
    });

    // --- Output -----------------------------------------------------------
    new cdk.CfnOutput(this, 'DemoAppUrl', {
      value: `https://${props.appDomain}/`,
      description: 'Open this in a browser: the demo page and its /api/provision endpoint, same origin.',
    });
  }
}
