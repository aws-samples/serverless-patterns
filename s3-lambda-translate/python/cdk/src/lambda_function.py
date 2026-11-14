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
s3 = boto3.client('s3')
s3_res = boto3.resource("s3")
dest_bucket = os.getenv("destination_bucket")
status = "Translation failed, please check logs!!"


def lambda_handler(event, context):
    """
    :param event: Input from the user, through a S3 bucket upload event
    :param context: Any methods and properties that provide information about the invocation, function, and execution environment
    :return: The response from Translate service after the translation of input document.
    """
    try:
        LOG.info(f"Event is {event}")

        s3_bucket = event["Records"][0]["s3"]["bucket"]["name"]
        # LOG.info(f"S3 bucket is {s3_bucket}")

        s3_file = event["Records"][0]["s3"]["object"]["key"]
        # LOG.info(f"S3 file is {s3_file}")

        obj = s3.get_object(Bucket=s3_bucket, Key=s3_file)
        data = obj['Body'].read()
        # LOG.info(f"Data collected is {data}")

        result = translate_obj.translate_document(
            Document={
                "Content": data,
                "ContentType": "text/html"
            },
            SourceLanguageCode=source_lang,
            TargetLanguageCode=target_lang
        )
        LOG.info(result)

        if "TranslatedDocument" in result:
            fileName = s3_file.split("/")[-1]
            tmpfile = f"{target_lang}-{fileName}"
            os.chdir('/tmp')
            with open(tmpfile, 'wb') as f:
                f.write((result["TranslatedDocument"]["Content"]))

            lambda_path = "/tmp/" + tmpfile
            s3_res.meta.client.upload_file(lambda_path, dest_bucket, tmpfile)
            status = f"Success, the translated document is uploaded in the bucket {dest_bucket}"

        LOG.info(status)
        return status

    except Exception as e:
        LOG.error("Translate action failed!!")
        raise e
