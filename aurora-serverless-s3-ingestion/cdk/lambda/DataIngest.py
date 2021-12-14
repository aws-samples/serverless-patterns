import csv
import os
import time
import tempfile
import boto3
from csv import reader
from botocore.exceptions import ClientError

rdsdata = boto3.client('rds-data')
s3 = boto3.client('s3')
my_resource_arn = os.environ.get('CLUSTER_ARN')
my_secret_arn = os.environ.get('SECRET_ARN')
my_database = 'mydatabase'

def insert_rows(values):
    sql_stm = f"""insert into movies values {values}"""
    return(sql_stm)

def create_table():
    response = rdsdata.execute_statement (
    resourceArn = my_resource_arn,
    secretArn = my_secret_arn,
    database = my_database,
    sql = 'Create table IF NOT EXISTS movies (Year int(4),Length int(5),Title varchar(150),Subject varchar(250),Actor varchar(150),Actress varchar(150),Director varchar(150),Popularity int(5),Awards varchar(150),Image varchar(250))'
    )

def wake_aurora():
    delay = 5
    max_attempts = 10

    attempt = 0
    while attempt < max_attempts:
        attempt += 1
        try:
            wake = rdsdata.execute_statement (
                resourceArn = my_resource_arn,
                secretArn = my_secret_arn,
                database = my_database,
                sql = 'select 1'
            )
            return
        except ClientError as ce:
            error_code = ce.response.get("Error").get('Code')
            error_msg = ce.response.get("Error").get('Message')
                # Aurora serverless is waking up
            if error_code == 'BadRequestException' and 'Communications link failure' in error_msg:
                time.sleep(delay)
            else:
                raise ce

        raise Exception('Waited for Aurora Serveless but still got errors')

def lambda_handler(event, context):
    
    wake_aurora()
    
    create_table()

    for record in event['Records']:
        source_bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        with tempfile.TemporaryDirectory() as tmpdir:
            download_path = os.path.join(tmpdir, key)
            s3.download_file(source_bucket, key, download_path)
            # items = read_csv(download_path)
            with open(download_path, 'r') as read_obj:
                # pass the file object to reader() to get the reader object
                csv_reader = reader(read_obj)
                # Iterate over each row in the csv using reader object
                next(csv_reader)
                for row in csv_reader:
                    counter = 0
                    for i in row:
                        if i == '':
                            # Transform null values into 0
                            row[counter] = 0
                        counter += 1
                    values = tuple(row)
                    sql_stm = insert_rows(values)
                    response2 = rdsdata.execute_statement (
                        resourceArn = my_resource_arn,
                        secretArn = my_secret_arn,
                        database = my_database,
                        sql = sql_stm
                        )

