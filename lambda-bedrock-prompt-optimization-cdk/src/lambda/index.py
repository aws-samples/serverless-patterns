import json
import os
import time
import boto3

bedrock = boto3.client('bedrock')
s3 = boto3.client('s3')

BUCKET = os.environ['BUCKET_NAME']


def handler(event, context):
    """Create an Advanced Prompt Optimization job, poll until complete, return results."""
    prompt_template = event.get('promptTemplate', 'You are a helpful assistant. Answer the following question concisely and accurately: {{question}}')
    template_id = event.get('templateId', 'qa-template-v1')
    model_id = event.get('modelId', 'us.anthropic.claude-sonnet-4-20250514-v1:0')
    samples = event.get('evaluationSamples', [
        {'inputVariables': [{'question': 'What is cloud computing?'}], 'referenceResponse': 'Cloud computing is the on-demand delivery of IT resources over the Internet with pay-as-you-go pricing.'},
        {'inputVariables': [{'question': 'What is serverless?'}], 'referenceResponse': 'Serverless is a cloud execution model where the provider manages infrastructure, scaling automatically and charging only for actual usage.'},
        {'inputVariables': [{'question': 'What is Amazon Bedrock?'}], 'referenceResponse': 'Amazon Bedrock is a fully managed service that offers foundation models from leading AI companies through a single API.'},
    ])

    # Build JSONL input (one line per template)
    input_entry = {
        'version': 'bedrock-2026-05-14',
        'templateId': template_id,
        'promptTemplate': prompt_template,
        'steeringCriteria': ['ACCURATE', 'CONCISE'],
        'evaluationSamples': samples,
    }
    input_key = f'input/{context.aws_request_id}.jsonl'
    s3.put_object(Bucket=BUCKET, Key=input_key, Body=json.dumps(input_entry))

    # Create optimization job
    job = bedrock.create_advanced_prompt_optimization_job(
        jobName=f'opt-{context.aws_request_id[:8]}',
        inputConfig={'s3Uri': f's3://{BUCKET}/{input_key}'},
        outputConfig={'s3Uri': f's3://{BUCKET}/output/{context.aws_request_id}/'},
        modelConfigurations=[{'modelId': model_id}],
    )
    job_arn = job['jobArn']

    # Poll for completion (max ~14 min with 15 min Lambda timeout)
    for _ in range(84):
        time.sleep(10)
        status = bedrock.get_advanced_prompt_optimization_job(jobIdentifier=job_arn)
        state = status.get('jobStatus', status.get('status', 'UNKNOWN'))
        if state in ('COMPLETED', 'SUCCEEDED'):
            return {
                'statusCode': 200,
                'jobArn': job_arn,
                'status': state,
                'outputUri': f's3://{BUCKET}/output/{context.aws_request_id}/',
            }
        if state in ('FAILED', 'STOPPED'):
            return {
                'statusCode': 500,
                'jobArn': job_arn,
                'status': state,
                'failureMessage': status.get('failureMessage', 'Unknown error'),
            }

    return {'statusCode': 408, 'jobArn': job_arn, 'status': 'TIMEOUT', 'message': 'Job did not complete within Lambda timeout'}
