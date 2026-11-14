#!/usr/bin/env python3
"""A benign sample target artifact for the 'script' target type.

It writes a small file and prints a line — nothing harmful. The supervisor's
collectors observe it from outside.
"""
import pathlib

pathlib.Path("script_artifact.txt").write_text("written by sample_target\n", encoding="utf-8")
print("sample_target ran")
