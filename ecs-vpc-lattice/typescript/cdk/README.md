# Amazon ECS blue/green deployments with Amazon VPC Lattice

This pattern deploys an Amazon ECS on AWS Fargate service that uses the built-in blue/green deployment strategy with Amazon VPC Lattice as the traffic layer. An AWS Lambda lifecycle hook tests the new (green) revision through a VPC Lattice test listener rule before production traffic shifts, and Amazon CloudWatch alarms roll the deployment back automatically.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured. Use a recent version, because the Amazon ECS service deployment commands used in Testing are new.
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node.js](https://nodejs.org/en/download/) 22 or later and npm installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/v2/guide/getting-started.html) (AWS CDK) installed and the target account and Region [bootstrapped](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html)

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/ecs-vpc-lattice/typescript/cdk
    ```
1. Install the dependencies:
    ```
    npm install
    ```
1. Look up the ID of the VPC Lattice managed prefix list in your Region (see [Security group source for VPC Lattice](#security-group-source-for-vpc-lattice)). Use the Region you deploy to. The command prints an ID that starts with `pl-`:
    ```
    REGION=${AWS_REGION:-$(aws configure get region)}
    PL=$(aws ec2 describe-managed-prefix-lists --region $REGION --filters "Name=prefix-list-name,Values=com.amazonaws.$REGION.vpc-lattice" --query "PrefixLists[0].PrefixListId" --output text)
    echo $PL
    ```
1. Deploy the stack. This deploys version `v1` of the app:
    ```
    npx cdk deploy --parameters LatticePrefixListId=$PL
    ```
1. Note the outputs from the deployment (cluster, service, hook function and log group names, and the VPC Lattice service, listener and rule IDs). They are used for testing.

## How it works

The stack creates the following resources:

* **Amazon ECS**: a Fargate service with `deploymentStrategy: BLUE_GREEN` running the public `busybox` image from Amazon ECR Public (nothing to build). The container serves `{"version":"<appVersion>"}` on port 8080, where `appVersion` comes from CDK context (default `v1`).
* **Amazon VPC Lattice**: a service network associated with the VPC, one service with an HTTP listener on port 80, two IP target groups (blue and green) and two listener rules. The test rule matches the header `x-environment: test`; the production rule matches every other request. Both rules start at blue 100 / green 0.
* **AWS Lambda**: a lifecycle hook (`lambda/hook.js`) in the stack's private isolated subnets, with no NAT gateway. It runs at the `POST_TEST_TRAFFIC_SHIFT` stage.
* **Amazon CloudWatch**: one alarm per Availability Zone on the `HTTPCode_5XX_Count` metric of the VPC Lattice service (VPC Lattice publishes its service metrics per Availability Zone, and an alarm only matches an exact set of dimensions). ECS watches the alarms during the deployment and rolls back if one fires.

A VPC with public and isolated subnets, security groups and an ECS infrastructure IAM role (the AWS managed policy `AmazonECSInfrastructureRolePolicyForVpcLattice`) complete the stack.

When you run `npx cdk deploy -c appVersion=v2` (with the same `--parameters` option as the first deployment), the task definition changes and ECS starts a blue/green deployment:

1. ECS starts the green tasks and registers them in the alternate VPC Lattice target group.
1. ECS edits the weights of the **test** listener rule so that requests with `x-environment: test` go to green. Production still goes to blue.
1. At `POST_TEST_TRAFFIC_SHIFT`, ECS invokes the hook Lambda. ECS passes `hookDetails` (the VPC Lattice service URL and the expected version, set in the service configuration) in the event. The function sends `GET` with the `x-environment: test` header to the VPC Lattice DNS name from inside the VPC. If it receives HTTP 200 and the expected version, it returns `{"hookStatus":"SUCCEEDED"}`. Otherwise (after five attempts) it returns `FAILED` with a reason and ECS rolls back.
1. ECS edits the weights of the **production** listener rule (100% to green), waits for the bake time, then stops the blue tasks. If one of the CloudWatch alarms fires during the deployment, ECS rolls back to blue.

### What is new compared with the ALB-based design

ECS blue/green with a Lambda lifecycle hook that tests the green revision through a test listener is already shown publicly with an Application Load Balancer, for example in [aws-reinvent-trivia-game](https://github.com/aws-samples/aws-reinvent-trivia-game/blob/master/trivia-backend/cdk/ecs-service-blue-green.ts). This pattern does not change that idea. What it adds is the VPC Lattice wiring, announced on 2026-10-02 ([What's New](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-ecs-vpc-lattice-blue-green-deployments)):

* The two listeners and target groups of the ALB design are replaced by one VPC Lattice listener with a **test rule** (header match) and a **production rule**, and by two VPC Lattice IP target groups that ECS registers tasks into.
* The service is configured through `vpcLatticeConfigurations` with an `advancedConfiguration` (alternate target group, production and test listener rule ARNs) and an ECS infrastructure role, instead of `loadBalancers`.
* The hook reaches the test endpoint through the VPC Lattice service network association and the service DNS name, with no load balancer and no NAT gateway.
* Task security groups allow VPC Lattice (not an ALB security group) to reach the tasks.

CDK notes: the `aws-cdk-lib` L2 `FargateService` does not expose VPC Lattice yet, so `vpcLatticeConfigurations` is set on the L1 `CfnService`, and `HookDetails` and `TimeoutConfiguration` of the lifecycle hook are added with `addPropertyOverride`.

### Security group source for VPC Lattice

VPC Lattice reaches the tasks, and runs its health checks, from the addresses in its managed prefix list `com.amazonaws.<region>.vpc-lattice` (the [VPC Lattice documentation](https://docs.aws.amazon.com/vpc-lattice/latest/ug/security-groups.html) describes them as private link-local addresses and non-routable public addresses and recommends referencing the prefix list ID in the target security group). The task security group therefore allows port 8080 from that prefix list. The ID is different in every Region, so the stack takes it as the `LatticePrefixListId` parameter and the Deployment Instructions look it up with the AWS CLI.

## Testing

All commands run from the pattern directory. They assume the stack name `EcsVpcLatticeBlueGreenStack` and the AWS Region that you deployed to.

1. Read the stack outputs into variables:
    ```bash
    STACK=EcsVpcLatticeBlueGreenStack
    out() { aws cloudformation describe-stacks --stack-name $STACK --query "Stacks[0].Outputs[?OutputKey=='$1'].OutputValue" --output text; }
    CLUSTER=$(out ClusterName); SERVICE=$(out ServiceName); FN=$(out HookFunctionName); LOGS=$(out HookLogGroupName)
    SVC=$(out LatticeServiceId); LISTENER=$(out LatticeListenerId); PROD_RULE=$(out ProductionRuleId); DNS=$(out LatticeServiceDnsName)
    REGION=${AWS_REGION:-$(aws configure get region)}
    PL=$(aws ec2 describe-managed-prefix-lists --region $REGION --filters "Name=prefix-list-name,Values=com.amazonaws.$REGION.vpc-lattice" --query "PrefixLists[0].PrefixListId" --output text)
    ```
1. Check the first deployment. Expected: the service has one running task and one service deployment with status `SUCCESSFUL`.
    ```bash
    aws ecs describe-services --cluster $CLUSTER --services $SERVICE --query "services[0].{running:runningCount,desired:desiredCount,deployments:deployments[].{status:status}}"
    aws ecs list-service-deployments --cluster $CLUSTER --service $SERVICE --query "sort_by(serviceDeployments, &startedAt)[].{status:status,startedAt:startedAt}"
    ```
1. Note the production rule weights. Expected: one target group at 100 and the other at 0.
    ```bash
    aws vpc-lattice get-rule --service-identifier $SVC --listener-identifier $LISTENER --rule-identifier $PROD_RULE --query "action.forward.targetGroups[].[targetGroupIdentifier,weight]" --output text
    ```
1. Call the service from inside the VPC. VPC Lattice DNS names resolve only inside the associated VPC, so invoke the hook function with a manual event and read its log tail. Expected: the production observation reports `"observedVersion":"v1"` and the function returns `SUCCEEDED`.
    ```bash
    aws lambda invoke --function-name $FN --cli-binary-format raw-in-base64-out \
      --payload "{\"lifecycleStage\":\"MANUAL\",\"hookDetails\":{\"url\":\"http://$DNS/\",\"expectedVersion\":\"v1\"}}" \
      --log-type Tail --query LogResult --output text /tmp/hook-out.json | base64 --decode
    cat /tmp/hook-out.json
    ```
1. Start the second (blue/green) deployment:
    ```bash
    npx cdk deploy --parameters LatticePrefixListId=$PL -c appVersion=v2
    ```
1. While it runs, in another terminal watch the lifecycle stage and the production rule weights. Expected: the lifecycle stage advances through the blue/green stages described in the [ECS documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-blue-green.html) (the hook runs at `POST_TEST_TRAFFIC_SHIFT`), and at the end the weights have swapped (the target group that had 0 now has 100):
    ```bash
    ARN=$(aws ecs list-service-deployments --cluster $CLUSTER --service $SERVICE --query "sort_by(serviceDeployments, &startedAt)[-1].serviceDeploymentArn" --output text)
    aws ecs describe-service-deployments --service-deployment-arns $ARN --query "serviceDeployments[0].{status:status,stage:lifecycleStage,hooks:lifecycleHookDetails}"
    aws vpc-lattice get-rule --service-identifier $SVC --listener-identifier $LISTENER --rule-identifier $PROD_RULE --query "action.forward.targetGroups[].[targetGroupIdentifier,weight]" --output text
    ```
1. After `cdk deploy` returns, read the hook logs. Expected: a `hook-invoked` line with the stage `POST_TEST_TRAFFIC_SHIFT`, a `test-listener-probe` line with `"observedVersion":"v2"` and `"status":200`, and a `hook-result` line with `"hookStatus":"SUCCEEDED"`:
    ```bash
    aws logs filter-log-events --log-group-name $LOGS --query "events[].message" --output text
    ```
1. Confirm the deployment result. Expected: the most recently started service deployment is `SUCCESSFUL`.
    ```bash
    aws ecs list-service-deployments --cluster $CLUSTER --service $SERVICE --query "sort_by(serviceDeployments, &startedAt)[-1].status" --output text
    ```
1. Repeat the in-VPC call from step 4 with `expectedVersion` `v2`. Expected: the production observation now reports `v2`. With `expectedVersion` `v9` the function retries five times (about 20 seconds) and returns `FAILED` with a reason, which is what makes ECS roll back a bad revision.

## Cleanup

1. Delete the stack:
    ```bash
    npx cdk destroy
    ```
1. Confirm the stack has been deleted:
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'EcsVpcLatticeBlueGreenStack')].StackStatus"
    ```
    The output shows `DELETE_COMPLETE` for the stack. Deleting the stack took between 8 and 30 minutes in my tests; most of that time is CloudFormation waiting for the VPC-attached hook function to be deleted.

To run the hook logic locally without AWS: `npm test`.

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
