import boto3
import os
import logging
import http
import json

LOG = logging.getLogger()
LOG.setLevel(logging.INFO)

region_name = os.getenv("region", "us-east-1")
translate_obj = boto3.client("translate", region_name=region_name)
source_lang = os.getenv("src_lang", "auto")
target_lang = os.getenv("target_lang", "fr")


def lambda_handler(event, context):
    """
    :param event: Input from the user, through API Gateway
    :param context: Any methods and properties that provide information about the invocation, function, and execution environment
    :return: THe response from Translate service after the translation of user input.
    """
    try:
        LOG.info(f"Event is {event}")

        # Invoke Translate Text API
        response = translate_obj.translate_text(
            Text=json.loads(event["body"])["input"],
            SourceLanguageCode=source_lang,
            TargetLanguageCode=target_lang,
            Settings={"Formality": "INFORMAL", "Profanity": "MASK"},
        )

        LOG.info(response["TranslatedText"])
        analyzed_response = json.dumps(
            {
                "Translated Text": response["TranslatedText"],
                "statusCode": http.HTTPStatus.OK,
                "Source Text": json.loads(event["body"])["input"],
            }
        )
        return analyzed_response

    except Exception as e:
        LOG.error("Translate action failed!!")
        raise e
