import logging
import traceback
import json
import sys
import boto3
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

#Instruments X-Ray tracing for boto3/aws downstream service calls
patch_all()



def lambda_handler(event, context):

    try:
        logger.debug(f'## EVENT\r' + json.dumps(event))

        #Place the code being debugged/implemented below

        return {'statusCode': 200, 'body': 'Hello World!'}

    except Exception as exp:
        exception_type, exception_value, exception_traceback = sys.exc_info()
        
        traceback_string = traceback.format_exception(exception_type, exception_value, exception_traceback)

        err_msg = json.dumps({"errorType": exception_type.__name__,"errorMessage": str(exception_value),"stackTrace": traceback_string})
        
        logger.error(err_msg)

        raise