import json
import boto3

# Get the service clients.
s3_client = boto3.client('s3')

#--------------------------------------------------
# function: lambda_handler
#--------------------------------------------------
def lambda_handler(event, context):

  result = { "status": "FAILED" }
  lines = []
  line = ''
  speaker = 'spk_1'
  most_recent_speaker = 'spk_1'

  transcript_uri =  event['TranscriptionJob']['TranscriptionJob']['Transcript']['TranscriptFileUri']

  # Get transcription URI from the event
  # The transcript URI will look something like this:
  # https://s3.[REGION].amazonaws.com/[BUCKET NAME]/transcriptions/bf90bf05-5300-415f-9dc2-a89d2f03a59f.json

  # ...so get the bucket name and filename based on that format.
  bucket_name = transcript_uri.split('/')[3]
  file_name = transcript_uri.split('/')[-2] + '/' + transcript_uri.split('/')[-1]

  try:
    # Download the file from S3.
    file_object = s3_client.get_object(Bucket=bucket_name, Key=file_name)
    data = json.loads(file_object['Body'].read())

    try:
      speaker_labels = data['results']['speaker_labels']
    except KeyError:
      # Speaker labels are off in processing; shouldn't happen given TranscribeJob setting above but catch in case.
      return

    # Loop through the speakers and add them to the transcription.
    items = data['results']['items']
    for item in items:

      if item.get('start_time'):  # This is a spoken item
        speaker = item['speaker_label']

        if speaker == most_recent_speaker:
          # Append the content to line and repeat
          line+=f" {item['alternatives'][0]['content']}"

        else:
          # New speaker
          lines.append(f'{line}\n\n')
          most_recent_speaker = speaker
          line=f" {item['start_time']} {speaker} {item['alternatives'][0]['content']}"

      elif item['type'] == 'punctuation':
        line+=item['alternatives'][0]['content']

    lines.append(line)

    speaker_formatted_content = ''
    for line in lines:
      speaker_formatted_content+=line

    speaker_transcription_file_name =  f"transcriptions/{event['Source']['Payload']['SourceFileName']}-speaker-transcription.txt"

    # Save the response value in S3.
    s3_client.put_object(
        Bucket=bucket_name,
        Key=speaker_transcription_file_name,
        Body=speaker_formatted_content,
        ContentType='text/plain'
        )

    result = {
      f"bucket_name": "{bucket_name}",
      f"speaker_transcription_key_name": "{speaker_transcription_file_name}"
    }

  except Exception as e:
    result['Error'] = str(e)

  return result
