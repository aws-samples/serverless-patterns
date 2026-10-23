# Amazon ECS Gateway with a shared Application Load Balancer, AWS WAF and Amazon S3 access logs

This pattern creates an Amazon ECS Gateway and connects two AWS Fargate services to it. The gateway owns the ingress: ECS provisions one internet-facing Application Load Balancer, its listener, the certificates and a generated HTTPS hostname per service, and the template contains none of them. Each service opts in with a single `GatewayConnectors` entry. The platform-level settings (an AWS WAF web ACL, Amazon S3 access logs, the inbound security group and the load balancer limit) are set once on the gateway and apply to every service behind it.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/ecs-gateway-typescript-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources. AWS CloudFormation passes the infrastructure role to Amazon ECS, so the deploying identity needs `iam:PassRole` on that role (the AWS CDK deployment role has it).
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured. Use AWS CLI v2 version 2.38.3 or later: that is the first release whose changelog lists Amazon ECS Gateway. In a test, version 2.31.3 failed with `Found invalid choice` on `describe-gateway-resources` and printed `null` for the gateway connections of a service. The commands in Testing were run with version 2.38.5. Check yours with `aws --version`.
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node.js](https://nodejs.org/en/download/) 22 or later and npm installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/v2/guide/getting-started.html) (AWS CDK) installed and the target account and Region [bootstrapped](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html) with `npx cdk bootstrap`
* A Region where Amazon ECS Gateway is available. The [documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/gateway-overview.html) lists all commercial AWS Regions. The template contains no Region-specific values; it was tested in us-west-2.

## Architecture

```
Client (the range you allow, HTTPS 443)
   |
   v
AWS WAF web ACL (per-IP rate limit)
   |
   v
Application Load Balancer, created and shared by the Amazon ECS Gateway ----> access logs ----> Amazon S3
   |-- host rule: https://ec-<id>.ecs.<region>.on.aws ----> AWS Fargate service "orders"
   '-- host rule: https://ec-<id>.ecs.<region>.on.aws ----> AWS Fargate service "catalog"
```

## How it works

The stack creates the following resources:

* **Amazon ECS Gateway** (`AWS::ECS::Gateway`): a `HostSharedAlb` gateway with an internet-facing scheme (internal with `-c scheme=internal`), subnets in two Availability Zones, your own inbound security group, the web ACL, the access log bucket and at most two load balancers. `DeletionProtection` is `false` so that `cdk destroy` works (the default is `true`), and `PropagateTags` is `NONE` (see CDK notes). A second resource, `AWS::ECS::GatewayClusterAssociations`, makes the gateway available to the cluster.
* **Amazon ECS**: a cluster and two Fargate services (`orders` and `catalog`) that run the public `busybox` image from Amazon ECR Public and serve one static page each on a task definition port named `web`. Each service sets `GatewayConnectors` with `PortName: web`, a health check path and port, and an access type filter.
* **AWS WAF**: a regional web ACL with one rate-based rule that blocks a client IP address above 50 requests in a 60 second window.
* **Amazon S3**: a bucket for the load balancer access logs. It blocks public access, requires TLS, uses SSE-S3 (the only encryption that the load balancer access log documentation allows for the bucket) and expires objects after 7 days. The bucket policy lets the Elastic Load Balancing log delivery service write to one prefix, with `aws:SourceAccount` and `aws:SourceArn` conditions. The `aws:SourceArn` value covers any load balancer of the account in the Region (`loadbalancer/*`), because ECS creates the load balancer after the bucket policy and its name is not known at synthesis.
* **AWS IAM**: the infrastructure role that ECS assumes to create the load balancer, listener, security groups and certificates. It trusts `ecs.amazonaws.com` and has only the AWS managed policy `AmazonECSInfrastructureRoleForGatewayHostSharedALB`.
* **Amazon VPC**: two Availability Zones with public and private subnets and one NAT gateway, so the private tasks can pull the public image. The gateway must cover every Availability Zone that a service uses, which is why both use the same two.

What happens at deployment:

1. CloudFormation creates the bucket and its policy, the web ACL and the role, then the gateway, the cluster and the association.
1. The services depend on the association. When a service with a connector deploys, ECS selects the compatible gateway (same VPC, matching access type, all Availability Zones covered), creates the load balancer for the first service and reuses it for the second, and gives each service its own certificate, listener rule, target group and hostname.
1. A request goes to the shared load balancer, the web ACL evaluates it, and host-based routing sends it to the service that owns the hostname. Access logs are delivered to the bucket under the `alb/` prefix.

On `cdk destroy`, CloudFormation deletes the services first, then the association and the gateway. According to the Amazon ECS documentation, a route is removed when its service is deleted, an association stays in `DISASSOCIATING` until every route is gone, and a gateway can be deleted only when it has no association in `ACTIVE` or `DISASSOCIATING` state. These removals are asynchronous, so a deletion can report `DELETE_FAILED` while a managed resource is still being removed (see Cleanup).

## Important Notes

### Who can reach what

The gateway creates an **internet-facing** Application Load Balancer. That is what the feature does by default, so the pattern makes the client range an explicit input instead of a default:

* The stack refuses to synthesize until you pass `-c allowedCidr=<IPv4 CIDR>`. Use your own address as a `/32`. The value becomes the only inbound rule (HTTPS, port 443) of the gateway's security group. The stack checks that it is a valid IPv4 CIDR (octets 0 to 255, prefix 0 to 32) and rejects any range with a prefix shorter than `/8`, which includes every `/0` such as `0.0.0.0/0` or `1.2.3.4/0`, unless you also pass `-c allowAnyone=true`.
* The load balancer listens on HTTPS port 443 only. The generated hostnames (`https://ec-<id>.ecs.<region>.on.aws`) are random, but they are not secrets, so do not rely on them for access control.
* The Fargate tasks run in private subnets and accept port 8080 only from the gateway's security group.
* The sample containers are static pages with no authentication. For a real workload, add authentication in the application or in front of it.
* The AWS WAF web ACL adds a per-IP rate limit. It is a safeguard, not access control.

**Private alternative:** deploy with `-c scheme=internal`. The gateway then uses an internal load balancer in the private subnets, and the services filter on `PRIVATE`, so they never connect to an internet-facing gateway. Set `allowedCidr` to the range of the clients inside the VPC (for example the VPC CIDR `10.0.0.0/16`) and test from a host in that VPC. The scheme and the subnets cannot be changed on an existing gateway, so choose the scheme at the first deployment and run `cdk destroy` before you switch to the other one. In a test of this variant, both service connections had access type `PRIVATE`, the load balancer scheme was `internal`, and the generated hostnames resolved to private addresses (`10.0.x.x`). A one-off Fargate task in the VPC's private subnets got `hello from orders` and `hello from catalog` with HTTP 200 from both URLs and no answer on plain HTTP (port 80), and the same URL from outside the VPC did not answer.

### CDK notes

* `aws-cdk-lib` has no construct for the gateway yet, so the stack uses `cdk.CfnResource` for `AWS::ECS::Gateway` and `AWS::ECS::GatewayClusterAssociations`, and `addPropertyOverride('GatewayConnectors', ...)` on the L1 service. CloudFormation accepted the properties on deployment (the CDK validator does not know the new resource types yet). When `aws-cdk-lib` adds typed constructs for them, replace the escape hatches with those.
* The association refers to the gateway with `Fn::GetAtt` on the documented `Arn` attribute.
* `PropagateTags: NONE` on the gateway is needed when CloudFormation deploys it. With the default (`GATEWAY`), ECS copies the gateway's tags to the certificates it requests for each service. CloudFormation adds `aws:cloudformation:*` tags to the gateway, AWS Certificate Manager rejects tag keys that start with `aws:` (`InvalidTagException` in CloudTrail), and the services stay in `CREATE_IN_PROGRESS`. In one test run the stack was still creating after 40 minutes.
* The health check port of a gateway connector defaults to 80, not to the container port. With the container on 8080 the health checks timed out (`Target.Timeout`) and the targets kept flapping, so the connector sets `HealthCheckPort`.
* `cdk synth` prints a warning that the CloudFormation validator does not know the resource type `AWS::ECS::GatewayClusterAssociations`, which is new. The deployment is not affected.
* `autoDeleteObjects` on the log bucket adds a small CDK helper function that empties the bucket on `cdk destroy`. It is not in the request path.

### How this differs from the existing ALB patterns

[fargate-cdk](../../../fargate-cdk) and [apigw-fargate-cdk](../../../apigw-fargate-cdk) put an Application Load Balancer in front of Fargate with `ApplicationLoadBalancedFargateService`, and [route53-alb-fargate-cdk-dotnet](../../../route53-alb-fargate-cdk-dotnet) adds a custom domain and certificate. Here the load balancer, listener, target groups, certificates and hostnames are not in the template: the gateway resource owns them and shares one load balancer across the services.

### Cost

The gateway has no additional charge. You pay for the resources it creates and for the rest of the stack: the Application Load Balancer (hourly and per LCU, shared by both services), the NAT gateway (hourly plus data), the AWS WAF web ACL and rule, the two Fargate tasks, public IPv4 addresses, Amazon CloudWatch Logs and the S3 bucket. Several of these bill by the hour, so delete the stack when you finish.

## Deployment Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/ecs-gateway/typescript/cdk
    ```
2. Install the dependencies:
    ```
    npm install
    ```
3. Find the public IP address that your requests come from and keep it in a variable:
    ```
    MY_CIDR=$(curl -s https://checkip.amazonaws.com)/32
    echo $MY_CIDR
    ```
4. Deploy the stack:
    ```
    npx cdk deploy -c allowedCidr=$MY_CIDR
    ```
    The first deployment takes several minutes, because ECS creates the load balancer and certificates when the first service connects (6 to 7 minutes in test runs in us-west-2). IAM roles can take a short time to become usable. If the stack fails with a message that the `infrastructureRoleArn` could not be assumed, run the same command again.
5. Note the outputs from the deployment (gateway, cluster, service, web ACL and bucket names, and the allowed range). They are used for testing.

## Testing

Run the commands from the pattern directory in the Region you deployed to, from the machine whose address you passed as `allowedCidr`. For the internal variant, the AWS CLI commands work from anywhere with credentials, but the `curl` calls must run from a host inside the VPC, and the expected values differ: access type `PRIVATE` and load balancer scheme `internal`.

Input guard (optional, needs no AWS credentials). Expected: the first three commands fail with an error message and synthesize nothing, and the fourth succeeds:

```bash
npx cdk synth -c allowedCidr=1.2.3.4/0
npx cdk synth -c allowedCidr=999.999.999.999/99
npx cdk synth -c allowedCidr=0.0.0.0/0
npx cdk synth -c allowedCidr=203.0.113.7/32
```

1. Read the stack outputs into variables:
    ```bash
    STACK=EcsGatewayStack
    out() { aws cloudformation describe-stacks --stack-name $STACK --query "Stacks[0].Outputs[?OutputKey=='$1'].OutputValue" --output text; }
    GATEWAY=$(out GatewayName); CLUSTER=$(out ClusterName); BUCKET=$(out LogBucketName)
    S1=$(out ServiceNames | cut -d, -f1); S2=$(out ServiceNames | cut -d, -f2)
    ```
1. Wait until both services are stable. Expected: the command returns without output.
    ```bash
    aws ecs wait services-stable --cluster $CLUSTER --services $S1 $S2
    ```
1. Read the gateway connections of both services. Expected: each service has one connection with status `ACTIVE`, access type `PUBLIC` and its own `https://ec-<id>.ecs.<region>.on.aws` URL, and the two URLs differ. If a status is `CREATE_IN_PROGRESS`, run the loop again after a minute.
    ```bash
    for S in $S1 $S2; do
      REV=$(aws ecs list-service-deployments --cluster $CLUSTER --service $S --query "sort_by(serviceDeployments, &startedAt)[-1].targetServiceRevisionArn" --output text)
      aws ecs describe-service-revisions --service-revision-arns $REV --query "serviceRevisions[0].ecsManagedResources.gatewayConnections[].{url:serviceUrl,status:status,access:accessType}" --output table
    done
    ```
1. Call both URLs. Replace `ORDERS_URL` and `CATALOG_URL` with the two URLs from the previous step. Expected: `hello from orders` and `hello from catalog`.
    ```bash
    curl -s ORDERS_URL/
    curl -s CATALOG_URL/
    ```
1. Confirm that the two services share one load balancer. Expected: the output lists one load balancer that carries two gateway routes.
    ```bash
    aws ecs describe-gateway-resources --gateway $GATEWAY
    ```
1. Read the load balancer itself, not only the ECS view of it. Expected: the scheme is `internet-facing`, there is one HTTPS listener on port 443, the listener has one host-header rule per service (`forward`) and a default rule that returns a fixed response (it prints `None` as its host, because it has no condition), and the two target groups each have one `healthy` target on port 8080:
    ```bash
    ALB=$(aws ecs describe-gateway-resources --gateway $GATEWAY --query "gatewayResources.resources.hostSharedAlb[0].loadBalancerArn" --output text)
    aws elbv2 describe-load-balancers --load-balancer-arns $ALB --query "LoadBalancers[0].Scheme" --output text
    aws elbv2 describe-listeners --load-balancer-arn $ALB --query "Listeners[].[Port,Protocol]" --output text
    LISTENER=$(aws elbv2 describe-listeners --load-balancer-arn $ALB --query "Listeners[0].ListenerArn" --output text)
    aws elbv2 describe-rules --listener-arn $LISTENER --query "Rules[].[Priority,Conditions[0].Values[0],Actions[0].Type]" --output text
    for TG in $(aws elbv2 describe-target-groups --load-balancer-arn $ALB --query "TargetGroups[].TargetGroupArn" --output text); do
      aws elbv2 describe-target-health --target-group-arn $TG --query "TargetHealthDescriptions[].[Target.Port,TargetHealth.State]" --output text
    done
    ```
1. Trigger the rate limit. Expected: the first requests return `200`, and once the client IP address is above 50 requests in the 60 second window, WAF returns `403`. WAF rate-based rules react after a short delay, so run the command again if the first run shows only `200`. In two test runs from one client address, 69 and 67 of the 200 requests returned `200` and the rest returned `403`, and requests returned `200` again 75 seconds after the burst.
    ```bash
    for i in $(seq 1 200); do curl -s -o /dev/null -w "%{http_code}\n" ORDERS_URL/; done | sort | uniq -c
    ```
1. Check the access logs. The load balancer delivers log files about every five minutes. Expected: objects under `alb/AWSLogs/<account-id>/elasticloadbalancing/` (plus a small `ELBAccessLogTestFile` that Elastic Load Balancing writes when it enables logging), and, in the second command, a count of the log records per service URL that you called (if it prints an error or nothing, no log file has been delivered yet: wait a few minutes and run it again):
    ```bash
    aws s3 ls s3://$BUCKET/alb/AWSLogs/ --recursive | head
    for KEY in $(aws s3api list-objects-v2 --bucket $BUCKET --prefix alb/AWSLogs/ --query "Contents[?ends_with(Key, '.log.gz')].Key" --output text); do
      aws s3 cp s3://$BUCKET/$KEY - | gunzip
    done | grep -o 'https://ec-[a-z0-9]*\.ecs\.[a-z0-9-]*\.on\.aws' | sort | uniq -c
    ```

Logs and metrics: the containers write to two Amazon CloudWatch Logs log groups (retention one week, created by the stack), the load balancer writes access logs to the bucket, and the web ACL publishes the `ecs-gateway` and `rate-limit-per-ip` metrics to CloudWatch.

## Cleanup

1. Delete the stack. This also deletes the access log bucket with the logs in it. The app refuses to synthesize without `allowedCidr`, so the command needs a value even though destroy does not use it: any valid CIDR with a prefix of /8 or longer works, and the variable from the deployment step is not needed (it is empty in a new shell). Confirm the prompt, or add `--force`:
    ```bash
    npx cdk destroy -c allowedCidr=203.0.113.7/32
    ```
    If you deployed the internal variant, add `-c scheme=internal` so the command matches the deployment. ECS removes the managed load balancer and its security groups after the services are gone, so the deletion takes several minutes (9 to 10 minutes in test runs). If the stack ends in `DELETE_FAILED` because a managed resource (the gateway association, a security group or the log bucket) is still being removed, wait a few minutes and run the same command again, and check the stack events for the resource that failed. If a deployment stays in `CREATE_IN_PROGRESS` for much longer than the 6 to 7 minutes above, `aws cloudformation delete-stack --stack-name EcsGatewayStack` also works on a stack in that state, and the stack events name the resource that is waiting.
1. Confirm the stack has been deleted:
    ```bash
    aws cloudformation describe-stacks --stack-name EcsGatewayStack
    ```
    Expected: an error that the stack does not exist.

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
