import * as cdk from 'aws-cdk-lib';
import { Template, Match } from 'aws-cdk-lib/assertions';
import { MicroVmCustomDomainsStack, MicroVmCustomDomainsConfig } from '../lib/microvm-custom-domains-stack';
import { MicroVmDemoApp } from '../lib/microvm-demo-app';

// The full config the app accepts: the core-stack fields plus the two
// demo-only fields (appDomain, microvmImageArn) consumed by MicroVmDemoApp.
type FullConfig = MicroVmCustomDomainsConfig & {
  microvmImageArn: string;
  appDomain: string;
};

const config: FullConfig = {
  hostedZoneId: 'Z0123456789ABCDEFGHIJ',
  hostedZoneName: 'example.com',
  customDomainBase: 'microvms.example.com',
  microvmEndpointBase: 'lambda-microvm.us-east-2.on.aws',
  microvmVpceServiceName: 'com.amazonaws.us-east-2.lambda-microvm',
  corsAllowOrigin: '*',
  microvmImageArn: 'arn:aws:lambda:us-east-2:111122223333:microvm-image:my-microvm-image',
  appDomain: 'customdomain.microvms.example.com',
};

// Synthesizes the core stack WITH the demo layer attached, exactly as bin/ wires
// them, so a single Template covers both files' resources.
function synth(overrides: Partial<FullConfig> = {}): Template {
  const c = { ...config, ...overrides };
  const app = new cdk.App();
  const stack = new MicroVmCustomDomainsStack(app, 'TestStack', {
    env: { account: '111122223333', region: 'us-east-2' },
    config: {
      hostedZoneId: c.hostedZoneId,
      hostedZoneName: c.hostedZoneName,
      customDomainBase: c.customDomainBase,
      microvmEndpointBase: c.microvmEndpointBase,
      microvmVpceServiceName: c.microvmVpceServiceName,
      corsAllowOrigin: c.corsAllowOrigin,
    },
  });
  new MicroVmDemoApp(stack, 'DemoApp', {
    listener: stack.httpsListener,
    appDomain: c.appDomain,
    microvmImageArn: c.microvmImageArn,
    customDomainBase: c.customDomainBase,
    microvmEndpointBase: c.microvmEndpointBase,
  });
  return Template.fromStack(stack);
}

describe('MicroVmCustomDomainsStack', () => {
  test('provisions an internet-facing ALB', () => {
    const t = synth();
    t.hasResourceProperties('AWS::ElasticLoadBalancingV2::LoadBalancer', {
      Scheme: 'internet-facing',
      Type: 'application',
    });
  });

  test('creates a wildcard ACM certificate for the custom domain base', () => {
    const t = synth();
    t.hasResourceProperties('AWS::CertificateManager::Certificate', {
      DomainName: '*.microvms.example.com',
    });
  });

  test('creates an interface endpoint to the MicroVM PrivateLink service', () => {
    const t = synth();
    t.hasResourceProperties('AWS::EC2::VPCEndpoint', {
      ServiceName: 'com.amazonaws.us-east-2.lambda-microvm',
      VpcEndpointType: 'Interface',
      PrivateDnsEnabled: false,
    });
  });

  test('target group speaks HTTPS to IP targets with a permissive health matcher', () => {
    const t = synth();
    t.hasResourceProperties('AWS::ElasticLoadBalancingV2::TargetGroup', {
      Protocol: 'HTTPS',
      Port: 443,
      TargetType: 'ip',
      Matcher: { HttpCode: '200,403,404' },
    });
  });

  test('forwarding rule rewrites the Host header via a Transform with a capture group', () => {
    const t = synth();
    t.hasResourceProperties('AWS::ElasticLoadBalancingV2::ListenerRule', {
      Transforms: [
        {
          Type: 'host-header-rewrite',
          HostHeaderRewriteConfig: {
            Rewrites: [
              {
                Regex: '^(.+)\\.microvms\\.example\\.com$',
                Replace: '$1.lambda-microvm.us-east-2.on.aws',
              },
            ],
          },
        },
      ],
    });
  });

  test('forwarding rule matches the host with a regex condition', () => {
    const t = synth();
    t.hasResourceProperties('AWS::ElasticLoadBalancingV2::ListenerRule', {
      Conditions: Match.arrayWith([
        Match.objectLike({
          Field: 'host-header',
          RegexValues: ['^(.+)\\.microvms\\.example\\.com$'],
        }),
      ]),
    });
  });

  test('answers OPTIONS preflight with a fixed 204 ahead of forwarding', () => {
    const t = synth();
    t.hasResourceProperties('AWS::ElasticLoadBalancingV2::ListenerRule', {
      Priority: 10,
      Actions: Match.arrayWith([
        Match.objectLike({
          Type: 'fixed-response',
          FixedResponseConfig: Match.objectLike({ StatusCode: '204' }),
        }),
      ]),
    });
  });

  test('creates a wildcard Route53 alias to the ALB', () => {
    const t = synth();
    t.hasResourceProperties('AWS::Route53::RecordSet', {
      Type: 'A',
      Name: '*.microvms.example.com.',
    });
  });

  test('a deploy-time IP-discovery custom resource is created', () => {
    const t = synth();
    // AwsCustomResource renders as a Custom::AWS resource.
    t.resourceCountIs('Custom::AWS', 1);
    t.hasResourceProperties('AWS::IAM::Policy', {
      PolicyDocument: {
        Statement: Match.arrayWith([
          Match.objectLike({ Action: 'ec2:DescribeNetworkInterfaces' }),
        ]),
      },
    });
  });

  test('inserts CORS response headers on the HTTPS listener', () => {
    const t = synth();
    t.hasResourceProperties('AWS::ElasticLoadBalancingV2::Listener', {
      ListenerAttributes: Match.arrayWith([
        Match.objectLike({
          Key: 'routing.http.response.access_control_allow_origin.header_value',
          Value: '*',
        }),
        Match.objectLike({
          Key: 'routing.http.response.access_control_allow_headers.header_value',
          Value: Match.stringLikeRegexp('x-aws-proxy-auth'),
        }),
      ]),
    });
  });

  test('creates the provisioning Lambda with the image ARN and least-privilege MicroVM permissions', () => {
    const t = synth();
    t.hasResourceProperties('AWS::Lambda::Function', {
      Environment: {
        Variables: Match.objectLike({
          MICROVM_IMAGE_ARN: 'arn:aws:lambda:us-east-2:111122223333:microvm-image:my-microvm-image',
        }),
      },
    });
    t.hasResourceProperties('AWS::IAM::Policy', {
      PolicyDocument: {
        Statement: Match.arrayWith([
          Match.objectLike({
            Action: Match.arrayWith([
              'lambda:RunMicrovm',
              'lambda:ListMicrovms',
              'lambda:GetMicrovm',
              'lambda:CreateMicrovmAuthToken',
            ]),
          }),
        ]),
      },
    });
  });

  test('serves the demo app as an ALB Lambda target (no Function URL)', () => {
    const t = synth();
    // The Lambda is registered as an ALB target group, not exposed via a URL.
    t.hasResourceProperties('AWS::ElasticLoadBalancingV2::TargetGroup', {
      TargetType: 'lambda',
    });
    t.resourceCountIs('AWS::Lambda::Url', 0);
  });

  test('routes the demo host to the app target ahead of the host-rewrite rule', () => {
    const t = synth();
    t.hasResourceProperties('AWS::ElasticLoadBalancingV2::ListenerRule', {
      Priority: 5,
      Conditions: Match.arrayWith([
        Match.objectLike({
          Field: 'host-header',
          HostHeaderConfig: { Values: ['customdomain.microvms.example.com'] },
        }),
      ]),
    });
  });
});
