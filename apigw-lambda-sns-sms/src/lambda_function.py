import boto3
import json


# Initialize Pinpoint client
pinpoint_client = boto3.client('pinpoint')
sns_client = boto3.client('sns')

def lambda_handler(event, context):
    
    print(event)
    event_body = json.loads(event['body'])
    
    destination_number = event_body["destination_number"]
    print(destination_number)
    
    message = "Your OTP is 1234"

    response = dict()
    try:
        response_number_validation = pinpoint_client.phone_number_validate(NumberValidateRequest={'PhoneNumber':destination_number})
        
        if response_number_validation["NumberValidateResponse"]["PhoneType"] != "INVALID":
            
            print("Sending SMS message.")
            
            response_send_message = sns_client.publish(
                PhoneNumber=destination_number,
                Message=message
            )
            
            message_id = response_send_message['MessageId']
            
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
    
    

        

        


        
    


