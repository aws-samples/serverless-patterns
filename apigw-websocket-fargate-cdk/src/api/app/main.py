from fastapi import FastAPI, Request
import boto3
import json
import os

app = FastAPI()


# get api gateway client
api_gateway_management_api = boto3.client(
    "apigatewaymanagementapi",
    endpoint_url=os.environ["WEBSOCKET_API_ENDPOINT"],
)


# send message over websocket using connection id
def send_message(connection_id, message):
    print(f"Sending message {message} to {connection_id}")

    api_gateway_management_api.post_to_connection(
        ConnectionId=connection_id, Data=json.dumps(message)
    )


@app.post("/")
async def index(event: Request):
    event_body = await event.json()
    print(f"incoming request: {event_body}")
    send_message(event_body["connectionId"], event_body["body"])
    return {"message": "ok"}


@app.get("/")
def get_root():
    return {"message": "ok"}
