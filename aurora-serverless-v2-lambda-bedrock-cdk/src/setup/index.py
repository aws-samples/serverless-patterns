"""Setup handler — creates the knowledge table and seeds sample data via RDS Data API."""

import json
import os
import boto3

rds_data = boto3.client("rds-data")

CLUSTER_ARN = os.environ["CLUSTER_ARN"]
SECRET_ARN = os.environ["SECRET_ARN"]
DB_NAME = os.environ["DB_NAME"]


def execute(sql, params=None):
    kwargs = {
        "resourceArn": CLUSTER_ARN,
        "secretArn": SECRET_ARN,
        "database": DB_NAME,
        "sql": sql,
    }
    if params:
        kwargs["parameters"] = params
    return rds_data.execute_statement(**kwargs)


def handler(event, _context):
    execute("""
        CREATE TABLE IF NOT EXISTS knowledge (
            id SERIAL PRIMARY KEY,
            topic TEXT NOT NULL,
            content TEXT NOT NULL
        )
    """)

    result = execute("SELECT count(*) FROM knowledge")
    count = result["records"][0][0]["longValue"]

    if count == 0:
        rows = [
            ("Aurora Serverless v2", "Aurora Serverless v2 platform version 4 delivers up to 30% better performance with enhanced scaling. It scales to zero when idle and is ideal for agentic AI workloads with burst patterns."),
            ("Lambda", "AWS Lambda supports up to 10 GB memory, 15-minute timeout, and features like durable functions, SnapStart, managed instances, and S3 Files mounting."),
            ("Bedrock", "Amazon Bedrock provides access to foundation models from Anthropic, Meta, Amazon, and OpenAI through a unified API with built-in security and governance."),
        ]
        for topic, content in rows:
            execute(
                "INSERT INTO knowledge (topic, content) VALUES (:topic, :content)",
                [
                    {"name": "topic", "value": {"stringValue": topic}},
                    {"name": "content", "value": {"stringValue": content}},
                ],
            )

    return {"statusCode": 200, "body": f"Setup complete. Rows: {count + len(rows) if count == 0 else count}"}
