"""
Amazon S3 Annotations enrichment handler.
Triggered by Amazon S3 Object Created events via Amazon EventBridge.
Reads the object, generates AI summary via Amazon Bedrock, writes annotation.
"""
import json
import boto3
import os

s3 = boto3.client('s3')
bedrock = boto3.client('bedrock-runtime')

MODEL_ID = 'us.anthropic.claude-sonnet-4-20250514-v1:0'
MAX_CONTENT_BYTES = 10_000  # Limit content sent to Bedrock


def handler(event, context):
    detail = event['detail']
    bucket = detail['bucket']['name']
    key = detail['object']['key']
    size = detail['object'].get('size', 0)

    # Skip non-text files and very large files
    if size > 5_000_000 or not _is_supported(key):
        print(f'Skipping {key} (size={size}, unsupported type)')
        return {'status': 'skipped', 'key': key}

    try:
        # Read object content
        response = s3.get_object(Bucket=bucket, Key=key)
        content = response['Body'].read(MAX_CONTENT_BYTES).decode('utf-8', errors='replace')

        # Generate summary via Amazon Bedrock
        summary = _generate_summary(key, content)

        # Write annotation
        annotation_payload = json.dumps({
            'ai_summary': summary['summary'],
            'keywords': summary['keywords'],
            'content_type': summary['content_type'],
            'model': MODEL_ID,
        })

        s3.put_object_annotation(
            Bucket=bucket,
            Key=key,
            AnnotationName='ai-enrichment',
            AnnotationPayload=annotation_payload.encode('utf-8'),
        )

        print(f'Annotated {key} with {len(annotation_payload)} bytes')
        return {'status': 'annotated', 'key': key, 'annotation_size': len(annotation_payload)}

    except Exception as e:
        print(f'Error processing {key}: {e}')
        raise


def _generate_summary(key, content):
    prompt = f"""Analyze this document and return a JSON object with:
- "summary": a 2-3 sentence summary
- "keywords": up to 5 relevant keywords as an array
- "content_type": the type of content (e.g. "report", "code", "article", "data", "log")

Filename: {key}
Content (first {MAX_CONTENT_BYTES} bytes):
{content}

Respond ONLY with valid JSON."""

    response = bedrock.invoke_model(
        modelId=MODEL_ID,
        contentType='application/json',
        accept='application/json',
        body=json.dumps({
            'anthropic_version': 'bedrock-2023-05-31',
            'max_tokens': 300,
            'messages': [{'role': 'user', 'content': prompt}],
        }),
    )

    result = json.loads(response['body'].read())
    text = result['content'][0]['text']

    # Parse JSON from response
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        # Fallback if model wraps in markdown
        import re
        match = re.search(r'\{.*\}', text, re.DOTALL)
        if match:
            return json.loads(match.group())
        return {'summary': text[:200], 'keywords': [], 'content_type': 'unknown'}


def _is_supported(key):
    supported = ('.txt', '.md', '.json', '.csv', '.xml', '.yaml', '.yml',
                 '.py', '.js', '.ts', '.java', '.html', '.log')
    return any(key.lower().endswith(ext) for ext in supported)
