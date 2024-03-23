"""
Sample DAG module to demonstrate usage of params and XCOM
"""
from datetime import timedelta, datetime
import json
import boto3
from airflow.operators.empty import EmptyOperator
from airflow.models.param import Param
from airflow.decorators import dag, task

s3 = boto3.client('s3')

# Default arguments for the DAGs
DAG_DEFAULT_ARGS = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime.now(),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'provide_context': True,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False
}

def read_s3_input_impl(context):
    """
    Task implementation to read input.json file from S3
    """
    bucket = context['params']['s3SourceBucket']
    key = context['params']['s3SourceBucketKey']
    print(f'Reading S3 object from bucket {bucket} and key {key}')
    data = s3.get_object(Bucket=bucket, Key=key)
    input = data['Body'].read().decode('utf-8')
    inputJson = json.loads(input)
    print(inputJson)

@dag(
    dag_id="hello-world-dag",
    description="Sample DAG to demo S3 object read",
    default_args=DAG_DEFAULT_ARGS,
    dagrun_timeout=timedelta(minutes=5),
    is_paused_upon_creation=False,
    schedule=None,
    params={
        's3SourceBucket': Param(
            type='string',
            title='S3 source bucket name',
            description="S3 source bucket name for dag flow configuration file"
        ),
        's3SourceBucketKey': Param(
            type='string',
            title='S3 source bucket key',
            description="S3 source bucket key for dag flow configuration file"
        )
    },
    tags=['ServerlessLand']
)
def generate_dag():
    """
    DAG Function defining the workflow with tasks
    """
    @task(
        task_id="read-s3-input",
    )
    def read_s3_input(**context):
        """
        Task function defining operation to read flow config file from S3
        """
        return read_s3_input_impl(context)

    end = EmptyOperator(
        task_id="end",
    )

    read_s3_input() >> end

# Call dag generator function to create dag
generate_dag()
