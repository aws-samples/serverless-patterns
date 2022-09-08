import json
import boto3
import os
import uuid

region = os.environ['AWS_DEFAULT_REGION']
output_bucket = 's3://' + os.environ['DestinationBucket']
convert_role = os.environ['MediaConvertRole']

# get the account-specific mediaconvert endpoint for this region
mc_client = boto3.client('mediaconvert', region_name=region)
endpoints = mc_client.describe_endpoints()

# add the account-specific endpoint to the client session
client = boto3.client('mediaconvert', region_name=region, endpoint_url=endpoints['Endpoints'][0]['Url'])


def handler(event, context):

    asset_id = str(uuid.uuid4())
    input_bucket = event['Records'][0]['s3']['bucket']['name']
    video_filename = event['Records'][0]['s3']['object']['key']
    full_video_path = 's3://' + input_bucket + '/' + video_filename
    b_name = os.path.splitext(os.path.basename(full_video_path))[0]

    job_metadata = {'assetID': asset_id}

    try:
        # Job settings are current working directory
        with open('job.json') as json_data:
            job_settings = json.load(json_data)

        # Update the job settings with the source video from the S3 event and destination
        # paths for converted videos
        job_settings['Inputs'][0]['FileInput'] = full_video_path

        for output_group in job_settings['OutputGroups']:
            if output_group['OutputGroupSettings']['Type'] == 'HLS_GROUP_SETTINGS':
                s3_key_hls = 'assets/' + asset_id + '/HLS/' + b_name
                job_settings['OutputGroups'][0]['OutputGroupSettings']['HlsGroupSettings']['Destination'] \
                    = output_bucket + '/' + s3_key_hls
            elif output_group['OutputGroupSettings']['Type'] == 'FILE_GROUP_SETTINGS':
                # Handle the output path
                pass
            elif output_group['OutputGroupSettings']['Type'] == 'DASH_ISO_GROUP_SETTINGS':
                # Handle the output path
                pass
            elif output_group['OutputGroupSettings']['Type'] == 'MS_SMOOTH_GROUP_SETTINGS':
                # Handle the output path
                pass
            elif output_group['OutputGroupSettings']['Type'] == 'CMAF_GROUP_SETTINGS':
                # Handle the output path
                pass
            else:
                # Unknown Output Group. Handle the error
                pass

        print('Job Settings:')
        print(json.dumps(job_settings))

        # Convert the video using AWS Elemental MediaConvert
        job = client.create_job(Role=convert_role, UserMetadata=job_metadata, Settings=job_settings)
        print(json.dumps(job, default=str))

    except Exception as e:
        print('Exception: %s' % e)
        raise
