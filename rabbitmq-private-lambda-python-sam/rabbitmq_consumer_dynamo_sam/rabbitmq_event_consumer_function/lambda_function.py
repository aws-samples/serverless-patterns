import os
import json
import base64
import time
import boto3

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('DYNAMO_DB_TABLE', 'RabbitMQDynamoDBTablePython')
table = dynamodb.Table(table_name)


def decode_header_value(header_value):
    if isinstance(header_value, dict) and 'bytes' in header_value:
        byte_array = header_value['bytes']
        return bytes(byte_array).decode('utf-8')
    return str(header_value)


def lambda_handler(event, context):
    try:
        print("Begin Event *************")
        print(json.dumps(event))
        print("End Event ***************")

        event_source = event.get('eventSource', '')
        event_source_arn = event.get('eventSourceArn', '')
        print(f"EventSource = {event_source}")
        print(f"EventSourceARN = {event_source_arn}")

        print("Now iterating through Map of all queues")
        rmq_messages_by_queue = event.get('rmqMessagesByQueue', {})

        for queue_key, messages in rmq_messages_by_queue.items():
            queue_name = queue_key.split("::")[0]
            print(f"Current Queue Name = {queue_name}")
            print(f"Now iterating through each message in this queue - {queue_name}")

            for message in messages:
                print("Now logging a new message")
                encoded_data = message.get('data', '')
                print(f"EncodedData = {encoded_data}")

                decoded_data = base64.b64decode(encoded_data).decode('utf-8')
                print(f"DecodedData = {decoded_data}")

                person = json.loads(decoded_data)
                print(f"This person = {person}")

                redelivered = message.get('redelivered', False)
                print(f"Whether Redelivered = {redelivered}")

                basic_properties = message.get('basicProperties', {})
                print(f"AppID = {basic_properties.get('appId')}")
                print(f"BodySize = {basic_properties.get('bodySize')}")
                print(f"ClusterId = {basic_properties.get('clusterId')}")
                print(f"ContentEncoding = {basic_properties.get('contentEncoding')}")
                print(f"ContentType = {basic_properties.get('contentType')}")
                print(f"CorrelationId = {basic_properties.get('correlationId')}")
                print(f"DeliveryMode = {basic_properties.get('deliveryMode')}")
                print(f"Expiration = {basic_properties.get('expiration')}")
                print(f"MessageId = {basic_properties.get('messageId')}")
                print(f"Priority = {basic_properties.get('priority')}")
                print(f"ReplyTo = {basic_properties.get('replyTo')}")
                print(f"Timestamp = {basic_properties.get('timestamp')}")
                print(f"Type = {basic_properties.get('type')}")
                print(f"UserId = {basic_properties.get('userId')}")

                print("Now iterating through the headers in this message")
                headers = basic_properties.get('headers', {})
                for header_name, header_value in headers.items():
                    decoded_header = decode_header_value(header_value)
                    print(f"Header Name = {header_name} and Header Value = {decoded_header}")
                print("Now done iterating through the headers in this message")
                print("Now done logging a new message")

                aws_sam_local = os.environ.get('AWS_SAM_LOCAL')
                if aws_sam_local is None:
                    insert_into_dynamodb(
                        message, person, queue_name,
                        event_source, event_source_arn
                    )

            print("Now done iterating through each message in this queue")

        print("Done iterating through Map of all queues")
        return "200"

    except Exception as e:
        print(f"An exception occurred - {str(e)}")
        return "500"


def insert_into_dynamodb(message, person, queue_name, event_source, event_source_arn):
    basic_properties = message.get('basicProperties', {})
    message_id = basic_properties.get('messageId', '')
    print(f"Now inserting a row in DynamoDB for messageID = {message_id}")

    item = {
        'MessageID': message_id,
        'EventSource': event_source,
        'EventSourceARN': event_source_arn,
        'Queue': queue_name,
        'Firstname': person.get('firstname', ''),
        'Lastname': person.get('lastname', ''),
        'Company': person.get('company', ''),
        'Street': person.get('street', ''),
        'City': person.get('city', ''),
        'County': person.get('county', ''),
        'State': person.get('state', ''),
        'Zip': person.get('zip', ''),
        'Cellphone': person.get('cellPhone', ''),
        'Homephone': person.get('homePhone', ''),
        'Email': person.get('email', ''),
        'Website': person.get('website', ''),
        'CorrelationID': basic_properties.get('correlationId', ''),
        'MessageType': message_id,
        'WhetherRedelivered': message.get('redelivered', False),
        'AppID': basic_properties.get('appId', ''),
        'BodySize': basic_properties.get('bodySize', 0),
        'ClusterId': basic_properties.get('clusterId', ''),
        'ContentEncoding': basic_properties.get('contentEncoding', ''),
        'ContentType': basic_properties.get('contentType', ''),
        'DeliveryMode': basic_properties.get('deliveryMode', 0),
        'Expiration': basic_properties.get('expiration', 0),
        'Priority': basic_properties.get('priority', 0),
        'Timestamp': basic_properties.get('timestamp', ''),
        'Type': basic_properties.get('type', ''),
        'UserId': basic_properties.get('userId', ''),
    }

    reply_to = basic_properties.get('replyTo')
    if reply_to is not None:
        item['ReplyTo'] = reply_to

    headers = basic_properties.get('headers', {})
    for header_name, header_value in headers.items():
        item[header_name] = decode_header_value(header_value)

    table.put_item(Item=item)
    print(f"Now done inserting a row in DynamoDB for messageID = {message_id}")
