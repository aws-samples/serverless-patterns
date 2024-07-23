#write a lambda handler

import json
import uuid
import boto3

def lambda_handler(event, context):
    event_bridge = boto3.client('events')

    #generate batch_id as uuid
    batch_id = str(uuid.uuid4())
    #client_id to preference dictionary
    client_id_preference_dict = {'1':'email', '2':'sftp', '3':'3papi'}

    for client_id_key_loop, preference_distribution in client_id_preference_dict.items():
        response = event_bridge.put_events(
            Entries=[
                        {                            
                            'Source': 'content-generator',                            
                            'DetailType': 'Client-data',                            
                            'Detail': json.dumps(
                                    {'clientId': client_id_key_loop, 
                                     'batchId':batch_id,                             
                                     'preferenceDistribution': preference_distribution,                                      
                                     })
                        }                
                    ]           
                    )
        print('Sent event '+client_id_key_loop+' '+preference_distribution)
        
          
    return {
        'statusCode': 200,
        'body': json.dumps('Completed')
    }