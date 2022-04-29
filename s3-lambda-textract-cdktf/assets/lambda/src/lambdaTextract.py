"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""

from aws_lambda_powertools import Logger
import json
import os
import boto3

import io
from PIL import Image, ImageDraw
from datetime import datetime

logger = Logger()


def draw_bounding_box(key, val, width, height, draw):
    # If a key is Geometry, draw the bounding box info in it
    if "Geometry" in key:
        box = val["BoundingBox"]
        left = width * box['Left']
        top = height * box['Top']
        draw.rectangle([left, top, left + (width * box['Width']),
                        top + (height * box['Height'])], outline='black')


def lambdaTextract(event, context):
    logger.info(f"{json.dumps(event)}")

    try:
        targetBucket = os.getenv('OUTPUT_BUCKET_NAME')
    except KeyError:
        logger.error('Cannot load <OUTPUT_BUCKET_NAME> environment variable')
        return

    try:
        saveOutputImage = os.getenv('SAVE_OUTPUT_IMAGE')
    except KeyError:
        saveOutputImage = False

    record = event['Records'][0]

    # Login to textract service using temporary
    # credentials and assuming the role
    textract = boto3.client('textract')

    # process using S3 object
    textractResponse = textract.analyze_expense(
        Document={"S3Object": {'Bucket': record['s3']['bucket']['name'],
                               "Name": record['s3']['object']['key']}})

    logger.info(textractResponse)
    result = []
    for expense_doc in textractResponse["ExpenseDocuments"]:
        summary = []
        for summary_field in expense_doc["SummaryFields"]:
            label = ""
            value = ""
            if "LabelDetection" in summary_field:
                label = str(summary_field.get("LabelDetection")["Text"])
            else:
                if "Type" in summary_field:
                    if str(summary_field.get("Type")["Text"]).upper() == "VENDOR_NAME":  # noqa: E501
                        label = summary_field.get("Type")["Text"]
            if "ValueDetection" in summary_field:
                value = str(summary_field.get("ValueDetection")["Text"])
            summary.append({"label": label, "value": value})

        result.append(summary)

    logger.info(result)

    s3Client = boto3.client('s3')
    directory = (datetime.now()).strftime("%Y-%m-%d-%H-%M-%S")

    logger.info(
        f"Saving json file to {targetBucket}/{directory}/"
        f"{os.path.splitext(record['s3']['object']['key'])[0]}.json")

    s3Client.put_object(
        Body=json.dumps(result),
        Bucket=f"{targetBucket}",
        Key=f"{directory}/{os.path.splitext(record['s3']['object']['key'])[0]}.json"   # noqa: E501
    )

    if saveOutputImage:
        logger.info("Drawing bounding boxes")
        # Get the document from S3
        s3Resource = boto3.resource('s3')
        s3SourceImage = s3Resource.Object(record['s3']['bucket']['name'],
                                          record['s3']['object']['key'])
        s3Image = s3SourceImage.get()

        # opening binary stream using an in-memory bytes buffer
        imageStream = io.BytesIO(s3Image['Body'].read())

        # loading stream into image
        image = Image.open(imageStream)

        # Create drawing object
        width, height = image.size
        draw = ImageDraw.Draw(image)

        # For draw bounding boxes
        for expense_doc in textractResponse["ExpenseDocuments"]:
            for summary_field in expense_doc["SummaryFields"]:
                if "LabelDetection" in summary_field:
                    for key, val in summary_field["LabelDetection"].items():
                        draw_bounding_box(key, val, width, height, draw)
                else:
                    if "Type" in summary_field:
                        if str(summary_field.get("Type")["Text"]).upper() == "VENDOR_NAME":  # noqa: E501
                            for key, val in summary_field["Type"].items():
                                draw_bounding_box(key, val, width, height, draw)   # noqa: E501
                if "ValueDetection" in summary_field:
                    for key, val in summary_field["ValueDetection"].items():
                        draw_bounding_box(key, val, width, height, draw)

        in_mem_file = io.BytesIO()

        image.save(in_mem_file, format="PNG")

        logger.info(
            f"Saving png file with bounding boxes to "
            f"{targetBucket}/{directory}/"
            f"{os.path.splitext(record['s3']['object']['key'])[0]}.png")

        s3Client.put_object(
            Body=in_mem_file.getvalue(),
            Bucket=f"{targetBucket}",
            Key=f"{directory}/{os.path.splitext(record['s3']['object']['key'])[0]}.png"  # noqa: E501
        )

    logger.info("Operation completed successfully")
