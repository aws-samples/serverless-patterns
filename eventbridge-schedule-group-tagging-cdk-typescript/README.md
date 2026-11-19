# Amazon EventBridge Scheduler schedule groups with tagging to Amazon SQS

This pattern demonstrates best practices for organizing and governing Amazon EventBridge Scheduler schedules using **schedule groups** and **tags**. Instead of placing every schedule in the account's built-in `default` group, it creates a dedicated, purpose-named schedule group, tags that group at creation time, and places two schedules in it that follow an intentional, prefix-friendly naming convention. Both schedules send a message to a single Amazon SQS queue through a least-privilege IAM role. The pattern is deployed using the AWS Cloud Development Kit (AWS CDK) for TypeScript.

Learn more about this pattern at Serverless Land Patterns: [eventbridge-schedule-group-tagging-cdk-typescript](https://serverlessland.com/patterns/eventbridge-schedule-group-tagging-cdk-typescript) 

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) (AWS CDK) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd eventbridge-schedule-group-tagging-cdk-typescript
    ```
1. Install the project dependencies:
    ```
    npm install
    ```
1. Deploy the stack to your default AWS account and Region. The default tag values and name prefix can be overridden with CDK context (see below):
    ```
    cdk deploy
    ```
1. To override the defaults, pass context values on deploy, for example:
    ```
    cdk deploy -c environment=staging -c owner=orders-team -c costCenter=cc-5678 -c application=orders
    ```
    The `environment` and `application` values populate the schedule group name and the schedule name prefix; `owner` and `costCenter` populate the group's `owner` and `cost-center` tags.

1. Note the outputs from the CDK deployment process. These contain the schedule group name and ARN, the queue URL, the scheduler role ARN, and the schedule name prefix, which are used for testing.

## How it works

Amazon EventBridge Scheduler uses **schedule groups** as the resource for organizing schedules. Every account starts with a built-in `default` group, and you can create up to 500 groups per account. This pattern creates one purpose-named group (for example `payments-production`) instead of dumping schedules into `default`, which keeps related schedules grouped for discovery, governance, and lifecycle management.

**Tags are applied to the group, not to individual schedules.** The stack tags the group with four consistent keys at creation time:

* `environment`
* `owner`
* `cost-center`
* `application`

Tagging at creation time (the `tags` property on the `CfnScheduleGroup` construct) means there is never a window where the group exists untagged. These tags can be activated as cost allocation tags in the Billing console to attribute cost, and used with the Resource Groups Tagging API for inventory.

**Tag matching is exact; the schedule name prefix is the native partial-match lever.** There is no wildcard or substring tag search anywhere in AWS - the Resource Groups Tagging API and Resource Groups queries match an exact key against an exact list of values. EventBridge Scheduler's own `ListSchedules` and `ListScheduleGroups` APIs do not filter by tag at all; they filter by `NamePrefix`. For that reason the two schedules are named with an intentional, sliceable convention (`<application>-<environment>-<task>`, for example `payments-production-invoice-sweep`). Operators can then list every schedule for a domain or environment straight from the Scheduler API or CLI with a `NamePrefix`, while the group's tags carry governance and cost-allocation metadata. The naming convention and the tags are complementary, not redundant. Because tag matching is exact, the tag taxonomy must be deliberate and uniform up front - `prod` versus `production` cannot be reconciled with a later wildcard search.

Each schedule runs its target call under a **least-privilege IAM role** that the scheduler service assumes. The role allows only `sqs:SendMessage` on the single target queue ARN and trusts only `scheduler.amazonaws.com`. Flexible time windows are explicitly disabled (`mode: 'OFF'`) for deterministic invocation.

**Do not put personally identifiable information (PII) or other sensitive data in tags.** Tags are visible to many AWS services, including billing, so they are not an appropriate place for secrets or personal data.

**Group deletion cascades.** Deleting a schedule group removes every schedule it contains, which makes the group the natural unit for lifecycle management and cleanup.

The pattern deploys one EventBridge Scheduler schedule group, two schedules, one Amazon SQS queue, and one IAM role.

## Testing

After the stack is successfully deployed, use the outputs to confirm the organization and tagging.

1. Confirm the group carries the four tags (replace `<ScheduleGroupArn>` with the stack output):
    ```bash
    aws scheduler list-tags-for-resource --resource-arn <ScheduleGroupArn>
    ```
1. Confirm both schedules live in the group (replace `<ScheduleGroupName>` with the stack output):
    ```bash
    aws scheduler list-schedules --group-name <ScheduleGroupName>
    ```
1. Confirm the name prefix slices the schedules the way the convention intends (replace `<ScheduleNamePrefix>` with the stack output, for example `payments-production-`):
    ```bash
    aws scheduler list-schedules --group-name <ScheduleGroupName> --name-prefix <ScheduleNamePrefix>
    ```
1. Confirm messages are being enqueued by checking the target queue (replace `<TargetQueueUrl>` with the stack output). The first message arrives within five minutes of deployment:
    ```bash
    aws sqs get-queue-attributes --queue-url <TargetQueueUrl> --attribute-names ApproximateNumberOfMessagesVisible
    ```
    You can also read a message to see its `{"task": ...}` payload:
    ```bash
    aws sqs receive-message --queue-url <TargetQueueUrl>
    ```

## Cleanup

1. Change directory to the pattern directory:
    ```
    cd eventbridge-schedule-group-tagging-cdk-typescript
    ```
1. Delete all created resources and follow the prompts:
    ```bash
    cdk destroy
    ```
    Deleting the stack deletes the schedule group, which cascades to and removes both schedules in it.

----
Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
