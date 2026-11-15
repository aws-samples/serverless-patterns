import json
import re

TENANT_ID_PATTERN = re.compile(r'^[a-zA-Z0-9-]{1,64}$')

def handler(event, context):
    tenant_id = context.tenant_id

    if not tenant_id:
        raise ValueError("tenant_id is missing from context")

    if not TENANT_ID_PATTERN.match(tenant_id):
        raise ValueError(f"Invalid tenant ID format: {tenant_id}")

    if not isinstance(event, dict):
        raise ValueError(f"Expected event to be a dict, got {type(event).__name__}")

    print(f"Processing request for tenant: {tenant_id}")
    print(f"Event data: {json.dumps(event)}")

    # Process tenant-specific logic here
    result = {
        'tenant_id': tenant_id,
        'message': 'Request processed successfully',
        'data': event
    }

    return result
