import json
import boto3
import logging
from jsonpath_ng.ext import parse


# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize AWS clients
bedrock = boto3.client("bedrock")
bedrock_runtime = boto3.client("bedrock-runtime")

# Mapping of model types to JSONPath expressions for response extraction
MODEL_REPLY_MAPPING = {
    "anthropic": "$.completion",
    "ai21": "$.completions[0].data.text",
    "amazon": "$.results[0].outputText",
    "meta": "$.generation",
}


# Method to generate a standardised API response
def generate_response(status_code, success, message, data=[]):
    return {
        "statusCode": status_code,
        "body": json.dumps(
            {
                "success": success,
                "message": message,
                "data": data,
            }
        ),
    }


# Method to list foundation models
def list_foundation_models():
    foundation_models = bedrock.list_foundation_models()
    return [
        {"modelName": model["modelName"], "modelId": model["modelId"]}
        for model in foundation_models["modelSummaries"]
    ]


# Method to invoke foundation models
def invoke_foundation_model(model_id, inference_parameters):
    # Invoke foundation model
    bedrock_runtime_body = json.dumps(inference_parameters)
    response = bedrock_runtime.invoke_model(body=bedrock_runtime_body, modelId=model_id)
    response_body = json.loads(response["body"].read())
    logger.info("Response: %s", response_body)

    # Get reply from response body from foundation model
    if model_id.startswith(tuple(MODEL_REPLY_MAPPING.keys())):
        json_path = MODEL_REPLY_MAPPING[model_id.split(".")[0]]
        jsonpath_expr = parse(json_path)
        answer = jsonpath_expr.find(response_body)[0].value

    else:
        answer = response_body

    return generate_response(
        200, True, "Successfully retrieved response from foundation model.", answer
    )


def handler(event, context):
    try:
        # Log incoming event
        logger.info("Event: %s", event)

        if event["httpMethod"] == "GET":
            # Handle GET request to retrieve foundation models list
            foundation_models = list_foundation_models()
            logger.info("Foundation Models: %s", foundation_models)
            return generate_response(
                200,
                True,
                "Successfully retrieved foundation models list.",
                foundation_models,
            )

        elif event["httpMethod"] == "POST":
            # Handle POST request to invoke foundation models with inference parameters
            body = json.loads(event["body"])
            model_id = body.get("modelId", None)
            inference_parameters = body.get("inferenceParameters", None)

            if not (model_id and inference_parameters):
                logger.info(
                    "Missing required parameters, model_id: %s, inferenceParameters: %s",
                    model_id,
                    inference_parameters,
                )
                return generate_response(422, False, "Missing required parameters.")

            return invoke_foundation_model(model_id, inference_parameters)

        else:
            # Handle any other request method
            logger.error("Invalid method: %s.", event["httpMethod"])
            return generate_response(400, False, "Invalid method")

    except Exception as err:
        logger.exception("Failed to retrieve response from foundation model.")
        return generate_response(
            err.response["ResponseMetadata"]["HTTPStatusCode"],
            False,
            err.response["Error"]["Message"],
        )
