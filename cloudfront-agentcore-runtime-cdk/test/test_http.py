#!/usr/bin/env python3

import requests
import json
import sys

def debug_response(resp):
    print(f"  [DEBUG] Status: {resp.status_code}")
    print(f"  [DEBUG] Headers: {dict(resp.headers)}")
    try:
        print(f"  [DEBUG] Body: {resp.text[:500]}")
    except:
        print(f"  [DEBUG] Body: {resp.text}")

def test_invocations(base_url, headers):
    print("\n[TEST] /rest/invocations (POST)")
    print(f"  [DEBUG] URL: {base_url}/rest/invocations")
    payload = {"prompt": "What is 2+2?"}
    print(f"  [DEBUG] Request: {json.dumps(payload, indent=2)}")
    resp = requests.post(f"{base_url}/rest/invocations", headers=headers, json=payload, stream=True)
    print(f"  [DEBUG] Status: {resp.status_code}")
    print(f"  [DEBUG] Headers: {dict(resp.headers)}")
    assert resp.status_code == 200, f"Invocations failed: {resp.status_code}"
    
    content_type = resp.headers.get("content-type", "")
    if "text/event-stream" in content_type:
        print("  [DEBUG] Streaming response (SSE):")
        for line in resp.iter_lines():
            if line:
                print(f"    {line.decode('utf-8')}")
        print(f"  [PASS] Got streaming response")
    else:
        print(f"  [DEBUG] Body: {resp.text[:500]}")
        print(f"  [PASS] Got response")

def main():
    import os
    base_url = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else os.environ.get("CF_URL", "").rstrip("/")
    token = sys.argv[2] if len(sys.argv) > 2 else os.environ.get("BEARER_TOKEN", "")
    
    if not base_url or not token:
        print("Usage: python test_http.py <cloudfront_url> <bearer_token>")
        print("Or set CF_URL and BEARER_TOKEN environment variables")
        sys.exit(1)
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    print("=" * 60)
    print("HTTP Protocol Validation")
    print("=" * 60)
    print(f"Base URL: {base_url}")
    print(f"Token: {token[:20]}...")
    
    try:
        test_invocations(base_url, headers)
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
