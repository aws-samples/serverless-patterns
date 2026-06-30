"""
AWS Lambda function: Personalized AI assistant with persistent memory.
Stores conversations in Amazon Bedrock AgentCore Memory, retrieves relevant
context via semantic search, and generates personalized responses using Amazon Bedrock.
"""

import json
import os
import uuid
from datetime import datetime, timezone
import boto3


def handler(event, context):
    """Personalized AI assistant with persistent memory across sessions."""
    try:
        memory_id = os.environ['MEMORY_ID']
        model_id = os.environ.get('MODEL_ID', 'us.anthropic.claude-sonnet-4-20250514-v1:0')
        region = os.environ.get('AWS_REGION', 'us-east-1')
        action = event.get('action', 'chat')

        agentcore_client = boto3.client('bedrock-agentcore', region_name=region)

        if action == 'store':
            session_id = event.get('sessionId', str(uuid.uuid4()))
            messages = event.get('messages', [
                {'role': 'user', 'content': 'My name is Alice and I prefer Python for data work'},
                {'role': 'assistant', 'content': 'Noted! I will remember your Python preference, Alice.'},
            ])
            actor_id = event.get('actorId', 'demo-user')

            payload = []
            for m in messages:
                role = 'USER' if m['role'] == 'user' else 'ASSISTANT'
                payload.append({'conversational': {'content': {'text': m['content']}, 'role': role}})

            agentcore_client.create_event(
                memoryId=memory_id, actorId=actor_id,
                sessionId=session_id, eventTimestamp=datetime.now(timezone.utc),
                payload=payload,
            )

            return {
                'statusCode': 200,
                'body': json.dumps({'action': 'store', 'sessionId': session_id}),
            }

        elif action == 'chat':
            question = event.get('question', 'What programming language should I use?')
            actor_id = event.get('actorId', 'demo-user')

            # Step 1: Retrieve relevant memories about this user
            memory_response = agentcore_client.retrieve_memory_records(
                memoryId=memory_id, namespace=actor_id,
                searchCriteria={'searchQuery': question, 'topK': 5},
            )
            records = memory_response.get('memoryRecords', [])
            memory_context = '\n'.join(str(r) for r in records) if records else 'No memories stored yet.'

            # Step 2: Generate personalized response using Amazon Bedrock
            bedrock_client = boto3.client('bedrock-runtime', region_name=region)

            prompt = f"""You are a personalized AI assistant. Use the following memories about the user to give a tailored, relevant response.

User Memories:
{memory_context}

User Question: {question}

Respond naturally, referencing what you know about the user from memory. If no memories exist, respond helpfully and note you're still learning about them."""

            response = bedrock_client.invoke_model(
                modelId=model_id, contentType='application/json', accept='application/json',
                body=json.dumps({
                    'anthropic_version': 'bedrock-2023-05-31',
                    'max_tokens': 512,
                    'messages': [{'role': 'user', 'content': prompt}],
                }),
            )

            body = json.loads(response['body'].read())
            answer = body['content'][0]['text']

            return {
                'statusCode': 200,
                'body': json.dumps({'action': 'chat', 'question': question, 'answer': answer, 'memoriesUsed': len(records)}),
            }

        else:
            return {'statusCode': 400, 'body': json.dumps({'error': f'Unknown action: {action}. Use store or chat.'})}

    except Exception as e:
        return {'statusCode': 500, 'body': json.dumps({'error': str(e)})}
