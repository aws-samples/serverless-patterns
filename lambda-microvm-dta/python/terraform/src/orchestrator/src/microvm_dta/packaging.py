from __future__ import annotations

from pathlib import Path
from typing import Iterable
import zipfile

EXCLUDE_PARTS = {"__pycache__", ".pytest_cache", ".mypy_cache"}
EXCLUDE_NAMES = {".DS_Store"}
EXCLUDE_SUFFIXES = {".pyc", ".pyo"}


def should_include(path: Path) -> bool:
    if any(part in EXCLUDE_PARTS for part in path.parts):
        return False
    if path.name in EXCLUDE_NAMES:
        return False
    if path.suffix in EXCLUDE_SUFFIXES:
        return False
    return True


def iter_files(source_dir: Path) -> Iterable[Path]:
    for path in source_dir.rglob("*"):
        if path.is_file() and should_include(path.relative_to(source_dir)):
            yield path


def package_microvm(source_dir: str | Path, output: str | Path) -> Path:
    source = Path(source_dir).resolve()
    out = Path(output).resolve()
    if not source.exists():
        raise FileNotFoundError(f"Source directory does not exist: {source}")
    if not (source / "Dockerfile").exists():
        raise FileNotFoundError(f"Source directory must contain Dockerfile: {source}")
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for file in iter_files(source):
            zf.write(file, file.relative_to(source).as_posix())
    return out
