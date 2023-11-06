import json

def lambda_handler(event, context):
    # Print the event details to see the contents received by the Lambda function
    print("Received event:")
    print(json.dumps(event, indent=2))
    
    
    #info = event.get('s3', {})
    #file_key = info.get('object', {}).get('key')
    #print("file_key",file_key)

    
    # Get the S3 event record from the event
    #s3_event_record = event['Records'][0]['s3']
    
    # Get the bucket name and object key from the S3 event record
    #bucket_name = s3_event_record['bucket']['name']
    #object_key = s3_event_record['object']['key']
    
    
    s3_event = event['detail']
    
     # Get the bucket name from the S3 event
    bucket_name = s3_event['bucket']['name']
    
    # Get the object key from the S3 event
    object_key = s3_event['object']['key']
    
    # Extract the file extension from the object key
    file_extension = object_key.split('.')[-1]
    
    # Define a dictionary to map file extensions to file types
    file_type_map = {
        'csv': 'CSV',
        'json': 'JSON',
        'xml': 'XML',
        'txt': 'Text',
        # Add more file types as needed
    }
    
    # Look up the file type based on the file extension
    file_type = file_type_map.get(file_extension.lower(), 'Unknown')
    
    print("file_type", file_type)
    
    # Prepare the response
    response = {
        'statusCode': 200,
        'body': {'file_type': file_type,
                 'bucket_name': bucket_name,
                 'object_key': object_key
        },
        'headers': {
            'Content-Type': 'application/json'
        }
    }
    
    return response
