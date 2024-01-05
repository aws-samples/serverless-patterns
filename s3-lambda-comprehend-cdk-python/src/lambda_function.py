import boto3
import os
import logging
import http
from datetime import datetime

LOG = logging.getLogger()
LOG.setLevel(logging.INFO)

region_name = os.getenv("region", "us-east-1")
dynamodb_table = os.getenv("dynamodb_table")
dynamodb_obj = boto3.resource("dynamodb").Table(dynamodb_table)
comprehend_obj = boto3.client("comprehend", region_name=region_name)
s3_obj = boto3.client("s3", region_name=region_name)
encoding = "utf-8"


def get_input_from_file(file_details):
    """
    :param file_details: The details of the file that is uploaded to S3
    :return: The list of sentences from the uploaded file.
    """
    try:
        s3_bucket = file_details["bucket"]["name"]
        # LOG.info(f"S3 bucket is {s3_bucket}")

        s3_file = file_details["object"]["key"]
        # LOG.info(f"S3 file is {s3_file}")

        response = s3_obj.get_object(Bucket=s3_bucket, Key=s3_file)
        list_of_sentences = (response["Body"].read()).decode(encoding).split(".")
        input_data = [sentence.strip('"') for sentence in list_of_sentences]
        LOG.info(f"Input data is {input_data}")
        return input_data, s3_file

    except Exception as e:
        LOG.error(f"Exception raised while parsing input data file!!")
        raise e


def lambda_handler(event, context):
    """
    :param event: Input from the user, through S3
    :param context: Any methods and properties that provide information about the invocation, function, and execution environment
    :return: THe response from Comprehend service about the Sentiment of the user input and insert the record into DynamoDB table.
    """
    try:
        LOG.info(f"Event is {event}")

        # Get the user input text
        user_input, s3_file = get_input_from_file(event["Records"][0]["s3"])
        # LOG.info(type(user_input))s

        # Invoke Comprehend Batch Detect Sentiment API
        response = comprehend_obj.batch_detect_sentiment(
            TextList=user_input, LanguageCode="en"
        )
        LOG.info(response["ResultList"])
        # return response["ResultList"]
        LOG.info(type(response["ResultList"]))
        # Insert the Batch Sentiment Analysis results into DynamoDB table
        dynamodb_obj.put_item(Item={"InputFile": s3_file, "SentimentAnalysis": str(response["ResultList"]), "TimeStamp": str(datetime.now())})

        return {"statusCode": http.HTTPStatus.OK}

    except Exception as e:
        LOG.error("Sentiment detection failed!!")
        raise e
