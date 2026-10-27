"""
Run the job steps locally, no AWS account needed:

    pip install -r tests/requirements.txt
    pytest tests/

These exercise the shared step code (identical in before/ and after/).
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "after"))

from steps import TransientError, fetch_source, publish_result, transform


def test_happy_path_runs_all_three_steps():
    source = fetch_source("job-ok", {"input": "hello"})
    assert source["bytes"] == len("hello")
    result = transform("job-ok", source, attempt=1)
    assert len(result["digest"]) == 64
    published = publish_result("job-ok", result)
    assert published["published"] is True
    assert published["digest"] == result["digest"]


def test_flaky_input_fails_first_attempt_then_succeeds():
    source = fetch_source("job-flaky", {"input": "this is flaky"})
    with pytest.raises(TransientError):
        transform("job-flaky", source, attempt=1)
    # Second attempt (a redelivery in the after/, a retry loop in the before/) succeeds.
    result = transform("job-flaky", source, attempt=2)
    assert len(result["digest"]) == 64
