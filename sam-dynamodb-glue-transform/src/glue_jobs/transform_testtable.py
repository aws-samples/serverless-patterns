import sys
from awsglue.transforms import *
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from awsglue.dynamicframe import DynamicFrame
from awsglue.dynamicframe import DynamicFrameCollection
from pyspark.sql import SparkSession
from awsglue.transforms import DropNullFields
import pyspark.sql.functions as f

spark = SparkSession.builder.getOrCreate()
args = getResolvedOptions(sys.argv, ["JOB_NAME", "BUCKET_NAME", "SOURCE_TABLE_ARN"])
glueContext = GlueContext(SparkContext.getOrCreate())
job = Job(glueContext)
job.init(args["JOB_NAME"], args)
bucket_name = args["BUCKET_NAME"]
source_table_arn = args["SOURCE_TABLE_ARN"]

config = {
    "sourceTableARN": source_table_arn,
    "targetTableName": "TestTable",
    # below s3 bucket should be present
    "s3BucketName": bucket_name,
    # if below key path does not exist it will be created automatically given bucket exists
    "s3KeyName": "temporary/ddbexport/table/testtable"
}

# Script generated for node Custom Transform
def MyTransform(glueContext, dfc) -> DynamicFrameCollection:
    selected_dynf = dfc.select(list(dfc.keys())[0])
    selected_df = selected_dynf.toDF()
    print("Original DataFrame")
    selected_df.show(n=5, vertical=True, truncate=False)

    # example transformations

    # Add new attribute "fullName" using the existing firstName and lastName values for each item
    selected_df = selected_df.withColumn(
        "fullName", f.when(
            (f.col("firstName").isNotNull() & f.col("lastName").isNotNull()),
            f.concat_ws(" ", f.col("firstName"), f.col("lastName")),
        )
    )

    # Renaming the column "birthday" to "dateOfBirth" for each item
    selected_df = selected_df.withColumn(
        "dateOfBirth", f.when(
            f.col("birthday").isNotNull(),
            f.col("birthday")
        )
    )
  
    selected_df = selected_df.drop(f.col("birthday")) # dropping because new renamed column was created

    modified_dynf = DynamicFrame.fromDF(selected_df, glueContext, "modified_dynf")
    modified_dynf = DropNullFields.apply(modified_dynf)

    print("Modified DataFrame")
    modified_dynf.toDF().show(n=5, vertical=True, truncate=False)
    return modified_dynf

source = glueContext.create_dynamic_frame.from_options(
    connection_type="dynamodb",
    connection_options={
        "dynamodb.export": "ddb",
        "dynamodb.s3.bucket": config["s3BucketName"],
        "dynamodb.s3.prefix": config["s3KeyName"],
        "dynamodb.tableArn": config["sourceTableARN"],
        "dynamodb.unnestDDBJson": True,
    },
    transformation_ctx="source",
)
source.printSchema()

df = source.toDF()
df.show()

# Script generated for node Custom Transform
transformation0 = MyTransform(
    glueContext,
    DynamicFrameCollection({"source": source}, glueContext),
)

glueContext.write_dynamic_frame_from_options(
    frame=transformation0,
    connection_type="dynamodb",
    connection_options={
        "dynamodb.output.tableName": config["targetTableName"],
        "dynamodb.output.retry": "50",
        "dynamodb.throughput.write.percent": "1.0"
    }
)

job.commit()