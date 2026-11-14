#! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: MIT-0
#
from boto3.session import Session 
import os
import json

session = Session()  
rds_data = session.client(
    service_name='rds-data'
)

DBClusterArn = os.environ['DBClusterArn']
DBName = os.environ['DBName']
SecretArn = os.environ['SecretArn']

def run_command(sql_statement, sql_values=None):
    print(f"SQL statement: {sql_statement}")
    result = ''
    
    if not sql_values:
        #Use the Data API ExecuteStatement operation to run the SQL command
        result = rds_data.execute_statement(
            resourceArn=DBClusterArn,
            secretArn=SecretArn,
            database=DBName,
            sql=sql_statement
        )
    else:    
        result = rds_data.execute_statement(
            resourceArn=DBClusterArn,
            secretArn=SecretArn,
            database=DBName,
            sql=sql_statement,
            includeResultMetadata=True,
            parameters=[
                {
                    'name':'artist', 
                    'value':{'stringValue':sql_values['artist']}
                },
                {
                    'name':'album',
                    'value':{'stringValue':sql_values['album']}
                }
            ] 
        )

    #print(f"SQL Result: {result}")
    return result

def lambda_handler(event, context):
    try:
        #Log event object and database name to CloudWatch Logs
        print(f"Event: {event}")
        print(f"Database Name: {DBName}")

        #Get data from test event
        if event['body']:
            body = event['body']
            artist = body['artist']
            album = body['album']
            
    except Exception as e:
         #Use default data if test event is not configured properly
        artist = "The Beatles"
        album = "Abbey Road"
        print(f"Error: {e}")

    sql_create = "CREATE TABLE IF NOT EXISTS music (id SERIAL PRIMARY KEY, artist VARCHAR(128), album VARCHAR(128));" 
    sql_insert = "INSERT INTO music (artist, album) VALUES (:artist, :album);"
    sql_select = "SELECT id, artist, album FROM music WHERE artist=:artist and album=:album;"
    sql_values = {'artist': artist, 'album': album}

    #Run the SQL commands one at a time
    run_command(sql_create)
    run_command(sql_insert, sql_values)
    result = run_command(sql_select, sql_values)
    
    #get column names
    meta = []
    for column in result['columnMetadata']:
        meta.append(column['name'])

    #get records data, linked to column names
    data = []
    for record in result['records']:
        data.append({
            meta[0]: record[0]['longValue'],
            meta[1]: record[1]['stringValue'],
            meta[2]: record[2]['stringValue']
        })

    return {
        "statusCode": 200,
        "body": json.dumps(data),
    }




    

  
