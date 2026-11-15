# Lambda Runtime delivers a batch of messages to the lambda function
# Each batch of messages has two fields EventSource and EventSourceARN
# Each batch of messages also has a field called Records
# The Records is a map with multiple keys and values
# Each key is a combination of the Topic Name and the Partition Number
# One batch of messages can contain messages from multiple partitions

import json
import base64

def lambda_handler(event, context):
    # Now logging the contents of the batch of Kafka messages delivered to the Lambda function
    print("Received an event: " + str(event))
    print("Event Source: " + event['eventSource'])
    print("Event Source ARN: " + event['eventSourceArn'])
    print("Bootstrap Servers: " + event['bootstrapServers'])
    print("Records: " + str(event['records']))
    # Defining a variable to keep track of the number of the message in the batch of messages
    i=1
    # Now looping through the map for each key (combination of topic and partition)
    for record in event['records']:
        print("Current Record: " + str(event['records'][record]))
        # Now looping through the kafka messages within a particular key
        for messages in event['records'][record]:
            print("********************")
            print("Now printing details of record number: " + str(i))
            print("Topic: " + str(messages['topic']))
            print("Partition: " + str(messages['partition']))
            print("Offset: " + str(messages['offset']))
            print("Topic: " + str(messages['topic']))
            print("Timestamp: " + str(messages['timestamp']))
            print("TimestampType: " + str(messages['timestampType']))
            # each kafka message has a key and a value that are base64 encoded
            if None is not messages.get('key'):
                b64decodedKey=base64.b64decode(messages['key'])
                decodedKey=b64decodedKey.decode('ascii')
            else:
                decodedKey="null"
            if None is not messages.get('value'):
                b64decodedValue=base64.b64decode(messages['value'])
                decodedValue=b64decodedValue.decode('ascii')
            else:
                decodedValue="null"
            print("Key = " + str(decodedKey))
            print("Value = " + str(decodedValue))
            print("Now finished printing details of record number: " + str(i))
            print("********************")
            i=i+1
    return {
        'statusCode': 200,
    }
