import json
import boto3
import os


def handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    message = event.get('detail')

    print("From Auth0: " + str(message))

    #get account email address from Auth0 Event
    user_email = message.get('user_name')

    #get the error message to use in subject line
    error_msg = message.get('details').get('error').get('message')

    #get the timestamp of the event
    time_stamp = message.get('date')

    #get the IP address and agent to added to output message body
    login_attempt_info = "A login attempt from " + str(message.get('ip')) + " on " + str(message.get('user_agent')) + " was blocked on your account."
    
    try:
        # you could send an email using SES here! 
        response = "The account belonging to " + user_email + " had a " + error_msg + " at " + time_stamp + ". " + login_attempt_info
        print(response)
        return response

    except Exception as e: 
        return e
    
