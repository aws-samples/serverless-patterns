#!/usr/bin/env python3
"""
Complete deployment script for Serverless AI Agent Gateway.
Packages and uploads both Lambda functions.
"""

import subprocess
import sys


def run_command(script_name: str, description: str) -> bool:
    """Run a deployment script and return success status."""
    print(f"\n{'=' * 60}")
    print(f"STEP: {description}")
    print('=' * 60)
    
    result = subprocess.run([sys.executable, script_name])
    
    if result.returncode != 0:
        print(f"\n✗ Failed: {description}")
        return False
    
    return True


def main():
    """Run complete deployment."""
    print("=" * 60)
    print("SERVERLESS AI AGENT GATEWAY - COMPLETE DEPLOYMENT")
    print("=" * 60)
    
    steps = [
        ("package_agent_lambda.py", "Package Agent Lambda"),
        ("package_interceptor_lambda.py", "Package Interceptor Lambda"),
        ("package_tool_lambda.py", "Package Tool Lambda"),
        ("upload_agent_lambda.py", "Upload Agent Lambda"),
        ("upload_interceptor_lambda.py", "Upload Interceptor Lambda"),
        ("upload_tool_lambda.py", "Upload Tool Lambda"),
    ]
    
    for script, description in steps:
        if not run_command(script, description):
            print("\n" + "=" * 60)
            print("✗ DEPLOYMENT FAILED")
            print("=" * 60)
            sys.exit(1)
    
    print("\n" + "=" * 60)
    print("✓ DEPLOYMENT COMPLETE")
    print("=" * 60)
    print("\nAll Lambda functions deployed successfully!")
    print("\nNext steps:")
    print("  1. Create a test user: python3 create_cognito_user.py")
    print("  2. Run E2E test: python3 test_e2e_flow.py")


if __name__ == "__main__":
    main()
