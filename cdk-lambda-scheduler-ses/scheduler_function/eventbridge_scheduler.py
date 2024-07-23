
import json
import boto3
import os
from datetime import datetime

scheduler = boto3.client('scheduler')

def create_scheduler(formatted_expirationDate, lambda_target_template):
    res=scheduler.create_schedule(
        Name='reminder_scheduler',
        Description='Pipeline Approval Reminder',
        ScheduleExpression='at({0})'.format(formatted_expirationDate.strftime("%Y-%m-%dT%H:%M:%S")),
        Target=lambda_target_template,
        FlexibleTimeWindow ={'Mode': 'OFF'},
        ActionAfterCompletion = 'DELETE'
       )
    return res

def lambda_handler(event, context):

    sendTime=event['datetime']
    message=event['message']
    destination_email=event['email']
    formatted_expirationDate= datetime.strptime(sendTime,"%Y-%m-%dT%H:%M:%SZ")
    
    lambda_target_template= {
        'Arn': 'arn:aws:scheduler:::aws-sdk:ses:sendEmail',
        'RoleArn': os.environ['SCHEDULER_ROLE_ARN'],
        'Input': "{\"Destination\": {\"ToAddresses\": [\"" + destination_email + "\"] }, \"Message\": {\"Body\": {\"Text\": {\"Data\": \"" + message + "\"}}, \"Subject\": {\"Data\": \"Reminder Email\"}}, \"Source\": \"" + os.environ['SES_SENDER_IDENTITY'] + "\"}"
        }
    create_scheduler(formatted_expirationDate, lambda_target_template)
    
