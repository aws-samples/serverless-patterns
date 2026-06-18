"""
AWS Lambda function demonstrating Amazon Bedrock AgentCore Browser operations.
Starts a browser session, navigates to a URL, and extracts page content.
"""

import json
import os
import boto3


def handler(event, context):
    """Demonstrate Amazon Bedrock AgentCore Browser session management."""
    try:
        browser_id = os.environ['BROWSER_ID']
        region = os.environ.get('AWS_REGION', 'us-east-1')
        action = event.get('action', 'browse')

        client = boto3.client('bedrock-agentcore', region_name=region)

        if action == 'browse':
            url = event.get('url', 'https://aws.amazon.com/bedrock/agentcore/')

            # Start a browser session
            session_response = client.start_browser_session(
                browserIdentifier=browser_id,
            )
            session_id = session_response['sessionId']

            # Invoke the browser to navigate and extract content
            browse_response = client.invoke_browser(
                browserIdentifier=browser_id,
                sessionId=session_id,
                action={
                    'navigate': {'url': url},
                },
            )

            # Get page content
            content_response = client.invoke_browser(
                browserIdentifier=browser_id,
                sessionId=session_id,
                action={
                    'getContent': {},
                },
            )

            # Stop the session
            client.stop_browser_session(
                browserIdentifier=browser_id,
                sessionId=session_id,
            )

            return {
                'statusCode': 200,
                'body': json.dumps({
                    'action': 'browse',
                    'url': url,
                    'sessionId': session_id,
                    'content': str(content_response.get('result', ''))[:2000],
                }),
            }

        elif action == 'list_sessions':
            response = client.list_browser_sessions(browserIdentifier=browser_id)
            sessions = response.get('browserSessions', [])
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'action': 'list_sessions',
                    'count': len(sessions),
                    'sessions': [str(s) for s in sessions[:5]],
                }, default=str),
            }

        else:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': f'Unknown action: {action}. Use browse or list_sessions.'}),
            }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
        }
