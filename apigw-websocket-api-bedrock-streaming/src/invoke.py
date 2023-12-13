import boto3
import json
import os
import logging
from botocore.exceptions import ClientError
from supported_model_list import MODELS_WITH_STREAMING_SUPPORT

# initialize logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Defaults
DEFAULT_MODEL_ID = os.environ.get("DEFAULT_MODEL_ID","anthropic.claude-instant-v1")
AWS_REGION = os.environ["AWS_REGION"]
TABLE_NAME = os.environ["WEBSOCKETS_DDB_TABLE"]
DEFAULT_MAX_TOKENS = 256
DEFAULT_TEMPERATURE = 0

# global variables - avoid creating a new client for every request
bedrock_client = None
apigw_client = None
table = None


def construct_request_body(modelId, parameters, prompt):
    provider = modelId.split(".")[0]
    request_body = None
    max_tokens = parameters.get('maxTokens', DEFAULT_MAX_TOKENS)
    temperature = parameters.get('temperature', DEFAULT_TEMPERATURE)

    # construct request body depending on model provider
    if provider == "anthropic":
        request_body = {
            "prompt": prompt,
            "max_tokens_to_sample": max_tokens,
            "temperature": temperature
        }
    elif provider == "amazon":
        textGenerationConfig = {
            "maxTokenCount": max_tokens,
            "temperature": temperature
        }
        request_body = {
            "inputText": prompt,
            "textGenerationConfig": textGenerationConfig
        }
    elif provider == "cohere":
        request_body = {
            "prompt": prompt,
            "max_tokens": max_tokens,
            "temperature": temperature
        }
    elif provider == "meta":
        request_body = {
            "prompt": prompt,
            "max_gen_len": max_tokens,
            "temperature": temperature
        }

    return request_body


def get_generated_text(modelId, response):
    provider = modelId.split(".")[0]
    generated_text = None
    if provider == "anthropic":
        generated_text = response.get("completion")
    elif provider == "amazon":
        generated_text = response.get("outputText")
    elif provider == "cohere":
        generated_text = response.get("generations")[0].get("text")
    elif provider == "meta":
        generated_text = response.get("generation")
    
    return generated_text


def post_to_websockets(apig_management_client, connection_id, message, table):
    try:
        apig_management_client.post_to_connection(
            Data=message, ConnectionId=connection_id
        )
    except ClientError:
        logger.exception("Couldn't post to connection %s.", connection_id)
    except apig_management_client.exceptions.GoneException:
        logger.info("Connection %s is gone, removing.", connection_id)
        try:
            table.delete_item(Key={"connection_id": connection_id})
        except ClientError:
            logger.exception("Couldn't remove connection %s.", connection_id)


def call_llm(table, connection_id, apig_management_client, parameters, prompt):
    global bedrock_client

    status_code = 200
    # check if model supports streaming response
    modelId = parameters.pop("modelId", DEFAULT_MODEL_ID)
    if modelId not in MODELS_WITH_STREAMING_SUPPORT:
        error_msg = f"Specified model does not support streaming response: {modelId}. Please try another model."
        post_to_websockets(apig_management_client, connection_id, error_msg, table)
        status_code = 400
        return status_code

    body = construct_request_body(modelId, parameters, prompt)
    if body == None:
        error_msg = "Unsupported provider: " + modelId.split(".")[0]
        post_to_websockets(apig_management_client, connection_id, error_msg, table)
        status_code = 400
        return status_code
    logger.info(f"ModelId {modelId}, Body: {body}")

    if (bedrock_client is None):
        bedrock_client = boto3.client(service_name='bedrock-runtime', region_name=AWS_REGION)

    response = bedrock_client.invoke_model_with_response_stream(
        body=json.dumps(body), 
        modelId=modelId, 
        accept='application/json', 
        contentType='application/json'
    )
    stream = response.get('body')
    
    if stream:
        for event in stream:
            chunk = event.get('chunk')
            if chunk:
                chunk_obj = json.loads(chunk.get('bytes').decode())
                # extract generated text based on model provider
                generated_text = get_generated_text(modelId, chunk_obj)

                if generated_text == None:
                    error_msg = "Unsupported provider: " + modelId.split(".")[0]
                    post_to_websockets(apig_management_client, connection_id, error_msg, table)
                    status_code = 400
                    return status_code

                # send data to WebSockets
                post_to_websockets(apig_management_client, connection_id, generated_text, table)

        # send a message to indicate end of LLM response
        end_msg = "<End of LLM response>"
        post_to_websockets(apig_management_client, connection_id, end_msg, table)
                
    return status_code


def lambda_handler(event, context):
    global apigw_client
    global table

    print("Event: ", json.dumps(event))

    # handle websockets request
    route_key = event.get("requestContext", {}).get("routeKey")
    connection_id = event.get("requestContext", {}).get("connectionId")
    if TABLE_NAME is None or route_key is None or connection_id is None:
        return {"statusCode": 400}
    if table is None:
        table = boto3.resource("dynamodb").Table(TABLE_NAME)
    logger.info("Request: %s, use table %s.", route_key, table.name)

    # set default status code
    response = {"statusCode": 200}

    # extract information from event
    body = json.loads(event.get("body"))
    domain = event.get("requestContext", {}).get("domainName")
    stage = event.get("requestContext", {}).get("stage")
    prompt = body["prompt"]
    parameters = body["parameters"]

    if domain is None or stage is None:
        logger.warning(
            "Couldn't send message. Bad endpoint in request: domain '%s', "
            "stage '%s'",
            domain,
            stage,
        )
        response["statusCode"] = 400
    else:
        if apigw_client is None:
            apigw_client = boto3.client("apigatewaymanagementapi", endpoint_url=f"https://{domain}/{stage}")
        response["statusCode"] = call_llm(table, connection_id, apigw_client, parameters, prompt)

    return response