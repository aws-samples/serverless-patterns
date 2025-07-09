#!/usr/bin/env python3
"""
Test script to verify that all dependencies are properly installed
and the virtual environment is working correctly.
"""

import sys
import os

def test_python_version():
    """Test that Python version is 3.9 or later."""
    print(f"Python version: {sys.version}")
    if sys.version_info < (3, 9):
        print("❌ Python 3.9 or later is required")
        return False
    print("✅ Python version is compatible")
    return True

def test_virtual_environment():
    """Test that we're running in a virtual environment."""
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ Running in virtual environment")
        print(f"   Virtual env path: {sys.prefix}")
        return True
    else:
        print("⚠️  Not running in virtual environment (this is okay for some setups)")
        return True

def test_imports():
    """Test that all required packages can be imported."""
    packages = [
        ('boto3', 'AWS SDK'),
        ('botocore', 'AWS Core'),
        ('kafka', 'Kafka Python client'),
        ('avro', 'Avro serialization'),
        ('pytest', 'Testing framework'),
        ('json', 'JSON handling (built-in)'),
        ('uuid', 'UUID generation (built-in)'),
        ('logging', 'Logging (built-in)'),
    ]
    
    all_good = True
    for package, description in packages:
        try:
            __import__(package)
            print(f"✅ {package} - {description}")
        except ImportError as e:
            print(f"❌ {package} - {description}: {e}")
            all_good = False
    
    return all_good

def test_lambda_functions():
    """Test that Lambda function modules can be imported."""
    print("\nTesting Lambda function imports...")
    
    # Test consumer function
    try:
        sys.path.insert(0, 'kafka_event_consumer_function')
        import app as consumer_app
        print("✅ Consumer function app module")
    except ImportError as e:
        print(f"❌ Consumer function app module: {e}")
        return False
    finally:
        sys.path.pop(0)
    
    # Test producer function
    try:
        sys.path.insert(0, 'kafka_event_producer_function')
        import app as producer_app
        import contact
        import kafka_producer_helper
        print("✅ Producer function modules")
    except ImportError as e:
        print(f"❌ Producer function modules: {e}")
        return False
    finally:
        sys.path.pop(0)
    
    return True

def main():
    """Run all tests."""
    print("MSK Lambda Schema Avro Python SAM - Setup Verification")
    print("=" * 60)
    
    tests = [
        ("Python Version", test_python_version),
        ("Virtual Environment", test_virtual_environment),
        ("Package Imports", test_imports),
        ("Lambda Functions", test_lambda_functions),
    ]
    
    all_passed = True
    for test_name, test_func in tests:
        print(f"\n{test_name}:")
        print("-" * len(test_name))
        if not test_func():
            all_passed = False
    
    print("\n" + "=" * 60)
    if all_passed:
        print("🎉 All tests passed! Your environment is ready.")
        print("\nNext steps:")
        print("1. Deploy MSK cluster: Use MSKAndKafkaClientEC2.yaml")
        print("2. Build application: sam build")
        print("3. Deploy application: sam deploy --guided")
    else:
        print("❌ Some tests failed. Please check the errors above.")
        print("\nTroubleshooting:")
        print("1. Make sure virtual environment is activated: source venv/bin/activate")
        print("2. Install dependencies: pip install -r requirements.txt")
        print("3. Check Python version: python --version")
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
