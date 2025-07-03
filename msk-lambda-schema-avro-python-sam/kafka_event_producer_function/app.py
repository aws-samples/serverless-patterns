"""
AWS Lambda function that produces AVRO messages to Amazon MSK using AWS Glue Schema Registry.

This function demonstrates:
- AVRO message serialization using aws-glue-schema-registry package
- Kafka message production to MSK with IAM authentication
- AWS Lambda Powertools for logging, tracing, and metrics
- Event filtering demonstration with different zip code prefixes
"""

import json
import os
import random
import boto3
import io
import fastavro
from typing import Dict, Any
from kafka import KafkaProducer

# AWS Lambda Powertools
from aws_lambda_powertools import Logger, Tracer, Metrics
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.metrics import MetricUnit

# AWS Glue Schema Registry
from aws_schema_registry import SchemaRegistryClient
from aws_schema_registry.serde import encode

# Initialize Powertools
logger = Logger()
tracer = Tracer()
metrics = Metrics(namespace="MSKProducer")

# Contact AVRO schema definition
CONTACT_AVRO_SCHEMA = {
    "type": "record",
    "name": "Contact",
    "namespace": "com.amazonaws.services.lambda.samples.events.msk",
    "fields": [
        {"name": "firstname", "type": ["null", "string"], "default": None},
        {"name": "lastname", "type": ["null", "string"], "default": None},
        {"name": "company", "type": ["null", "string"], "default": None},
        {"name": "street", "type": ["null", "string"], "default": None},
        {"name": "city", "type": ["null", "string"], "default": None},
        {"name": "county", "type": ["null", "string"], "default": None},
        {"name": "state", "type": ["null", "string"], "default": None},
        {"name": "zip", "type": ["null", "string"], "default": None},
        {"name": "homePhone", "type": ["null", "string"], "default": None},
        {"name": "cellPhone", "type": ["null", "string"], "default": None},
        {"name": "email", "type": ["null", "string"], "default": None},
        {"name": "website", "type": ["null", "string"], "default": None}
    ]
}


def get_schema_version_id(registry_name: str, schema_name: str) -> str:
    """Get or register schema version using AWS Glue Schema Registry."""
    try:
        glue_client = boto3.client('glue')
        schema_registry_client = SchemaRegistryClient(
            glue_client=glue_client,
            registry_name=registry_name
        )
        
        schema_version = schema_registry_client.get_or_register_schema_version(
            definition=json.dumps(CONTACT_AVRO_SCHEMA),
            schema_name=schema_name,
            data_format='AVRO'
        )
        
        logger.info("Schema version obtained", 
                   schema_version_id=str(schema_version.version_id),
                   version_number=schema_version.version_number,
                   schema_name=schema_name,
                   registry_name=registry_name)
        
        return schema_version.version_id
        
    except Exception as e:
        logger.exception("Failed to get schema version", 
                        error=str(e),
                        registry_name=registry_name,
                        schema_name=schema_name)
        raise


def serialize_avro_message(contact_data: Dict[str, Any], schema_version_id: str) -> bytes:
    """Serialize contact data to AVRO format with AWS Glue Schema Registry header."""
    try:
        # Serialize data using fastavro
        avro_buffer = io.BytesIO()
        fastavro.schemaless_writer(avro_buffer, CONTACT_AVRO_SCHEMA, contact_data)
        avro_data = avro_buffer.getvalue()
        
        # Add AWS Glue Schema Registry header using the package
        encoded_message = encode(avro_data, schema_version_id)
        
        logger.debug("Message serialized", 
                    avro_data_size=len(avro_data),
                    total_message_size=len(encoded_message),
                    header_size=len(encoded_message) - len(avro_data))
        
        return encoded_message
        
    except Exception as e:
        logger.exception("Failed to serialize message", 
                        error=str(e),
                        contact_data=contact_data)
        raise


def create_sample_contact(index: int) -> Dict[str, Any]:
    """Create a sample contact with realistic data."""
    first_names = ["John", "Jane", "Michael", "Sarah", "David", "Emily", "Robert", "Lisa", "William", "Alice"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis"]
    companies = ["TechCorp", "DataSys", "CloudInc", "DevCo", "InfoTech", "SoftWare", "NetSolutions"]
    cities = ["Seattle", "Portland", "San Francisco", "Los Angeles", "Denver"]
    states = ["WA", "OR", "CA", "CO", "TX"]
    
    # Alternate between zip codes starting with 1000 and 2000 for filtering demo
    zip_prefix = "1000" if index % 2 == 0 else "2000"
    zip_suffix = f"{random.randint(10, 99)}"
    
    return {
        "firstname": first_names[index % len(first_names)],
        "lastname": last_names[index % len(last_names)],
        "company": companies[index % len(companies)],
        "street": f"{random.randint(100, 9999)} {random.choice(['Main St', 'Oak Ave', 'Pine Rd', 'Elm Dr'])}",
        "city": cities[index % len(cities)],
        "county": f"{random.choice(['King', 'Pierce', 'Snohomish'])} County",
        "state": states[index % len(states)],
        "zip": f"{zip_prefix}{zip_suffix}",
        "homePhone": f"({random.randint(200, 999)}) {random.randint(200, 999)}-{random.randint(1000, 9999)}",
        "cellPhone": f"({random.randint(200, 999)}) {random.randint(200, 999)}-{random.randint(1000, 9999)}",
        "email": f"user{index}@example.com",
        "website": f"https://www.example{index}.com"
    }


def get_bootstrap_brokers(cluster_arn: str) -> str:
    """Get bootstrap brokers for an MSK cluster."""
    try:
        kafka_client = boto3.client('kafka')
        response = kafka_client.get_bootstrap_brokers(ClusterArn=cluster_arn)
        return response['BootstrapBrokerStringSaslIam']
    except Exception as e:
        logger.exception("Failed to get bootstrap brokers", cluster_arn=cluster_arn)
        raise


@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_lambda_handler
@metrics.log_metrics
def lambda_handler(event: Dict[str, Any], context: Any) -> str:
    """
    Lambda function handler that produces AVRO messages to a Kafka topic.
    
    Args:
        event: Lambda event containing configuration
        context: Lambda context
        
    Returns:
        Success message
    """
    logger.info("=== MSK AVRO Producer Lambda started ===")
    
    try:
        # Get configuration from environment variables
        cluster_arn = os.environ.get('MSK_CLUSTER_ARN')
        kafka_topic = os.environ.get('MSK_TOPIC', 'msk-serverless-topic')
        message_count = int(os.environ.get('MESSAGE_COUNT', '10'))
        registry_name = os.environ.get('REGISTRY_NAME', 'GlueSchemaRegistryForMSK')
        schema_name = os.environ.get('CONTACT_SCHEMA_NAME', 'ContactSchema')
        
        if not cluster_arn:
            raise ValueError("MSK_CLUSTER_ARN environment variable is required")
        
        logger.info("Configuration loaded", 
                   cluster_arn=cluster_arn,
                   kafka_topic=kafka_topic,
                   message_count=message_count,
                   registry_name=registry_name,
                   schema_name=schema_name)
        
        # Get schema version ID
        schema_version_id = get_schema_version_id(registry_name, schema_name)
        
        # Get bootstrap brokers and create Kafka producer
        bootstrap_servers = get_bootstrap_brokers(cluster_arn)
        producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            security_protocol='SASL_SSL',
            sasl_mechanism='AWS_MSK_IAM',
            key_serializer=lambda x: x.encode('utf-8') if x else None,
            value_serializer=lambda x: x,  # Raw bytes - AVRO data is already serialized
            acks='all',
            retries=3,
            max_block_ms=120000,
            request_timeout_ms=60000,
        )
        
        logger.info("Starting message production", 
                   topic=kafka_topic,
                   message_count=message_count,
                   schema_version_id=str(schema_version_id))
        
        # Track zip code distribution for filtering demo
        zip_1000_count = 0
        zip_2000_count = 0
        
        # Send messages
        for i in range(message_count):
            contact = create_sample_contact(i)
            message_key = f"contact-{i+1}"
            
            # Track zip code distribution
            if contact['zip'].startswith('1000'):
                zip_1000_count += 1
            elif contact['zip'].startswith('2000'):
                zip_2000_count += 1
            
            # Serialize and send message
            avro_message = serialize_avro_message(contact, schema_version_id)
            future = producer.send(kafka_topic, key=message_key, value=avro_message)
            record_metadata = future.get(timeout=60)
            
            logger.info("Message sent successfully", 
                       message_number=i+1,
                       message_key=message_key,
                       partition=record_metadata.partition,
                       offset=record_metadata.offset,
                       message_size=len(avro_message))
            
            # Add metrics
            metrics.add_metric(name="AvroMessagesSent", unit=MetricUnit.Count, value=1)
            metrics.add_metric(name="AvroMessageSize", unit=MetricUnit.Bytes, value=len(avro_message))
        
        # Add distribution metrics for filtering demo
        metrics.add_metric(name="AvroMessages1000Prefix", unit=MetricUnit.Count, value=zip_1000_count)
        metrics.add_metric(name="AvroMessages2000Prefix", unit=MetricUnit.Count, value=zip_2000_count)
        
        # Close producer
        producer.close()
        
        success_message = (
            f"Successfully sent {message_count} AVRO messages to Kafka topic: {kafka_topic} "
            f"using schema {schema_name} (version {schema_version_id}) from registry {registry_name} "
            f"(Zip codes: {zip_1000_count} with prefix 1000, {zip_2000_count} with prefix 2000)"
        )
        
        logger.info("MSK AVRO Producer Lambda completed successfully", 
                   success_message=success_message,
                   total_messages_sent=message_count,
                   schema_version_id=str(schema_version_id))
        
        return success_message
        
    except Exception as e:
        logger.exception("Error in lambda_handler", 
                        error=str(e),
                        error_type=type(e).__name__)
        metrics.add_metric(name="AvroErrors", unit=MetricUnit.Count, value=1)
        raise RuntimeError(f"Failed to send AVRO messages: {str(e)}") from e
