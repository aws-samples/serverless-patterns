import json
import boto3
import os


def handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    message = event.get('detail')

    print("From PagerDuty: " + str(message))

    #get account email address from PagerDuty Event
    user_email = str(message.get('log_entries')[0].get('agent').get('id')) + "@pagerduty.com"

    #get the incident summary to use in subject line
    incident_msg = message.get('log_entries')[0].get('summary')

    #get the timestamp of the event
    time_stamp = event.get('time')

    #get the incident id agent added to output message body
    incident_info = "The incident number " + str(message.get('log_entries')[3].get('incident').get('id')) + " has been acknowledged by " + str(message.get('log_entries')[0].get('agent').get('id')) + "." 
    
    try:
        # you could send an email using SES here! 
        response = "The account belonging to " + user_email + " had an incident acknowledged at " + time_stamp + ". " + incident_info
        print(response)
        return response

    except Exception as e: 
        return e
    
