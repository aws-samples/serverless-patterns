#!/usr/bin/env python3

import requests
import json
import uuid
import sys

def debug_response(resp):
    print(f"  [DEBUG] Status: {resp.status_code}")
    print(f"  [DEBUG] Headers: {dict(resp.headers)}")
    try:
        print(f"  [DEBUG] Body: {json.dumps(resp.json(), indent=2)}")
    except:
        print(f"  [DEBUG] Body: {resp.text[:500]}")

def test_agent_card(base_url, headers):
    print("\n[TEST] /.well-known/agent-card.json (GET)")
    print(f"  [DEBUG] URL: {base_url}/a2a/.well-known/agent-card.json")
    resp = requests.get(f"{base_url}/a2a/.well-known/agent-card.json", headers=headers)
    debug_response(resp)
    assert resp.status_code == 200, f"Agent card failed: {resp.status_code}"
    data = resp.json()
    required_fields = ["name", "description", "skills"]
    for field in required_fields:
        assert field in data, f"Missing {field} in agent card"
    assert len(data["skills"]) > 0, "Agent must have at least one skill"
    print(f"  [PASS] Agent '{data['name']}' with {len(data['skills'])} skill(s)")

def test_message_send(base_url, headers):
    print("\n[TEST] / (POST message/send)")
    print(f"  [DEBUG] URL: {base_url}/a2a/")
    payload = {
        "jsonrpc": "2.0",
        "id": str(uuid.uuid4()),
        "method": "message/send",
        "params": {
            "message": {
                "role": "user",
                "parts": [{"kind": "text", "text": "Hello, what is 1+1?"}],
                "messageId": str(uuid.uuid4())
            }
        }
    }
    print(f"  [DEBUG] Request: {json.dumps(payload, indent=2)}")
    resp = requests.post(f"{base_url}/a2a/", headers=headers, json=payload)
    debug_response(resp)
    assert resp.status_code == 200, f"Message send failed: {resp.status_code}"
    data = resp.json()
    assert "jsonrpc" in data, "Missing jsonrpc in response"
    assert data["jsonrpc"] == "2.0", "Invalid jsonrpc version"
    assert "id" in data, "Missing id in response"
    if "error" in data:
        print(f"  [WARN] Error response: {data['error']}")
    else:
        assert "result" in data, "Missing result in response"
        print(f"  [PASS] Got valid JSON-RPC response")

def main():
    import os
    base_url = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else os.environ.get("CF_URL", "").rstrip("/")
    token = sys.argv[2] if len(sys.argv) > 2 else os.environ.get("BEARER_TOKEN", "")
    
    if not base_url or not token:
        print("Usage: python test_a2a.py <cloudfront_url> <bearer_token>")
        print("Or set CF_URL and BEARER_TOKEN environment variables")
        sys.exit(1)
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    print("=" * 60)
    print("A2A Protocol Validation")
    print("=" * 60)
    print(f"Base URL: {base_url}")
    print(f"Token: {token[:20]}...")
    
    try:
        test_agent_card(base_url, headers)
        test_message_send(base_url, headers)
        print("\n" + "=" * 60)
        print("All tests passed!")
        print("=" * 60)
    except AssertionError as e:
        print(f"\n[FAIL] {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n[ERROR] {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
