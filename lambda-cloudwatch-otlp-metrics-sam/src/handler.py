"""Record custom application metrics and send them to CloudWatch over OTLP.

This function only uses the OpenTelemetry metrics API. The AWS Distro for
OpenTelemetry Lambda layer starts a collector that signs each request with SigV4
and forwards it to the CloudWatch OTLP endpoint, so the application code never
calls PutMetricData, never writes embedded metric format logs, and does no AWS
request signing of its own.
"""
from opentelemetry import metrics

meter = metrics.get_meter("orders")

orders_processed = meter.create_counter(
    name="orders.processed",
    unit="1",
    description="Number of orders processed.",
)

order_value = meter.create_histogram(
    name="orders.value",
    unit="USD",
    description="Distribution of order values.",
)


def handler(event, context):
    order = (event or {}).get("order") or {}

    # Dimensions are plain OpenTelemetry attributes. The OTLP endpoint accepts up to
    # 150 labels per metric, well above the 30 dimensions allowed by PutMetricData.
    attributes = {
        "order.channel": order.get("channel", "web"),
        "order.country": order.get("country", "IN"),
    }

    value = float(order.get("value", 49.99))

    orders_processed.add(1, attributes)
    order_value.record(value, attributes)

    # Lambda freezes the execution environment as soon as the handler returns, so
    # flush now rather than waiting for the next periodic export, which would
    # otherwise be lost.
    provider = metrics.get_meter_provider()
    if hasattr(provider, "force_flush"):
        provider.force_flush()

    return {
        "recorded": {"orders.processed": 1, "orders.value": value},
        "attributes": attributes,
    }
