"""Pytest configuration for OpenAPI Agent Gateway tests."""

import sys
from pathlib import Path

# Add src directory to Python path for imports
src_path = Path(__file__).parent.parent / 'src'
sys.path.insert(0, str(src_path))
