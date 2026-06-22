"""Unit tests for migration completeness checks.

Verifies that the Strands SDK migration is complete by checking:
- Obsolete modules are deleted
- Legacy patterns are removed from agent source files
- handler.py no longer references MEMORY_ID
- Dependencies are updated correctly

Requirements: 1.5, 2.3, 2.4, 2.5, 2.6, 4.3, 4.4, 5.1, 5.2, 5.3, 5.4, 9.1, 9.2, 9.3
"""

import os
import re
from pathlib import Path

import pytest

# Paths relative to project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent
AGENT_SRC_DIR = PROJECT_ROOT / "src" / "agent"
REQUIREMENTS_FILE = PROJECT_ROOT / "agent-requirements.txt"


class TestObsoleteModulesDeleted:
    """Verify obsolete modules have been removed from src/agent/."""

    def test_gateway_client_does_not_exist(self) -> None:
        """gateway_client.py must not exist after migration.

        **Validates: Requirements 4.3, 9.1**
        """
        assert not (AGENT_SRC_DIR / "gateway_client.py").exists(), (
            "gateway_client.py should have been deleted during migration"
        )

    def test_memory_client_does_not_exist(self) -> None:
        """memory_client.py must not exist after migration.

        **Validates: Requirements 4.4, 9.2**
        """
        assert not (AGENT_SRC_DIR / "memory_client.py").exists(), (
            "memory_client.py should have been deleted during migration"
        )


class TestHandlerNoMemoryReferences:
    """Verify handler.py does not reference MEMORY_ID."""

    def test_handler_no_memory_id(self) -> None:
        """handler.py must not contain MEMORY_ID references.

        **Validates: Requirements 9.3**
        """
        handler_path = AGENT_SRC_DIR / "handler.py"
        content = handler_path.read_text()
        assert "MEMORY_ID" not in content, (
            "handler.py still references MEMORY_ID — it should have been removed"
        )


class TestNoLegacyPatterns:
    """Verify no agent source files contain legacy manual implementation patterns."""

    LEGACY_PATTERNS = [
        "invoke_model",
        "list_gateway_targets",
        "get_gateway_target",
        "requests.post",
    ]

    # JSON-RPC construction patterns
    JSONRPC_PATTERNS = [
        re.compile(r"""['"]jsonrpc['"]"""),
        re.compile(r"""['"]2\.0['"].*['"]method['"]""", re.DOTALL),
    ]

    def _get_agent_source_files(self) -> list[Path]:
        """Return all .py files in src/agent/ (excluding __pycache__)."""
        return [
            p for p in AGENT_SRC_DIR.glob("*.py")
            if p.name != "__init__.py"
        ]

    @pytest.mark.parametrize("pattern", LEGACY_PATTERNS)
    def test_no_legacy_pattern_in_agent_sources(self, pattern: str) -> None:
        """No agent source file should contain legacy pattern '{pattern}'.

        **Validates: Requirements 1.5, 2.3, 2.4, 2.5, 2.6**
        """
        for source_file in self._get_agent_source_files():
            content = source_file.read_text()
            # Allow the pattern in comments/docstrings that describe what was removed,
            # but not in actual code. We check for the pattern as a code identifier.
            # Skip lines that are pure comments or docstring content.
            for line_num, line in enumerate(content.splitlines(), 1):
                stripped = line.strip()
                # Skip comment-only lines and empty lines
                if stripped.startswith("#") or not stripped:
                    continue
                # Skip lines inside docstrings (triple-quoted strings)
                # A simple heuristic: skip lines that don't contain assignment, call, or import
                if pattern in stripped:
                    # Check it's not just in a string literal (docstring line)
                    # by verifying it appears outside of quotes
                    code_without_strings = re.sub(
                        r'("""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\'|"[^"]*"|\'[^\']*\')',
                        "",
                        stripped,
                    )
                    assert pattern not in code_without_strings, (
                        f"{source_file.name}:{line_num} contains legacy pattern "
                        f"'{pattern}' in code: {stripped}"
                    )

    def test_no_jsonrpc_construction_in_agent_sources(self) -> None:
        """No agent source file should contain JSON-RPC construction patterns.

        **Validates: Requirements 2.6**
        """
        for source_file in self._get_agent_source_files():
            content = source_file.read_text()
            # Remove all string literals (docstrings, comments) to avoid false positives
            code_without_strings = re.sub(
                r'("""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\')', "", content
            )
            code_without_strings = re.sub(r"#.*$", "", code_without_strings, flags=re.MULTILINE)

            for pattern in self.JSONRPC_PATTERNS:
                assert not pattern.search(code_without_strings), (
                    f"{source_file.name} contains JSON-RPC construction pattern"
                )


class TestDependencies:
    """Verify agent-requirements.txt has correct dependencies."""

    def _read_requirements(self) -> list[str]:
        """Read and return non-empty, non-comment lines from requirements file."""
        content = REQUIREMENTS_FILE.read_text()
        return [
            line.strip()
            for line in content.splitlines()
            if line.strip() and not line.strip().startswith("#")
        ]

    def test_contains_strands_agents(self) -> None:
        """agent-requirements.txt must include strands-agents>=1.0.0.

        **Validates: Requirements 5.1**
        """
        reqs = self._read_requirements()
        assert any("strands-agents" in r for r in reqs), (
            "agent-requirements.txt is missing strands-agents dependency"
        )
        assert any("strands-agents>=1.0.0" in r for r in reqs), (
            "agent-requirements.txt should have strands-agents>=1.0.0"
        )

    def test_contains_mcp(self) -> None:
        """agent-requirements.txt must include mcp>=1.0.0.

        **Validates: Requirements 5.2**
        """
        reqs = self._read_requirements()
        assert any("mcp" in r and "mcp" == r.split(">=")[0].split("==")[0].strip() for r in reqs), (
            "agent-requirements.txt is missing mcp dependency"
        )
        assert any("mcp>=1.0.0" in r for r in reqs), (
            "agent-requirements.txt should have mcp>=1.0.0"
        )

    def test_retains_boto3(self) -> None:
        """agent-requirements.txt must retain boto3.

        **Validates: Requirements 5.3**
        """
        reqs = self._read_requirements()
        assert any(r.startswith("boto3") for r in reqs), (
            "agent-requirements.txt is missing boto3 dependency"
        )

    def test_retains_pyjwt(self) -> None:
        """agent-requirements.txt must retain PyJWT.

        **Validates: Requirements 5.3**
        """
        reqs = self._read_requirements()
        assert any(r.startswith("PyJWT") for r in reqs), (
            "agent-requirements.txt is missing PyJWT dependency"
        )

    def test_retains_cryptography(self) -> None:
        """agent-requirements.txt must retain cryptography.

        **Validates: Requirements 5.3**
        """
        reqs = self._read_requirements()
        assert any(r.startswith("cryptography") for r in reqs), (
            "agent-requirements.txt is missing cryptography dependency"
        )

    def test_does_not_contain_requests(self) -> None:
        """agent-requirements.txt must not contain requests dependency.

        **Validates: Requirements 5.4**
        """
        reqs = self._read_requirements()
        # Check that no line is exactly "requests" or starts with "requests=="/"requests>="
        for req in reqs:
            pkg_name = re.split(r"[>=<!\[]", req)[0].strip()
            assert pkg_name != "requests", (
                "agent-requirements.txt should not contain 'requests' dependency"
            )


# ---------------------------------------------------------------------------
# CloudFormation template validation
# ---------------------------------------------------------------------------
import yaml

CFN_TEMPLATE_PATH = PROJECT_ROOT / "infrastructure" / "cloudformation-template.yaml"


class _CfnLoader(yaml.SafeLoader):
    """YAML loader that handles CloudFormation intrinsic function tags."""


# Register constructors for common CloudFormation tags so the template can be parsed.
for _tag in ("!Ref", "!Sub", "!GetAtt", "!Select", "!Join", "!If"):
    _CfnLoader.add_constructor(_tag, lambda loader, node: loader.construct_scalar(node))

for _tag in ("!GetAtt",):
    _CfnLoader.add_constructor(
        _tag, lambda loader, node: (
            loader.construct_sequence(node)
            if isinstance(node, yaml.SequenceNode)
            else loader.construct_scalar(node)
        ),
    )

for _multi_tag in ("!Sub", "!Join", "!Select", "!Split", "!If", "!Equals"):
    _CfnLoader.add_multi_constructor(
        f"tag:yaml.org,2002:{_multi_tag}",
        lambda loader, suffix, node: loader.construct_sequence(node),
    )


def _load_cfn_template() -> dict:
    """Load and parse the CloudFormation template (handling CFN intrinsic tags)."""
    return yaml.load(CFN_TEMPLATE_PATH.read_text(), Loader=_CfnLoader)


def _get_agent_lambda_role_statements(template: dict) -> list[dict]:
    """Return all IAM policy statements from AgentLambdaRole."""
    role = template["Resources"]["AgentLambdaRole"]
    statements: list[dict] = []
    for policy in role["Properties"].get("Policies", []):
        stmts = policy["PolicyDocument"].get("Statement", [])
        statements.extend(stmts)
    return statements


def _collect_all_actions(statements: list[dict]) -> list[str]:
    """Flatten all Action entries across statements into a single list."""
    actions: list[str] = []
    for stmt in statements:
        raw = stmt.get("Action", [])
        if isinstance(raw, str):
            actions.append(raw)
        else:
            actions.extend(raw)
    return actions


class TestCloudFormationIAMActions:
    """Verify Agent Lambda IAM role has correct actions after migration."""

    def _actions(self) -> list[str]:
        template = _load_cfn_template()
        stmts = _get_agent_lambda_role_statements(template)
        return _collect_all_actions(stmts)

    def test_includes_bedrock_converse(self) -> None:
        """IAM actions must include bedrock:Converse.

        **Validates: Requirements 6.1**
        """
        assert "bedrock:Converse" in self._actions()

    def test_includes_bedrock_converse_stream(self) -> None:
        """IAM actions must include bedrock:ConverseStream.

        **Validates: Requirements 6.2**
        """
        assert "bedrock:ConverseStream" in self._actions()

    def test_retains_bedrock_get_gateway(self) -> None:
        """IAM actions must retain bedrock-agentcore:GetGateway.

        **Validates: Requirements 6.3**
        """
        assert "bedrock-agentcore:GetGateway" in self._actions()

    def test_no_list_gateway_targets(self) -> None:
        """IAM actions must NOT include bedrock-agentcore:ListGatewayTargets.

        **Validates: Requirements 9.5**
        """
        assert "bedrock-agentcore:ListGatewayTargets" not in self._actions()

    def test_no_get_gateway_target(self) -> None:
        """IAM actions must NOT include bedrock-agentcore:GetGatewayTarget.

        **Validates: Requirements 9.5**
        """
        assert "bedrock-agentcore:GetGatewayTarget" not in self._actions()


class TestCloudFormationAgentLambdaConfig:
    """Verify Agent Lambda resource configuration after migration."""

    def _agent_lambda(self) -> dict:
        template = _load_cfn_template()
        return template["Resources"]["AgentLambda"]["Properties"]

    def test_timeout_is_120(self) -> None:
        """Agent Lambda timeout must be 120 seconds.

        **Validates: Requirements 7.1**
        """
        assert self._agent_lambda()["Timeout"] == 120

    def test_memory_is_1024(self) -> None:
        """Agent Lambda memory must be 1024 MB.

        **Validates: Requirements 7.2**
        """
        assert self._agent_lambda()["MemorySize"] == 1024

    def test_no_memory_id_env_var(self) -> None:
        """Agent Lambda environment must NOT contain MEMORY_ID.

        **Validates: Requirements 9.4**
        """
        env_vars = self._agent_lambda()["Environment"]["Variables"]
        assert "MEMORY_ID" not in env_vars, (
            "MEMORY_ID environment variable should have been removed"
        )


class TestCloudFormationDurationAlarm:
    """Verify Agent Lambda duration alarm threshold after migration."""

    def test_duration_alarm_threshold_is_100000(self) -> None:
        """AgentLambdaDurationAlarm threshold must be 100000 ms.

        **Validates: Requirements 7.3**
        """
        template = _load_cfn_template()
        alarm = template["Resources"]["AgentLambdaDurationAlarm"]["Properties"]
        assert alarm["Threshold"] == 100000
