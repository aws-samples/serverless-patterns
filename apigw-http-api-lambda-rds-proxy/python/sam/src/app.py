import json
import boto3
from os import environ

import pymysql


client = boto3.client('rds')  # get the rds object


def create_proxy_connection_token(username):
    # get the required parameters to create a token
    region = environ.get('region')  # get the region
    hostname = environ.get('rds_endpoint')  # get the rds proxy endpoint
    port = environ.get('port')  # get the database port

    # generate the authentication token -- temporary password
    token = client.generate_db_auth_token(
        DBHostname=hostname,
        Port=port,
        DBUsername=username,
        Region=region
    )

    return token


def db_ops():
    username = environ.get('username')

    token = create_proxy_connection_token(username)

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
    except pymysql.MySQLError as e:
        print(e)
        return e

    return connection


def lambda_handler(event, context):
    conn = db_ops()
    cursor = conn.cursor()
    query = "select curdate() from dual"
    cursor.execute(query)
    results = cursor.fetchmany(1)

    return {
        'statusCode': 200,
        'body': json.dumps(results, default=str)
    }
