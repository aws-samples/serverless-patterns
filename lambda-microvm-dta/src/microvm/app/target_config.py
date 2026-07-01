"""Strict target configuration parsing and validation for the v0.2 supervisor.

The supervisor executes *untrusted* targets, so the config format is
deliberately narrow: argv arrays only, never shell strings. This module loads,
validates, and normalizes a target config (YAML or JSON) into typed objects the
supervisor can act on.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional
import json
import re

# Constructs that signal a copy-pasted shell one-liner rather than a clean argv
# element. argv is executed WITHOUT a shell, so these are only ever literal
# arguments — but rejecting them in public-sample mode keeps intent unambiguous
# and steers users toward argv arrays / script targets. We intentionally allow
# lone ';', '(', ')' and '$' because they appear in normal inline code (e.g.
# `python3 -c "a;b"`); we reject pipes, redirects, command substitution,
# backticks, chaining operators, and embedded newlines.
_SHELL_METACHARACTERS = re.compile(r"[|`><\n]|\$\(|&&|\|\||(?:^|\s)&(?:\s|$)")

SUPPORTED_TARGET_TYPES = {"command", "script", "archive"}


class TargetConfigError(ValueError):
    pass


@dataclass(frozen=True)
class TargetSpec:
    type: str
    argv: List[str]
    timeout_seconds: float
    working_directory: Optional[str]
    environment: Dict[str, str]
    # script: path to a script file to copy into the workspace and execute.
    source: Optional[str] = None
    # archive: path to a zip/tar to extract; argv is the entrypoint after extraction.
    archive: Optional[str] = None


@dataclass(frozen=True)
class CollectorsSpec:
    process: bool = True
    filesystem: bool = True
    canary: bool = True
    strace: bool = False
    network_procnet: bool = True
    network_vpc_flow_logs: bool = False


@dataclass(frozen=True)
class PolicySpec:
    fail_on_severity: str = "high"
    fail_on_policy_violation: bool = True
    fail_closed: bool = True


@dataclass(frozen=True)
class AnalysisConfig:
    target: TargetSpec
    collectors: CollectorsSpec
    policy: PolicySpec
    raw: Dict[str, Any] = field(default_factory=dict)


def _load_mapping(path: Path) -> Dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        data = json.loads(text)
    else:
        try:
            import yaml  # type: ignore

            data = yaml.safe_load(text)
        except ModuleNotFoundError:
            data = _parse_limited_yaml(text)
    if not isinstance(data, dict):
        raise TargetConfigError("Target config must load to a mapping/object")
    return data


def _parse_limited_yaml(text: str) -> Dict[str, Any]:
    """Minimal YAML fallback for the target-config shape used by examples.

    Supports nested mappings (by indentation), inline ``["a", "b"]`` flow lists,
    scalars, and booleans/integers. Not a general YAML parser; PyYAML is used
    whenever it is installed (it is in the MicroVM image).
    """
    root: Dict[str, Any] = {}
    # stack of (indent, container)
    stack: List[tuple[int, Dict[str, Any]]] = [(-1, root)]
    for raw in text.splitlines():
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(" "))
        key, _, rest = line.strip().partition(":")
        key = key.strip()
        rest = rest.strip()
        while stack and indent <= stack[-1][0]:
            stack.pop()
        parent = stack[-1][1]
        if rest == "":
            child: Dict[str, Any] = {}
            parent[key] = child
            stack.append((indent, child))
        else:
            parent[key] = _coerce_scalar(rest)
    return root


def _coerce_scalar(value: str) -> Any:
    if value == "{}":
        return {}
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [_coerce_scalar(part.strip()) for part in _split_flow(inner)]
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        return value[1:-1]
    low = value.lower()
    if low in {"true", "false"}:
        return low == "true"
    if low in {"null", "~", "none"}:
        return None
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    if re.fullmatch(r"-?\d+\.\d+", value):
        return float(value)
    return value


def _split_flow(inner: str) -> List[str]:
    parts: List[str] = []
    buf = ""
    quote = ""
    for ch in inner:
        if quote:
            buf += ch
            if ch == quote:
                quote = ""
        elif ch in "\"'":
            quote = ch
            buf += ch
        elif ch == ",":
            parts.append(buf)
            buf = ""
        else:
            buf += ch
    if buf.strip():
        parts.append(buf)
    return parts


def _validate_argv(argv: Any, *, allow_shell_strings: bool) -> List[str]:
    if not isinstance(argv, list) or not argv or not all(isinstance(a, str) for a in argv):
        raise TargetConfigError("target.argv must be a non-empty list of strings")
    if not allow_shell_strings:
        for arg in argv:
            if _SHELL_METACHARACTERS.search(arg):
                raise TargetConfigError(
                    f"target.argv element contains shell metacharacters and is rejected in public-sample mode: {arg!r}"
                )
    return list(argv)


def load_target_config(path: str | Path, *, allow_shell_strings: bool = False) -> AnalysisConfig:
    return parse_target_config(_load_mapping(Path(path)), allow_shell_strings=allow_shell_strings)


def parse_target_config(data: Dict[str, Any], *, allow_shell_strings: bool = False) -> AnalysisConfig:
    target_raw = data.get("target")
    if not isinstance(target_raw, dict):
        raise TargetConfigError("Config must contain a 'target' object")

    ttype = str(target_raw.get("type", ""))
    if ttype not in SUPPORTED_TARGET_TYPES:
        raise TargetConfigError(f"Unsupported target.type: {ttype!r} (allowed: {sorted(SUPPORTED_TARGET_TYPES)})")

    argv = _validate_argv(target_raw.get("argv"), allow_shell_strings=allow_shell_strings)

    timeout = target_raw.get("timeoutSeconds", 60)
    try:
        timeout = float(timeout)
    except (TypeError, ValueError):
        raise TargetConfigError("target.timeoutSeconds must be a number")
    if timeout <= 0:
        raise TargetConfigError("target.timeoutSeconds must be > 0")

    env_raw = target_raw.get("environment") or {}
    if not isinstance(env_raw, dict):
        raise TargetConfigError("target.environment must be a mapping")
    environment = {str(k): str(v) for k, v in env_raw.items()}

    source = target_raw.get("source")
    archive = target_raw.get("archive")
    if ttype == "script" and not source:
        raise TargetConfigError("target.type 'script' requires 'source'")
    if ttype == "archive" and not archive:
        raise TargetConfigError("target.type 'archive' requires 'archive'")

    target = TargetSpec(
        type=ttype,
        argv=argv,
        timeout_seconds=timeout,
        working_directory=target_raw.get("workingDirectory"),
        environment=environment,
        source=str(source) if source else None,
        archive=str(archive) if archive else None,
    )

    collectors = _parse_collectors(data.get("collectors") or {})
    policy = _parse_policy(data.get("policy") or {})
    return AnalysisConfig(target=target, collectors=collectors, policy=policy, raw=data)


def _parse_collectors(raw: Dict[str, Any]) -> CollectorsSpec:
    network = raw.get("network") or {}
    if not isinstance(network, dict):
        network = {}
    return CollectorsSpec(
        process=bool(raw.get("process", True)),
        filesystem=bool(raw.get("filesystem", True)),
        canary=bool(raw.get("canary", True)),
        strace=bool(raw.get("strace", False)),
        network_procnet=bool(network.get("procNet", True)),
        network_vpc_flow_logs=bool(network.get("vpcFlowLogs", False)),
    )


def _parse_policy(raw: Dict[str, Any]) -> PolicySpec:
    return PolicySpec(
        fail_on_severity=str(raw.get("failOnSeverity", "high")),
        fail_on_policy_violation=bool(raw.get("failOnPolicyViolation", True)),
        fail_closed=bool(raw.get("failClosed", True)),
    )
