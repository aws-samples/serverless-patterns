import boto3  
import os 
sqs = boto3.client('sqs') 

def delete_message(queue_url, receipt_handle, message):
    response = sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=receipt_handle)
    return "Message " + "'" + message + "'" + " deleted"
    
def poll_messages(queue_url):
    print("Polling from " + queue_url)
    QueueUrl=queue_url
    response = sqs.receive_message(
        QueueUrl=QueueUrl,
        AttributeNames=[],
        MaxNumberOfMessages=1,
        MessageAttributeNames=['All'],
        WaitTimeSeconds=3
    )
    if "Messages" in response:
        receipt_handle=response['Messages'][0]['ReceiptHandle']
        message = response['Messages'][0]['Body']
        print("message = " + message)
        delete_response = delete_message(QueueUrl,receipt_handle,message)
        return delete_response
    else:
        print("No more messages to poll in " + queue_url)
        return "No more messages to poll"

def lambda_handler(event, context):
    response = poll_messages(os.environ['HighPriorityQueue'])
    print("Response = " + response)
    if response == "No more messages to poll":
        response = poll_messages(os.environ['MediumPriorityQueue'])
        print("Response = " + response)
        if response == "No more messages to poll":
            response = poll_messages(os.environ['LowPriorityQueue'])
    return response
