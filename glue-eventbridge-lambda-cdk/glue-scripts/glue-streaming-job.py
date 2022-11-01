import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.types import StructType, StructField, StringType

args = getResolvedOptions(sys.argv, [
    "JOB_NAME",
    "bucket_name"
])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

s3_bucket = "s3://"+args["bucket_name"]

def createSchema():
    return StructType() \
        .add("name", StringType()) \
        .add("location", StringType()) \
        .add("age", StringType()) \
        .add("year", StringType())

def processBatch(data_frame, batchId):
    print(data_frame.count())
    if (data_frame.count() > 0):
        collects = data_frame.collect()
        for row in collects:
            print(row)
        
def main():
    dataframe = spark \
        .readStream \
        .schema(createSchema()) \
        .csv(s3_bucket + "/glue-python-scripts/sample_test/") \
        .writeStream.foreachBatch(processBatch).start().awaitTermination()

if __name__ == '__main__':
    print("init job")
    main()