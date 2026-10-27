"""
API-layer tests for the AFTER half. Invoke the Lambda handlers the way
production does - the API via API Gateway proxy events through Mangum, the
worker via an SQS event - against a fake in-memory DynamoDB table and SQS
client. No AWS account needed:

    pip install -r tests/requirements.txt
    pytest tests/

Every live-only bug lived here: reserved-word aliasing, idempotent enqueue,
stale-error clearing, partial batch failure.
"""

import importlib
import json
import sys
from pathlib import Path

import pytest

AFTER = Path(__file__).resolve().parent.parent / "after"
sys.path.insert(0, str(AFTER))


class FakeTable:
    """Minimal DynamoDB table: conditional put, get, and the aliased UpdateExpression."""

    def __init__(self):
        self.items = {}

        class _Exc:
            class ConditionalCheckFailedException(Exception):
                pass

        class _Meta:
            client = type("c", (), {"exceptions": _Exc})()

        self.meta = _Meta()

    def put_item(self, Item, ConditionExpression=None):
        key = Item["job_id"]
        if ConditionExpression == "attribute_not_exists(job_id)" and key in self.items:
            raise self.meta.client.exceptions.ConditionalCheckFailedException()
        self.items[key] = dict(Item)

    def get_item(self, Key):
        item = self.items.get(Key["job_id"])
        return {"Item": dict(item)} if item else {}

    def update_item(self, Key, UpdateExpression, ExpressionAttributeNames,
                    ExpressionAttributeValues):
        item = self.items.setdefault(Key["job_id"], {"job_id": Key["job_id"]})
        # Resolve "#f0 = :v0, #f1 = :v1 REMOVE #r0" using the alias maps.
        set_part, _, remove_part = UpdateExpression.partition(" REMOVE ")
        set_part = set_part[len("SET "):]
        for assignment in set_part.split(","):
            name_alias, _, val_alias = assignment.strip().partition(" = ")
            item[ExpressionAttributeNames[name_alias]] = ExpressionAttributeValues[val_alias]
        for alias in filter(None, (a.strip() for a in remove_part.split(","))):
            item.pop(ExpressionAttributeNames[alias], None)


class FakeSqs:
    def __init__(self):
        self.sent = []

    def send_message(self, QueueUrl, MessageBody):
        self.sent.append({"QueueUrl": QueueUrl, "MessageBody": MessageBody})


@pytest.fixture
def mods(monkeypatch):
    """Import api + worker with env set and their module-level clients faked."""
    monkeypatch.setenv("JOBS_TABLE", "jobs")
    monkeypatch.setenv("JOBS_QUEUE_URL", "https://sqs.local/jobs")
    monkeypatch.setenv("AWS_DEFAULT_REGION", "us-east-1")
    table = FakeTable()
    sqs = FakeSqs()
    import api
    import worker
    importlib.reload(api)
    importlib.reload(worker)
    api.table = table
    api.sqs = sqs
    worker.table = table
    return api, worker, table, sqs


def _proxy(method, path, body=None, path_params=None):
    return {
        "httpMethod": method,
        "path": path,
        "resource": path,
        "pathParameters": path_params,
        "queryStringParameters": None,
        "headers": {"Content-Type": "application/json", "host": "test"},
        "requestContext": {"http": {"method": method}, "stage": "prod"},
        "body": json.dumps(body) if body is not None else None,
        "isBase64Encoded": False,
    }


def _call(api, event):
    resp = api.lambda_handler(event, None)
    return resp["statusCode"], json.loads(resp["body"])


def test_post_enqueues_once_and_returns_pending(mods):
    api, _worker, table, sqs = mods
    code, body = _call(api, _proxy("POST", "/v1/jobs", {"job_id": "a", "input": "hi"}))
    assert code == 202
    assert body == {"job_id": "a", "status": "PENDING"}
    # The row exists and exactly one message was enqueued.
    assert table.items["a"]["status"] == "PENDING"
    assert len(sqs.sent) == 1
    assert json.loads(sqs.sent[0]["MessageBody"])["job_id"] == "a"


def test_duplicate_post_does_not_enqueue_again(mods):
    api, _worker, _table, sqs = mods
    _call(api, _proxy("POST", "/v1/jobs", {"job_id": "dup", "input": "hi"}))
    code, body = _call(api, _proxy("POST", "/v1/jobs", {"job_id": "dup", "input": "hi"}))
    assert code == 200
    assert body["job_id"] == "dup"
    # Still only one message: the conditional put blocked the second send.
    assert len(sqs.sent) == 1


def test_bad_json_returns_400(mods):
    api, _worker, _table, _sqs = mods
    event = _proxy("POST", "/v1/jobs")
    event["body"] = "{not json"
    code, body = _call(api, event)
    assert code == 400
    assert "JSON" in body["error"]


def test_get_unknown_job_returns_404(mods):
    api, _worker, _table, _sqs = mods
    code, _body = _call(api, _proxy("GET", "/v1/jobs/missing",
                                    path_params={"job_id": "missing"}))
    assert code == 404


def test_worker_runs_job_to_done(mods):
    api, worker, table, _sqs = mods
    _call(api, _proxy("POST", "/v1/jobs", {"job_id": "w1", "input": "hello"}))
    out = worker.lambda_handler(_sqs_event("w1", {"input": "hello"}, receive=1), None)
    assert out == {"batchItemFailures": []}
    row = table.items["w1"]
    assert row["status"] == "DONE"
    assert row["result"]["published"] is True
    assert "error" not in row  # nothing to clear, stays absent


def test_flaky_job_redelivers_then_clears_error(mods):
    api, worker, table, _sqs = mods
    _call(api, _proxy("POST", "/v1/jobs", {"job_id": "w2", "input": "flaky thing"}))
    # First delivery: transient failure -> reported for redelivery, error stamped.
    out1 = worker.lambda_handler(_sqs_event("w2", {"input": "flaky thing"}, receive=1), None)
    assert out1["batchItemFailures"] == [{"itemIdentifier": "m-w2"}]
    assert table.items["w2"]["status"] == "RUNNING"
    assert "error" in table.items["w2"]
    # Redelivery (receive count 2): transform succeeds, DONE, stale error cleared.
    out2 = worker.lambda_handler(_sqs_event("w2", {"input": "flaky thing"}, receive=2), None)
    assert out2["batchItemFailures"] == []
    assert table.items["w2"]["status"] == "DONE"
    assert "error" not in table.items["w2"]


def _sqs_event(job_id, payload, receive):
    return {
        "Records": [
            {
                "messageId": f"m-{job_id}",
                "attributes": {"ApproximateReceiveCount": str(receive)},
                "body": json.dumps({"job_id": job_id, "payload": payload}),
            }
        ]
    }
