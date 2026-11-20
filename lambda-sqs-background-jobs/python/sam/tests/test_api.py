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
from types import SimpleNamespace

import pytest

AFTER = Path(__file__).resolve().parent.parent / "after"
sys.path.insert(0, str(AFTER))

# What Powertools' inject_lambda_context reads off the Lambda context object.
CONTEXT = SimpleNamespace(
    function_name="t",
    memory_limit_in_mb=128,
    invoked_function_arn="arn:aws:lambda:us-east-1:000000000000:function:t",
    aws_request_id="r",
)


class FakeTable:
    """Minimal DynamoDB table: conditional put, get, conditional delete, and the
    aliased UpdateExpression with attribute_exists."""

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

    def delete_item(self, Key, ConditionExpression=None, ExpressionAttributeNames=None,
                    ExpressionAttributeValues=None):
        item = self.items.get(Key["job_id"])
        if ConditionExpression:
            # Only "#alias = :alias" is used.
            name_alias, _, val_alias = ConditionExpression.partition(" = ")
            field = ExpressionAttributeNames[name_alias]
            if item is None or item.get(field) != ExpressionAttributeValues[val_alias]:
                raise self.meta.client.exceptions.ConditionalCheckFailedException()
        self.items.pop(Key["job_id"], None)

    def update_item(self, Key, UpdateExpression, ExpressionAttributeNames,
                    ExpressionAttributeValues, ConditionExpression=None):
        if ConditionExpression == "attribute_exists(job_id)" and Key["job_id"] not in self.items:
            raise self.meta.client.exceptions.ConditionalCheckFailedException()
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
        self.fail_with = None  # set to an exception to make send_message raise

    def send_message(self, QueueUrl, MessageBody):
        if self.fail_with is not None:
            raise self.fail_with
        self.sent.append({"QueueUrl": QueueUrl, "MessageBody": MessageBody})


@pytest.fixture
def mods(monkeypatch):
    """Import api + worker with env set and their module-level clients faked."""
    monkeypatch.setenv("JOBS_TABLE", "jobs")
    monkeypatch.setenv("JOBS_QUEUE_URL", "https://sqs.local/jobs")
    monkeypatch.setenv("AWS_DEFAULT_REGION", "us-east-1")
    # Powertools: no X-Ray daemon here; metrics need a namespace to serialize.
    monkeypatch.setenv("POWERTOOLS_TRACE_DISABLED", "1")
    monkeypatch.setenv("POWERTOOLS_METRICS_NAMESPACE", "tests")
    monkeypatch.setenv("POWERTOOLS_SERVICE_NAME", "tests")
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
        "requestContext": {"http": {"method": method}, "stage": "prod", "requestId": "req-1"},
        "body": json.dumps(body) if body is not None else None,
        "isBase64Encoded": False,
    }


def _call(api, event):
    resp = api.lambda_handler(event, CONTEXT)
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


def test_enqueue_failure_rolls_back_row_and_returns_503(mods):
    api, _worker, table, sqs = mods
    sqs.fail_with = RuntimeError("sqs unavailable")
    code, body = _call(api, _proxy("POST", "/v1/jobs", {"job_id": "nq", "input": "hi"}))
    assert code == 503
    assert body["job_id"] == "nq"
    assert "retry" in body["error"]
    # The PENDING row was deleted, so a retry with the same job_id can enqueue.
    assert "nq" not in table.items
    sqs.fail_with = None
    code, _body = _call(api, _proxy("POST", "/v1/jobs", {"job_id": "nq", "input": "hi"}))
    assert code == 202
    assert len(sqs.sent) == 1


def test_unhandled_sdk_error_returns_json_500(mods):
    api, _worker, table, _sqs = mods

    def boom(**_kwargs):
        raise RuntimeError("ProvisionedThroughputExceededException")

    table.get_item = boom
    code, body = _call(api, _proxy("GET", "/v1/jobs/x", path_params={"job_id": "x"}))
    assert code == 500
    assert body == {"error": "internal error"}


def test_bad_json_returns_400(mods):
    api, _worker, _table, _sqs = mods
    event = _proxy("POST", "/v1/jobs")
    event["body"] = "{not json"
    code, body = _call(api, event)
    assert code == 400
    assert "JSON" in body["error"]


def test_non_object_body_returns_400(mods):
    api, _worker, _table, sqs = mods
    for raw in ("[1, 2]", '"a string"', "null", "{}"):
        event = _proxy("POST", "/v1/jobs")
        event["body"] = raw
        code, _body = _call(api, event)
        assert code == 400, raw
    assert len(sqs.sent) == 0


def test_worker_treats_a_non_object_message_as_malformed(mods):
    _api, worker, _table, _sqs = mods
    # A JSON body that parses but is not a job object must be reported for
    # redelivery (-> DLQ), never crash the batch with an unbound job id.
    event = {
        "Records": [
            {"messageId": "m1", "attributes": {"ApproximateReceiveCount": "1"}, "body": "null"},
            {"messageId": "m2", "attributes": {"ApproximateReceiveCount": "1"}, "body": "[1, 2]"},
        ]
    }
    out = worker.lambda_handler(event, CONTEXT)
    assert out["batchItemFailures"] == [{"itemIdentifier": "m1"}, {"itemIdentifier": "m2"}]


def test_get_unknown_job_returns_404(mods):
    api, _worker, _table, _sqs = mods
    code, _body = _call(api, _proxy("GET", "/v1/jobs/missing",
                                    path_params={"job_id": "missing"}))
    assert code == 404


def test_worker_runs_job_to_done(mods):
    api, worker, table, _sqs = mods
    _call(api, _proxy("POST", "/v1/jobs", {"job_id": "w1", "input": "hello"}))
    out = worker.lambda_handler(_sqs_event("w1", {"input": "hello"}, receive=1), CONTEXT)
    assert out == {"batchItemFailures": []}
    row = table.items["w1"]
    assert row["status"] == "DONE"
    assert row["result"]["published"] is True
    assert "error" not in row  # nothing to clear, stays absent


def test_worker_drops_message_for_unknown_job_without_creating_a_row(mods):
    _api, worker, table, _sqs = mods
    # The row expired (TTL) before a redelivery, or never existed: the
    # attribute_exists condition fails, the message is consumed (no redelivery)
    # and no phantom row without expires_at is written.
    out = worker.lambda_handler(_sqs_event("gone", {"input": "hello"}, receive=2), CONTEXT)
    assert out == {"batchItemFailures": []}
    assert "gone" not in table.items


def test_flaky_job_redelivers_then_completes(mods):
    api, worker, table, _sqs = mods
    _call(api, _proxy("POST", "/v1/jobs", {"job_id": "w2", "input": "flaky thing"}))
    # First delivery: transient failure -> reported for redelivery. The row
    # stays RUNNING and NO error is stamped, so a GET in the redelivery window
    # never shows RUNNING-with-a-stale-error.
    out1 = worker.lambda_handler(_sqs_event("w2", {"input": "flaky thing"}, receive=1), CONTEXT)
    assert out1["batchItemFailures"] == [{"itemIdentifier": "m-w2"}]
    assert table.items["w2"]["status"] == "RUNNING"
    assert "error" not in table.items["w2"]
    # Redelivery (receive count 2): transform succeeds, job is DONE, no error.
    out2 = worker.lambda_handler(_sqs_event("w2", {"input": "flaky thing"}, receive=2), CONTEXT)
    assert out2["batchItemFailures"] == []
    assert table.items["w2"]["status"] == "DONE"
    assert "error" not in table.items["w2"]


def test_malformed_message_redelivers_without_failing_the_batch(mods):
    _api, worker, table, _sqs = mods
    # A good message and a non-JSON message in one batch: the good one must run
    # to DONE, and only the bad one is reported for redelivery.
    event = {
        "Records": [
            {"messageId": "good", "attributes": {"ApproximateReceiveCount": "1"},
             "body": json.dumps({"job_id": "ok", "payload": {"input": "hi"}})},
            {"messageId": "bad", "attributes": {"ApproximateReceiveCount": "1"},
             "body": "{not json"},
        ]
    }
    table.put_item(Item={"job_id": "ok", "status": "PENDING"})
    out = worker.lambda_handler(event, CONTEXT)
    assert out["batchItemFailures"] == [{"itemIdentifier": "bad"}]
    assert table.items["ok"]["status"] == "DONE"


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
