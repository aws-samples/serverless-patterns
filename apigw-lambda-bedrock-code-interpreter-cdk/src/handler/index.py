"""
AWS Lambda function: AI Data Analyst.
Amazon Bedrock generates Python analysis code from natural language questions,
Amazon Bedrock AgentCore Code Interpreter executes it in a secure sandbox.
"""

import json
import os
import boto3


def handler(event, context):
    """Generate and execute data analysis code from natural language."""
    try:
        body = json.loads(event.get('body', '{}')) if isinstance(event.get('body'), str) else event
        question = body.get('question', '')
        data = body.get('data', '')

        if not question:
            return {
                'statusCode': 400,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'error': 'question field is required'}),
            }

        code_interpreter_id = os.environ['CODE_INTERPRETER_ID']
        model_id = os.environ.get('MODEL_ID', 'us.anthropic.claude-sonnet-4-5-20250929-v1:0')
        region = os.environ['AWS_REGION']

        # Step 1: Use Amazon Bedrock to generate Python code for the question
        bedrock_client = boto3.client('bedrock-runtime', region_name=region)

        code_gen_prompt = f"""Write a Python script that answers this data analysis question. 
The script should print the answer clearly to stdout.
Use only standard library modules (json, math, statistics, datetime, collections, itertools, csv, re).
Do not use external packages like pandas or numpy.

Question: {question}
{f"Data: {data}" if data else ""}

Return ONLY the Python code, no explanation. No markdown code fences."""

        response = bedrock_client.invoke_model(
            modelId=model_id, contentType='application/json', accept='application/json',
            body=json.dumps({
                'anthropic_version': 'bedrock-2023-05-31',
                'max_tokens': 1024,
                'messages': [{'role': 'user', 'content': code_gen_prompt}],
            }),
        )

        bedrock_body = json.loads(response['body'].read())
        generated_code = bedrock_body['content'][0]['text'].strip()
        # Strip markdown fences if present
        if generated_code.startswith('```'):
            generated_code = '\n'.join(generated_code.split('\n')[1:-1])

        # Step 2: Execute the generated code in Amazon Bedrock AgentCore Code Interpreter
        agentcore_client = boto3.client('bedrock-agentcore', region_name=region)

        session = agentcore_client.start_code_interpreter_session(
            codeInterpreterIdentifier=code_interpreter_id,
        )
        session_id = session['sessionId']

        exec_response = agentcore_client.invoke_code_interpreter(
            codeInterpreterIdentifier=code_interpreter_id,
            sessionId=session_id,
            name='executeCode',
            arguments={
                'code': generated_code,
                'language': 'python',
            },
        )

        # Parse EventStream response
        result_text = ''
        error_text = ''
        event_stream = exec_response.get('body', {})
        for event in event_stream:
            if 'chunk' in event:
                chunk = event['chunk']
                sc = chunk.get('structuredContent', {})
                if sc.get('stdout'):
                    result_text += sc['stdout']
                if sc.get('stderr'):
                    error_text += sc['stderr']
            elif 'result' in event:
                r = event['result']
                sc = r.get('structuredContent', {})
                if sc.get('stdout'):
                    result_text += sc['stdout']
                if sc.get('stderr'):
                    error_text += sc['stderr']

        stdout = result_text or 'Code executed successfully (no stdout output)'
        stderr = error_text

        agentcore_client.stop_code_interpreter_session(
            codeInterpreterIdentifier=code_interpreter_id,
            sessionId=session_id,
        )

        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({
                'question': question,
                'generatedCode': generated_code,
                'result': stdout,
                'errors': stderr if stderr else None,
            }),
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': str(e)}),
        }
