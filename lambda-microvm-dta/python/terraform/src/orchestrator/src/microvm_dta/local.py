from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Optional
import sys


def _repo_root() -> Path:
    # Source-tree layout: <repo>/orchestrator/src/microvm_dta/local.py → parents[3].
    candidate = Path(__file__).resolve().parents[3]
    if (candidate / "microvm").exists():
        return candidate
    return Path.cwd()


def _load_microvm_modules(repo_root: Path) -> None:
    microvm_dir = repo_root / "microvm"
    if str(microvm_dir) not in sys.path:
        sys.path.insert(0, str(microvm_dir))


def run_local_analysis(
    *,
    target_config: str | Path,
    root: str | Path,
    rules_file: Optional[str | Path] = None,
    correlation_id: Optional[str] = None,
    commit_sha: Optional[str] = None,
    allow_shell_strings: bool = False,
) -> Dict[str, Any]:
    """Run a v0.2 DTA analysis locally (no AWS) and return the report dict.

    The MicroVM ``app`` package implements the supervisor; we put ``microvm/`` on
    the path and call it directly so local and in-MicroVM behavior share code.
    """
    repo_root = _repo_root()
    _load_microvm_modules(repo_root)
    from app.target_config import load_target_config  # type: ignore
    from app.supervisor import run_analysis  # type: ignore

    rules = rules_file or (repo_root / "microvm" / "rules" / "default.yaml")
    config = load_target_config(target_config, allow_shell_strings=allow_shell_strings)
    result = run_analysis(
        config,
        root=root,
        rules_file=rules,
        source_base=Path(target_config).resolve().parent,
        correlation_id=correlation_id,
        commit_sha=commit_sha,
        mode="local",
    )
    return result.report
