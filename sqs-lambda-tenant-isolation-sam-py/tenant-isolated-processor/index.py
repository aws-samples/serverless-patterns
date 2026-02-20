import json

def handler(event, context):
    tenant_id = context.tenant_id
    
    print(f"Processing request for tenant: {tenant_id}")
    print(f"Event data: {json.dumps(event)}")
    
    # Process tenant-specific logic here
    result = {
        'tenant_id': tenant_id,
        'message': 'Request processed successfully',
        'data': event
    }
    
    return result
