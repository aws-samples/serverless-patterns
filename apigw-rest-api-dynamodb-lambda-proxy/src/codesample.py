import json
import boto3

dynamodb = boto3.resource("dynamodb")

table = dynamodb.Table("my-table")


def lambda_handler(event, context):
    # TODO implement
    print("event ", json.dumps(event))

    method = event["httpMethod"]
    para = event["pathParameters"]

    if method == "DELETE":
        return handle_delete(para)
    elif method == "POST":
        return handle_post(para, event["body"])
    elif method == "GET":
        return handle_get(para)
    else:
        return "Invalid method", 405


def handle_delete(para):
    table.delete_item(Key={"ID": para["ID"]})
    return {"statusCode": 200, "body": "Item deleted"}


def handle_post(para, body):
    body = json.loads(body)
    # print('here', body['Name'], body['Description'])
    table.update_item(
        Key={"ID": para["ID"]},
        UpdateExpression="SET ProductName = :n, Description = :p",
        ExpressionAttributeValues={
            ":n": body["ProductName"],
            ":p": body["Description"],
        },
    )
    return {"statusCode": 200, "body": "Item updated"}


def handle_get(para):
    response = table.get_item(Key={"ID": para["ID"]})
    return {"statusCode": 200, "body": json.dumps(response)}
