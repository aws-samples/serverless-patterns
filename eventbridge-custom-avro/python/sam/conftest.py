# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

"""Ensure the sample root is importable so tests can `import common`,
`import publisher`, and `import consumer` regardless of pytest's rootdir."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
