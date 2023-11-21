# Copyright 2023, Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Amazon Software License (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#  http://aws.amazon.com/asl/
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

"""
For processing data sent to Firehose by Cloudwatch Logs subscription filters.

Cloudwatch Logs sends to Firehose records that look like this where type is DATA_MESSAGE:

{
  "messageType": "DATA_MESSAGE",
  "owner": "123456789012",
  "logGroup": "log_group_name",
  "logStream": "log_stream_name",
  "subscriptionFilters": [
    "subscription_filter_name"
  ],
  "logEvents": [
    {
      "id": "01234567890123456789012345678901234567890123456789012345",
      "timestamp": 1510109208016,
      "message": "log message 1"
    },
    {
      "id": "01234567890123456789012345678901234567890123456789012345",
      "timestamp": 1510109208017,
      "message": "log message 2"
    }
    ...
  ]
}

The "message" value is compressed with GZIP and base64 encoded.

The code below will:

1) Iterate through all all records sent by CloudWatch and process the DATA_MESSAGE type.
2) Decode & Unzip the message payload
3) Look for JSON payloads and load objects if found. 
4) Package each log event message as a separate record, adding metadata and converting timestamp to utc date/time value
5) combine all log event records into JSON array 
6) Build KDF JSON response object with log events base64 encoded (NOTE: code will not GZIP output)

The output to S3 file will:

1) Be formatted as a JSON file that constitutes a JSON array with each log entry as a separate JSON object
2) Each log entry will include metadata that can be omitted by OSI 

Example output file:
[
    {
        "cloudwatch": {
            "logGroup": "/aws/lambda/my-lambda-function",
            "logStream": "2023/09/14/[$LATEST]9ae39e4917c04e7486a6cb81f892f33b",
            "owner": "12334567890"
        },
        "id": "37793152654191904442680491486618333209652445892414210048",
        "message": "[INFO] 2023-09-14T15:06:10.876Z 39b7ff85-5079-42bd-ae5e-39d102773384 example application message",
        "timestamp": "2023-09-14T14:59:36.842000Z"
    },...
]


Note: modify transformLogEvent() to change this output format to your desired output.

"""
import boto3
import base64
import json
import gzip
from datetime import datetime
import time
import uuid
import os
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)
_LIST_KEY_NAME_ = "multivalue"
_logGroup = ""
_logStream = ""
_owner = ""
_cloudwatch_metadata = {}


def has_key(thedict, keyvalue):
    if thedict.get(keyvalue) == None:
      return False
    else:
      return True


def transformLogEvent(log_event):
    """Transform each log event.

    The default implementation below just extracts the message and appends a newline to it.

    Args:
    log_event (dict): The original log event. Structure is {"id": str, "timestamp": long, "message": str}

    Returns:
    str: The transformed log event.
    """
    processed_log_event = {
        "message": "",
        "timestamp": "",
        "id": ""
    }
            
    # reformat timestamp
    epoch_time_datetime = datetime.fromtimestamp(log_event['timestamp']/1000).isoformat()+'Z'
    
    logger.info("[KDFXFORM] processing record: "+str(log_event))
    
    try:
        
        # try to parse message for json 
        json_message = json.loads(log_event["message"])
        logger.info("[KDFXFORM] JSON Object Found! Using JSON object as log event. message set to JSON string value.")
        
        # if no exception thrown, message is json.  use dict object a log event message.
        # if object is an array then it must be enclosed in a JSON dict object
        if isinstance(json_message, list):
            logger.info("[KDFXFORM] JSON object type is <list>.  Assigning to global key name <{}>".format(_LIST_KEY_NAME_))
            processed_log_event[_LIST_KEY_NAME_] = json_message.copy()
        else:
            logger.info("[KDFXFORM] JSON object type is {}. Using json object direct copy".format(str(type(json_message))))
            processed_log_event = json_message.copy()

        processed_log_event['json_object'] = str(type(json_message))
        processed_log_event['message'] = log_event["message"]
        processed_log_event['timestamp'] = epoch_time_datetime
        processed_log_event['id'] = log_event['id']   # uncomment if you want to keep the original id

       
        
    except:
        if type(log_event) is dict: 

            if has_key(log_event,"message"): 
                processed_log_event['message'] = log_event["message"]
            else:
                logger.error("[KDFXFORM] \"message\" key not found in log event!  setting to null.")
                processed_log_event['message'] = ""
                

            processed_log_event['timestamp'] = epoch_time_datetime
            
            if has_key(log_event,"id"): 
                processed_log_event['id'] = log_event["id"]   # uncomment if you want to keep the original id
            else:
                logger.error("[KDFXFORM] \"id\" key not found in log event!  setting to null.")
                processed_log_event['id'] = ""               
        else:
            # json parsing failure means message is string.  use original string as log event message.
            logger.error("[KDFXFORM] log event is not a dict! Skipped Processing.")
            processed_log_event = log_event
    
    
    return processed_log_event





def processRecords(records):
    """Process the records.
    
    This function processes the records and returns the processed records.
    
    Args:
        records (list): The list of records to process.
    
    Returns:
        list: A list of processed records.
    
    """

    processedRecords=[]
    result = []
    
    for record in records:
        # Kinesis data streams are base64 encoded so decode here
        payload = loadJsonGzipBase64(record['data'])

        # set cloudwatch met values
        try:
            _logGroup = payload['logGroup']
            _logStream = payload['logStream']
            _owner = payload['owner']
            _cloudwatch_metadata = {
                "logGroup": _logGroup,
                "logStream": _logStream,
                "owner": _owner
            }
            
            logger.info("[KDFXFORM] processing next record with cloudwatch metadata:" + str(_cloudwatch_metadata))

            
        except Exception as ex:
            # log error message
            logger.error("[KDFXFORM] ERROR trying to access logevent metadata values: "+str(ex))
            
        # process the record

        if(payload['messageType'] == 'DATA_MESSAGE'):

            for log_event in payload['logEvents']:
                # append to list of processed records
                xform_event = transformLogEvent(log_event)
                
                xform_event["cloudwatch"] = {
                    "logGroup": _logGroup,
                    "logStream": _logStream,
                    "owner": _owner
                }
    
                # log transformed event 
                logger.info("[KDFXFORM] transformed event: "+str(xform_event))
                
                result.append(xform_event)
        

    if(len(result)>0):
            b64result = base64.b64encode(json.dumps(result).encode("utf-8"))
            processedRecords.append(
                    {
                        'recordId': record['recordId'],
                        'result': 'Ok',
                        'data': b64result
                    }
            )
                
    else:
            processedRecords.append(
                    {
                        'recordId': record['recordId'],
                        'result': 'Dropped',
                        'data': record['data']
                    }
            )


    # return list of processed records
    return processedRecords



def loadJsonGzipBase64(base64Data):
    return json.loads(gzip.decompress(base64.b64decode(base64Data)))



def lambda_handler(event, context):
    

    """
    This function receives the event from Kinesis Firehose and processes the records.
    """
    # process the records
    records = processRecords(event['records'])
    # print the records
    x = { "records": records }
    logger.info("FINAL VALUE: "+str(x))

    # return the processed records
    return {'records': records}
