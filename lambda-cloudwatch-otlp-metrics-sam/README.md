# Send custom Lambda metrics to Amazon CloudWatch over OTLP

This pattern records custom application metrics in an AWS Lambda function using the OpenTelemetry metrics API and sends them to Amazon CloudWatch over OTLP. The AWS Distro for OpenTelemetry (ADOT) Lambda layer runs a collector next to the function that signs each request with SigV4 and forwards it to the CloudWatch OTLP endpoint. The function makes no PutMetricData calls, writes no embedded metric format logs, and performs no request signing of its own.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-cloudwatch-otlp-metrics-sam

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## How it works

```
   AWS Lambda                                  Amazon CloudWatch
   +----------------------------+              +--------------------------+
   |  handler.py                |   OTLP       |  OTLP metrics endpoint   |
   |  OpenTelemetry metrics API |  over HTTP   |  monitoring.<region>     |
   |            |               |  SigV4       |  .amazonaws.com          |
   |            v               | -----------> |                          |
   |  ADOT layer collector      |              |  queried with PromQL     |
   +----------------------------+              +--------------------------+
```

- The function uses only the OpenTelemetry metrics API to record a counter and a histogram.
- The ADOT Lambda layer starts a reduced OpenTelemetry collector that receives those metrics locally over OTLP.
- The collector signs each request with SigV4 (signing name `monitoring`) and forwards it to the CloudWatch OTLP endpoint.
- The only IAM permission the function needs is `cloudwatch:PutMetricData`.

## Why OTLP rather than PutMetricData or embedded metric format

- No per series charge. Embedded metric format bills log ingestion plus a monthly charge for every unique metric and dimension combination, which grows with cardinality. OTLP is billed on volume.
- Up to 150 labels per metric, against the 30 dimensions allowed by PutMetricData, so you can attach much richer context.
- No synchronous AWS API call inside the invocation, because the collector handles delivery.

## Requirements

- An AWS account with permissions to create Lambda functions and IAM roles.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) v2.
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html).
- The CloudWatch OTLP endpoint enabled for your account and Region, as shown below.

## Enable the CloudWatch OTLP endpoint

The endpoint is turned off by default. Enable it once per account and Region, otherwise every export fails and no metrics appear.

```bash
REGION=us-east-1
aws cloudwatch start-otel-enrichment --region $REGION
aws observabilityadmin start-telemetry-enrichment --region $REGION

# Both should report Running
aws cloudwatch get-otel-enrichment --region $REGION
aws observabilityadmin get-telemetry-enrichment-status --region $REGION
```

## Deployment

```bash
sam build
sam deploy --guided
#   - Stack Name  : otlp-metrics
#   - AWS Region  : us-east-1
#   - AdotLayerArn: keep the default for us-east-1, or change the Region in the ARN
```

The `AdotLayerArn` parameter is Region specific. The default points at the ADOT Python layer in us-east-1, so replace the Region in the ARN when deploying elsewhere.

## Testing

### 1. Invoke the function

```bash
FN=<the MetricsFunctionName output>
echo {\"order\":{\"channel\":\"mobile\",\"country\":\"IN\",\"value\":129.50}} > event.json
aws lambda invoke --function-name $FN --cli-binary-format raw-in-base64-out --payload file://event.json out.json
cat out.json
```

Invoke it a few times so there is more than one data point.

### 2. Confirm the metrics arrived

These metrics are queried with PromQL. They do not appear in the classic CloudWatch metrics list, so `aws cloudwatch list-metrics` returns nothing for them. In the CloudWatch console open Metrics and switch the query editor to PromQL, then run:

```promql
{__name__="orders.processed"}
```

The metric names keep their dots, so they must be selected with `__name__` rather than written directly. You should see a value equal to the number of invocations, carrying the `order.channel` and `order.country` labels from the function plus resource labels such as `@resource.faas.name` and `@resource.service.name` added automatically by the layer.

The same query is available over HTTP at `https://monitoring.<region>.amazonaws.com/api/v1/query`, signed with SigV4. Listing available names is a quick check:

```
GET https://monitoring.<region>.amazonaws.com/api/v1/label/__name__/values
```

Querying requires `cloudwatch:GetMetricData` and `cloudwatch:ListMetrics` on the caller, which is separate from the permission the function needs to publish.

## Notes

- The collector configuration deliberately declares no processors. The collector build inside the ADOT Lambda layer is compiled without them, so naming one such as `batch` stops the collector from starting and nothing is exported.
- Use `metrics_endpoint` in the exporter, not `endpoint`. The exporter appends the signal path to `endpoint`, so setting `endpoint` to the full metrics URL produces `/v1/metrics/v1/metrics` and every export fails with HTTP 404.
- The function flushes the meter provider before returning. Lambda freezes the execution environment as soon as the handler returns, so waiting for the next periodic export would lose the data.
- The exporter is named `otlp_http`. Older collector builds use the `otlphttp` alias, which now logs a deprecation warning.

## Cleanup

```bash
sam delete
```

Optionally turn the endpoint back off:

```bash
aws cloudwatch stop-otel-enrichment --region $REGION
aws observabilityadmin stop-telemetry-enrichment --region $REGION
```

----

Author: Manish S

Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved. SPDX-License-Identifier: MIT-0
