"""Makefile assertion tests for the Docker-free SAM build.

Parses the root ``Makefile`` and asserts the ``build-AgentLambdaFunction`` and
``build-McpServerLambda`` targets exist and each runs the project's proven
two-step ``pip3`` manylinux install plus the ``src`` copy.

This is a deterministic lint guarding the Docker-free build approach
(BuildMethod: makefile). See .kiro/steering/project-conventions.md.

Validates: Requirements 2.1, 2.5, 2.6, 9.3, 11.1, 13.1
"""

import os
import re
from typing import Dict, List

import pytest

# ---------------------------------------------------------------------------
# Fixture: locate and read the project-root Makefile
# ---------------------------------------------------------------------------

MAKEFILE_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "Makefile"
)

# The pure-Python package set installed in Step B (--no-deps), in order.
PURE_PYTHON_PACKAGES = [
    "requests", "urllib3", "charset-normalizer", "idna", "certifi",
    "PyJWT", "cryptography", "cffi", "mcp",
]

REQUIRED_TARGETS = ["build-AgentLambdaFunction", "build-McpServerLambda"]


@pytest.fixture(scope="session")
def makefile_text() -> str:
    """Read the raw Makefile text once per session."""
    assert os.path.exists(MAKEFILE_PATH), (
        f"Expected a Makefile at the project root: {MAKEFILE_PATH}"
    )
    with open(MAKEFILE_PATH, "r") as fh:
        return fh.read()


@pytest.fixture(scope="session")
def target_recipes(makefile_text) -> Dict[str, List[str]]:
    """Split the Makefile into {target_name: [recipe_lines]}.

    A target starts at a line matching ``^<name>:`` and owns the following
    tab-indented recipe lines until the next non-indented line.
    """
    recipes: Dict[str, List[str]] = {}
    current: str = None
    for line in makefile_text.splitlines():
        # A target header: starts at column 0, ends with ':' before any recipe.
        header = re.match(r"^([A-Za-z0-9_.\-]+):\s*(.*)$", line)
        if header and not line.startswith("\t"):
            current = header.group(1)
            recipes[current] = []
            continue
        if current is not None and line.startswith("\t"):
            recipes[current].append(line[1:])  # strip the leading tab
            continue
        # Blank line inside a recipe is allowed by make; keep collecting.
        if current is not None and line.strip() == "":
            continue
        # Any other non-indented line ends the current target block.
        current = None
    return recipes


def _recipe_text(recipes: Dict[str, List[str]], target: str) -> str:
    """Join a target's recipe lines into a single searchable string."""
    return "\n".join(recipes[target])


def _command_lines(recipe_lines: List[str]) -> List[str]:
    """Return recipe lines that are commands (strip comment-only lines)."""
    cmds = []
    for ln in recipe_lines:
        stripped = ln.strip()
        if not stripped or stripped.startswith("#"):
            continue
        cmds.append(ln)
    return cmds


# ---------------------------------------------------------------------------
# 1. Both build targets exist (Requirement 2.1)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("target", REQUIRED_TARGETS)
def test_build_target_exists(target_recipes, target):
    """SAM BuildMethod: makefile requires build-<FunctionLogicalId> targets."""
    assert target in target_recipes, (
        f"Makefile must declare a '{target}:' target so SAM's "
        f"BuildMethod: makefile can resolve it"
    )
    assert target_recipes[target], (
        f"'{target}:' target must have a non-empty recipe"
    )


# ---------------------------------------------------------------------------
# 2. Step A — binary install from requirements.txt (Requirements 2.5, 13.1)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("target", REQUIRED_TARGETS)
def test_step_a_only_binary_requirements(target_recipes, target):
    """Step A must install with --only-binary=:all: against requirements.txt."""
    text = _recipe_text(target_recipes, target)
    assert "--only-binary=:all:" in text, (
        f"'{target}' must use --only-binary=:all: (Step A binary wheels)"
    )
    assert "-r requirements.txt" in text, (
        f"'{target}' Step A must install -r requirements.txt"
    )


# ---------------------------------------------------------------------------
# 3. Step B — pure-Python package set with --no-deps (Requirements 2.5, 13.1)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("target", REQUIRED_TARGETS)
def test_step_b_no_deps_pure_python_set(target_recipes, target):
    """Step B must use --no-deps and install the pure-Python package set."""
    text = _recipe_text(target_recipes, target)
    assert "--no-deps" in text, (
        f"'{target}' must use --no-deps for the pure-Python set (Step B); "
        f"--only-binary silently skips pure-Python packages"
    )
    for pkg in PURE_PYTHON_PACKAGES:
        assert re.search(rf"(?<![\w-]){re.escape(pkg)}(?![\w-])", text), (
            f"'{target}' Step B must install pure-Python package '{pkg}'"
        )


# ---------------------------------------------------------------------------
# 4. Both steps target manylinux2014_x86_64 / python 3.12 (Requirement 2.6)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("target", REQUIRED_TARGETS)
def test_platform_and_python_version(target_recipes, target):
    """Both pip3 steps must pin --platform manylinux2014_x86_64 and 3.12."""
    text = _recipe_text(target_recipes, target)
    platform_count = text.count("--platform manylinux2014_x86_64")
    pyversion_count = text.count("--python-version 3.12")
    assert platform_count >= 2, (
        f"'{target}' must use --platform manylinux2014_x86_64 in BOTH pip3 "
        f"steps, found {platform_count}"
    )
    assert pyversion_count >= 2, (
        f"'{target}' must use --python-version 3.12 in BOTH pip3 steps, "
        f"found {pyversion_count}"
    )


# ---------------------------------------------------------------------------
# 5. src copied into $(ARTIFACTS_DIR) preserving the src/ prefix (Req 9.3)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("target", REQUIRED_TARGETS)
def test_copies_src_into_artifacts_dir(target_recipes, target):
    """Each target must copy src into $(ARTIFACTS_DIR), preserving src/ prefix."""
    text = _recipe_text(target_recipes, target)
    assert re.search(r'cp\s+-r\s+src\s+"?\$\(ARTIFACTS_DIR\)/src"?', text), (
        f"'{target}' must copy src into $(ARTIFACTS_DIR)/src "
        f'(e.g. cp -r src "$(ARTIFACTS_DIR)/src")'
    )


# ---------------------------------------------------------------------------
# 6. Uses pip3, never a bare pip invocation (Requirement 11.1)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("target", REQUIRED_TARGETS)
def test_uses_pip3_not_bare_pip(target_recipes, target):
    """Recipe command lines must invoke pip3, never bare 'pip'."""
    text = _recipe_text(target_recipes, target)
    assert "pip3 install" in text, (
        f"'{target}' must use 'pip3 install'"
    )
    for cmd in _command_lines(target_recipes[target]):
        # A bare pip invocation is 'pip' followed by space/end, not 'pip3'.
        assert not re.search(r"(?<![\w/])pip(?![3\w])", cmd), (
            f"'{target}' recipe must use 'pip3', found a bare 'pip' "
            f"invocation: {cmd!r}"
        )


def test_no_bare_pip_anywhere_in_recipes(target_recipes):
    """No build target recipe line may contain a bare 'pip' invocation."""
    for target in REQUIRED_TARGETS:
        for cmd in _command_lines(target_recipes[target]):
            assert not re.search(r"(?<![\w/])pip(?![3\w])", cmd), (
                f"Bare 'pip' invocation found in '{target}': {cmd!r} — "
                f"use 'pip3'"
            )
