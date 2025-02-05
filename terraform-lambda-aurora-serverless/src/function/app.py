# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import os
import json
import pymysql
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # Get database connection info from environment variables
    host = os.environ['DB_ENDPOINT']
    database = os.environ['DB_NAME']
    username = os.environ['DB_USERNAME']
    password = os.environ['DB_PASSWORD']
    
    try:
        # Attempt database connection
        conn = pymysql.connect(
            host=host,
            user=username,
            password=password,
            database=database,
            connect_timeout=5
        )
        
        # Execute simple test query
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
        
        conn.close()
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Successfully connected to the database',
                'database': database,
                'host': host
            })
        }
        
    except Exception as e:
        logger.error(f"Database connection failed: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Failed to connect to database',
                'error': str(e)
            })
        }
