from __future__ import annotations

from typing import Any, Dict, Optional
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
import json
import time


class EndpointError(RuntimeError):
    pass


# Idempotent methods may be safely retried on a 5xx response. A non-idempotent
# POST (e.g. /analysis/start, which re-runs the whole scenario suite server-side)
# must NOT be retried on 5xx, or a single failure multiplies the work.
_IDEMPOTENT_METHODS = {"GET", "HEAD", "PUT", "DELETE", "OPTIONS"}
_RETRIABLE_STATUS = {429, 500, 502, 503, 504}


def request_json(
    method: str,
    url: str,
    *,
    token: Optional[str] = None,
    port: int = 8080,
    payload: Optional[Dict[str, Any]] = None,
    timeout: float = 20.0,
    retries: int = 3,
    raw: bool = False,
):
    """Make an authenticated request to a MicroVM endpoint.

    Returns the parsed JSON dict by default, or raw ``bytes`` when ``raw=True``
    (used for ``events.jsonl`` and other non-JSON artifacts).
    """
    body = None if payload is None else json.dumps(payload).encode("utf-8")
    accept = "application/octet-stream" if raw else "application/json"
    headers = {"Accept": accept, "X-aws-proxy-port": str(port)}
    if body is not None:
        headers["Content-Type"] = "application/json"
    if token:
        headers["X-aws-proxy-auth"] = token
    # 429 (throttling) is always safe to retry; other 5xx only for idempotent methods.
    retriable_status = {429} if method.upper() not in _IDEMPOTENT_METHODS else _RETRIABLE_STATUS
    last_error: Optional[BaseException] = None
    for attempt in range(1, retries + 1):
        try:
            req = Request(url, data=body, headers=headers, method=method)
            with urlopen(req, timeout=timeout) as resp:  # nosec B310 - endpoint is Lambda MicroVM URL from AWS
                raw_bytes = resp.read()
            if raw:
                return raw_bytes
            decoded = raw_bytes.decode("utf-8")
            return json.loads(decoded) if decoded else {}
        except HTTPError as exc:
            raw = exc.read().decode("utf-8", errors="replace")
            if exc.code in retriable_status and attempt < retries:
                last_error = exc
                time.sleep(min(10.0, 2 ** attempt))
                continue
            raise EndpointError(f"HTTP {exc.code} from {url}: {raw}") from exc
        except (URLError, TimeoutError, OSError) as exc:
            last_error = exc
            if attempt < retries:
                time.sleep(min(10.0, 2 ** attempt))
                continue
            raise EndpointError(f"Request to {url} failed after {retries} attempts: {exc}") from exc
    raise EndpointError(f"Request to {url} failed: {last_error}")
