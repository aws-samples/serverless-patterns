# Change the State of an EventBridge Rule on a Schedule

EventBridge [rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html) allow users to match events
based on a pattern and invoke targets. Users can change the state of a rule, i.e., configure a rule as `ENABLED` or
`DISABLED`. When a rule is in `DISABLED` state, no events are processed and sent to its target(s). Temporarily disabling
a rule can be useful during debugging or when performing maintenance on downstream services.

This pattern demonstrates using EventBridge Scheduler, a serverless scheduler that enables you to schedule tasks and
events at scale, to disable and re-enable an EventBridge rule at specific days and times in a week, such as a periodic
maintenance window on a weekend.

Learn more about this pattern at Serverless Land Patterns:
https://serverlessland.com/patterns/eventbridge-schedule-disable-eventbridge-rule-cdk-typescript

Important: this application uses various AWS services and there are costs associated with these services after the Free
Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any
AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already
  have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls
  and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:

    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
    
1. Change directory to the pattern directory:

    ```
    cd serverless-patterns/eventbridge-schedule-disable-eventbridge-rule-cdk-typescript/cdk
    ```
    
1. Install dependencies:

    ```
    npm install
    ```
    
1. From the command line, configure AWS CDK (unless already done):

   ```
   # cdk bootstrap <ACCOUNT-NUMBER/REGION>
   cdk bootstrap 1111111111/us-east-1
   ```

1. From the command line, use AWS CDK to deploy the AWS resources for the pattern:
   
    ```
    cdk deploy 
    ```

## How it works

EventBridge schedules, using [universal
target](https://docs.aws.amazon.com/scheduler/latest/UserGuide/managing-targets-universal.html) integrations and
powerful [cron](https://docs.aws.amazon.com/scheduler/latest/UserGuide/schedule-types.html#cron-based) expressions are
highly configurable. This pattern demonstrates using EventBridge schedules with universal targets to disable an
EventBridge rule on a custom event bus *every Sunday 8AM (UTC)*, and then enable the rule again after a one hour
maintenance window *every Sunday 9AM (UTC)*. In case of invocation errors, scheduler events are sent to an Amazon SQS
dead-letter queue after one retry attempt (configurable).

## Cleanup

Delete the stack:

```
cdk destroy
```

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0