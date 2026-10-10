import json
import os
import time
import random
import logging
from datetime import datetime, timezone

logger = logging.getLogger()
logger.setLevel(os.environ.get('LOG_LEVEL', 'INFO'))


def lambda_handler(event, context):
    """
    Main scheduled Lambda function invoked by EventBridge Scheduler.
    Simulates processing work and can simulate failures for testing.
    """
    logger.info('=' * 80)
    logger.info('SCHEDULED LAMBDA EXECUTION - Started')
    logger.info('=' * 80)

    log_info('Scheduled function invoked by EventBridge Scheduler', {'event': event})

    execution_time = datetime.now(timezone.utc).isoformat()
    simulate_failure = os.environ.get('SIMULATE_FAILURE', 'false').lower() == 'true'

    try:
        logger.info('Execution Time: %s', execution_time)
        logger.info('Simulate Failure: %s', simulate_failure)

        # Simulate failure if environment variable is set
        if simulate_failure:
            logger.info('SIMULATING FAILURE')
            logger.info('This will trigger:')
            logger.info('1. Lambda async retry (up to 2 times)')
            logger.info('2. After all retries fail - Event sent to Lambda Execution DLQ')
            raise Exception('Simulated failure for testing Lambda Execution DLQ flow')

        # Simulate some processing work
        logger.info('Processing scheduled task...')

        # Example: Process data, call APIs, update databases, etc.
        processing_result = {
            'tasksProcessed': random.randint(1, 100),
            'recordsUpdated': random.randint(0, 50),
            'apiCallsMade': random.randint(0, 10),
            'dataProcessedMB': round(random.uniform(0, 100), 2)
        }

        logger.info('Tasks processed: %s', processing_result['tasksProcessed'])
        logger.info('Records updated: %s', processing_result['recordsUpdated'])
        logger.info('API calls made: %s', processing_result['apiCallsMade'])
        logger.info('Data processed: %s MB', processing_result['dataProcessedMB'])

        # Simulate processing time
        time.sleep(0.1 + random.random() * 0.4)

        result = {
            'statusCode': 200,
            'success': True,
            'executionTime': execution_time,
            'processingResult': processing_result,
            'message': 'Scheduled task completed successfully'
        }

        log_info('Scheduled function completed successfully', {'result': result})

        logger.info('=' * 80)
        logger.info('SCHEDULED LAMBDA EXECUTION - Completed Successfully')
        logger.info('=' * 80)

        return result

    except Exception as error:
        logger.error('=' * 80)
        logger.error('SCHEDULED LAMBDA EXECUTION - Failed')
        logger.error('Error: %s', str(error))
        logger.error('Lambda async retry will attempt this execution again')
        logger.error('After retries exhausted, event goes to Lambda Execution DLQ')
        logger.error('=' * 80)

        log_error('Scheduled function failed', error, {'executionTime': execution_time})

        # Re-raise to trigger retry and DLQ behavior
        raise


def log_info(message, data=None):
    """Log informational message in JSON format"""
    log_entry = {
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'level': 'INFO',
        'message': message
    }
    if data:
        log_entry.update(data)
    logger.info(json.dumps(log_entry))


def log_error(message, error, data=None):
    """Log error message in JSON format"""
    log_entry = {
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'level': 'ERROR',
        'message': message,
        'error': str(error),
        'errorType': type(error).__name__
    }
    if data:
        log_entry.update(data)
    logger.error(json.dumps(log_entry))
