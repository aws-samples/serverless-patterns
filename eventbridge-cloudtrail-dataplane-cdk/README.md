# Amazon EventBridge Data Plane Logging with AWS CloudTrail

This pattern enables CloudTrail data plane logging for Amazon EventBridge and triggers a Lambda function when PutEvents API calls are detected, providing security and operational visibility into event bus activity.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-cloudtrail-dataplane-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details.

## Requirements

* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed
* [Node.js](https://nodejs.org/en/download/) installed

## Deployment Instructions

1. Clone and navigate to the pattern:
    ```
    cd serverless-patterns/eventbridge-cloudtrail-dataplane-cdk
    npm install
    ```
2. Deploy:
    ```
    cdk deploy
    ```

## How it works

- A CloudTrail trail is created with data event logging enabled
- EventBridge data plane API calls (PutEvents) are now logged to CloudTrail (new May 2026 feature)
- An EventBridge rule captures these CloudTrail events matching `aws.events` source with `PutEvents` event name
- A Lambda function processes the events, logging the caller identity, source IP, event bus, and entry count
- This enables security teams to audit who is putting events to which bus

## Testing

```bash
# Put a test event to the default event bus
aws events put-events --entries '[{"Source":"test.app","DetailType":"TestEvent","Detail":"{\"key\":\"value\"}"}]'

# Check Lambda logs (allow ~5 minutes for CloudTrail delivery)
aws logs tail /aws/lambda/$(aws cloudformation describe-stacks \
  --stack-name EventbridgeCloudtrailDataplaneStack \
  --query 'Stacks[0].Outputs[?OutputKey==`ProcessorFunctionName`].OutputValue' --output text) \
  --follow
```

## Cleanup

```
cdk destroy
```

---

Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
