import json
import pathlib

import app

EVENT = json.loads((pathlib.Path(__file__).resolve().parents[1] / "events" / "event.json").read_text())


def test_parse_records():
    messages = app.parse_records(EVENT)
    assert len(messages) == 10
    assert messages[0]["topic"] == "KafkaOAuthBearerLambdaTopic"
    assert messages[0]["partition"] == 1
    assert messages[0]["offset"] == 208
    assert messages[0]["timestamp"] == 1790996330920
    assert messages[0]["timestampType"] == "CREATE_TIME"
    assert messages[0]["decodedKey"] == "jthomas@example.org"
    person = json.loads(messages[0]["decodedValue"])
    assert person["firstName"] == "George"
    assert person["lastName"] == "Yang"
    assert person["email"] == "jthomas@example.org"
    assert messages[1]["offset"] == 209
    assert messages[1]["decodedKey"] == "robert96@example.org"


def test_handler_returns_200_without_table(monkeypatch):
    # With no DYNAMODB_TABLE_NAME set, the handler parses/logs but skips DynamoDB.
    monkeypatch.delenv("DYNAMODB_TABLE_NAME", raising=False)
    assert app.lambda_handler(EVENT, None) == "200 OK"
