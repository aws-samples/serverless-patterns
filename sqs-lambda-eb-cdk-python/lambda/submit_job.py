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

    totalJobsScheduled = 0
    i = 0
    hitLimit = False
    totalMessages = 0

    while(i < max_jobs_to_submit):
        messages = getMessagesFromQueue(qUrl)
        if(messages):

            totalMessages = len(messages)
            print("Total messages: {}".format(totalMessages))

            for message in messages:
                receipt_handle = message['ReceiptHandle']

                try:
                    if(hitLimit):
                        changeVisibility(qUrl, receipt_handle)
                    else:
                        #SUBMIT JOB TO THE DOWNSTREAM SERVICE
                        print("Submitting job to downstream service...")

                        ### CATCH ERROR FROM DOWNSTREAM SERVICE ###
                        #Implement getting the error response from the service the an error cannot be thrown

                        # Delete received message from queue
                        deleteMessagesFromQueue(qUrl, receipt_handle)
                        totalJobsScheduled += 1
                        i += 1
                except Exception as e:
                    print("Error while starting job: {}".format(e))
                    changeVisibility(qUrl, receipt_handle)

                    ### CATCH ERROR FROM DOWNSTREAM SERVICE ###
                    #ERROR FROM DOWNSTREAM SERVICE (if the code used to submit jobs throws an error)
                    #IF ERROR, THE DOWNSTREAM SERVICE CANNOT ACCEPT ANY JOBS ANYMORE -> STOP SUBMITTING AND STOP THE WHILE LOOP
                    if(e.__class__.__name__ == 'LimitExceededException'
                        or e.__class__.__name__ == "ProvisionedThroughputExceededException"):
                        hitLimit = True
                        i = max_jobs_to_submit

        else:
            i = max_jobs_to_submit


    output = "Started {} jobs.".format(totalJobsScheduled)
    if(hitLimit):
        output += " Hit limit."

    if hitLimit or (totalJobsScheduled > 0) :
        print(output)

    return {
        'statusCode': 200,
        'body': output
    }

