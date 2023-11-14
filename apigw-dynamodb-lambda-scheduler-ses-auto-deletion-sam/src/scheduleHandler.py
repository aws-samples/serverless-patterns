import json
import os
import boto3
from datetime import datetime, timedelta

scheduler_client = boto3.client('scheduler')

def lambda_handler(event, context):

    for record in event['Records']:

        reminder_id = record['dynamodb']['Keys']['id']['S']

        if record['eventName'] == 'INSERT' or record['eventName'] == 'MODIFY':

            reminder_datetime = datetime.strptime(record['dynamodb']['NewImage']['datetime']['S'],"%Y-%m-%dT%H:%M:%SZ")
            description = record['dynamodb']['NewImage']['description']['S']
            email = record['dynamodb']['NewImage']['email']['S']
            formatted_datetime = reminder_datetime.strftime("%Y-%m-%dT%H:%M:%S")

            ses_target_template = {
                "RoleArn": os.environ['SCHEDULER_ROLE_ARN'],
                "Arn": "arn:aws:scheduler:::aws-sdk:ses:sendEmail",
                "Input": "{\"Destination\": {\"ToAddresses\": [\"" + email + "\"] }, \"Message\": {\"Body\": {\"Text\": {\"Data\": \"" + description + " at " + formatted_datetime + " UTC\"}}, \"Subject\": {\"Data\": \"Reminder Email -  " + description + "\"}}, \"Source\": \"" + os.environ['SES_SENDER_IDENTITY'] + "\"}"
            } 

        ## Create Schedules

        if record['eventName'] == 'INSERT':

            ## Schedule for email reminder before 10 minutes
            
            email_reminder_1 = scheduler_client.create_schedule (
                Name = reminder_id + '-reminder-before-10-minutes',
                Target = ses_target_template,
                FlexibleTimeWindow = {
                    'Mode': 'OFF',
                },
                Description = 'Email reminder before 10 minutes for ' + description,
                ScheduleExpression = 'at({0})'.format((reminder_datetime - timedelta(minutes=10)).strftime("%Y-%m-%dT%H:%M:%S")),
                ActionAfterCompletion = 'DELETE'
            )

            ## Schedule for email reminder at actual time

            email_reminder_2 = scheduler_client.create_schedule (
                Name = reminder_id + '-reminder-actual-time',
                Target = ses_target_template,
                FlexibleTimeWindow = {
                    'Mode': 'OFF',
                },
                Description = 'Email reminder at actual time ' + description,
                ScheduleExpression = 'at({0})'.format(formatted_datetime),
                ActionAfterCompletion = 'DELETE'
            )
        
        ## Update Schedules

        elif record['eventName'] == 'MODIFY':

            ## Schedule for email reminder before 10 minutes
            
            update_email_reminder_1 = scheduler_client.update_schedule (
                Name = reminder_id + '-reminder-before-10-minutes',
                Target = ses_target_template,
                FlexibleTimeWindow = {
                    'Mode': 'OFF',
                },
                Description = 'Email reminder before 10 minutes for ' + description,
                ScheduleExpression = 'at({0})'.format((reminder_datetime - timedelta(minutes=10)).strftime("%Y-%m-%dT%H:%M:%S")),
                ActionAfterCompletion = 'DELETE'
            )

            ## Schedule for email reminder at actual time

            update_email_reminder_2 = scheduler_client.update_schedule (
                Name = reminder_id + '-reminder-actual-time',
                Target = ses_target_template,
                FlexibleTimeWindow = {
                    'Mode': 'OFF',
                },
                Description = 'Email reminder at actual time ' + description,
                ScheduleExpression = 'at({0})'.format(formatted_datetime),
                ActionAfterCompletion = 'DELETE'
            )

        ## Delete Schedules
            
        elif record['eventName'] == 'REMOVE':

            delete_email_reminder_1 = scheduler_client.delete_schedule(
                Name = reminder_id + '-reminder-before-10-minutes'
            )

            delete_email_reminder_2 = scheduler_client.delete_schedule(
                Name = reminder_id + '-reminder-actual-time'
            )

        else:
            print("Invalid Event Type")

        return {
                "statusCode": 200,
                "body": json.dumps("Reminders Created Successfully")
            }   