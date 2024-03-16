import json

# Create an AWS Lambda function that processes emails received by Amazon SES
def lambda_handler(event, context):
    # Get the email message from the event data
    message = event['Records'][0]['ses']['mail']
    
    # Extract the email address from the sender
    sender = message['commonHeaders']['from'][0]
    
    # Extract the subject line from the email
    subject = message['commonHeaders']['subject']
    
    
    # Log the email details
    print(f"Received email from {sender} with subject {subject}")
    
    # Return a success message
    return {
        'statusCode': 200,
        'body': json.dumps('Email processed successfully!')
    }
