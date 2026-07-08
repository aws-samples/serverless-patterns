"""Unit tests for the SAM deploy script (scripts/deploy.sh) and Makefile build.

After the migration from raw CloudFormation to AWS SAM:
  - Orchestration (validate / build / deploy) lives in scripts/deploy.sh and
    uses the `sam` CLI.
  - Lambda packaging (the two-step pip3 install) lives in the root Makefile,
    invoked by `sam build` via BuildMethod: makefile (no Docker required).
"""

import os
import re

_SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "scripts", "deploy.sh"
)
_MAKEFILE_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "Makefile"
)

with open(_SCRIPT_PATH) as _fh:
    DEPLOY_CONTENT = _fh.read()

with open(_MAKEFILE_PATH) as _fh:
    MAKEFILE_CONTENT = _fh.read()


# ── Makefile: two-step pip3 install (packaging moved out of deploy.sh) ──

class TestTwoStepPipInstall:
    """Verify the two-step pip3 install pattern lives in the Makefile."""

    def test_first_step_has_only_binary(self):
        """First pip3 install uses --only-binary=:all:"""
        first_pip = re.search(
            r"pip3\s+install\b.*?--only-binary=:all:", MAKEFILE_CONTENT, re.DOTALL
        )
        assert first_pip is not None, "First pip3 install must use --only-binary=:all:"

    def test_first_step_has_platform_targeting(self):
        """First pip3 install targets manylinux2014_x86_64."""
        assert re.search(
            r"pip3\s+install\b.*--platform\s+manylinux2014_x86_64", MAKEFILE_CONTENT, re.DOTALL
        ), "First pip3 install must target --platform manylinux2014_x86_64"

    def test_first_step_has_python_version(self):
        """First pip3 install specifies --python-version 3.12."""
        assert re.search(
            r"pip3\s+install\b.*--python-version\s+3\.12", MAKEFILE_CONTENT, re.DOTALL
        ), "First pip3 install must specify --python-version 3.12"

    def test_second_step_has_no_deps(self):
        """Second pip3 install uses --no-deps for pure Python packages."""
        no_deps_match = re.search(
            r"pip3\s+install\b.*?--no-deps", MAKEFILE_CONTENT, re.DOTALL
        )
        assert no_deps_match is not None, "Second pip3 install must use --no-deps"

    def test_second_step_includes_pure_python_packages(self):
        """Second step installs the expected pure Python packages."""
        no_deps_section = re.search(
            r"pip3\s+install\b.*?--no-deps\b(.*)", MAKEFILE_CONTENT, re.DOTALL
        )
        assert no_deps_section is not None
        block = no_deps_section.group(0)
        for pkg in ["requests", "urllib3", "charset-normalizer", "idna", "certifi", "PyJWT", "cryptography", "cffi"]:
            assert pkg in block, f"Second pip3 install must include {pkg}"

    def test_at_least_two_pip3_install_commands(self):
        """There should be at least two pip3 install invocations (binary + pure Python)."""
        invocations = re.findall(r"\bpip3\s+install\b", MAKEFILE_CONTENT)
        assert len(invocations) >= 2, f"Expected at least 2 pip3 install commands, found {len(invocations)}"


# ── No .dist-info removal ──

class TestNoDistInfoRemoval:
    def test_no_dist_info_removal(self):
        """Neither the Makefile nor deploy.sh must remove .dist-info directories."""
        combined = MAKEFILE_CONTENT + "\n" + DEPLOY_CONTENT
        assert not re.search(r"rm\s.*\.dist-info", combined), (
            "Must not remove .dist-info directories"
        )
        assert not re.search(r"find.*\.dist-info.*-delete", combined), (
            "Must not delete .dist-info via find"
        )


# ── SAM build handles packaging + artifact upload ──

class TestSamBuildAndDeploy:
    def test_uses_sam_build(self):
        """Script builds the Lambda with `sam build`."""
        assert re.search(r"\bsam\s+build\b", DEPLOY_CONTENT), "Script must call sam build"

    def test_uses_sam_deploy(self):
        """Script deploys with `sam deploy`."""
        assert re.search(r"\bsam\s+deploy\b", DEPLOY_CONTENT), "Script must call sam deploy"

    def test_sam_deploy_has_named_iam_capability(self):
        """SAM deploy must pass CAPABILITY_NAMED_IAM for the named roles."""
        assert "CAPABILITY_NAMED_IAM" in DEPLOY_CONTENT

    def test_sam_deploy_resolves_artifact_bucket(self):
        """SAM deploy manages the artifact bucket via --resolve-s3."""
        assert "--resolve-s3" in DEPLOY_CONTENT

    def test_makefile_build_method(self):
        """The Makefile exposes the SAM build target for the function."""
        assert "build-AgentLambdaFunction" in MAKEFILE_CONTENT


# ── Required dependencies ──

class TestRequiredDependencies:
    def test_requirements_txt_referenced(self):
        """Makefile references requirements.txt for pip install."""
        assert "requirements.txt" in MAKEFILE_CONTENT


# ── Template validation before deployment ──

class TestTemplateValidation:
    def test_validate_template_before_deploy(self):
        """Script validates the SAM template before deploying."""
        validate_pos = DEPLOY_CONTENT.find("sam validate")
        deploy_pos = DEPLOY_CONTENT.find("sam deploy")
        assert validate_pos != -1, "Script must call sam validate"
        assert deploy_pos != -1, "Script must call sam deploy"
        assert validate_pos < deploy_pos, "sam validate must come before sam deploy"

    def test_references_sam_template(self):
        """Script references the SAM template path."""
        assert "infrastructure/template.yaml" in DEPLOY_CONTENT


# ── Smithy model upload (must precede stack deploy) ──

class TestSmithyModelUpload:
    def test_uploads_smithy_model_to_s3(self):
        """Script uploads the Smithy model with `aws s3 cp`."""
        assert re.search(r"aws\s+s3\s+cp\b", DEPLOY_CONTENT), (
            "Script must upload the Smithy model with aws s3 cp"
        )

    def test_smithy_upload_before_deploy(self):
        """Smithy model must be in S3 before the stack (and its target) deploys."""
        upload_pos = DEPLOY_CONTENT.find("aws s3 cp")
        deploy_pos = DEPLOY_CONTENT.find("sam deploy")
        assert upload_pos != -1 and deploy_pos != -1
        assert upload_pos < deploy_pos, "Smithy upload must precede sam deploy"


# ── Cognito test user creation ──

class TestCognitoUser:
    def test_creates_cognito_user(self):
        """Script creates a Cognito test user."""
        assert "admin-create-user" in DEPLOY_CONTENT
        assert "admin-set-user-password" in DEPLOY_CONTENT


# ── pip3 exclusively (in the Makefile) ──

class TestPip3Exclusively:
    def test_all_pip_commands_use_pip3(self):
        """All pip install commands use pip3, not bare pip."""
        invocations = re.findall(r"\b(pip3?)\s+install\b", MAKEFILE_CONTENT)
        assert len(invocations) > 0, "Must have pip install commands"
        for inv in invocations:
            assert inv == "pip3", f"Found bare '{inv}' instead of 'pip3'"


# ── No credential provider commands ──

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
