import boto3
import logging
import os
import base64
import json

# Initialize AWS SDK clients Kinesis
kinesis_client = boto3.client('kinesis')

# Environment variables for lambda function read message from Kinesis data Stream
KINESIS_STREAM_NAME = os.environ['KINESIS_STREAM_NAME']

# Initialize and configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Entry point to the Lambda function
def lambda_handler(event, context):
    # Record/Data should match the below Keys and the data type
    required_fields = {"AtomicNumber": int, "Element": str, "Symbol": str, "AtomicMass": float}
    logger.info(f"Incoming event: -->  {event}")
    
    # Variable to print the Unique sequence of each record
    curRecordSequenceNumber = ""
    
    # Loop through the Records to read each record
    for record in event['Records']:
        curRecordSequenceNumber = record["kinesis"]["sequenceNumber"]
        logger.info(f"Sequence Number of the current record --> {curRecordSequenceNumber}")

        # Convert the base64 data into utf before validating for the schema
        payload = json.loads(base64.b64decode(record['kinesis']['data']).decode('utf-8'))
        logger.info(f"Individual record content --> {payload}")
        if not isinstance(payload, dict):
            logger.info("Invalid JSON Data Structure.The parsed data does not adhere to the expeced JSON data structure.")
            raise ValueError("Invalid JSON Data Structure",
                             "The parsed data does not adhere to the expeced JSON data structure.")

        # Verify if the key, value are as per expectations    
        for key, value_type in required_fields.items():
            if key not in payload:
                logger.info(f"Missing '{key}' field in JSON.")
                raise ValueError(f"Missing '{key}' field in JSON.")
            if not isinstance(payload[key], value_type):
                logger.info(f"'{key}' field should be of type {value_type.__name__}.")
                raise ValueError(f"'{key}' field should be of type {value_type.__name__}.") 