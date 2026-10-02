# Send custom AWS Lambda metrics to Amazon CloudWatch over OTLP

This pattern records custom application metrics in an AWS Lambda function using the OpenTelemetry metrics API and sends them to Amazon CloudWatch over the OpenTelemetry Protocol (OTLP). The AWS Distro for OpenTelemetry (ADOT) Lambda layer runs a collector next to the function that signs each request with AWS Signature Version 4 (SigV4) and forwards it to the Amazon CloudWatch OTLP metrics endpoint. The function makes no PutMetricData calls, writes no embedded metric format logs, and performs no request signing of its own. The metrics are then queried with Prometheus Query Language (PromQL).

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

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-cloudwatch-otlp-metrics-sam

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* Python 3 (`python3`) with the `botocore` library, used by the `promql_query.py` script in the Testing section to sign requests to the CloudWatch Prometheus-compatible HTTP API. The AWS CLI v2 installer bundles `botocore` for its own interpreter but does not expose it to your `python3`, so install it with `python3 -m pip install botocore` if `python3 -c "import botocore"` fails.
* A Region that supports both OTLP metrics ingestion and the ADOT Python Lambda layer. OTLP metrics ingestion, PromQL querying and Query Studio are available in the Regions listed under "Supported AWS Regions" in [Query metrics with PromQL](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-PromQL.html). The ADOT Python Lambda layer is published in a smaller set: `ap-northeast-1`, `ap-northeast-2`, `ap-south-1`, `ap-southeast-1`, `ap-southeast-2`, `ca-central-1`, `eu-central-1`, `eu-north-1`, `eu-west-1`, `eu-west-2`, `eu-west-3`, `sa-east-1`, `us-east-1`, `us-east-2`, `us-west-1` and `us-west-2`, per [AWS Distro for OpenTelemetry Lambda Support For Python](https://aws-otel.github.io/docs/getting-started/lambda/lambda-python). Deploy in one of those 16 Regions, or copy the layer into your own Region first.
* No account level enablement is needed for the OTLP metrics endpoint itself. Beyond basic Lambda logging permissions, the only permission the function needs is `cloudwatch:PutMetricData`, which the template grants. See [Publish custom metrics with OpenTelemetry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/metrics-otel-send.html).

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/lambda-cloudwatch-otlp-metrics-sam
    ```
1. From the command line, build the function and use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yaml file:
    ```
    sam build
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region. Use one of the 16 Regions listed in Requirements.
    * `Parameter AdotLayerArn`: the default is `arn:aws:lambda:us-east-1:901920570463:layer:aws-otel-python-amd64-ver-1-32-0:7`. Keep it for `us-east-1`, otherwise replace `us-east-1` in the ARN with your Region. To run the function on arm64, set `Architectures` to `arm64` in template.yaml and replace `amd64` with `arm64` in this ARN as well.
    * `Parameter ServiceName`: the default is `orders-service`. This becomes the `service.name` resource attribute, which is the `@resource.service.name` label you filter on in PromQL. Keep the default to follow the Testing section as written.
    * Confirm changes before deploy: accept the default
    * Allow SAM CLI to create IAM roles with the required permissions
    * Disable rollback: accept the default
    * Save arguments to configuration file, SAM configuration file and SAM configuration environment: accept the defaults

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing. This pattern outputs `MetricsFunctionName`, `LogGroupName` and `ServiceNameValue`.

## How it works

* The function uses only the OpenTelemetry metrics API to record a counter (`orders.processed`) and a histogram (`orders.value`).
* The ADOT Lambda layer starts a reduced OpenTelemetry collector as a Lambda extension that receives those metrics locally over OTLP.
* The collector signs each request with SigV4 (signing name `monitoring`) and forwards it to the CloudWatch OTLP metrics endpoint, `https://monitoring.<region>.amazonaws.com/v1/metrics`.
* Beyond basic Lambda logging permissions, the only permission the function needs is `cloudwatch:PutMetricData`.
* The function flushes the meter provider before returning, because Lambda freezes the execution environment as soon as the handler returns.
* The stack owns the function log group, so the function and the collector diagnostics are deleted with the stack.

## Testing

1. Set the function name from the `MetricsFunctionName` stack output, and the Region you deployed to:

    ```bash
    FN=<the MetricsFunctionName output>
    REGION=<the Region you deployed to>
    ```

1. Invoke the function with the test event in `events/order.json`:

    ```json
    {
      "order": {
        "channel": "mobile",
        "country": "IN",
        "value": 129.50
      }
    }
    ```

    ```bash
    aws lambda invoke --function-name $FN --region $REGION --payload fileb://events/order.json out.json
    cat out.json
    ```

    `invoke` prints the call status and `cat` prints the response body:

    ```
    {
        "StatusCode": 200,
        "ExecutedVersion": "$LATEST"
    }
    {"recorded": {"orders.processed": 1, "orders.value": 129.5}, "attributes": {"order.channel": "mobile", "order.country": "IN"}}
    ```

    A payload with no `order` field, or with a `channel` or `country` that is missing, records `unknown` for that label, and a `value` that is not a number records `0.0` and logs a warning.

1. Invoke it four more times so there is more than one data point:

    ```bash
    for i in 1 2 3 4; do aws lambda invoke --function-name $FN --region $REGION --payload fileb://events/order.json out.json > /dev/null; done
    ```

1. Query the counter with PromQL. Metrics typically appear within 1 to 2 minutes of the first data point being sent, as described in [Publish custom metrics with OpenTelemetry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/metrics-otel-send.html), so wait a couple of minutes before the first query.

    The `promql_query.py` script in this folder signs a request to the CloudWatch Prometheus-compatible HTTP API with SigV4 and prints the JSON response:

    ```bash
    python3 promql_query.py 'sum({__name__="orders.processed"})' $REGION
    ```

    The counter is cumulative and the collector reports one series per Lambda execution environment, so the raw selector can return several series whose individual values are below the invocation count. `sum()` adds them up, so after five invocations the result is `5`:

    ```
    {
      "status": "success",
      "data": {
        "resultType": "vector",
        "result": [
          {
            "metric": {},
            "value": [
              1790961875.028,
              "5"
            ]
          }
        ]
      }
    }
    ```

    The metric names keep their dots, so they must be selected with `__name__` rather than written directly. Dropping `sum()` shows the labels on each series: `order.channel` and `order.country` from the function, plus resource labels such as `@resource.faas.name`, `@resource.service.name`, `@aws.account` and `@aws.region` that the layer and the endpoint add automatically.

    ```bash
    python3 promql_query.py '{__name__="orders.processed"}' $REGION
    ```

1. Query the histogram. `orders.value` is exported as a native histogram, so the response carries a `count`, a `sum` and buckets rather than a single value. After five invocations of the sample event the count is `5` and the sum is `647.5`:

    ```bash
    python3 promql_query.py '{__name__="orders.value"}' $REGION
    ```

1. Confirm that these metrics are not classic CloudWatch metrics. They are queried with PromQL only, so `list-metrics` returns an empty list:

    ```bash
    aws cloudwatch list-metrics --metric-name orders.processed --region $REGION
    ```

    ```
    {
        "Metrics": []
    }
    ```

    You can run the same queries interactively in the CloudWatch console. Open the console, navigate to Query Studio and run the PromQL query there, as described in "Running PromQL queries in Query Studio" in [Query metrics with PromQL](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-PromQL.html). Querying requires `cloudwatch:GetMetricData` and `cloudwatch:ListMetrics` on the caller, which is separate from the permission the function needs to publish.

## Why OTLP rather than PutMetricData or embedded metric format

* No per series charge. Embedded metric format bills log ingestion plus a monthly charge for every unique metric and dimension combination, which grows with cardinality. OTLP metrics are billed on ingested volume with storage and query access included, per [OTel metrics pricing and storage](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/metrics-otel-pricing.html).
* Up to 150 labels per data point, against the 30 dimensions allowed by PutMetricData, so you can attach much richer context. See the metrics limits table in [OTLP Endpoints](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTLPEndpoint.html).
* No synchronous AWS API call inside the invocation, because the collector handles delivery.

## Notes

* This pattern uses the ADOT collector that ships inside the Lambda layer, rather than an SDK that exports directly, because the layer gives you a collector in the execution environment with a custom configuration (`src/collector.yaml`) pointing at the CloudWatch OTLP metrics endpoint, without packaging an exporter or running a separate collector gateway. The [ADOT Python Lambda page](https://aws-otel.github.io/docs/getting-started/lambda/lambda-python) marks this layer as the legacy approach to ADOT on Lambda, and it remains the simplest way to get a configurable collector next to a Lambda function.
* The collector configuration deliberately declares no processors. The collector build inside the ADOT Lambda layer is compiled without them, so naming one such as `batch` stops the collector from starting and nothing is exported. The example configuration in the CloudWatch documentation includes `batch` and therefore does not work in this layer.
* Use `metrics_endpoint` in the exporter, not `endpoint`. The exporter appends the signal path to `endpoint`, so setting `endpoint` to the full metrics URL produces `/v1/metrics/v1/metrics` and every export fails with HTTP 404.
* The exporter is named `otlp_http`. Older collector builds use the `otlphttp` alias, which now logs a deprecation warning.

## Troubleshooting

If no data appears in PromQL after a few minutes, the invocation itself can still succeed, because an export failure in the collector does not fail the handler. Check the function log group for collector export errors, using the `LogGroupName` stack output:

```bash
aws logs tail <the LogGroupName output> --region $REGION --since 15m
```

A healthy start logs `Everything is ready. Begin running and processing data.` and `EXTENSION Name: collector State: Ready`. Export problems appear as lines containing `Exporting failed` or `otlp_http`, together with the HTTP status the endpoint returned. For example, pointing the exporter at `endpoint` instead of `metrics_endpoint` produces `responded with HTTP Status Code 404`.

## Optional: add AWS resource tag labels

The OTLP metrics endpoint needs no account level enablement, and the resource labels shown in Testing arrive without it. Two separate, account and Region wide CloudWatch features add more labels: resource tags on telemetry, and OTel enrichment, which makes AWS vended metrics queryable through PromQL and adds resource ARN and resource tag labels to them. They are optional for this pattern. If you want them, enable them in this order, because OTel enrichment requires resource tags on telemetry first, as stated in [AWS vended metrics in OpenTelemetry format](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTelEnrichment.html) ("Before you start OTel enrichment, you must enable resource tags on telemetry for your account"):

```bash
aws observabilityadmin start-telemetry-enrichment --region $REGION
aws cloudwatch start-otel-enrichment --region $REGION
```

See [Enable resource tags on telemetry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/EnableResourceTagsOnTelemetry.html) for the permissions each call needs.

## Cleanup

1. Delete the stack. This also deletes the function log group, which the stack owns:
    ```bash
    sam delete --stack-name STACK_NAME
    ```
1. Delete the local files created while testing:
    ```bash
    rm -f out.json
    rm -rf .aws-sam
    ```
1. The two enrichment settings in the optional section above are account and Region wide, were not created by this stack, and affect other workloads, so leave them alone unless you enabled them only for this walkthrough.
1. The metric data points that were ingested cannot be deleted. They age out under the included retention described in [OTel metrics pricing and storage](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/metrics-otel-pricing.html).
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
