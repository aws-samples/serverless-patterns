# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import json
import boto3
from os import environ
import logging

import sys
sys.path.insert(0, 'package/')
import pymysql


client = boto3.client('rds')  

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def generate_connection_token(username):
    # get the required parameters to create a token
    logging.info('## Loading environment variables to generate auth token')
    region = environ.get('region')  # get the region
    proxy_endpoint = environ.get('rds_endpoint')  # get the rds proxy endpoint
    port = environ.get('port')  # get the database port
    variables = {'region':region, 'proxy_endpoint':proxy_endpoint, 'port':port}
    logging.info(json.dumps(variables))
    
    token = client.generate_db_auth_token(
        DBHostname=proxy_endpoint,
        Port=port,
        DBUsername=username,
        Region=region
    )
    logging.info('## Generated database auth token')
    return token


def get_connector():
    username = environ.get('username')

    token = generate_connection_token(username)

    try:
        # create a connection object
        connection = pymysql.connect(
            host=environ.get('rds_endpoint'),
            # getting the rds proxy endpoint from the environment variables
            user=username,
            password=token,
            db=environ.get('database'),
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            ssl={"use": True}
        )
        logging.info('## Established a connection to the proxy endpoint')
    except pymysql.MySQLError as e:
        logging.info('Encountered error: {}'.format(e))
        return e

    return connection


def lambda_handler(event, context):
    conn = get_connector()
    cursor = conn.cursor()
    query = "select session_user()"
    cursor.execute(query)
    results = cursor.fetchmany(1)
    logging.info(f"## Executed query using proxy endpoint, results = {results}")
    response = {
        "status":"Success",
        'message': "Information retrieved",
        "results": results
    }

    return {
        'statusCode': 200,
        "headers": {
                "Content-Type": "application/json"
            },
        'body': json.dumps(response, default=str)
    }