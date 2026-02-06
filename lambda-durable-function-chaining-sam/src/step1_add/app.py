def lambda_handler(event, context):
    """Step 1: Add initial data fields to the input."""
    return {
        'id': event.get('id', 'unknown'),
        'name': event.get('name', 'default'),
        'step1_completed': True,
        'value': event.get('value', 0) + 10
    }
