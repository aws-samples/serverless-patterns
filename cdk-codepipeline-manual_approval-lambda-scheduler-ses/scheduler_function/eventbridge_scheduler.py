import json
import boto3
import os
from datetime import datetime, timedelta

pipeline = boto3.client('codepipeline')
scheduler = boto3.client('scheduler')

def get_pipeline_name(event):
    pipelineDetails = json.loads(event['Records'][0]['Sns']['Message'])
    expirationDate=pipelineDetails['approval']['expires']
    formatted_expirationDate= datetime.strptime(expirationDate,"%Y-%m-%dT%H:%MZ")
    pipelineName=pipelineDetails['approval']['pipelineName']
    stageName=pipelineDetails['approval']['stageName']
    actionName=pipelineDetails['approval']['actionName']
    region=pipelineDetails['region']
    return formatted_expirationDate, pipelineName, stageName, actionName, region

def get_pipeline_execution_id(pipelineName):
    execution_summary = pipeline.list_pipeline_executions(pipelineName=pipelineName)
    arr=execution_summary['pipelineExecutionSummaries']
    for i in arr:
        for key in i.keys():
            if i['status'] == 'InProgress':
                response = i['pipelineExecutionId']
            else:
                continue
    return response
    
#Add a try and except block in create_scheduler function that checks if create_schedule was successful or not.
#If not, then send an email to the SES_DESTINATION_EMAIL with the error message.
#If successful, then return the response from create_schedule.

def create_scheduler(formatted_expirationDate, lambda_target_template):
    try:
        res = scheduler.create_schedule(
            Name='pipeline_approval_reminder',
            Description='Pipeline Approval Reminder',
            FlexibleTimeWindow={'Mode': 'OFF'},
            ScheduleExpression='at({0})'.format((formatted_expirationDate - timedelta(days=6, hours=12)).strftime("%Y-%m-%dT%H:%M:%S")),
            Target=lambda_target_template,
            ActionAfterCompletion = 'DELETE',
        )
        print(res)
    except Exception as e:
        print(e)
        print("Error in creating eventbridge scheduler")
        raise e  
     
def lambda_handler(event, context):
    formatted_expirationDate, pipelineName, stageName, actionName, region=get_pipeline_name(event)
    pipeline_execution_id = get_pipeline_execution_id(pipelineName)
    lambda_target_template= {
        'Arn': os.environ['TRIGGER_LAMBDA_ARN'],
        'RoleArn': os.environ['SCHEDULER_ROLE_ARN'],
        'Input': "{\"destinationEmail\": \"" + os.environ['SES_DESTINATION_EMAIL'] + "\", \"pipelineName\": \"" + pipelineName + "\", \"pipelineExecutionID\": \"" + pipeline_execution_id + "\", \"stageName\": \"" + stageName + "\", \"actionName\": \"" + actionName + "\", \"region\": \"" + region + "\" }"
        
    }
    create_scheduler(formatted_expirationDate, lambda_target_template)
    