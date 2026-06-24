"""Query handler — searches Aurora via Data API, sends context to Bedrock for answer."""

import json
import os
import boto3

rds_data = boto3.client("rds-data")
bedrock = boto3.client("bedrock-runtime")

CLUSTER_ARN = os.environ["CLUSTER_ARN"]
SECRET_ARN = os.environ["SECRET_ARN"]
DB_NAME = os.environ["DB_NAME"]


def handler(event, _context):
    question = event.get("question", "What is Aurora Serverless v2?")
    stop_words = {"what", "is", "the", "a", "an", "how", "does", "do", "can", "tell", "me", "about"}
    keywords = [w for w in question.split() if w.lower().strip("?.,!") not in stop_words]
    search_term = keywords[0] if keywords else "Aurora"

    # Query Aurora for relevant knowledge via Data API
    result = rds_data.execute_statement(
        resourceArn=CLUSTER_ARN,
        secretArn=SECRET_ARN,
        database=DB_NAME,
        sql="SELECT topic, content FROM knowledge WHERE content ILIKE :term OR topic ILIKE :term LIMIT 3",
        parameters=[{"name": "term", "value": {"stringValue": f"%{search_term}%"}}],
    )

    rows = result.get("records", [])
    context = "\n".join(
        f"[{r[0]['stringValue']}]: {r[1]['stringValue']}" for r in rows
    ) if rows else "No context found."

    # Send context + question to Bedrock
    response = bedrock.invoke_model(
        modelId=os.environ["MODEL_ID"],
        contentType="application/json",
        accept="application/json",
        body=json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 512,
            "messages": [
                {
                    "role": "user",
                    "content": f"Context from database:\n{context}\n\nQuestion: {question}\n\nAnswer based on the context above.",
                }
            ],
        }),
    )
    answer = json.loads(response["body"].read())["content"][0]["text"]

    return {"statusCode": 200, "body": json.dumps({"question": question, "answer": answer, "sources": len(rows)})}
