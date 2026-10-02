"""Record custom application metrics and send them to CloudWatch over OTLP.

This function only uses the OpenTelemetry metrics API. The AWS Distro for
OpenTelemetry Lambda layer starts a collector that signs each request with AWS
Signature Version 4 and forwards it to the CloudWatch OpenTelemetry Protocol
(OTLP) metrics endpoint, so the application code never calls PutMetricData,
never writes embedded metric format logs, and does no AWS request signing of
its own.
"""
import logging

from opentelemetry import metrics

logger = logging.getLogger()
logger.setLevel(logging.INFO)

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

DEFAULT_LABEL = "unknown"
DEFAULT_VALUE = 0.0


def handler(event, context):
    # A Lambda event can be any JSON value, so accept only a mapping and treat
    # anything else (a list, a string, null) as an order with no fields.
    order = event.get("order") if isinstance(event, dict) else None
    if not isinstance(order, dict):
        order = {}

    # Dimensions are plain OpenTelemetry attributes. The OTLP endpoint accepts up to
    # 150 labels per metric, well above the 30 dimensions allowed by PutMetricData.
    attributes = {
        "order.channel": order.get("channel") or DEFAULT_LABEL,
        "order.country": order.get("country") or DEFAULT_LABEL,
    }

    # A malformed value should not fail the invocation in a sample that is about
    # metrics, so log a warning and record the default instead.
    try:
        value = float(order.get("value", DEFAULT_VALUE))
    except (TypeError, ValueError):
        logger.warning(
            "order.value %r is not a number, recording %s instead",
            order.get("value"),
            DEFAULT_VALUE,
        )
        value = DEFAULT_VALUE

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
