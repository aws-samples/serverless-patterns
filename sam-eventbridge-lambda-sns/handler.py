import json
import boto3
import os
from datetime import datetime

sns = boto3.client('sns')
bedrock = boto3.client('bedrock-runtime')

def process_health_event(event, context):
    """Process AWS Health events and send notifications"""
    
    try:
        # Extract health event details
        detail = event.get('detail', {})
        event_type = detail.get('eventTypeCode', 'Unknown')
        service = detail.get('service', 'Unknown')
        region = detail.get('eventRegion', 'Unknown')
        status = detail.get('statusCode', 'Unknown')
        
        # Handle eventDescription safely
        event_descriptions = detail.get('eventDescription', [])
        description = 'No description available'
        
        if event_descriptions and len(event_descriptions) > 0:
            description = event_descriptions[0].get('latestDescription', 'No description available')
        
        # Get AI analysis from Bedrock
        ai_analysis = get_bedrock_analysis(event_type, service, region, status, description)
        
        # Format notification message with AI insights
        message = format_notification(event_type, service, region, status, description, ai_analysis)
        
        # Send to SNS (skip if running locally)
        sns_topic_arn = os.environ.get('SNS_TOPIC_ARN')
        if sns_topic_arn and sns_topic_arn != 'test-topic-arn':
            response = sns.publish(
                TopicArn=sns_topic_arn,
                Subject=f'AWS Health Alert: {event_type}',
                Message=message
            )
            message_id = response['MessageId']
        else:
            print("Local testing - SNS message would be sent:")
            print(f"Subject: AWS Health Alert: {event_type}")
            print(f"Message: {message}")
            message_id = 'local-test-message-id'
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Health event processed successfully',
                'messageId': response['MessageId']
            })
        }
        
    except Exception as e:
        print(f"Error processing health event: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

def get_bedrock_analysis(event_type, service, region, status, description):
    """Get AI analysis from Bedrock"""
    try:
        prompt = f"""
Analyze this AWS Health event and provide:
1. A brief summary (2-3 sentences)
2. Potential impact on services
3. Recommended actions

Event Details:
- Type: {event_type}
- Service: {service}
- Region: {region}
- Status: {status}
- Description: {description}

Provide a concise, actionable response.
"""
        
        response = bedrock.invoke_model(
            modelId='anthropic.claude-3-haiku-20240307-v1:0',
            body=json.dumps({
                'anthropic_version': 'bedrock-2023-05-31',
                'max_tokens': 300,
                'messages': [{
                    'role': 'user',
                    'content': prompt
                }]
            })
        )
        
        result = json.loads(response['body'].read())
        return result['content'][0]['text']
        
    except Exception as e:
        print(f"Bedrock analysis failed: {str(e)}")
        return "AI analysis unavailable"

def format_notification(event_type, service, region, status, description, ai_analysis):
    """Format the notification message with AI insights"""
    
    timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
    
    message = f"""
🚨 AWS Health Event Alert

Event Type: {event_type}
Service: {service}
Region: {region}
Status: {status}
Timestamp: {timestamp}

Description:
{description}

🤖 AI Analysis & Recommendations:
{ai_analysis}

---
This is an automated notification with AI-powered insights.
"""
    
    return message.strip()