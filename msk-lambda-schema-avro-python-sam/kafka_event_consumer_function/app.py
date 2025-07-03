"""
AWS Lambda function that consumes AVRO messages from Amazon MSK using AWS Lambda Powertools.

This function demonstrates:
- AVRO message deserialization using AWS Lambda Powertools
- Event source mapping with filtering (only processes messages with zip codes starting with "2000")
- Automatic dead letter queue handling for failed messages
- Structured logging with AWS Lambda Powertools
"""

from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.kafka import ConsumerRecords, SchemaConfig, kafka_consumer
from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger()

# Contact AVRO schema definition (must match producer schema)
CONTACT_AVRO_SCHEMA = """
{
    "type": "record",
    "name": "Contact",
    "namespace": "com.amazonaws.services.lambda.samples.events.msk",
    "fields": [
        {"name": "firstname", "type": ["null", "string"], "default": null},
        {"name": "lastname", "type": ["null", "string"], "default": null},
        {"name": "company", "type": ["null", "string"], "default": null},
        {"name": "street", "type": ["null", "string"], "default": null},
        {"name": "city", "type": ["null", "string"], "default": null},
        {"name": "county", "type": ["null", "string"], "default": null},
        {"name": "state", "type": ["null", "string"], "default": null},
        {"name": "zip", "type": ["null", "string"], "default": null},
        {"name": "homePhone", "type": ["null", "string"], "default": null},
        {"name": "cellPhone", "type": ["null", "string"], "default": null},
        {"name": "email", "type": ["null", "string"], "default": null},
        {"name": "website", "type": ["null", "string"], "default": null}
    ]
}
"""

# Configure schema for automatic AVRO deserialization
schema_config = SchemaConfig(
    value_schema_type="AVRO",
    value_schema=CONTACT_AVRO_SCHEMA,
)


@kafka_consumer(schema_config=schema_config)
def lambda_handler(event: ConsumerRecords, context: LambdaContext):
    """
    Lambda handler for processing MSK events with automatic AVRO deserialization.
    
    Note: This function only receives messages with zip codes starting with "2000"
    due to the event source mapping filter configuration in the SAM template.
    
    Args:
        event: ConsumerRecords containing Kafka records with automatic AVRO deserialization
        context: Lambda context
        
    Returns:
        Success response
    """
    logger.info("=== MSK AVRO Consumer Lambda started ===")
    
    try:
        for record in event.records:
            logger.info(f"Processing record - Topic: {record.topic}, Partition: {record.partition}, Offset: {record.offset}")
            logger.info(f"Timestamp: {record.timestamp}, TimestampType: {record.timestamp_type}")
            
            # Record key (automatically decoded from base64)
            logger.info(f"Record key: {record.key}")
            
            # Record value (automatically deserialized from AVRO by AWS Lambda Powertools)
            contact = record.value
            logger.info(f"Contact data: {contact}")
            
            # Process the contact data
            if contact:
                name = f"{contact.get('firstname', '')} {contact.get('lastname', '')}".strip()
                zip_code = contact.get('zip', '')
                email = contact.get('email', '')
                
                logger.info(f"Contact details - Name: {name}, Zip: {zip_code}, Email: {email}")
                
                # Add your business logic here
                # For example: save to database, send notifications, etc.
            
        logger.info(f"Successfully processed {len(list(event.records))} records")
        logger.info("=== MSK AVRO Consumer Lambda completed ===")
        
        return {"statusCode": 200}
        
    except Exception as e:
        logger.exception(f"Error processing Kafka records: {str(e)}")
        # Let the exception propagate to trigger DLQ handling
        raise
