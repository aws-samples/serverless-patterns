# Amazon EventBridge Data Plane Logging with AWS CloudTrail

This pattern enables CloudTrail data plane logging for Amazon EventBridge and triggers a Lambda function when PutEvents API calls are detected, providing security and operational visibility into event bus activity.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-cloudtrail-dataplane-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details.

> **Note:** CloudTrail data events are billed separately from management events. See [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/) for current data event rates.

## Requirements

* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed
* [Node.js 20+](https://nodejs.org/en/download/) installed

## Deployment Instructions

1. Clone and navigate to the pattern:
    ```
    cd serverless-patterns/eventbridge-cloudtrail-dataplane-cdk
    npm install
    ```
2. Bootstrap CDK (first-time CDK users only):
    ```
    cdk bootstrap
    ```
3. Deploy:
    ```
    cdk deploy
    ```

## How it works

- A CloudTrail trail is created with data event logging enabled for EventBridge event buses (`AWS::Events::EventBus`)
- EventBridge data plane API calls (PutEvents) are now logged to CloudTrail (new May 2026 feature)
- An EventBridge rule captures these CloudTrail events matching `aws.events` source with `PutEvents` event name
- A Lambda function processes the events, logging the caller identity, source IP, event bus, and entry count
- This enables security teams to audit who is putting events to which bus

EventBridge rules are region-local. The trail is multi-region, but the rule in this stack only matches events in the region where it is deployed, so deploy it in each region you want to alert in.

## Testing

The check puts one event, then polls the function log group every 15 seconds for up to 20 minutes. It prints `PASS` when a record is logged and exits non-zero otherwise. CloudTrail delivers events with a delay of several minutes, and a newly created trail can take noticeably longer, so the check waits up to 20 minutes instead of a fixed short time. Save the block as `smoke-test.sh` and run it with `bash smoke-test.sh` (the `exit 1` would close your shell if you pasted it into an interactive session). The AWS CLI default Region must be the Region you deployed to.

```bash
STACK=EventbridgeCloudtrailDataplaneStack
FN=$(aws cloudformation describe-stacks --stack-name $STACK \
  --query 'Stacks[0].Outputs[?OutputKey==`ProcessorFunctionName`].OutputValue' --output text)
[ -n "$FN" ] || { echo "FAIL: stack output not found (check the CLI Region)"; exit 1; }
START=$(( $(date +%s) * 1000 ))

# Put a test event to the default event bus
aws events put-events --entries '[{"Source":"test.app","DetailType":"TestEvent","Detail":"{\"key\":\"value\"}"}]'

# Poll the function log group (80 tries x 15 s = 20 minutes); exit non-zero if no record appears
N=0
for i in $(seq 1 80); do
  N=$(aws logs filter-log-events --log-group-name "/aws/lambda/$FN" \
    --filter-pattern '"EventBridge data plane API call detected"' \
    --start-time "$START" --query 'events[].eventId' --output text | wc -w | tr -d ' ')
  [ "$N" -gt 0 ] && break
  sleep 15
done
[ "$N" -gt 0 ] && echo "PASS: $N record(s) logged" || { echo "FAIL: no record logged"; exit 1; }
```

## Cleanup

```
cdk destroy
```

---

Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
