import boto3
import os

pipeline = boto3.client('codepipeline')
client = boto3.client('ses')

def lambda_handler(event, context):
    pipelineName=event['pipelineName']
    pipelineExecutionId=event['pipelineExecutionID']
    current_state= pipeline.get_pipeline_execution(
         pipelineName=pipelineName,
         pipelineExecutionId=pipelineExecutionId
        )
    if current_state['pipelineExecution']['status'] == 'InProgress':
        action_detail= pipeline.list_action_executions(
            pipelineName=pipelineName,
            filter={
                'pipelineExecutionId': pipelineExecutionId
            })
        for i in action_detail['actionExecutionDetails']: 
            if i['stageName'] == event['stageName'] and i['actionName'] == event['actionName'] and i['status'] == 'InProgress':
                response = client.send_email(
                    Destination={
                        'ToAddresses': [event['destinationEmail']]
                        },
                    Message={
                        'Body': {
                            'Text': {
                                'Charset': 'UTF-8',
                                'Data': 'The pipeline ' + pipelineName + ' present in the region ' + event['region'] + ' has still not completed execution as it is stuck on the action ' + event['actionName'] + ' in the ' + event['stageName'] + ' stage. Please review the pipeline and take appropriate action.',
                                }
                                },
                        'Subject': {
                            'Charset': 'UTF-8',
                            'Data': 'CodePipeline Action Needed',
                            }
                            },
                        Source= os.environ['SES_SOURCE_EMAIL']
                        )
                print(response)
                break
    
    else: 
        print("No reminder email needed")