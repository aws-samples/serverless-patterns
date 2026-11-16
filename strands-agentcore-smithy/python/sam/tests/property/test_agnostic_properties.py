"""Property-based tests for agent code target-type agnosticism (Property 8).

Feature: agentcore-smithy-bedrock
Property 8: Agent code is target-type agnostic
  Validates: Requirements 11.1

Scans all Python source files in src/agent/ and src/shared/ to verify that
none contain DynamoDB-specific or Smithy-specific identifiers.
"""

import os
import re

from hypothesis import given, settings, assume
from hypothesis import strategies as st

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_SRC_ROOT = os.path.join(os.path.dirname(__file__), "..", "..", "src")

# Identifiers that must NOT appear in agent/shared code.
# Case-insensitive patterns for DynamoDB and Smithy references.
_FORBIDDEN_PATTERNS: list[re.Pattern] = [
    re.compile(r"\bdynamodb\b", re.IGNORECASE),
    re.compile(r"\bGetItem\b"),
    re.compile(r"\bPutItem\b"),
    re.compile(r"\bQuery\b"),
    re.compile(r"\bTableName\b"),
    re.compile(r"\bsmithy\b", re.IGNORECASE),
    re.compile(r"\bSmithyModel\b"),
    re.compile(r"\bInlinePayload\b"),
]

_SOURCE_DIRS = ["agent", "shared"]


def _collect_source_files() -> list[str]:
    """Return all .py files under src/agent/ and src/shared/."""
    files: list[str] = []
    for subdir in _SOURCE_DIRS:
        dirpath = os.path.join(_SRC_ROOT, subdir)
        if not os.path.isdir(dirpath):
            continue
        for fname in os.listdir(dirpath):
            if fname.endswith(".py"):
                files.append(os.path.join(dirpath, fname))
    return files


_SOURCE_FILES = _collect_source_files()
_SOURCE_CONTENTS: dict[str, str] = {}
for _f in _SOURCE_FILES:
    with open(_f) as _fh:
        _SOURCE_CONTENTS[_f] = _fh.read()


# ---------------------------------------------------------------------------
# Property 8: Agent code is target-type agnostic
# Tag: Feature: agentcore-smithy-bedrock, Property 8: Agent code is
#      target-type agnostic
# ---------------------------------------------------------------------------

# Strategy: pick a random source file and a random forbidden pattern,
# then assert the pattern does not appear in that file.

source_file_st = st.sampled_from(list(_SOURCE_CONTENTS.keys()))
forbidden_pattern_st = st.sampled_from(_FORBIDDEN_PATTERNS)


@given(filepath=source_file_st, pattern=forbidden_pattern_st)
@settings(max_examples=100)
def test_property8_no_dynamodb_or_smithy_identifiers(filepath, pattern):
    """For all source files in src/agent/ and src/shared/, none shall
    contain DynamoDB-specific or Smithy-specific identifiers."""
    content = _SOURCE_CONTENTS[filepath]
    matches = pattern.findall(content)
    rel = os.path.relpath(filepath, _SRC_ROOT)
    assert not matches, (
        f"{rel} contains forbidden identifier matching /{pattern.pattern}/: {matches}"
    )
