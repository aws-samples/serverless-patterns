#Write an S3 Object Lambda function to read a pdf file using and use amazon textract for extract the key value pair
import boto3
import json
import urllib3


def handler(event, context):

    #Get Operation Context from event
    print(event)
    operation_context = event["getObjectContext"]

    # Retrieve the Operation Context and the outputRoute, outputToken, and inputS3Url
    output_route = operation_context["outputRoute"]
    output_token = operation_context["outputToken"]
    s3_url = operation_context["inputS3Url"]
    print(output_route)
    http = urllib3.PoolManager()
    response = http.request('GET', s3_url)

    # Get object from response
    original_object = response.data
    #Create a textract client
    textract = boto3.client('textract')
    # Convert the PDF to JSON using Amazon Textract
    textract_response = textract.detect_document_text(Document={'Bytes': original_object})
    print(textract_response)
    # Convert the JSON to a string
    textract_string = json.dumps(textract_response)
    print(textract_string)
    # Write the string to S3
    s3 = boto3.client('s3')
    s3.write_get_object_response(
        Body=textract_string,
        RequestRoute=output_route,
        RequestToken=output_token)

    return {
        'statusCode': 200,
        'body': textract_response
    }