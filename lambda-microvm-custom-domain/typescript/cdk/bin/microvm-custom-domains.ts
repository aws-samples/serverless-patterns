#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { MicroVmCustomDomainsStack, MicroVmCustomDomainsConfig } from '../lib/microvm-custom-domains-stack';
import { MicroVmDemoApp, MicroVmDemoAppProps } from '../lib/microvm-demo-app';

const app = new cdk.App();

// All configuration lives under the "microvm-custom-domains" key in cdk.json.
// Any value can be overridden on the CLI, e.g.:
//   npx cdk deploy -c microvm-custom-domains:hostedZoneId=Z123...
const cfg = (app.node.tryGetContext('microvm-custom-domains') ?? {}) as Partial<MicroVmCustomDomainsConfig> &
  Partial<Pick<MicroVmDemoAppProps, 'appDomain' | 'microvmImageArn'>> & {
    account?: string;
    region?: string;
  };

function required<T>(value: T | undefined | '', name: string): T {
  if (value === undefined || value === '' || value === 'REPLACE_WITH_HOSTED_ZONE_ID') {
    throw new Error(
      `Missing required config "${name}". Set it under the "microvm-custom-domains" key in cdk.json ` +
        `or pass -c microvm-custom-domains:${name}=<value>.`,
    );
  }
  return value;
}

const customDomainBase = required(cfg.customDomainBase, 'customDomainBase');
const microvmEndpointBase = required(cfg.microvmEndpointBase, 'microvmEndpointBase');

// The core, reusable networking pattern from the blog post: everything in the
// hot request path, and nothing else.
const stack = new MicroVmCustomDomainsStack(app, 'MicroVmCustomDomainsStack', {
  env: {
    account: cfg.account ?? process.env.CDK_DEFAULT_ACCOUNT,
    region: cfg.region ?? process.env.CDK_DEFAULT_REGION ?? 'us-east-2',
  },
  description:
    'Self-service custom domains for AWS Lambda MicroVMs via ALB Host-header rewrite over PrivateLink (no CloudFront, no request-path compute).',
  config: {
    hostedZoneId: required(cfg.hostedZoneId, 'hostedZoneId'),
    hostedZoneName: required(cfg.hostedZoneName, 'hostedZoneName'),
    customDomainBase,
    microvmEndpointBase,
    microvmVpceServiceName: required(cfg.microvmVpceServiceName, 'microvmVpceServiceName'),
    corsAllowOrigin: cfg.corsAllowOrigin ?? '*',
  },
});

// The OPTIONAL demo layer (single-page app + provisioning API), deployed
// together with the core stack by attaching to its HTTPS listener. Remove this
// block to deploy the pure networking pattern on its own.
new MicroVmDemoApp(stack, 'DemoApp', {
  listener: stack.httpsListener,
  appDomain: required(cfg.appDomain, 'appDomain'),
  microvmImageArn: required(cfg.microvmImageArn, 'microvmImageArn'),
  customDomainBase,
  microvmEndpointBase,
});

app.synth();
