#!/usr/bin/env python3
"""
Package Agent Lambda deployment package with dependencies.
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path


def package_agent_lambda():
    """Create deployment package for Agent Lambda."""
    print("=" * 60)
    print("PACKAGING AGENT LAMBDA")
    print("=" * 60)
    
    # Paths
    package_dir = Path("agent-lambda-package")
    src_dir = Path("src")
    deps_dir = Path("agent-lambda-deps")
    
    # Clean previous package
    if package_dir.exists():
        print(f"Removing existing package directory: {package_dir}")
        shutil.rmtree(package_dir)
    
    # Create package directory
    print(f"Creating package directory: {package_dir}")
    package_dir.mkdir(exist_ok=True)
    
    # Copy pre-built dependencies
    if deps_dir.exists():
        print(f"\nCopying pre-built dependencies from {deps_dir}...")
        for item in deps_dir.iterdir():
            if item.name not in ['__pycache__', '.DS_Store']:
                dst = package_dir / item.name
                if item.is_dir():
                    shutil.copytree(item, dst, dirs_exist_ok=True)
                else:
                    shutil.copy2(item, dst)
        print("  ✓ Dependencies copied")
    else:
        print(f"\n✗ Pre-built dependencies not found at {deps_dir}")
        print("  Please ensure agent-lambda-deps directory exists")
        return False
    
    # Copy source code
    print("\nCopying source code...")
    
    # Copy agent module
    agent_src = src_dir / "agent"
    agent_dst = package_dir / "agent"
    print(f"  Copying {agent_src} -> {agent_dst}")
    shutil.copytree(agent_src, agent_dst, dirs_exist_ok=True)
    
    # Copy shared module
    shared_src = src_dir / "shared"
    shared_dst = package_dir / "shared"
    print(f"  Copying {shared_src} -> {shared_dst}")
    shutil.copytree(shared_src, shared_dst, dirs_exist_ok=True)
    
    print("  ✓ Source code copied")
    
    # Clean up unnecessary files
    print("\nCleaning up...")
    patterns_to_remove = [
        "**/__pycache__",
        "**/*.pyc",
        "**/*.pyo",
        "**/*.egg-info",
        "**/tests",
        "**/.pytest_cache"
    ]
    # NOTE: Do NOT remove .dist-info directories — opentelemetry
    # (transitive dep of strands-agents) needs them for
    # importlib.metadata.entry_points() discovery at runtime.
    
    for pattern in patterns_to_remove:
        for path in package_dir.glob(pattern):
            if path.is_dir():
                shutil.rmtree(path)
            else:
                path.unlink()
    
    print("  ✓ Cleanup complete")
    
    # Create zip file
    print("\nCreating deployment package...")
    zip_file = "agent-lambda-deployment.zip"
    
    if Path(zip_file).exists():
        Path(zip_file).unlink()
    
    shutil.make_archive(
        "agent-lambda-deployment",
        "zip",
        package_dir
    )
    
    zip_size = Path(zip_file).stat().st_size / (1024 * 1024)
    print(f"  ✓ Created {zip_file} ({zip_size:.2f} MB)")
    
    # Verify package contents
    print("\nVerifying package contents...")
    result = subprocess.run(
        ["unzip", "-l", zip_file],
        capture_output=True,
        text=True
    )
    
    if "agent/handler.py" in result.stdout and "shared/" in result.stdout:
        print("  ✓ Package structure verified")
    else:
        print("  ✗ Package structure invalid")
        return False
    
    print("\n" + "=" * 60)
    print("✓ AGENT LAMBDA PACKAGE READY")
    print("=" * 60)
    print(f"\nPackage: {zip_file}")
    print(f"Size: {zip_size:.2f} MB")
    print("\nNext step: python3 upload_agent_lambda.py")
    
    return True


if __name__ == "__main__":
    success = package_agent_lambda()
    sys.exit(0 if success else 1)
