import boto3
import sys
import logging
import os
import subprocess
import json
import datetime
import csv
from json import JSONDecodeError

client = boto3.client('s3')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
lambda_tmp_dir = '/tmp'
s3_csv_dir = os.environ['S3_BUCKET_NAME']
output_file_list = []

def lambda_handler(event, context):
    for r in event['Records']:
        s3 = r['s3']
        bucket = s3['bucket']['name']
        key = s3['object']['key']
        if '.csv' in key:
            logger.debug("found .csv in key {0}".format(key))
            key = key.replace('csv', 'json')
        source = download_json(bucket, key)
        print(source)
        output_file_list = convert_json_2_csv(source)
        for output in output_file_list:
            upload_csv(output, bucket)
            print(output)
    logger.info("{0} records processed.".format(len(event['Records'])))
    return True

def download_json(bucket, key):
    local_source_json = lambda_tmp_dir + "/" + key
    directory = os.path.dirname(local_source_json)
    if not os.path.exists(directory):
        os.makedirs(directory)
    client.download_file(bucket, key, local_source_json)
    return local_source_json

def upload_csv(local_csv_file, bucket):
    basename = os.path.basename(local_csv_file)
    full_key = "{0}/{1}".format(s3_csv_dir, basename)
    logger.debug('uploading to S3 bucket: {}, key: {}'.format(bucket, full_key))
    client.upload_file(local_csv_file, bucket, full_key)
    
def convert_json_2_csv(source):
    decoder = json.JSONDecoder()
    with open(source, 'r') as content_file:
        content = content_file.read()
        content_length = len(content)
        decode_index = 0
        obj_count = 0
        component_list_set=set()
        while decode_index < content_length:
            try:
                objs, decode_index = decoder.raw_decode(content, decode_index)
                component_list_set.add(objs['Component'])
            except JSONDecodeError as e:
                print("JSONDecodeError:", e)
                decode_index += 1
        decode_index=0
        frequency = 1
        tm = datetime.datetime.now()
        tm = tm - datetime.timedelta(
            minutes=frequency *2,
            seconds=tm.second,
            microseconds=tm.microsecond
        )
        tm = tm + datetime.timedelta(minutes=+frequency)
        current_timestamp = (tm).strftime(format='%Y%m%d%H%M%S')
        output_file=[]
        for component_list in component_list_set:
            print(component_list)
        
            with open(f'{lambda_tmp_dir}/{component_list}_{current_timestamp}.csv','w') as f:
                while decode_index < content_length:
                    try:
                        objs, decode_index = decoder.raw_decode(content, decode_index)
                        if objs['Component'] == component_list:
                            if obj_count == 0:
                                w = csv.writer(f)
                                del objs['Component']
                                w.writerow(objs.keys())
                                w.writerow(objs.values())
                                obj_count += 1
                            else:
                                w = csv.writer(f)
                                del objs['Component']
                                w.writerow(objs.values())
                                obj_count += 1
                    except JSONDecodeError as e:
                        print("JSONDecodeError:", e)
                        decode_index += 1
                obj_count=0
                decode_index=0
                output_file.append(f.name)
        
    return output_file
