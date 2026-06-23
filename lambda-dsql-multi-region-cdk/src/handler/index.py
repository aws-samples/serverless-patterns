"""
AWS Lambda function demonstrating Amazon Aurora DSQL multi-region active-active operations.
Connects using IAM authentication (no passwords), creates tables, writes data, and reads
across regions to demonstrate active-active replication.
"""

import json
import os
import boto3
import psycopg2


def get_auth_token(endpoint, region):
    """Generate an IAM authentication token for Amazon Aurora DSQL."""
    try:
        client = boto3.client('dsql', region_name=region)
        token = client.generate_db_connect_admin_auth_token(endpoint, region)
        return token
    except Exception as e:
        raise RuntimeError(f'Failed to generate auth token: {e}')


def get_connection(endpoint, region):
    """Create a connection to Amazon Aurora DSQL using IAM auth."""
    token = get_auth_token(endpoint, region)
    conn = psycopg2.connect(
        host=endpoint,
        port=5432,
        user='admin',
        password=token,
        dbname='postgres',
        sslmode='require',
    )
    conn.autocommit = True
    return conn


def handler(event, context):
    """Demonstrate Amazon Aurora DSQL multi-region read/write with IAM authentication."""
    try:
        endpoint = os.environ['CLUSTER_ENDPOINT']
        region = os.environ.get('CLUSTER_REGION', os.environ.get('AWS_REGION', 'us-east-1'))
        action = event.get('action', 'read')

        conn = get_connection(endpoint, region)
        cur = conn.cursor()

        if action == 'setup':
            cur.execute('''
                CREATE TABLE IF NOT EXISTS messages (
                    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
                    region TEXT NOT NULL,
                    content TEXT NOT NULL,
                    created_at TIMESTAMPTZ DEFAULT NOW()
                )
            ''')
            return {
                'statusCode': 200,
                'body': json.dumps({'action': 'setup', 'result': 'Table created'}),
            }

        elif action == 'write':
            content = event.get('content', 'Hello from Lambda')
            cur.execute(
                'INSERT INTO messages (region, content) VALUES (%s, %s) RETURNING id, created_at',
                (region, content),
            )
            row = cur.fetchone()
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'action': 'write',
                    'id': str(row[0]),
                    'region': region,
                    'created_at': str(row[1]),
                }),
            }

        elif action == 'read':
            cur.execute('SELECT id, region, content, created_at FROM messages ORDER BY created_at DESC LIMIT 10')
            rows = cur.fetchall()
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'action': 'read',
                    'count': len(rows),
                    'messages': [
                        {'id': str(r[0]), 'region': r[1], 'content': r[2], 'created_at': str(r[3])}
                        for r in rows
                    ],
                }),
            }

        else:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': f'Unknown action: {action}. Use setup, write, or read.'}),
            }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
        }
    finally:
        if 'conn' in dir() and conn:
            conn.close()
