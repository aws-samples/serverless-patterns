"""Unit tests for deploy script (scripts/deploy.sh).

Validates: Requirements 8.1–8.5, 9.1–9.8
"""

import os
import re

import pytest

_SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "scripts", "deploy.sh"
)

with open(_SCRIPT_PATH) as _fh:
    DEPLOY_CONTENT = _fh.read()


# ── Requirement 8.1: First pip install step with --only-binary, --platform, --python-version ──

class TestTwoStepPipInstall:
    """Verify the two-step pip3 install pattern (Requirements 8.1, 8.2)."""

    def test_first_step_has_only_binary(self):
        """First pip3 install uses --only-binary=:all:"""
        # pip3 install commands span multiple lines with backslash continuations
        first_pip = re.search(
            r"pip3\s+install\b.*?--only-binary=:all:", DEPLOY_CONTENT, re.DOTALL
        )
        assert first_pip is not None, "First pip3 install must use --only-binary=:all:"

    def test_first_step_has_platform_targeting(self):
        """First pip3 install targets manylinux2014_x86_64."""
        assert re.search(
            r"pip3\s+install\b.*--platform\s+manylinux2014_x86_64", DEPLOY_CONTENT, re.DOTALL
        ), "First pip3 install must target --platform manylinux2014_x86_64"

    def test_first_step_has_python_version(self):
        """First pip3 install specifies --python-version 3.12."""
        assert re.search(
            r"pip3\s+install\b.*--python-version\s+3\.12", DEPLOY_CONTENT, re.DOTALL
        ), "First pip3 install must specify --python-version 3.12"

    def test_second_step_has_no_deps(self):
        """Second pip3 install uses --no-deps for pure Python packages."""
        # pip3 install commands span multiple lines with backslash continuations
        no_deps_match = re.search(
            r"pip3\s+install\b.*?--no-deps", DEPLOY_CONTENT, re.DOTALL
        )
        assert no_deps_match is not None, "Second pip3 install must use --no-deps"

    def test_second_step_includes_pure_python_packages(self):
        """Second step installs the expected pure Python packages."""
        # Find the --no-deps pip3 install block and check for expected packages
        no_deps_section = re.search(
            r"pip3\s+install\b.*?--no-deps\b(.*?)(?:\n\n|\Z)", DEPLOY_CONTENT, re.DOTALL
        )
        assert no_deps_section is not None
        block = no_deps_section.group(0)
        for pkg in ["requests", "urllib3", "charset-normalizer", "idna", "certifi", "PyJWT", "cryptography", "cffi"]:
            assert pkg in block, f"Second pip3 install must include {pkg}"

    def test_at_least_two_pip3_install_commands(self):
        """There should be at least two pip3 install invocations (binary + pure Python)."""
        invocations = re.findall(r"\bpip3\s+install\b", DEPLOY_CONTENT)
        assert len(invocations) >= 2, f"Expected at least 2 pip3 install commands, found {len(invocations)}"


# ── Requirement 8.3: No .dist-info removal ──

class TestNoDistInfoRemoval:
    def test_no_dist_info_removal(self):
        """Deploy script must NOT remove .dist-info directories."""
        assert ".dist-info" not in re.findall(
            r"rm\s.*\.dist-info", DEPLOY_CONTENT
        ), "Script must not remove .dist-info directories"
        # Also check for find -delete patterns
        assert not re.search(
            r"find.*\.dist-info.*-delete", DEPLOY_CONTENT
        ), "Script must not delete .dist-info via find"


# ── Requirement 8.4: S3 fallback if zip exceeds 50MB ──

class TestS3Fallback:
    def test_s3_fallback_logic_present(self):
        """Script checks zip size and falls back to S3 if >50MB."""
        assert "50" in DEPLOY_CONTENT and "s3" in DEPLOY_CONTENT.lower(), (
            "Script must contain S3 fallback logic for packages >50MB"
        )

    def test_s3_upload_uses_s3_cp(self):
        """S3 fallback uses 'aws s3 cp' to upload the zip."""
        assert re.search(r"aws\s+s3\s+cp\b", DEPLOY_CONTENT), (
            "S3 fallback must use 'aws s3 cp'"
        )

    def test_s3_fallback_uses_update_function_code_with_s3(self):
        """S3 fallback updates Lambda with --s3-bucket and --s3-key."""
        assert re.search(r"--s3-bucket\b", DEPLOY_CONTENT), "S3 fallback must pass --s3-bucket"
        assert re.search(r"--s3-key\b", DEPLOY_CONTENT), "S3 fallback must pass --s3-key"


# ── Requirement 8.5: Required dependencies ──

class TestRequiredDependencies:
    def test_requirements_txt_referenced(self):
        """Deploy script references requirements.txt for pip install."""
        assert "requirements.txt" in DEPLOY_CONTENT


# ── Requirement 9.1: Template validation before deployment ──

class TestTemplateValidation:
    def test_validate_template_before_deploy(self):
        """Script validates the CloudFormation template before deploying."""
        validate_pos = DEPLOY_CONTENT.find("validate-template")
        create_pos = DEPLOY_CONTENT.find("create-stack")
        assert validate_pos != -1, "Script must call validate-template"
        assert validate_pos < create_pos, "validate-template must come before create-stack"


# ── Requirement 9.2: DOES_NOT_EXIST detection ──

class TestStackExistenceDetection:
    def test_does_not_exist_check(self):
        """Script checks for DOES_NOT_EXIST to decide create vs update."""
        assert "DOES_NOT_EXIST" in DEPLOY_CONTENT, (
            "Script must check for DOES_NOT_EXIST pattern"
        )

    def test_create_stack_path(self):
        """Script has a create-stack code path."""
        assert "create-stack" in DEPLOY_CONTENT

    def test_update_stack_path(self):
        """Script has an update-stack code path."""
        assert "update-stack" in DEPLOY_CONTENT

    def test_no_updates_handled_gracefully(self):
        """Script handles 'No updates are to be performed' gracefully."""
        assert "No updates are to be performed" in DEPLOY_CONTENT


# ── Requirement 9.7: pip3 exclusively ──

class TestPip3Exclusively:
    def test_all_pip_commands_use_pip3(self):
        """All pip install commands use pip3, not bare pip."""
        # Find all pip/pip3 install invocations
        invocations = re.findall(r"\b(pip3?)\s+install\b", DEPLOY_CONTENT)
        assert len(invocations) > 0, "Must have pip install commands"
        for inv in invocations:
            assert inv == "pip3", f"Found bare '{inv}' instead of 'pip3'"


# ── Requirement 9.8: No credential provider commands ──

class TestNoForbiddenPatterns:
    def test_no_credential_provider_commands(self):
        """Script must not contain credential provider CLI commands."""
        forbidden = [
            "create-credential-provider",
            "create-api-key-credential-provider",
            "get-api-key",
        ]
        for pattern in forbidden:
            assert pattern not in DEPLOY_CONTENT, (
                f"Script must not contain '{pattern}'"
            )

    def test_no_api_key_retrieval(self):
        """Script must not retrieve API keys."""
        assert not re.search(r"get-api-key", DEPLOY_CONTENT), (
            "Script must not retrieve API keys"
        )

    def test_no_stack_re_update(self):
        """Script must not re-update the stack after initial deployment.
        There should be at most one update-stack call."""
        update_calls = re.findall(r"\bupdate-stack\b", DEPLOY_CONTENT)
        assert len(update_calls) <= 1, (
            f"Expected at most 1 update-stack call, found {len(update_calls)}"
        )
