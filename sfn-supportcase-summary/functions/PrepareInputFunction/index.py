import json
import datetime

#--------------------------------------------------
# function: lambda_handler
#--------------------------------------------------
def lambda_handler(event, context):

    print(json.dumps(event, default=str))

    key_name = event['detail']['object']['key']

    # Get the filename from the path without the extension.
    filename_without_extension = key_name.split('/')[-1].split('.')[0]

    # Get the file extension.
    file_extension = key_name.split('.')[-1]

    # Remove any strings from the name. The transcription job will use the file key
    # name for its output, but it can't contain spaces.
    filename_without_extension = filename_without_extension.replace(' ', '_')

    # Get today's date in YYYY-mm-DD format and add hours and minutes using local time.
    date_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")

    return {
        "SourceBucketName": event['detail']['bucket']['name'],
        "SourceKeyName": key_name,
        "SourceFileName": f'{filename_without_extension}.{file_extension}',
        "SourceFileNameWithDate": f'{filename_without_extension}-{date_time}.{file_extension}'
    }
