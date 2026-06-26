import base64
import json
import os
import time
import boto3

dynamodb = boto3.resource("dynamodb")
table_name = os.environ.get("DYNAMO_DB_TABLE", "ACTIVEMQ_LAMBDA_DYNAMO_TABLE")
table = dynamodb.Table(table_name)


def lambda_handler(event, context):
    print("Begin Event *************")
    print(json.dumps(event))
    print("End Event ***************")

    for msg in event.get("messages", []):
        try:
            current_time = int(time.time() * 1000)
            print("Begin Message *************")
            print(json.dumps(msg))
            print("End Message ***************")

            print("Begin Message Body *************")
            base64_data = msg.get("data", "")
            decoded_data = base64.b64decode(base64_data).decode("utf-8") if base64_data else ""
            print(decoded_data)
            print("End Message Body ***************")

            print(f"EventSource = {event.get('eventSource')}")
            print(f"EventSourceARN = {event.get('eventSourceArn')}")
            print(f"CorrelationID = {msg.get('correlationID')}")
            print(f"MessageID = {msg.get('messageID')}")
            print(f"MessageType = {msg.get('messageType')}")
            print(f"ReplyTo = {msg.get('replyTo')}")
            print(f"Type = {msg.get('type')}")
            print(f"BrokerInTime = {msg.get('brokerInTime')}")
            print(f"BrokerOutTime = {msg.get('brokerOutTime')}")
            print(f"DeliveryMode = {msg.get('deliveryMode')}")
            print(f"Expiration = {msg.get('expiration')}")
            print(f"Priority = {msg.get('priority')}")
            print(f"TimeStamp = {msg.get('timestamp')}")
            print(f"Queue = {msg.get('destination', {}).get('physicalName')}")
            print(f"WhetherRedelivered = {msg.get('redelivered')}")

            person = json.loads(decoded_data)
            print(f"This person = {json.dumps(person)}")

            aws_sam_local = os.environ.get("AWS_SAM_LOCAL")
            if aws_sam_local is None:
                insert_into_dynamodb(event, msg, person, current_time)

        except Exception as e:
            print(f"An exception happened - {str(e)}")
            return "500"

    return "200"


def insert_into_dynamodb(event, msg, person, receive_time):
    print(f"Now inserting a row in DynamoDB for messageID = {msg.get('messageID')}")
    item = {
        "MessageID": msg.get("messageID"),
        "EventSource": event.get("eventSource"),
        "EventSourceARN": event.get("eventSourceArn"),
        "Firstname": person.get("firstname", ""),
        "Lastname": person.get("lastname", ""),
        "Company": person.get("company", ""),
        "Street": person.get("street", ""),
        "City": person.get("city", ""),
        "County": person.get("county", ""),
        "State": person.get("state", ""),
        "Zip": person.get("zip", ""),
        "Cellphone": person.get("cellPhone", ""),
        "Homephone": person.get("homePhone", ""),
        "Email": person.get("email", ""),
        "Website": person.get("website", ""),
        "CorrelationID": msg.get("correlationID", ""),
        "MessageType": msg.get("messageType", ""),
        "ReplyTo": msg.get("replyTo"),
        "Type": msg.get("type"),
        "BrokerInTime": msg.get("brokerInTime", 0),
        "BrokerOutTime": msg.get("brokerOutTime", 0),
        "DeliveryMode": msg.get("deliveryMode", 0),
        "Expiration": msg.get("expiration", 0),
        "Priority": msg.get("priority", 0),
        "TimeStamp": msg.get("timestamp", 0),
        "Queue": msg.get("destination", {}).get("physicalName", ""),
        "WhetherRedelivered": msg.get("redelivered", False),
        "ReceiveTime": receive_time,
    }
    table.put_item(Item=item)
    print(f"Now done inserting a row in DynamoDB for messageID = {msg.get('messageID')}")
