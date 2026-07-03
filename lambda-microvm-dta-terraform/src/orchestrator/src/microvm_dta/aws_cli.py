from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional
import json
import subprocess
import time


class AwsCliError(RuntimeError):
    pass


@dataclass
class AwsCli:
    profile: Optional[str] = None
    region: Optional[str] = None
    dry_print: bool = False

    def _base(self) -> List[str]:
        cmd = ["aws"]
        if self.profile:
            cmd.extend(["--profile", self.profile])
        if self.region:
            cmd.extend(["--region", self.region])
        return cmd

    def run(self, args: List[str], *, expect_json: bool = True) -> Dict[str, Any] | str:
        cmd = self._base() + args
        if expect_json and "--output" not in args:
            cmd.extend(["--output", "json"])
        if self.dry_print:
            print(" ".join(cmd))
            return {}
        proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
        if proc.returncode != 0:
            raise AwsCliError(
                "AWS CLI command failed\n"
                f"command: {' '.join(cmd)}\n"
                f"returncode: {proc.returncode}\n"
                f"stdout: {proc.stdout}\n"
                f"stderr: {proc.stderr}"
            )
        if not expect_json:
            return proc.stdout
        stdout = proc.stdout.strip()
        if not stdout:
            return {}
        try:
            return json.loads(stdout)
        except json.JSONDecodeError as exc:
            raise AwsCliError(f"Expected JSON from AWS CLI but could not parse stdout: {stdout}") from exc

    def microvms(self, args: List[str], *, expect_json: bool = True) -> Dict[str, Any] | str:
        return self.run(["lambda-microvms", *args], expect_json=expect_json)


def sleep_with_backoff(attempt: int, base: float = 1.0, cap: float = 15.0) -> None:
    delay = min(cap, base * (2 ** max(0, attempt - 1)))
    time.sleep(delay)
