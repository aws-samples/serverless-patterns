#!/usr/bin/env python3
"""
Local test script for the EventBridge ECS Cron job
Run this to test the job locally before deploying to ECS
"""

import os
import sys

# Add the current directory to Python path so we can import app
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Set some test environment variables
os.environ["TASK_FAMILY"] = "local-test-task"
os.environ["CLUSTER_NAME"] = "local-test-cluster"

# Import and run the main application
from app import main

if __name__ == "__main__":
    print("🚀 Running EventBridge ECS Cron Job locally...")
    print("=" * 50)
    
    try:
        main()
        print("=" * 50)
        print("✅ Job completed successfully!")
        
    except Exception as e:
        print("=" * 50)
        print(f"❌ Job failed: {e}")
        sys.exit(1)