from __future__ import print_function

import json
import logging as logging
import ssl
import time
from http.client import HTTPSConnection
from os import path
from typing import Union, AnyStr
from urllib.parse import urlsplit, urlunsplit

logger = logging.getLogger(__name__)


def _send_response(response_url: AnyStr, response_body: AnyStr, ssl_verify: Union[bool, AnyStr] = None):
    try:
        json_response_body = json.dumps(response_body)
    except Exception as e:
        msg = "Failed to convert response to json: {}".format(str(e))
        logger.error(msg, exc_info=True)
        response_body = {'Status': 'FAILED', 'Data': {}, 'Reason': msg}
        json_response_body = json.dumps(response_body)
    logger.debug("CFN response URL: {}".format(response_url))
    logger.debug(json_response_body)
    headers = {'content-type': '', 'content-length': str(len(json_response_body))}
    split_url = urlsplit(response_url)
    host = split_url.netloc
    url = urlunsplit(("", "", *split_url[2:]))
    ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    if isinstance(ssl_verify, str):
        if path.exists(ssl_verify):
            ctx.load_verify_locations(cafile=ssl_verify)
        else:
            logger.warning("Cert path {0} does not exist!.  Falling back to using system cafile.".format(ssl_verify))
    if ssl_verify is False:
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
    # If ssl_verify is True or None dont modify the context in any way.
    while True:
        try:
            connection = HTTPSConnection(host, context=ctx)
            connection.request(method="PUT", url=url, body=json_response_body, headers=headers)
            response = connection.getresponse()
            logger.info("CloudFormation returned status code: {}".format(response.reason))
            break
        except Exception as e:
            logger.error("Unexpected failure sending response to CloudFormation {}".format(e), exc_info=True)
            time.sleep(5)
