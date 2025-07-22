import json


def handler(event, context):
    print(event)
    connection_id = event['requestContext']['connectionId']
    route_key = event['requestContext']['routeKey']
    
    # Handle different route types
    if route_key == "$connect":
        print("Connect Route Triggered, Connection ID:", connection_id)
        return handle_connect(connection_id)
    elif route_key == "$disconnect":
        print("Disconnect Route Triggered, Connection ID:", connection_id)
        return handle_disconnect(connection_id)
    else:
        # Handle other route types or invalid routes
        print("Default Route Triggered, Connection ID:", connection_id)
        return handle_default(event, connection_id)

def handle_connect(connection_id):
    return {
        'statusCode': 200,
        'body': f'Connected with ID: {connection_id}'
    }

def handle_disconnect(connection_id):
    return {
        'statusCode': 200,
        'body': f'Disconnected ID: {connection_id}'
    }

def handle_default(event, connection_id):
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Message received',
            'connectionId': connection_id,
            'event': event
        })
    }