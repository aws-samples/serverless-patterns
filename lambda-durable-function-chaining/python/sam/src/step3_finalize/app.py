def lambda_handler(event, context):
    """Step 3: Finalize the data with status."""
    return {
        **event,
        'step3_completed': True,
        'status': 'COMPLETED',
        'final_value': event.get('value', 0) + 5
    }
