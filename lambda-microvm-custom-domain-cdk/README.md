# Custom domains for AWS Lambda MicroVMs with Application Load Balancer

This pattern gives each of your [AWS Lambda MicroVMs](https://docs.aws.amazon.com/lambda/latest/dg/lambda-microvms-guide.html) a domain **you** own — e.g. `92cfc7f9-….microvms.example.com` — instead of exposing the service-generated `92cfc7f9-….lambda-microvm-….on.aws` endpoint directly.

It is built entirely from load-balancing and networking primitives: **no CloudFront** and **no compute in the request path** — just an Application Load Balancer (ALB) that rewrites the `Host` header with an [ALB Host header rewrite](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-url-and-host-header-rewrite-with-aws-application-load-balancers/) and forwards to the MicroVM service over AWS PrivateLink. A wildcard ACM certificate and a Route 53 wildcard record cover every MicroVM id under a single base domain.

The CDK app is split into two parts, deployed together as one stack:
- **`lib/microvm-custom-domains-stack.ts`** — the reusable core pattern (VPC, interface VPC endpoint, ACM cert, ALB, host-rewrite listener rule, Route 53 wildcard record). This is the only part in the request path.
- **`lib/microvm-demo-app.ts`** — an *optional* demo layer (a single-page app plus an unauthenticated provisioning API on one ALB-invoked Lambda) that makes the pattern easy to try. Remove the `new MicroVmDemoApp(...)` block from `bin/microvm-custom-domains.ts` to deploy the pure networking pattern on its own.

Learn more about this pattern at [Serverless Land Patterns](https://serverlessland.com/patterns/lambda-microvm-custom-domain-cdk).

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

> ⚠️ **The optional demo layer is DEMO ONLY — NOT PRODUCTION-SAFE.** Its `POST /api/provision` endpoint is completely unauthenticated, it returns auth tokens to the browser, and it uses wide-open CORS (`Access-Control-Allow-Origin: *`). The **core pattern** (`MicroVmCustomDomainsStack`) is production-oriented networking, but before deploying the demo layer, put real authentication in front of the provisioning API, pin CORS to your own origin, and scope IAM and tokens to the minimum. Deploy the demo only in an isolated, non-production account.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured.
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
* [Node.js 18+](https://nodejs.org/en/download/) and [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) installed (`npx cdk` works; no global install required).
* An **existing Amazon Route 53 public hosted zone** for your domain (e.g. `example.com`). This stack imports it and adds a wildcard record.
* Access to [AWS Lambda MicroVMs](https://docs.aws.amazon.com/lambda/latest/dg/lambda-microvms-guide.html) and its regional PrivateLink service (`com.amazonaws.<region>.lambda-microvm`) in your target Region.
* The **ALB Host/URL rewrite (Transforms) feature** available in your account/Region.

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd serverless-patterns/lambda-microvm-custom-domain-cdk
    ```
3. Install dependencies:
    ```
    npm install
    ```
4. Edit the configuration under the `microvm-custom-domains` key in [`cdk.json`](./cdk.json). At minimum set `account`, `region`, `hostedZoneId`, `hostedZoneName`, `customDomainBase`, `microvmEndpointBase`, and `microvmVpceServiceName`. (The `microvmImageArn` and `appDomain` keys are only needed if you keep the optional demo layer.)

    | Key | Meaning |
    | --- | --- |
    | `account` / `region` | Where to deploy. Region **must** match the MicroVM PrivateLink service region (PrivateLink is regional). |
    | `hostedZoneId` / `hostedZoneName` | Your existing Route 53 public hosted zone. |
    | `customDomainBase` | Wildcard base your clients use, e.g. `microvms.example.com`. |
    | `microvmEndpointBase` | What `Host` is rewritten **to**, e.g. `lambda-microvm.us-east-2.on.aws`. Everything ahead of this suffix (the MicroVM id, and any future subdomains) is preserved per request. |
    | `microvmVpceServiceName` | AWS-managed PrivateLink service, e.g. `com.amazonaws.us-east-2.lambda-microvm`. |
    | `corsAllowOrigin` | Value for the `Access-Control-Allow-Origin` header the ALB inserts (`*` for the demo; pin to your origin otherwise). |
    | `microvmImageArn` | **Demo only.** MicroVM image the provisioning Lambda launches when no running MicroVM is available. |
    | `appDomain` | **Demo only.** Single host under `customDomainBase` that serves the demo page and its `/api/provision` endpoint. |

5. From the command line, deploy the AWS resources for the pattern:
    ```
    npx cdk deploy
    ```
    Note the outputs — `WildcardDomain`, `AlbDnsName`, `CertificateArn`, and (with the demo layer) `DemoAppUrl`.

## How it works

A client sends an HTTPS request to `https://<uuid>.microvms.example.com` (plus the MicroVM `X-aws-proxy-auth` / `X-aws-proxy-port` headers). Route 53 resolves the wildcard record to the ALB. The ALB terminates TLS with a wildcard ACM certificate, then a listener rule:

1. **matches** the incoming host with a regex condition — `^(.+)\.microvms\.example\.com$` — capturing everything ahead of the base domain suffix;
2. **rewrites** the `Host` header with a `host-header-rewrite` Transform — `$1.lambda-microvm.<region>.on.aws` — swapping only the suffix and preserving everything before it;
3. **forwards** to an IP target group whose targets are the private ENI IPs of a MicroVM interface VPC endpoint (discovered at deploy time by an `AwsCustomResource`; this is the only Lambda in the package and it never runs in the request path).

The request reaches the MicroVM service front-end over PrivateLink, which routes to the correct MicroVM using the rewritten `Host` header and enforces the JWE auth token the client supplied. Because a Transform (not a redirect) performs the rewrite, the customer's domain stays intact end to end — the browser address bar never shows the `.on.aws` URL.

CORS is handled entirely at the ALB: `OPTIONS` preflights are answered with a fast `204`, and `Access-Control-Allow-*` headers are inserted on every response via ALB listener header-modification attributes — no change to the application inside the MicroVM.

See the source files and code comments for full detail on health-check matchers (`200,403,404`), TLS re-origination, and the optional demo layer.

## Testing

The `WildcardDomain` output shows the base domain. Derive a MicroVM's custom domain by taking its service-generated endpoint and **swapping the suffix** — replace `.lambda-microvm.<region>.on.aws` with your `.microvms.example.com` base, keeping everything ahead of the suffix. For example:

```
78d01d43-96e8-b9f7-49cf-f152af2532af.lambda-microvm.us-east-2.on.aws
                                     ─────────────── swap suffix ──────────────►
78d01d43-96e8-b9f7-49cf-f152af2532af.microvms.example.com
```

Then call the MicroVM through your custom domain, supplying the auth token and port from `create-microvm-auth-token`:

```
curl "https://78d01d43-96e8-b9f7-49cf-f152af2532af.microvms.example.com/" \
  -H "X-aws-proxy-auth: <JWE-auth-token>" \
  -H "X-aws-proxy-port: 8080"
```

A missing or expired token returns `403 Forbidden` — the ALB only rewrites `Host`; the client still supplies the token. If you deployed the optional demo layer, open the `DemoAppUrl` output in a browser to provision a MicroVM and call it end to end from a single page.

## Cleanup

1. Delete the stack:
    ```
    npx cdk destroy
    ```

----
Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
