import json
import os
import time
import random
from datetime import datetime


def lambda_handler(event, context):
    """
    Main scheduled Lambda function invoked by EventBridge Scheduler.
    Simulates processing work and can simulate failures for testing.
    """
    print('=' * 80)
    print('SCHEDULED LAMBDA EXECUTION - Started')
    print('=' * 80)
    
    log_info('Scheduled function invoked by EventBridge Scheduler', {'event': event})
    
    execution_time = datetime.utcnow().isoformat() + 'Z'
    simulate_failure = os.environ.get('SIMULATE_FAILURE', 'false').lower() == 'true'
    
    try:
        print(f'\nExecution Time: {execution_time}')
        print(f'Simulate Failure: {simulate_failure}')
        
        # Simulate failure if environment variable is set
        if simulate_failure:
            print('\nSIMULATING FAILURE')
            print('This will trigger:')
            print('1. Lambda async retry (up to 2 times)')
            print('2. After all retries fail - Event sent to Lambda Execution DLQ')
            raise Exception('Simulated failure for testing Lambda Execution DLQ flow')
        
        # Simulate some processing work
        print('\nProcessing scheduled task...')
        
        # Example: Process data, call APIs, update databases, etc.
        processing_result = {
            'tasksProcessed': random.randint(1, 100),
            'recordsUpdated': random.randint(0, 50),
            'apiCallsMade': random.randint(0, 10),
            'dataProcessedMB': round(random.uniform(0, 100), 2)
        }
        
        print(f'Tasks processed: {processing_result["tasksProcessed"]}')
        print(f'Records updated: {processing_result["recordsUpdated"]}')
        print(f'API calls made: {processing_result["apiCallsMade"]}')
        print(f'Data processed: {processing_result["dataProcessedMB"]} MB')
        
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
        
        print('\n' + '=' * 80)
        print('SCHEDULED LAMBDA EXECUTION - Completed Successfully')
        print('=' * 80 + '\n')
        
        return result
        
    except Exception as error:
        print('\n' + '=' * 80)
        print('SCHEDULED LAMBDA EXECUTION - Failed')
        print(f'Error: {str(error)}')
        print('Lambda async retry will attempt this execution again')
        print('After retries exhausted, event goes to Lambda Execution DLQ')
        print('=' * 80 + '\n')
        
        log_error('Scheduled function failed', error, {'executionTime': execution_time})
        
        # Re-raise to trigger retry and DLQ behavior
        raise


def log_info(message, data=None):
    """Log informational message in JSON format"""
    log_entry = {
        'timestamp': datetime.utcnow().isoformat() + 'Z',
        'level': 'INFO',
        'message': message
    }
    if data:
        log_entry.update(data)
    print(json.dumps(log_entry))


def log_error(message, error, data=None):
    """Log error message in JSON format"""
    log_entry = {
        'timestamp': datetime.utcnow().isoformat() + 'Z',
        'level': 'ERROR',
        'message': message,
        'error': str(error),
        'errorType': type(error).__name__
    }
    if data:
        log_entry.update(data)
    print(json.dumps(log_entry))
