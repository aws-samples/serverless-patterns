from fastapi import FastAPI, Request
import boto3
import json
import os
import logging


app = FastAPI()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# get api gateway client
api_gateway_management_api = boto3.client(
    "apigatewaymanagementapi",
    endpoint_url=os.environ["WEBSOCKET_API_ENDPOINT"],
)


# send message over websocket using connection id
def send_message(connection_id, message):
    logger.info(f"Sending message {message} to {connection_id}")

    api_gateway_management_api.post_to_connection(
        ConnectionId=connection_id, Data=json.dumps(message)
    )


@app.post("/")
async def index(event: Request):
    # add try catch block
    try:
        event_body = await event.json()
        logger.info(f"incoming request json: {event_body}")
        send_message(event_body["connectionId"], event_body["body"])
    except Exception as err:
        logger.error("Error sending message", err)
        return {"error": err}
    return {"message": "ok"}


@app.get("/")
def get_root():
    return {"message": "ok"}
