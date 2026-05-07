#!/usr/bin/env python3
"""Package Interceptor Lambda function for deployment."""

import shutil
import sys
from pathlib import Path


def package_interceptor_lambda():
    """Package Interceptor Lambda with dependencies."""
    print("="*60)
    print("Packaging Interceptor Lambda")
    print("="*60)
    
    # Define paths
    package_dir = Path("interceptor-lambda-package")
    src_dir = Path("src")
    deps_dir = Path("agent-lambda-deps")  # Reuse same deps as Agent Lambda
    
    # Clean previous package
    if package_dir.exists():
        print(f"\n1. Cleaning previous package: {package_dir}")
        shutil.rmtree(package_dir)
    
    # Create package directory
    print(f"\n2. Creating package directory: {package_dir}")
    package_dir.mkdir(parents=True, exist_ok=True)
    
    # Copy pre-built dependencies
    print(f"\n3. Copying pre-built dependencies from {deps_dir}")
    if not deps_dir.exists():
        print(f"✗ Pre-built dependencies not found at {deps_dir}")
        print("  The agent-lambda-deps directory contains Linux x86_64 binaries")
        return False
    
    for item in deps_dir.iterdir():
        if item.name not in ['__pycache__', '.DS_Store', 'bin']:
            dst = package_dir / item.name
            if item.is_dir():
                print(f"   Copying directory: {item.name}")
                shutil.copytree(item, dst, dirs_exist_ok=True)
            else:
                print(f"   Copying file: {item.name}")
                shutil.copy2(item, dst)
    
    # Copy interceptor source code
    print(f"\n4. Copying interceptor source code")
    interceptor_src = src_dir / "interceptor"
    if interceptor_src.exists():
        dst = package_dir / "interceptor"
        shutil.copytree(interceptor_src, dst, dirs_exist_ok=True)
        print(f"   ✓ Copied {interceptor_src} -> {dst}")
    else:
        print(f"   ✗ Interceptor source not found: {interceptor_src}")
        return False
    
    # Copy shared modules
    print(f"\n5. Copying shared modules")
    shared_src = src_dir / "shared"
    if shared_src.exists():
        dst = package_dir / "shared"
        shutil.copytree(shared_src, dst, dirs_exist_ok=True)
        print(f"   ✓ Copied {shared_src} -> {dst}")
    else:
        print(f"   ✗ Shared modules not found: {shared_src}")
        return False
    
    # Create deployment zip
    print(f"\n6. Creating deployment package")
    zip_path = Path("interceptor-lambda-deployment.zip")
    if zip_path.exists():
        zip_path.unlink()
    
    shutil.make_archive(
        "interceptor-lambda-deployment",
        'zip',
        package_dir
    )
    
    # Get package size
    size_mb = zip_path.stat().st_size / (1024 * 1024)
    print(f"   ✓ Created {zip_path} ({size_mb:.2f} MB)")
    
    print("\n" + "="*60)
    print("✓ Interceptor Lambda packaged successfully!")
    print("="*60)
    print(f"\nDeployment package: {zip_path}")
    print(f"Package size: {size_mb:.2f} MB")
    
    return True


if __name__ == '__main__':
    success = package_interceptor_lambda()
    sys.exit(0 if success else 1)
