import json
import os
import boto3


def publishMessage(iotapiendpoint, message):
    iotdata = boto3.client("iot-data", endpoint_url=iotapiendpoint)
    response = iotdata.publish(
        topic=message["topic"], payload=message["payload"], qos=0
    )
    return response


def lambda_handler(event, context):
    iotapiendpoint = os.environ["IOT_DATA_ENDPOINT"]

    try:
        content = event["Records"][0]["body"]
        json_object = json.loads(content)
        iottopic = json_object["topic"]
        msg = json_object["message"]
    except:
        print("exception")
        iottopic = os.environ["IOT_TOPIC"]
        msg = event["Records"][0]["body"]
        pass

    print(msg)
    print(iottopic)

    message = {"topic": iottopic, "payload": json.dumps(msg), "qos": 0}
    response = publishMessage(iotapiendpoint, message)
    print(response)

    return {"statusCode": 200, "body": json.dumps(response)}
