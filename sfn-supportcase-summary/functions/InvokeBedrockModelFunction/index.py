import json
import boto3
import os

# Get the service clients.
bedrock_client = boto3.client('bedrock-runtime')
s3_client = boto3.client('s3')

# Use the provided instructions to provide the summary. Use a default if no intructions are provided.
SUMMARY_INSTRUCTIONS = os.getenv('SUMMARY_INSTRUCTIONS', 'Your task is list Key Stakeholders and highlight Key Discussion Points and list Decisions and outline Action Items and provide meeting notes and create a concise summary.')

# Use the provided model ID to invoke the model.
BEDROCK_MODEL_ID = os.getenv('BEDROCK_MODEL_ID')

#--------------------------------------------------
# function: lambda_handler
#--------------------------------------------------
def lambda_handler(event, context):

    print(json.dumps(event))

    result = {"status": "FAILED"}

    transcript_uri =  event['TranscriptionJob']['TranscriptionJob']['Transcript']['TranscriptFileUri']

    # Get transcription URI from the event; it will look something like this:
    # https://s3.[REGION].amazonaws.com/[BUCKET NAME]/transcriptions/bf90bf05-5300-415f-9dc2-a89d2f03a59f.json

    # ...so get the bucket name and filename based on that format.
    bucket_name = transcript_uri.split('/')[3]
    file_name = transcript_uri.split('/')[-2] + '/' + transcript_uri.split('/')[-1]

    try:
        # Download the file from S3.
        file_object = s3_client.get_object(Bucket=bucket_name, Key=file_name)
        data = json.loads(file_object['Body'].read())

        # Get the transcript.
        transcript = json.dumps(data['results']['transcripts'][0]['transcript'])

        # Create the payload to provide to the Anthropic model.
        messages = [{ "role":"user", "content":[{"type":"text","text": SUMMARY_INSTRUCTIONS + " " + transcript}]}]

        body=json.dumps(
            {
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": 4096,
                "messages": messages,
                "temperature": 0,
                "top_p": 1.
            }
        )

        print(f'Invoking model: {BEDROCK_MODEL_ID}')

        response = bedrock_client.invoke_model(body=body, modelId=BEDROCK_MODEL_ID)

        print(f'response: {response}')

        # Save the response value.
        assistant_response = json.loads(response.get('body').read())
        print(f'assistant_response: {assistant_response}')

        summary_file_name =  f"transcriptions/{event['Source']['Payload']['SourceFileName']}-summary.txt"
        print(f'summary_file_name: {summary_file_name}')

        # Save the response value in S3.
        s3_client.put_object(
            Bucket=bucket_name,
            Key=summary_file_name,
            Body=assistant_response['content'][0]['text'],
            ContentType='text/plain'
            )

        result = {
            "bucket_name": bucket_name,
            "summary_key_name": summary_file_name,
            "status": "SUCCEEDED"
        }

    except Exception as e:
        result['Error'] = str(e)

    print(f'result: {result}')

    return result
