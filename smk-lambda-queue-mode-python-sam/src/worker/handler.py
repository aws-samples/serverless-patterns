"""KQD Worker Lambda -- Kafka Queue mode (KIP-932) consumer."""

import base64
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    failures = []

    for tp_key, records in event.get("records", {}).items():
        for r in records:
            try:
                payload = json.loads(base64.b64decode(r["value"]).decode("utf-8"))
            except Exception:
                payload = {"raw": r.get("value", "")}

            logger.info(
                "KAFKA_RECORD topic=%s partition=%s offset=%s payload=%s",
                r.get("topic"),
                r.get("partition"),
                r.get("offset"),
                json.dumps(payload),
            )

            if payload.get("shouldFail"):
                identifier = f"{r['topic']}-{r['partition']}-{r['offset']}"
                logger.warning("Simulated failure, releasing record: %s", identifier)
                failures.append({"itemIdentifier": identifier})

    logger.info(
        "Batch done: %d record(s), %d failure(s)",
        sum(len(v) for v in event.get("records", {}).values()),
        len(failures),
    )
    return {"batchItemFailures": failures}
