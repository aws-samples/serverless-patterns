"""
Exercise both FastAPI apps through the Lambda handler (Mangum) with API Gateway
proxy events, no AWS account needed. boto3 is replaced with small fakes so the
tests cover the HTTP layer: status codes, idempotent starts, the legacy-row
branch, and the one durable-specific trap (a duplicate start must not
overwrite the stored execution ARN).
"""

import importlib.util
import json
import os
import sys
import types
from pathlib import Path

import boto3
import pytest

ROOT = Path(__file__).resolve().parent.parent


class ConditionalCheckFailedException(Exception):
    pass


class FakeTable:
    """Just enough of boto3's Table: conditional put, get, in-memory rows."""

    meta = types.SimpleNamespace(
        client=types.SimpleNamespace(
            exceptions=types.SimpleNamespace(
                ConditionalCheckFailedException=ConditionalCheckFailedException
            )
        )
    )

    def __init__(self):
        self.rows: dict[str, dict] = {}

    def put_item(self, Item, ConditionExpression=None):
        if ConditionExpression and Item["job_id"] in self.rows:
            raise ConditionalCheckFailedException()
        self.rows[Item["job_id"]] = dict(Item)

    def get_item(self, Key):
        row = self.rows.get(Key["job_id"])
        return {"Item": row} if row else {}


class FakeLambda:
    """Invoke returns an ARN stamped with the CURRENT version, like the real API."""

    def __init__(self):
        self.version = 1
        self.executions: dict[str, dict] = {}

    def invoke(self, **kw):
        name = kw["DurableExecutionName"]
        self.executions.setdefault(
            name, {"version": self.version, "Status": "SUCCEEDED", "Result": '{"ok":1}'}
        )
        return {
            "DurableExecutionArn": f"arn:fn:{self.version}/durable-execution/{name}"
        }

    def get_durable_execution(self, DurableExecutionArn):
        version, name = DurableExecutionArn.split(":")[-1].split("/durable-execution/")
        execution = self.executions[name]
        if int(version) != execution["version"]:
            raise RuntimeError("Durable Execution does not exist")
        return execution


def _load(half: str, table: FakeTable, lam: FakeLambda):
    """Import before/api.py or after/api.py with boto3 pointed at the fakes."""
    os.environ["JOBS_TABLE"] = "jobs"
    os.environ["JOB_FUNCTION"] = "arn:fn:live"
    boto3.resource = lambda *_: types.SimpleNamespace(Table=lambda _n: table)
    boto3.client = lambda *_: lam
    spec = importlib.util.spec_from_file_location(f"{half}_api", ROOT / half / "api.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _event(method: str, path: str, body=None):
    return {
        "httpMethod": method,
        "path": path,
        "resource": path,
        "pathParameters": None,
        "headers": {"content-type": "application/json"},
        "multiValueHeaders": {},
        "queryStringParameters": None,
        "multiValueQueryStringParameters": None,
        "body": body,
        "isBase64Encoded": False,
        "requestContext": {
            "stage": "prod",
            "requestId": "r",
            "identity": {"sourceIp": "127.0.0.1"},
            "path": f"/prod{path}",
            "httpMethod": method,
        },
    }


def _call(module, method, path, body=None):
    response = module.lambda_handler(_event(method, path, body), None)
    return response["statusCode"], json.loads(response["body"])


@pytest.fixture
def before():
    return _load("before", FakeTable(), FakeLambda())


@pytest.fixture
def after_env():
    table, lam = FakeTable(), FakeLambda()
    return _load("after", table, lam), table, lam


def test_before_create_poll_and_errors(before):
    assert _call(before, "POST", "/v1/jobs", '{"job_id":"j1","input":"x"}') == (
        202,
        {"job_id": "j1", "status": "PENDING"},
    )
    # Duplicate start reports the real state, not a fresh PENDING.
    status, body = _call(before, "POST", "/v1/jobs", '{"job_id":"j1"}')
    assert (status, body["status"]) == (200, "PENDING")
    assert _call(before, "GET", "/v1/jobs/j1")[0] == 200
    assert _call(before, "GET", "/v1/jobs/nope")[0] == 404
    assert _call(before, "POST", "/v1/jobs", "{nope")[0] == 400
    assert _call(before, "PUT", "/v1/jobs/j1")[0] == 405


def test_after_create_and_read(after_env):
    after, table, _ = after_env
    assert _call(after, "POST", "/v2/jobs", '{"job_id":"j2","input":"x"}') == (
        202,
        {"job_id": "j2", "status": "RUNNING"},
    )
    assert table.rows["j2"]["execution_arn"].endswith("/durable-execution/j2")
    status, body = _call(after, "GET", "/v2/jobs/j2")
    assert (status, body["status"], body["result"]) == (200, "DONE", {"ok": 1})
    assert _call(after, "GET", "/v2/jobs/nope")[0] == 404
    assert _call(after, "POST", "/v2/jobs", "{nope")[0] == 400


def test_after_duplicate_start_keeps_original_arn(after_env):
    """A redeploy moves the alias to a new version. A duplicate POST then gets an
    ARN stamped with that new version, but the execution still lives under the
    old one. The row must keep the original ARN or later GETs 404."""
    after, table, lam = after_env
    _call(after, "POST", "/v2/jobs", '{"job_id":"j3","input":"x"}')
    original = table.rows["j3"]["execution_arn"]

    lam.version = 2  # the redeploy
    status, body = _call(after, "POST", "/v2/jobs", '{"job_id":"j3","input":"x"}')
    assert (status, body["status"]) == (200, "DONE")
    assert table.rows["j3"]["execution_arn"] == original
    assert _call(after, "GET", "/v2/jobs/j3")[0] == 200


def test_after_serves_legacy_row(after_env):
    after, table, _ = after_env
    table.rows["old"] = {"job_id": "old", "status": "RUNNING", "step": "transform"}
    status, body = _call(after, "GET", "/v2/jobs/old")
    assert status == 200
    assert body == {
        "job_id": "old",
        "status": "RUNNING",
        "step": "transform",
        "legacy": True,
    }
