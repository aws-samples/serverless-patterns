import logging
import boto3
import json
import os

# Initialize Pinpoint client
pinpoint_client = boto3.client('pinpoint')

def lambda_handler(event, context):
    
    print(event)
    event_body = json.loads(event['body'])
    
    app_id = os.environ.get("PINPOINT_APP_ID")
    
    destination_number = event_body["destination_number"]
    
    message = "Your OTP is 1234"
    
    origination_number = ""
    
    message_type = "TRANSACTIONAL"
    

    response = dict()
    try:
        response_number_validation = pinpoint_client.phone_number_validate(NumberValidateRequest={'PhoneNumber':destination_number})
        
        if response_number_validation["NumberValidateResponse"]["PhoneType"] != "INVALID":
            
            print("Sending SMS message.")
            
            response_send_message = pinpoint_client.send_messages(
            ApplicationId=app_id,
            MessageRequest={
                'Addresses': {destination_number: {'ChannelType': 'SMS'}},
                'MessageConfiguration': {
                    'SMSMessage': {
                        'Body': message,
                        'MessageType': message_type,
                        'OriginationNumber': origination_number}}})
            
            
            message_id = response_send_message['MessageResponse']['Result'][destination_number]['MessageId']
            
            if message_id:
                
                print(f"Message sent! Message ID: {message_id}.")
                response = dict()
                response['statusCode'] = 200
                response['body'] = f"Message sent! Message ID: {message_id}."
                return response
                
            else:
                
                print(f"Unable to send message")
                response = dict()
                response['statusCode'] = 500
                response['body'] = response_send_message
                return response
        
        
    except Exception as e:
        
        print("Couldn't send message!")
        response['statusCode'] = 500
        response['body'] = "Couldn't send message!\n" + str(e)
        return response
    
    

        

        


        
    


