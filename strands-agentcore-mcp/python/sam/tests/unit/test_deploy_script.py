"""Deploy-script lint tests.

Reads scripts/deploy.sh as text and asserts the NEW SAM-based deploy flow and
the conventions from .kiro/steering/project-conventions.md are followed.

The deploy script no longer packages Lambdas by hand or runs a separate
update-function-code step. It now wraps `sam build` + `sam deploy` and runs the
ordered post-deploy steps (MCP target create/update, synchronize, DynamoDB
seed, Cognito test user, test.sh generation).

These tests guard the deploy script mechanically so regressions are caught
before a real deployment attempt.

Requirements covered: 3.2, 3.3, 10.1, 10.3, 10.4, 10.5, 11.1, 11.2, 11.3, 13.2
"""

import os
import re

import pytest

DEPLOY_SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "scripts", "deploy.sh"
)


@pytest.fixture(scope="session")
def deploy_script() -> str:
    """Read the deploy script once per session."""
    with open(DEPLOY_SCRIPT_PATH, "r") as fh:
        return fh.read()


# ---------------------------------------------------------------------------
# Helper: extract non-comment lines from the deploy script
# ---------------------------------------------------------------------------

def _non_comment_lines(script: str) -> str:
    """Return the script with comment-only lines removed."""
    lines = []
    for line in script.splitlines():
        stripped = line.strip()
        if not stripped.startswith("#"):
            lines.append(line)
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# 1. SAM build + deploy flow (Requirement 10.1)
# ---------------------------------------------------------------------------

def test_sam_build_present(deploy_script):
    """Script must invoke 'sam build'."""
    code_only = _non_comment_lines(deploy_script)
    assert re.search(r'\bsam\s+build\b', code_only), (
        "deploy.sh must invoke 'sam build'"
    )


def test_sam_build_without_use_container(deploy_script):
    """The build is Docker-free — 'sam build' must NOT use --use-container."""
    code_only = _non_comment_lines(deploy_script)
    assert "--use-container" not in code_only, (
        "deploy.sh must invoke 'sam build' WITHOUT --use-container "
        "(Docker-free build via the Makefile's BuildMethod: makefile targets)"
    )


def test_sam_deploy_present(deploy_script):
    """Script must invoke 'sam deploy'."""
    code_only = _non_comment_lines(deploy_script)
    assert re.search(r'\bsam\s+deploy\b', code_only), (
        "deploy.sh must invoke 'sam deploy'"
    )


def test_sam_build_before_sam_deploy(deploy_script):
    """'sam build' must appear before 'sam deploy'."""
    code_only = _non_comment_lines(deploy_script)
    build_match = re.search(r'\bsam\s+build\b', code_only)
    deploy_match = re.search(r'\bsam\s+deploy\b', code_only)
    assert build_match and deploy_match, "Expected both 'sam build' and 'sam deploy'"
    assert build_match.start() < deploy_match.start(), (
        "'sam build' must appear before 'sam deploy' in deploy.sh"
    )


# ---------------------------------------------------------------------------
# 2. No separate update-function-code step (Requirement 3.2)
# ---------------------------------------------------------------------------

def test_no_update_function_code(deploy_script):
    """Script must NOT contain a separate 'aws lambda update-function-code' step."""
    assert "update-function-code" not in deploy_script, (
        "deploy.sh must not include a separate 'aws lambda update-function-code' "
        "step — SAM deploys real code in one shot"
    )


# ---------------------------------------------------------------------------
# 3. No manual two-step pip3 packaging in the deploy script (Requirement 3.3)
#
# The two-step pip3 manylinux install now lives in the root Makefile's
# build-* targets, NOT in deploy.sh.
# ---------------------------------------------------------------------------

def test_no_manual_pip_packaging(deploy_script):
    """Script must NOT contain the two-step pip3 manylinux packaging logic."""
    assert "--only-binary=:all:" not in deploy_script, (
        "deploy.sh must not contain '--only-binary=:all:' packaging — "
        "it now lives in the Makefile"
    )
    assert "--platform manylinux2014_x86_64" not in deploy_script, (
        "deploy.sh must not contain '--platform manylinux2014_x86_64' packaging — "
        "it now lives in the Makefile"
    )


def test_no_package_lambda_function(deploy_script):
    """Script must NOT define a package_lambda() function."""
    assert not re.search(r'\bpackage_lambda\b', deploy_script), (
        "deploy.sh must not define or call a package_lambda() function — "
        "packaging moved to the Makefile"
    )


# ---------------------------------------------------------------------------
# 4. No bare pip (only pip3) (Requirement 11.1)
# ---------------------------------------------------------------------------

def test_no_bare_pip_invocations(deploy_script):
    """Script must use pip3, never bare pip."""
    non_comment_matches = []
    for line in deploy_script.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            continue
        found = re.findall(r'\bpip\b(?!3)', stripped)
        non_comment_matches.extend(found)

    assert not non_comment_matches, (
        f"deploy.sh must use 'pip3', not bare 'pip'. "
        f"Found {len(non_comment_matches)} bare 'pip' occurrence(s)"
    )


# ---------------------------------------------------------------------------
# 5. PID-based temp file names (Requirement 11.2)
# ---------------------------------------------------------------------------

def test_pid_based_temp_files(deploy_script):
    """Script must use $$-based PID temp file names."""
    assert re.search(r'\.\$\$\.', deploy_script), (
        "deploy.sh must use PID-based temp file names "
        "(e.g. /tmp/agentcore-mcp.$$.stack-output.json)"
    )


def test_no_mktemp_suffix_templates(deploy_script):
    """Script must NOT use mktemp suffix templates (macOS incompatible)."""
    assert not re.search(r'mktemp\s+.*-t\s+\S*X{3,}', deploy_script), (
        "deploy.sh must not use 'mktemp -t XXXXX' suffix templates — "
        "use $$-based PID names instead"
    )
    assert not re.search(r'mktemp\s+.*--suffix', deploy_script), (
        "deploy.sh must not use 'mktemp --suffix' — "
        "use $$-based PID names instead"
    )


# ---------------------------------------------------------------------------
# 6. Generated test.sh uses heredoc + sed substitution (Requirement 11.3)
# ---------------------------------------------------------------------------

def test_test_sh_generated_via_heredoc(deploy_script):
    """Generated test.sh must be produced via a heredoc, not nested echo JSON."""
    assert re.search(r'cat\s+>\s*scripts/test\.sh', deploy_script), (
        "deploy.sh must use 'cat > scripts/test.sh <<...' to generate the test script"
    )


def test_test_sh_uses_sed_substitution(deploy_script):
    """Generated test.sh placeholders must be substituted via sed -i.bak."""
    assert "sed -i.bak" in deploy_script, (
        "deploy.sh must use 'sed -i.bak' to substitute baked-in values into test.sh"
    )


# ---------------------------------------------------------------------------
# 7. Ordered post-deploy steps (Requirement 10.3)
#
# Order: MCP target create/update -> synchronize -> DynamoDB seed
#        -> Cognito user -> test.sh generation
# ---------------------------------------------------------------------------

def test_post_deploy_steps_in_order(deploy_script):
    """Post-deploy steps must appear in the required order."""
    markers = [
        ("MCP target create/update", "list-gateway-targets"),
        ("MCP target synchronize", "synchronize_gateway_targets"),
        ("DynamoDB seed", "aws dynamodb put-item"),
        ("Cognito user", "admin-create-user"),
        ("test.sh generation", "cat > scripts/test.sh"),
    ]

    positions = []
    for label, marker in markers:
        pos = deploy_script.find(marker)
        assert pos != -1, f"deploy.sh is missing the {label} step (marker: {marker!r})"
        positions.append((label, pos))

    for (prev_label, prev_pos), (next_label, next_pos) in zip(positions, positions[1:]):
        assert prev_pos < next_pos, (
            f"Post-deploy step '{prev_label}' must appear before '{next_label}' "
            f"in deploy.sh"
        )


# ---------------------------------------------------------------------------
# 8. DynamoDB seeding: >=3 put-item calls spanning >=2 categories (Req 10.4)
# ---------------------------------------------------------------------------

def test_dynamodb_seeding_at_least_three_products(deploy_script):
    """Script must seed at least three products via put-item."""
    put_item_calls = re.findall(r'aws\s+dynamodb\s+put-item', deploy_script)
    assert len(put_item_calls) >= 3, (
        f"deploy.sh must seed at least 3 products with 'aws dynamodb put-item', "
        f"found {len(put_item_calls)}"
    )


def test_dynamodb_seeding_at_least_two_categories(deploy_script):
    """Seeded products must span at least two categories."""
    categories = set(re.findall(r'"category":\s*\{"S":\s*"([^"]+)"\}', deploy_script))
    assert len(categories) >= 2, (
        f"deploy.sh must seed products across at least 2 categories, "
        f"found: {sorted(categories)}"
    )


# ---------------------------------------------------------------------------
# 9. Cognito test user with permanent password (Requirement 10.5)
# ---------------------------------------------------------------------------

def test_cognito_test_user_creation(deploy_script):
    """Script must create a Cognito test user."""
    assert "admin-create-user" in deploy_script, (
        "deploy.sh must call 'aws cognito-idp admin-create-user'"
    )


def test_cognito_permanent_password(deploy_script):
    """Script must set a permanent password so the user is confirmed."""
    assert "admin-set-user-password" in deploy_script, (
        "deploy.sh must call 'aws cognito-idp admin-set-user-password'"
    )
    assert "--permanent" in deploy_script, (
        "deploy.sh must use the --permanent flag to confirm the test user"
    )


# ---------------------------------------------------------------------------
# 10. Old removed flow must be gone (Requirements 3.2, 3.3)
# ---------------------------------------------------------------------------

def test_no_validate_template(deploy_script):
    """Script must NOT call 'aws cloudformation validate-template' (SAM validates)."""
    assert "validate-template" not in deploy_script, (
        "deploy.sh must not call 'aws cloudformation validate-template' — "
        "SAM validates during build/deploy"
    )


def test_no_create_or_update_stack_decision_tree(deploy_script):
    """Script must NOT use the create-stack/update-stack decision tree."""
    assert "aws cloudformation create-stack" not in deploy_script, (
        "deploy.sh must not call 'aws cloudformation create-stack' — "
        "SAM handles create-vs-update"
    )
    assert "aws cloudformation update-stack" not in deploy_script, (
        "deploy.sh must not call 'aws cloudformation update-stack' — "
        "SAM handles create-vs-update"
    )


def test_no_rollback_complete_handling(deploy_script):
    """Script must NOT contain ROLLBACK_COMPLETE handling (SAM manages rollback)."""
    assert "ROLLBACK_COMPLETE" not in deploy_script, (
        "deploy.sh must not contain ROLLBACK_COMPLETE handling — "
        "SAM manages rollback"
    )
