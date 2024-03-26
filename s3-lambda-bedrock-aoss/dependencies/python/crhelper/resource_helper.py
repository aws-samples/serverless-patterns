# -*- coding: utf-8 -*-
"""
TODO:
* Async mode – take a wait condition handle as an input, increases max timeout to 12 hours
* Idempotency – If a duplicate request comes in (say there was a network error in signaling back to cfn) the subsequent
  request should return the already created response, will need a persistent store of some kind...
* Functional tests
"""

from __future__ import print_function
import threading
from crhelper.utils import _send_response
from crhelper import log_helper
import logging
import random
import boto3
import string
import json
import os
from time import sleep

logger = logging.getLogger(__name__)

SUCCESS = 'SUCCESS'
FAILED = 'FAILED'


class CfnResource(object):

    def __init__(self, json_logging=False, log_level='DEBUG', boto_level='ERROR', polling_interval=2, sleep_on_delete=120, ssl_verify=None):
        self._sleep_on_delete = sleep_on_delete
        self._create_func = None
        self._update_func = None
        self._delete_func = None
        self._poll_create_func = None
        self._poll_update_func = None
        self._poll_delete_func = None
        self._timer = None
        self._init_failed = None
        self._json_logging = json_logging
        self._log_level = log_level
        self._boto_level = boto_level
        self._send_response = False
        self._polling_interval = polling_interval
        self.Status = ""
        self.Reason = ""
        self.PhysicalResourceId = ""
        self.StackId = ""
        self.RequestId = ""
        self.LogicalResourceId = ""
        self.Data = {}
        self.NoEcho = False
        self._event = {}
        self._context = None
        self._response_url = ""
        self._sam_local = os.getenv('AWS_SAM_LOCAL')
        self._region = os.getenv('AWS_REGION')
        self._ssl_verify = ssl_verify
        try:
            if not self._sam_local:
                self._lambda_client = boto3.client('lambda', region_name=self._region, verify=self._ssl_verify)
                self._events_client = boto3.client('events', region_name=self._region, verify=self._ssl_verify)
                self._logs_client = boto3.client('logs', region_name=self._region, verify=self._ssl_verify)
            if json_logging:
                log_helper.setup(log_level, boto_level=boto_level, RequestType='ContainerInit')
            else:
                log_helper.setup(log_level, formatter_cls=None, boto_level=boto_level)
        except Exception as e:
            logger.error(e, exc_info=True)
            self.init_failure(e)

    def __call__(self, event, context):
        try:
            self._log_setup(event, context)
            logger.debug(event)
            if not self._crhelper_init(event, context):
                return
            # Check for polling functions
            if self._poll_enabled() and self._sam_local:
                logger.info("Skipping poller functionality, as this is a local invocation")
            elif self._poll_enabled():
                self._polling_init(event)
            # If polling is not enabled, then we should respond
            else:
                logger.debug("enabling send_response")
                self._send_response = True
            logger.debug("_send_response: %s" % self._send_response)
            if self._send_response:
                if self.RequestType == 'Delete':
                    self._wait_for_cwlogs()
                self._cfn_response(event)
        except Exception as e:
            logger.error(e, exc_info=True)
            self._send(FAILED, str(e))
        finally:
            if self._timer:
                self._timer.cancel()

    def _wait_for_cwlogs(self, sleep=sleep):
        time_left = int(self._context.get_remaining_time_in_millis() / 1000) - 15
        sleep_time = 0

        if time_left > self._sleep_on_delete:
            sleep_time = self._sleep_on_delete

        if sleep_time > 1:
            sleep(sleep_time)

    def _log_setup(self, event, context):
        if self._json_logging:
            log_helper.setup(self._log_level, boto_level=self._boto_level, RequestType=event['RequestType'],
                             StackId=event['StackId'], RequestId=event['RequestId'],
                             LogicalResourceId=event['LogicalResourceId'], aws_request_id=context.aws_request_id)
        else:
            log_helper.setup(self._log_level, boto_level=self._boto_level, formatter_cls=None)

    def _crhelper_init(self, event, context):
        self._send_response = False
        self.Status = SUCCESS
        self.Reason = ""
        self.PhysicalResourceId = ""
        self.StackId = event["StackId"]
        self.RequestId = event["RequestId"]
        self.LogicalResourceId = event["LogicalResourceId"]
        self.Data = {}
        if "CrHelperData" in event.keys():
            self.Data = event["CrHelperData"]
        self.RequestType = event["RequestType"]
        self._event = event
        self._context = context
        self._response_url = event['ResponseURL']
        if self._timer:
            self._timer.cancel()
        if self._init_failed:
            self._send(FAILED, str(self._init_failed))
            return False
        self._set_timeout()
        self._wrap_function(self._get_func())
        return True

    def _polling_init(self, event):
        # Setup polling on initial request
        logger.debug("pid1: %s" % self.PhysicalResourceId)
        if 'CrHelperPoll' not in event.keys() and self.Status != FAILED:
            logger.info("Setting up polling")
            self.Data["PhysicalResourceId"] = self.PhysicalResourceId
            self._setup_polling()
            self.PhysicalResourceId = None
            logger.debug("pid2: %s" % self.PhysicalResourceId)
        # if physical id is set, or there was a failure then we're done
        logger.debug("pid3: %s" % self.PhysicalResourceId)
        if self.PhysicalResourceId or self.Status == FAILED:
            logger.info("Polling complete, removing cwe schedule")
            self._remove_polling()
            self._send_response = True

    def generate_physical_id(self, event):
        return '_'.join([
            event['StackId'].split('/')[1],
            event['LogicalResourceId'],
            self._rand_string(8)
        ])

    def _cfn_response(self, event):
        # Use existing PhysicalResourceId if it's in the event and no ID was set
        if not self.PhysicalResourceId and "PhysicalResourceId" in event.keys():
            logger.info("PhysicalResourceId present in event, Using that for response")
            self.PhysicalResourceId = event['PhysicalResourceId']
        # Generate a physical id if none is provided
        elif not self.PhysicalResourceId or self.PhysicalResourceId is True:
            logger.info("No physical resource id returned, generating one...")
            self.PhysicalResourceId = self.generate_physical_id(event)
        self._send()

    def _poll_enabled(self):
        return getattr(self, "_poll_{}_func".format(self._event['RequestType'].lower()))

    def create(self, func):
        self._create_func = func
        return func

    def update(self, func):
        self._update_func = func
        return func

    def delete(self, func):
        self._delete_func = func
        return func

    def poll_create(self, func):
        self._poll_create_func = func
        return func

    def poll_update(self, func):
        self._poll_update_func = func
        return func

    def poll_delete(self, func):
        self._poll_delete_func = func
        return func

    def _wrap_function(self, func):
        try:
            self.PhysicalResourceId = func(self._event, self._context) if func else ''
        except Exception as e:
            logger.error(str(e), exc_info=True)
            self.Reason = str(e)
            self.Status = FAILED

    def _timeout(self):
        logger.error("Execution is about to time out, sending failure message")
        self._send(FAILED, "Execution timed out")

    def _set_timeout(self):
        self._timer = threading.Timer((self._context.get_remaining_time_in_millis() / 1000.00) - 0.5,
                                      self._timeout)
        self._timer.start()

    def _get_func(self):
        request_type = "_{}_func"
        if "CrHelperPoll" in self._event.keys():
            request_type = "_poll" + request_type
        return getattr(self, request_type.format(self._event['RequestType'].lower()))

    def _send(self, status=None, reason="", send_response=_send_response):
        if len(str(str(self.Reason))) > 256:
            self.Reason = "ERROR: (truncated) " + str(self.Reason)[len(str(self.Reason)) - 240:]
        if len(str(reason)) > 256:
            reason = "ERROR: (truncated) " + str(reason)[len(str(reason)) - 240:]
        response_body = {
            'Status': self.Status,
            'PhysicalResourceId': str(self.PhysicalResourceId),
            'StackId': self.StackId,
            'RequestId': self.RequestId,
            'LogicalResourceId': self.LogicalResourceId,
            'Reason': str(self.Reason),
            'Data': self.Data,
            'NoEcho': self.NoEcho,
        }
        if status:
            response_body.update({'Status': status, 'Reason': reason})
        send_response(self._response_url, response_body, self._ssl_verify)

    def init_failure(self, error):
        self._init_failed = error
        logger.error(str(error), exc_info=True)

    def _cleanup_response(self):
        for k in ["CrHelperPoll", "CrHelperPermission", "CrHelperRule"]:
            if k in self.Data.keys():
                del self.Data[k]

    @staticmethod
    def _rand_string(l):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(l))

    def _add_permission(self, rule_arn):
        sid = self._event['LogicalResourceId'] + self._rand_string(8)
        self._lambda_client.add_permission(
            FunctionName=self._context.function_name,
            StatementId=sid,
            Action='lambda:InvokeFunction',
            Principal='events.amazonaws.com',
            SourceArn=rule_arn
        )
        return sid

    def _put_rule(self):
        schedule_unit = 'minutes' if self._polling_interval != 1 else 'minute'
        response = self._events_client.put_rule(
            Name=self._event['LogicalResourceId'] + self._rand_string(8),
            ScheduleExpression='rate({} {})'.format(self._polling_interval, schedule_unit),
            State='ENABLED',
        )
        return response["RuleArn"]

    def _put_targets(self, func_name):
        region = self._event['CrHelperRule'].split(":")[3]
        account_id = self._event['CrHelperRule'].split(":")[4]
        partition = self._event['CrHelperRule'].split(":")[1]
        rule_name = self._event['CrHelperRule'].split("/")[1]
        logger.debug(self._event)
        self._events_client.put_targets(
            Rule=rule_name,
            Targets=[
                {
                    'Id': '1',
                    'Arn': 'arn:%s:lambda:%s:%s:function:%s' % (partition, region, account_id, func_name),
                    'Input': json.dumps(self._event)
                }
            ]
        )

    def _remove_targets(self, rule_arn):
        self._events_client.remove_targets(
            Rule=rule_arn.split("/")[1],
            Ids=['1']
        )

    def _remove_permission(self, sid):
        self._lambda_client.remove_permission(
            FunctionName=self._context.function_name,
            StatementId=sid
        )

    def _delete_rule(self, rule_arn):
        self._events_client.delete_rule(
            Name=rule_arn.split("/")[1]
        )

    def _setup_polling(self):
        self._event['CrHelperData'] = self.Data
        self._event['CrHelperPoll'] = True
        self._event['CrHelperRule'] = self._put_rule()
        self._event['CrHelperPermission'] = self._add_permission(self._event['CrHelperRule'])
        self._put_targets(self._context.function_name)

    def _remove_polling(self):
        if 'CrHelperData' in self._event.keys():
            self._event.pop('CrHelperData')
        if "PhysicalResourceId" in self.Data.keys():
            self.Data.pop("PhysicalResourceId")
        if 'CrHelperRule' in self._event.keys():
            self._remove_targets(self._event['CrHelperRule'])
        else:
            logger.error("Cannot remove CloudWatch events rule, Rule arn not available in event")
        if 'CrHelperPermission' in self._event.keys():
            self._remove_permission(self._event['CrHelperPermission'])
        else:
            logger.error("Cannot remove lambda events permission, permission id not available in event")
        if 'CrHelperRule' in self._event.keys():
            self._delete_rule(self._event['CrHelperRule'])
        else:
            logger.error("Cannot remove CloudWatch events target, Rule arn not available in event")
