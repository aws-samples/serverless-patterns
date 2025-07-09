# MSK Lambda Schema Avro Python SAM - Setup Guide

This guide provides step-by-step instructions for setting up and using the MSK Lambda Schema Avro Python SAM project.

## Quick Start

1. **Set up Python environment:**
   ```bash
   ./setup_venv.sh
   ```

2. **Activate virtual environment:**
   ```bash
   source venv/bin/activate
   ```

3. **Verify setup:**
   ```bash
   python test_setup.py
   ```

4. **Deploy (if MSK cluster exists):**
   ```bash
   ./deploy.sh
   ```

## Project Structure

```
msk-lambda-schema-avro-python-sam/
├── README.md                           # Main documentation
├── SETUP_GUIDE.md                     # This setup guide
├── requirements.txt                    # Root-level Python dependencies
├── setup_venv.sh                      # Virtual environment setup script
├── test_setup.py                      # Setup verification script
├── deploy.sh                          # Automated deployment script
├── cleanup.sh                         # Cleanup script
├── template.yaml                      # SAM template (working version)
├── template_original.yaml             # SAM template with placeholders
├── MSKAndKafkaClientEC2.yaml         # CloudFormation for MSK cluster
├── example-pattern.json              # Pattern metadata
├── samconfig.toml                     # SAM configuration
├── .gitignore                         # Git ignore file
├── venv/                              # Python virtual environment
├── events/
│   └── event.json                     # Sample event for testing
├── schemas/
│   └── contact.avsc                   # Avro schema definition
├── kafka_event_consumer_function/
│   ├── app.py                         # Consumer Lambda handler
│   ├── requirements.txt               # Consumer dependencies
│   └── tests/
│       ├── test_app.py                # Unit tests
│       └── requirements.txt           # Test dependencies
└── kafka_event_producer_function/
    ├── app.py                         # Producer Lambda handler
    ├── contact.py                     # Contact data class
    ├── kafka_producer_helper.py       # Kafka helper utilities
    └── requirements.txt               # Producer dependencies
```

## Dependencies

### Root Level Dependencies (`requirements.txt`)
- **boto3** - AWS SDK for Python
- **botocore** - AWS SDK core functionality
- **kafka-python** - Kafka client library
- **avro-python3** - Avro serialization library
- **pytest** - Testing framework
- **pytest-mock** - Mocking for tests
- **requests** - HTTP library
- **urllib3** - HTTP client
- **six** - Python 2/3 compatibility

### Lambda Function Dependencies
Each Lambda function has its own `requirements.txt` with the specific dependencies needed for that function.

## Virtual Environment

The project uses a Python virtual environment to isolate dependencies:

- **Location**: `venv/` directory
- **Python Version**: 3.9+ (tested with 3.13)
- **Activation**: `source venv/bin/activate`
- **Deactivation**: `deactivate`

### Virtual Environment Commands

```bash
# Create virtual environment (done by setup_venv.sh)
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Verify installation
python test_setup.py

# Deactivate virtual environment
deactivate

# Remove virtual environment
rm -rf venv/
```

## Development Workflow

### 1. Initial Setup
```bash
# Clone or navigate to project directory
cd msk-lambda-schema-avro-python-sam

# Set up virtual environment
./setup_venv.sh

# Activate virtual environment
source venv/bin/activate

# Verify setup
python test_setup.py
```

### 2. Development
```bash
# Always activate virtual environment first
source venv/bin/activate

# Make code changes
# ...

# Run tests
cd kafka_event_consumer_function
python -m pytest tests/ -v
cd ..

# Test locally (optional)
sam build
sam local invoke LambdaMSKProducerPythonFunction --event events/event.json
```

### 3. Deployment
```bash
# Activate virtual environment
source venv/bin/activate

# Automated deployment (recommended)
./deploy.sh

# OR manual deployment
sam build
sam deploy --guided
```

### 4. Testing
```bash
# Activate virtual environment
source venv/bin/activate

# Invoke producer function
sam remote invoke LambdaMSKProducerPythonFunction --region $AWS_REGION --stack-name msk-lambda-schema-avro-python-sam

# Check consumer logs
sam logs --name LambdaMSKConsumerPythonFunction --stack-name msk-lambda-schema-avro-python-sam --region $AWS_REGION
```

### 5. Cleanup
```bash
# Activate virtual environment
source venv/bin/activate

# Clean up AWS resources
./cleanup.sh

# Clean up local environment
deactivate
rm -rf venv/
```

## Troubleshooting

### Common Issues

1. **Import Errors**
   ```bash
   # Solution: Activate virtual environment
   source venv/bin/activate
   
   # Verify dependencies
   python test_setup.py
   ```

2. **Virtual Environment Not Found**
   ```bash
   # Solution: Create virtual environment
   ./setup_venv.sh
   ```

3. **Python Version Issues**
   ```bash
   # Check Python version
   python --version
   
   # Should be 3.9 or later
   # Install newer Python if needed
   ```

4. **SAM Build Failures**
   ```bash
   # Ensure Docker is running
   docker --version
   
   # Ensure virtual environment is activated
   source venv/bin/activate
   
   # Clean and rebuild
   sam build --use-container
   ```

5. **Kafka Connection Issues**
   ```bash
   # Check if MSK cluster is running
   aws kafka list-clusters
   
   # Verify VPC and security group settings
   # Check CloudFormation outputs
   ```

### Verification Commands

```bash
# Check virtual environment
echo $VIRTUAL_ENV

# Check Python path
which python

# Check installed packages
pip list

# Test imports
python -c "import boto3, kafka, avro; print('All imports successful')"

# Run setup verification
python test_setup.py
```

## Environment Variables

The Lambda functions use these environment variables:

### Consumer Function
- `LOG_LEVEL` - Logging level (INFO, DEBUG, etc.)
- `PARAM1` - Example parameter

### Producer Function
- `MSK_CLUSTER_ARN` - ARN of the MSK cluster
- `MSK_TOPIC` - Kafka topic name
- `REGISTRY_NAME` - Glue Schema Registry name
- `CONTACT_SCHEMA_NAME` - Avro schema name
- `LOG_LEVEL` - Logging level

## Next Steps

1. **Deploy MSK Cluster**: Use `MSKAndKafkaClientEC2.yaml`
2. **Configure Parameters**: Update template with your MSK details
3. **Deploy Lambda Functions**: Run `./deploy.sh`
4. **Test the Application**: Invoke producer and check consumer logs
5. **Monitor**: Use CloudWatch for monitoring and debugging

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify your setup with `python test_setup.py`
3. Review the main README.md for detailed documentation
4. Check AWS CloudWatch logs for runtime errors
