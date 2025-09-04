#############################################
# This script will be used by Glue for zero
# ETL copy of data from DynamoDB to S3.
#############################################

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'source-table', 'target-bucket'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read data from DynamoDB
datasource = glueContext.create_dynamic_frame.from_options(
    connection_type="dynamodb",
    connection_options={
        "dynamodb.input.tableName": args['source_table'],
        "dynamodb.throughput.read.percent": "0.5"
    }
)

# Write data to S3 in the specified format
glueContext.write_dynamic_frame.from_options(
    frame=datasource,
    connection_type="s3",
    connection_options={
        "path": f"s3://{args['target_bucket']}/data/"
    },
    format="parquet"
)

job.commit()
