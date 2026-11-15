import json
import os
import boto3

sqs_client = boto3.client("sqs")

def getMessagesFromQueue(qUrl):
    # Receive message from SQS queue
    #You can pull them one by one or more that one
    response = sqs_client.receive_message(
        QueueUrl=qUrl,
        MaxNumberOfMessages=1,
        VisibilityTimeout=60 #14400
    )

    if('Messages' in response):
        return response['Messages']
    else:
        print("No messages in queue.")
        return None

def deleteMessagesFromQueue(qUrl, receipt_handle):
    #Delete message from queue
    try:
        sqs_client.delete_message(
            QueueUrl=qUrl,
            ReceiptHandle=receipt_handle
        )
        print('Deleted item from queue...')
    except Exception as e:
        print(f"Failed to delete message for {receipt_handle} with error: {e}")

def changeVisibility(sqs, qUrl, receipt_handle):
    #Change message status : from 'in flight' to 'available'
    try:
        sqs.change_message_visibility(
                QueueUrl=qUrl,
                ReceiptHandle=receipt_handle,
                VisibilityTimeout=0
            )
    except Exception as e:
        print(f"Failed to change visibility for {receipt_handle} with error: {e}")

def handler(event, context):
    print("Lambda function invoked")
    print(json.dumps(event))

    qUrl = os.environ['QUEUE_URL']

    #change this value according to the limits of your downstream service
    max_jobs_to_submit = 5

    total_jobs_scheduled = 0
    i = 0
    hit_limit = False
    total_messages = 0

    while(i < max_jobs_to_submit):
        messages = getMessagesFromQueue(qUrl)
        if(messages):

            total_messages = len(messages)
            print("Total messages: {}".format(total_messages))

            for message in messages:
                receipt_handle = message['ReceiptHandle']

                try:
                    if(hit_limit):
                        changeVisibility(qUrl, receipt_handle)
                    else:
                        #SUBMIT JOB TO THE DOWNSTREAM SERVICE
                        print("Submitting job to downstream service...")

                        ### CATCH ERROR FROM DOWNSTREAM SERVICE ###
                        #Implement getting the error response from the service the an error cannot be thrown

                        # Delete received message from queue
                        deleteMessagesFromQueue(qUrl, receipt_handle)
                        total_jobs_scheduled += 1
                        i += 1
                except Exception as e:
                    print("Error while starting job: {}".format(e))
                    changeVisibility(qUrl, receipt_handle)

                    ### CATCH ERROR FROM DOWNSTREAM SERVICE ###
                    #ERROR FROM DOWNSTREAM SERVICE (if the code used to submit jobs throws an error)
                    #IF ERROR, THE DOWNSTREAM SERVICE CANNOT ACCEPT ANY JOBS ANYMORE -> STOP SUBMITTING AND STOP THE WHILE LOOP
                    if(e.__class__.__name__ == 'LimitExceededException'
                        or e.__class__.__name__ == "ProvisionedThroughputExceededException"):
                        hit_limit = True
                        i = max_jobs_to_submit

        else:
            i = max_jobs_to_submit


    output = "Started {} jobs.".format(total_jobs_scheduled)
    if(hit_limit):
        output += " Hit limit."

    if hit_limit or (total_jobs_scheduled > 0) :
        print(output)

    return {
        'statusCode': 200,
        'body': output
    }

