"""Property-based tests for the Makefile build (Property 7).

Feature: agentcore-smithy-bedrock
Property 7: Lambda packaging uses pip3 exclusively
  Validates: pip3-only packaging

After the migration to AWS SAM, Lambda packaging (the pip install steps)
lives in the root Makefile, invoked by `sam build` via BuildMethod: makefile.
This property verifies every pip install invocation uses pip3, not bare pip.
"""

import os
import re

from hypothesis import given, settings
from hypothesis import strategies as st

# ---------------------------------------------------------------------------
# Load Makefile content (packaging now lives here, not in deploy.sh)
# ---------------------------------------------------------------------------

_MAKEFILE_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "Makefile"
)

with open(_MAKEFILE_PATH) as _fh:
    _MAKEFILE_CONTENT = _fh.read()

# Find all pip/pip3 install invocations
_PIP_INVOCATIONS = re.findall(r"\b(pip3?)\s+install\b", _MAKEFILE_CONTENT)

assert len(_PIP_INVOCATIONS) > 0, "No pip install commands found in Makefile"

pip_invocation_st = st.sampled_from(_PIP_INVOCATIONS)

# ---------------------------------------------------------------------------
# Property 7: Lambda packaging uses pip3 exclusively
# Tag: Feature: agentcore-smithy-bedrock, Property 7: Lambda packaging uses
#      pip3 exclusively
# ---------------------------------------------------------------------------


@given(invocation=pip_invocation_st)
@settings(max_examples=100)
def test_property7_all_pip_commands_use_pip3(invocation):
    """For all pip install commands in the Makefile, each command shall
    use pip3 (not pip) as the executable name."""
    assert invocation == "pip3", (
        "Found bare 'pip' instead of 'pip3' in Makefile"
    )
