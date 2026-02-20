import json, boto3, os, uuid

# Initialize clients
agent_core_client = boto3.client('bedrock-agentcore')
s3_client = boto3.client('s3')

def preparePayload(event: dict) -> str:
    bucket = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    prompt = f"Categorize and identify metadata for this file: s3://{bucket}/{object_key}"
    payload = json.dumps({"prompt": prompt})
    return payload

def lambda_handler(event,context):
    print('### event ###)')
    print(event)
    
    # Get input file details
    bucket = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    output_bucket = os.environ.get('OUTPUT_BUCKET')
    
    agent_arn = os.environ.get('AGENT_ARN')
    print('### agent_arn ###)')
    print(agent_arn)
    payload = preparePayload(event)
    print('### payload ###)')
    print(payload)
    session_id = str(uuid.uuid4())
    print('### session_id ###)')
    print(session_id)
  
    # Invoke the agent
    response = agent_core_client.invoke_agent_runtime(
        agentRuntimeArn=agent_arn,
        runtimeSessionId=session_id,
        payload=payload
    )
    
    # Process the response
    raw_response = ""
    if "text/event-stream" in response.get("contentType", ""):
        # Handle streaming response
        content = []
        for line in response["response"].iter_lines(chunk_size=10):
            if line:
                line = line.decode("utf-8")
                if line.startswith("data: "):
                    line = line[6:]
                    print(line)
                    content.append(line)
        raw_response = "\n".join(content)
        print("\nComplete response:", raw_response)

    elif response.get("contentType") == "application/json":
        # Handle standard JSON response
        content = []
        for chunk in response.get("response", []):
            content.append(chunk.decode('utf-8'))
        raw_response = ''.join(content)
        print(raw_response)
    
    else:
        # Handle raw response
        raw_response = str(response)
        print(response)
    
    # Extract JSON from markdown code fences if present
    if "```json" in raw_response:
        start = raw_response.find("```json") + 7
        end = raw_response.find("```", start)
        json_str = raw_response[start:end].strip()
        result = json.loads(json_str)
    elif "```" in raw_response:
        start = raw_response.find("```") + 3
        end = raw_response.find("```", start)
        json_str = raw_response[start:end].strip()
        try:
            result = json.loads(json_str)
        except:
            result = {"response": raw_response}
    else:
        try:
            result = json.loads(raw_response)
        except:
            result = {"response": raw_response}

    # Save result to output bucket
    output_key = f"{object_key}.json"
    s3_client.put_object(
        Bucket=output_bucket,
        Key=output_key,
        Body=json.dumps(result, indent=2),
        ContentType='application/json'
    )
    print(f"Saved result to s3://{output_bucket}/{output_key}")
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'input': f"s3://{bucket}/{object_key}",
            'output': f"s3://{output_bucket}/{output_key}"
        })
    }