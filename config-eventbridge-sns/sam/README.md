# AWS Config to Amazon EventBridge to Amazon SNS

This pattern sends an email notification whenever AWS Config reports a resource as `NON_COMPLIANT`. AWS Config emits a **Config Rules Compliance Change** event, an Amazon EventBridge rule on the default event bus filters for non-compliant results, and the matching event is delivered to an Amazon SNS topic that emails its subscribers.

There is **no AWS Lambda function** in this pattern - it is a pure service-to-service integration (Config -> EventBridge -> SNS), which keeps the compliance-notification path simple and with nothing to patch or maintain.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/getting-started.html) recording in the target Region, with at least one Config rule. This pattern doesn't enable AWS Config. Without an active recorder, no compliance-change events are sent.

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/config-eventbridge-sns/sam
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yaml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * **Stack Name**: enter a stack name.
    * **AWS Region**: enter the desired AWS Region.
    * **Parameter EmailAddress**: enter the email address that should receive non-compliance notifications.
    * **Parameter RuleName**: accept the default (`config-noncompliant-to-sns`) or provide your own. Rule names must be unique in an account and Region, so use a different name if you deploy this pattern more than once. If you change it, use your name in the testing commands below.
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and ARNs which are used for testing.

## How it works

* AWS Config continuously evaluates your resources against Config rules. When a resource's compliance state changes, Config publishes a **Config Rules Compliance Change** event to the default EventBridge event bus.
* The EventBridge rule matches only events where `source` is `aws.config`, `detail-type` is `Config Rules Compliance Change`, and `detail.newEvaluationResult.complianceType` is `NON_COMPLIANT`. Filtering to non-compliant results means subscribers are only notified about real drift, not routine `COMPLIANT` re-evaluations.
* The rule targets the SNS topic. An SNS topic policy authorizes the `events.amazonaws.com` service principal to `sns:Publish`, scoped to this account and this rule's ARN, so no other source can publish.
* The topic is encrypted at rest with a customer managed AWS KMS key that the stack creates, with automatic key rotation turned on. The key policy lets EventBridge use the key (`kms:GenerateDataKey*` and `kms:Decrypt`) when it publishes.
* SNS delivers the event body by email to every confirmed subscriber.

> **Why a customer managed key:** the AWS managed key for SNS (`alias/aws/sns`) doesn't allow EventBridge to use it, and you can't change its key policy. A topic encrypted with it rejects every publish from EventBridge, so no email arrives and nothing reports an error. See [Enable compatibility between event sources from AWS services and encrypted topics](https://docs.aws.amazon.com/sns/latest/dg/sns-key-management.html).
>
> The EventBridge statement in the key policy has no `aws:SourceAccount` or `aws:SourceArn` conditions, because SNS doesn't support them for EventBridge-to-encrypted topics. Publishing is still limited to this rule by the topic policy, which does use both conditions.
>
> A customer managed key has a monthly cost. See [AWS KMS pricing](https://aws.amazon.com/kms/pricing/).

## Testing

> **Confirm the SNS subscription FIRST.** When the stack is created, SNS sends a confirmation email to the address you supplied. Until you click the confirmation link, the subscription stays in `PendingConfirmation` and **no notifications are delivered** - the pattern will look broken even though it is working. Check your inbox (and spam folder) and confirm before testing.

You can verify the subscription state at any time (replace the ARN with the `ComplianceTopicArn` output):

```bash
aws sns list-subscriptions-by-topic \
  --topic-arn <ComplianceTopicArn> \
  --query "Subscriptions[].SubscriptionArn" \
  --profile YOUR_PROFILE
```

A confirmed subscription shows a real ARN; an unconfirmed one shows `PendingConfirmation`.

### Fast path: check the event filter

EventBridge reserves `aws.*` event sources for AWS services, so you can't inject a fake `aws.config` event with `aws events put-events` (it fails with `NotAuthorizedForSourceException`). Instead, use `test-event-pattern` to confirm that the rule's filter matches a real Config compliance-change event. `event.json` in this directory is a sample `Config Rules Compliance Change` event with a `NON_COMPLIANT` result:

```bash
aws events test-event-pattern \
  --event-pattern "$(aws events describe-rule --name config-noncompliant-to-sns --query EventPattern --output text --profile YOUR_PROFILE)" \
  --event file://event.json \
  --profile YOUR_PROFILE
```

Expected result: `{"Result": true}`. If you change `complianceType` in `event.json` to `COMPLIANT`, the result is `false`, which shows that only non-compliant results get through. This checks the filter only. It doesn't send an email. Use the real path below to test the whole chain.

### Real path: end-to-end with a real Config evaluation

This test runs the whole chain from Config to EventBridge to SNS to email. It needs an **active AWS Config recorder and delivery channel** in the Region. Enabling AWS Config incurs cost.

1. Make sure AWS Config is recording (Console: **Config -> Settings**, or [set up a recorder](https://docs.aws.amazon.com/config/latest/developerguide/getting-started.html)).
1. Add the AWS managed rule [`ec2-volume-inuse-check`](https://docs.aws.amazon.com/config/latest/developerguide/ec2-volume-inuse-check.html). It flags EBS volumes that aren't attached to an instance:
    ```bash
    aws configservice put-config-rule \
      --config-rule '{"ConfigRuleName":"ec2-volume-inuse-check","Source":{"Owner":"AWS","SourceIdentifier":"EC2_VOLUME_INUSE_CHECK"},"Scope":{"ComplianceResourceTypes":["AWS::EC2::Volume"]}}' \
      --profile YOUR_PROFILE
    ```
1. Create a small unattached EBS volume. A new volume is unattached by default, so it's non-compliant straight away. Note the `VolumeId` the command returns:
    ```bash
    aws ec2 create-volume --availability-zone <REGION>a --size 1 --volume-type gp3 \
      --query VolumeId --output text --profile YOUR_PROFILE
    ```
1. Wait for Config to evaluate. This usually takes a few minutes. When the volume is marked `NON_COMPLIANT`, you receive an email from `no-reply@sns.amazonaws.com` with the subject `AWS Notification Message`. You can check the evaluation with:
    ```bash
    aws configservice get-compliance-details-by-config-rule \
      --config-rule-name ec2-volume-inuse-check --profile YOUR_PROFILE
    ```

A compliance-change event is only emitted when a resource's compliance state changes. A resource that's already non-compliant won't send a second email. To test again, create a new volume.

## Cleanup

1. From the pattern directory, delete the stack:
    ```bash
    sam delete --stack-name STACK_NAME --profile YOUR_PROFILE
    ```
1. Confirm the stack has been deleted:
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus" --profile YOUR_PROFILE
    ```

    Deleting the stack schedules the KMS key for deletion after a 7-day waiting period, which is the minimum. Until then the key shows as `Pending deletion` in the AWS KMS console.

> **If you ran the real-path test, clean those resources up separately - they are not part of this stack and can incur ongoing cost:**
> * Delete the test EBS volume (EBS storage bills while the volume exists):
>   ```bash
>   aws ec2 delete-volume --volume-id <VolumeId> --profile YOUR_PROFILE
>   ```
> * Delete the Config rule:
>   ```bash
>   aws configservice delete-config-rule --config-rule-name ec2-volume-inuse-check --profile YOUR_PROFILE
>   ```
> * If you enabled an AWS Config recorder / delivery channel solely for this test, and you do not use Config elsewhere, disable or delete it (AWS Config bills for configuration items recorded and rule evaluations).

----
Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
