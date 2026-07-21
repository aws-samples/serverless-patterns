"""Property-based tests for deploy script (Property 7).

Feature: agentcore-smithy-bedrock
Property 7: Deploy script uses pip3 exclusively
  Validates: Requirements 9.7
"""

import os
import re

from hypothesis import given, settings
from hypothesis import strategies as st

# ---------------------------------------------------------------------------
# Load deploy script content
# ---------------------------------------------------------------------------

_SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "scripts", "deploy.sh"
)

with open(_SCRIPT_PATH) as _fh:
    _SCRIPT_CONTENT = _fh.read()

# Extract all lines that contain pip install commands (pip or pip3)
_PIP_COMMAND_PATTERN = re.compile(r"^\s*(pip3?|pip)\s+install\b", re.MULTILINE)
_PIP_LINES = [
    (i + 1, line)
    for i, line in enumerate(_SCRIPT_CONTENT.splitlines())
    if _PIP_COMMAND_PATTERN.search(line)
]

# Also find continuation lines that start a pip/pip3 command
_PIP_INVOCATIONS = re.findall(r"\b(pip3?)\s+install\b", _SCRIPT_CONTENT)

assert len(_PIP_INVOCATIONS) > 0, "No pip install commands found in deploy script"

pip_invocation_st = st.sampled_from(_PIP_INVOCATIONS)

# ---------------------------------------------------------------------------
# Property 7: Deploy script uses pip3 exclusively
# Tag: Feature: agentcore-smithy-bedrock, Property 7: Deploy script uses
#      pip3 exclusively
# ---------------------------------------------------------------------------


@given(invocation=pip_invocation_st)
@settings(max_examples=100)
def test_property7_all_pip_commands_use_pip3(invocation):
    """For all pip install commands in the deploy script, each command shall
    use pip3 (not pip) as the executable name."""
    assert invocation == "pip3", (
        f"Found bare 'pip' instead of 'pip3' in deploy script"
    )
