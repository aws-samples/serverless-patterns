def lambda_handler(event, context):
    """Step 2: Transform and enrich the data."""
    return {
        **event,
        'step2_completed': True,
        'value': event.get('value', 0) * 2,
        'transformed_name': event.get('name', '').upper()
    }
