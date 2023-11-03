import json
import boto3

# Create a client for Amazon Comprehend
comprehend = boto3.client("comprehend")


def lambda_handler(event, context):
    # Extract the request body from the event object
    body = json.loads(event["body"])

    # Extract the input string from the request body
    input_string = body["input"]

    # Call the Comprehend DetectSentiment API
    prediction = comprehend.detect_sentiment(Text=input_string, LanguageCode="en")

    # Extract the sentiment from the response
    sentiment = prediction["Sentiment"]

    # Extract the confidence level from the response
    confidence_scores = prediction["SentimentScore"]

    # Return the results to Amazon API Gateway
    return {
        "statusCode": 200,
        "body": json.dumps(
            {"sentiment": sentiment, "confidence_scores": confidence_scores}
        ),
    }
