"""Unit tests for the SAM deploy script (scripts/deploy.sh) and Makefile build.

After the migration to AWS SAM:
  - Orchestration (validate / build / deploy) lives in scripts/deploy.sh
    and uses the `sam` CLI.
  - Lambda packaging (the two-step pip3 install) lives in the root Makefile,
    invoked by `sam build` via BuildMethod: makefile (no Docker required).
  - The Smithy model S3 bucket name includes the AWS account ID for
    global uniqueness.
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


# ── Makefile: two-step pip3 install (packaging lives here, not deploy.sh) ──

class TestTwoStepPipInstall:
    """Verify the two-step pip3 install pattern lives in the Makefile."""

    def test_first_step_has_only_binary(self):
        first_pip = re.search(
            r"pip3\s+install\b.*?--only-binary=:all:", MAKEFILE_CONTENT, re.DOTALL
        )
        assert first_pip is not None, "First pip3 install must use --only-binary=:all:"

    def test_first_step_has_platform_targeting(self):
        assert re.search(
            r"pip3\s+install\b.*--platform\s+manylinux2014_x86_64", MAKEFILE_CONTENT, re.DOTALL
        ), "First pip3 install must target --platform manylinux2014_x86_64"

    def test_first_step_has_python_version(self):
        assert re.search(
            r"pip3\s+install\b.*--python-version\s+3\.13", MAKEFILE_CONTENT, re.DOTALL
        ), "First pip3 install must specify --python-version 3.13"

    def test_second_step_has_no_deps(self):
        assert re.search(
            r"pip3\s+install\b.*?--no-deps", MAKEFILE_CONTENT, re.DOTALL
        ), "Second pip3 install must use --no-deps"

    def test_second_step_includes_pure_python_packages(self):
        no_deps_section = re.search(
            r"pip3\s+install\b.*?--no-deps\b(.*)", MAKEFILE_CONTENT, re.DOTALL
        )
        assert no_deps_section is not None
        block = no_deps_section.group(0)
        for pkg in ["requests", "urllib3", "charset-normalizer", "idna", "certifi", "PyJWT", "cryptography", "cffi"]:
            assert pkg in block, f"Second pip3 install must include {pkg}"

    def test_at_least_two_pip3_install_commands(self):
        invocations = re.findall(r"\bpip3\s+install\b", MAKEFILE_CONTENT)
        assert len(invocations) >= 2


# ── No .dist-info removal ──

class TestNoDistInfoRemoval:
    def test_no_dist_info_removal(self):
        combined = MAKEFILE_CONTENT + "\n" + DEPLOY_CONTENT
        assert not re.search(r"rm\s.*\.dist-info", combined)
        assert not re.search(r"find.*\.dist-info.*-delete", combined)


# ── SAM build and deploy ──

class TestSamBuildAndDeploy:
    def test_uses_sam_build(self):
        assert re.search(r"\bsam\s+build\b", DEPLOY_CONTENT), "Script must call sam build"

    def test_uses_sam_deploy(self):
        assert re.search(r"\bsam\s+deploy\b", DEPLOY_CONTENT), "Script must call sam deploy"

    def test_sam_deploy_has_named_iam_capability(self):
        assert "CAPABILITY_NAMED_IAM" in DEPLOY_CONTENT

    def test_sam_deploy_resolves_artifact_bucket(self):
        assert "--resolve-s3" in DEPLOY_CONTENT

    def test_makefile_build_target_exists(self):
        assert "build-AgentLambdaFunction" in MAKEFILE_CONTENT


# ── Required dependencies ──

class TestRequiredDependencies:
    def test_requirements_txt_referenced_in_makefile(self):
        assert "requirements.txt" in MAKEFILE_CONTENT


# ── Template validation before deployment ──

class TestTemplateValidation:
    def test_validate_before_deploy(self):
        validate_pos = DEPLOY_CONTENT.find("sam validate")
        deploy_pos = DEPLOY_CONTENT.find("sam deploy")
        assert validate_pos != -1, "Script must call sam validate"
        assert deploy_pos != -1, "Script must call sam deploy"
        assert validate_pos < deploy_pos, "sam validate must precede sam deploy"

    def test_references_sam_template(self):
        assert "infrastructure/template.yaml" in DEPLOY_CONTENT


# ── Smithy model bucket is account-scoped ──

class TestSmithyBucketUniqueness:
    def test_bucket_includes_account_id(self):
        """Bucket name must be account-scoped to guarantee global uniqueness."""
        assert "ACCOUNT_ID" in DEPLOY_CONTENT, (
            "Smithy bucket name must incorporate the AWS account ID"
        )

    def test_gets_account_id_from_sts(self):
        assert "sts get-caller-identity" in DEPLOY_CONTENT

    def test_smithy_upload_before_deploy(self):
        upload_pos = DEPLOY_CONTENT.find("aws s3 cp")
        deploy_pos = DEPLOY_CONTENT.find("sam deploy")
        assert upload_pos < deploy_pos, "Smithy upload must precede sam deploy"


# ── pip3 exclusively ──

class TestPip3Exclusively:
    def test_all_pip_commands_use_pip3(self):
        invocations = re.findall(r"\b(pip3?)\s+install\b", MAKEFILE_CONTENT)
        assert len(invocations) > 0
        for inv in invocations:
            assert inv == "pip3", f"Found bare '{inv}' instead of 'pip3'"


# ── No forbidden patterns ──

class TestNoForbiddenPatterns:
    def test_no_credential_provider_commands(self):
        for pattern in ["create-credential-provider", "create-api-key-credential-provider", "get-api-key"]:
            assert pattern not in DEPLOY_CONTENT

    def test_no_api_key_retrieval(self):
        assert not re.search(r"get-api-key", DEPLOY_CONTENT)
