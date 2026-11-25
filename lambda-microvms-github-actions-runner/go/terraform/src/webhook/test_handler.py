"""Unit tests for handler.py's MicroVM launch and secret handling (Secrets
Manager stubbed, GitHub and AWS calls mocked, no AWS or network calls).

Run from src/webhook/: pip install -r requirements.txt pytest && python3 -m pytest -v
"""
import email.message
import hashlib
import hmac
import json
import os
import urllib.error

import pytest
from botocore.stub import Stubber

# handler.py reads its config from the environment at import time.
os.environ.update(
    {
        "AWS_DEFAULT_REGION": "us-east-1",
        "AWS_ACCESS_KEY_ID": "testing",
        "AWS_SECRET_ACCESS_KEY": "testing",
        "GITHUB_OWNER": "example-owner",
        "GITHUB_REPO": "example-repo",
        "PAT_SECRET_ARN": "arn:aws:secretsmanager:us-east-1:ACCOUNT:secret:pat",
        "WEBHOOK_SECRET_ARN": "arn:aws:secretsmanager:us-east-1:ACCOUNT:secret:webhook",
        "MICROVM_IMAGE_ARN": "arn:aws:lambda:us-east-1:ACCOUNT:microvm-image:example-runner-image",
        "MICROVM_EXECUTION_ROLE_ARN": "arn:aws:iam::ACCOUNT:role/example-exec",
        "JIT_BUCKET": "example-jit",
    }
)

import handler

# --- Secret handling -------------------------------------------------------

PAT_ARN = os.environ["PAT_SECRET_ARN"]
WEBHOOK_ARN = os.environ["WEBHOOK_SECRET_ARN"]
FAKE_PAT = "github_pat_FAKE0123456789abcdefTOKEN"
WEBHOOK_SECRET = "test-webhook-secret"


@pytest.fixture
def secrets(monkeypatch):
    monkeypatch.setattr(handler, "_cache", {})
    clock = {"now": 1000.0}
    monkeypatch.setattr(handler.time, "monotonic", lambda: clock["now"])
    with Stubber(handler._secrets) as stub:
        stub.clock = clock
        yield stub
        stub.assert_no_pending_responses()


def _add_secret(stub, arn, value):
    stub.add_response("get_secret_value", {"SecretString": value}, {"SecretId": arn})


def _queued_event(secret=WEBHOOK_SECRET):
    body = json.dumps(
        {"action": "queued", "workflow_job": {"id": 7, "labels": ["self-hosted", "lambda"]}}
    )
    sig = "sha256=" + hmac.new(secret.encode(), body.encode(), hashlib.sha256).hexdigest()
    return {"body": body, "headers": {"X-GitHub-Event": "workflow_job", "X-Hub-Signature-256": sig}}


def _logged(capsys, caplog):
    out, err = capsys.readouterr()
    return out + err + caplog.text


def test_secret_whitespace_is_stripped(secrets):
    _add_secret(secrets, PAT_ARN, f"  {FAKE_PAT}\n")
    assert handler._secret(PAT_ARN) == FAKE_PAT


def test_empty_secret_returns_500_without_leaking(secrets, capsys, caplog):
    _add_secret(secrets, WEBHOOK_ARN, " \n\t")
    resp = handler.handler(_queued_event(), None)
    assert resp == {"statusCode": 500, "body": "internal error"}
    assert WEBHOOK_ARN not in handler._cache  # an empty value is never cached
    logged = _logged(capsys, caplog)
    assert "is empty" in logged
    assert WEBHOOK_SECRET not in logged


def test_github_error_embedding_token_is_not_logged(secrets, monkeypatch, capsys, caplog):
    _add_secret(secrets, WEBHOOK_ARN, WEBHOOK_SECRET)
    _add_secret(secrets, PAT_ARN, FAKE_PAT)

    def urlopen(req, timeout):
        # What http.client raised in the live run (token with a trailing newline).
        raise ValueError(f"Invalid header value b'Bearer {FAKE_PAT}\\n'")

    monkeypatch.setattr(handler.urllib.request, "urlopen", urlopen)
    resp = handler.handler(_queued_event(), None)
    assert resp == {"statusCode": 500, "body": "internal error"}
    logged = _logged(capsys, caplog)
    assert "generate-jitconfig failed (ValueError)" in logged
    assert FAKE_PAT not in logged
    assert "Bearer" not in logged


def test_github_401_drops_cached_pat(secrets, monkeypatch, capsys, caplog):
    _add_secret(secrets, PAT_ARN, FAKE_PAT)
    _add_secret(secrets, PAT_ARN, "github_pat_ROTATED")

    def urlopen(req, timeout):
        raise urllib.error.HTTPError(req.full_url, 401, "Unauthorized", email.message.Message(), None)

    monkeypatch.setattr(handler.urllib.request, "urlopen", urlopen)
    with pytest.raises(handler.SafeError, match="HTTP 401 Unauthorized"):
        handler._generate_jitconfig("lambda-jit-7")
    assert PAT_ARN not in handler._cache
    assert handler._secret(PAT_ARN) == "github_pat_ROTATED"  # refetched, within TTL
    assert FAKE_PAT not in _logged(capsys, caplog)


def test_secret_refetched_after_ttl(secrets):
    _add_secret(secrets, PAT_ARN, FAKE_PAT)
    _add_secret(secrets, PAT_ARN, "github_pat_ROTATED")
    assert handler._secret(PAT_ARN) == FAKE_PAT
    secrets.clock["now"] += handler.SECRET_CACHE_TTL - 1
    assert handler._secret(PAT_ARN) == FAKE_PAT  # no second Secrets Manager call
    secrets.clock["now"] += 1
    assert handler._secret(PAT_ARN) == "github_pat_ROTATED"


def test_handler_launches_configured_image(monkeypatch):
    monkeypatch.setattr(handler, "_secret", lambda _arn: WEBHOOK_SECRET)
    monkeypatch.setattr(handler, "_generate_jitconfig", lambda _name: "jit")
    monkeypatch.setattr(handler._s3, "put_object", lambda **_kw: None)
    monkeypatch.setattr(handler._s3, "generate_presigned_url", lambda *_a, **_kw: "https://example/presigned")
    calls = []

    def run_microvm(**kwargs):
        calls.append(kwargs)
        return {"microvmId": "mvm-1"}

    monkeypatch.setattr(handler._microvms, "run_microvm", run_microvm)
    resp = handler.handler(_queued_event(), None)
    assert resp["statusCode"] == 202
    assert calls[0]["imageIdentifier"] == os.environ["MICROVM_IMAGE_ARN"]
    assert "imageVersion" not in calls[0]
