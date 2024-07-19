import json
import boto3
import os

# Get the service clients.
s3_client = boto3.client('s3')
sns_client = boto3.client('sns')

# Get the SNS topic ARN from the environment variable.
SNS_TOPIC_ARN = os.environ['SNS_TOPIC_ARN']

#--------------------------------------------------
# function: lambda_handler
#--------------------------------------------------
def lambda_handler(event, context):

    print(json.dumps(event))

    bucket_name = event['RecordingSummary']['Payload']['bucket_name']
    summary_key_name = event['RecordingSummary']['Payload']['summary_key_name']

    # Get the name of the original file.
    source_file_name = event['Source']['Payload']['SourceFileName']

    # Get the object contents.
    obj = s3_client.get_object(Bucket=bucket_name, Key=summary_key_name)

    # Get the size of the contents. If it's greater than 256 KB, then use the
    # Extended Client Library for Python:
    # https://docs.aws.amazon.com/sns/latest/dg/large-message-payloads.html
    summary_contents = f"{source_file_name}\n\n{obj['Body'].read().decode('utf-8')}"

    if len(summary_contents) <= 256 * 1024:
        # Post the summary to the SNS topic.
        response = sns_client.publish(TopicArn=SNS_TOPIC_ARN, Message=summary_contents)
    else:
        summary_contents = f"{source_file_name}\n\nThe message exceeds the 256KB message limit."

        response = sns_client.publish(TopicArn=SNS_TOPIC_ARN, Message=summary_contents)
        raise

    return response
