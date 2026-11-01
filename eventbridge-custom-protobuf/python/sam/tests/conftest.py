# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

"""Skip the whole suite with a clear message if the Protobuf bindings or the
protobuf-py runtime are missing — the sample can't be exercised until
scripts/generate.sh has been run in a venv with the deps installed."""

import importlib.util

import pytest


def _spec_exists(name: str) -> bool:
    # find_spec raises ModuleNotFoundError when a PARENT package is missing
    # (e.g. common.gen not generated yet), so treat that as "not present".
    try:
        return importlib.util.find_spec(name) is not None
    except ModuleNotFoundError:
        return False


def _missing():
    # The generated module imports `protobuf` (protobuf-py); both must be present.
    if not _spec_exists("protobuf"):
        return "protobuf-py not installed (pip install -r publisher/requirements.txt)"
    if not _spec_exists("common.gen.order_placed_pb"):
        return "Protobuf bindings not generated (run scripts/generate.sh)"
    return None


_reason = _missing()
if _reason:
    pytest.skip(f"skipping: {_reason}", allow_module_level=True)
