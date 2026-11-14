import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.gluetypes import *
from awsglue import DynamicFrame

def _find_null_fields(ctx, schema, path, output, nullStringSet, nullIntegerSet, frame):
    if isinstance(schema, StructType):
        for field in schema:
            new_path = path + "." if path != "" else path
            output = _find_null_fields(ctx, field.dataType, new_path + field.name, output, nullStringSet, nullIntegerSet, frame)
    elif isinstance(schema, ArrayType):
        if isinstance(schema.elementType, StructType):
            output = _find_null_fields(ctx, schema.elementType, path, output, nullStringSet, nullIntegerSet, frame)
    elif isinstance(schema, NullType):
        output.append(path)
    else:
        x, distinct_set = frame.toDF(), set()
        for i in x.select(path).distinct().collect():
            distinct_ = i[path.split(".")[-1]]
            if isinstance(distinct_, list):
                distinct_set |= set([item.strip() if isinstance(item, str) else item for item in distinct_])
            elif isinstance(distinct_, str) :
                distinct_set.add(distinct_.strip())
            else:
                distinct_set.add(distinct_)
        if isinstance(schema, StringType):
            if distinct_set.issubset(nullStringSet):
                output.append(path)
        elif isinstance(schema, IntegerType) or isinstance(schema, LongType) or isinstance(schema, DoubleType):
            if distinct_set.issubset(nullIntegerSet):
                output.append(path)
    return output

def drop_nulls(glueContext, frame, nullStringSet, nullIntegerSet, transformation_ctx) -> DynamicFrame:
    nullColumns = _find_null_fields(frame.glue_ctx, frame.schema(), "", [], nullStringSet, nullIntegerSet, frame)
    return DropFields.apply(frame=frame, paths=nullColumns, transformation_ctx=transformation_ctx)

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'input_bucket', 'output_bucket'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Amazon S3
AmazonS3_node1717754154437 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": [f"s3://{args['input_bucket']}"], "recurse": True}, transformation_ctx="AmazonS3_node1717754154437")

# Script generated for node Drop Null Fields
DropNullFields_node1717754572606 = drop_nulls(glueContext, frame=AmazonS3_node1717754154437, nullStringSet={"", "null"}, nullIntegerSet={}, transformation_ctx="DropNullFields_node1717754572606")

# Script generated for node Amazon S3
AmazonS3_node1717754793354 = glueContext.getSink(path=f"s3://{args['output_bucket']}", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="AmazonS3_node1717754793354")
AmazonS3_node1717754793354.setCatalogInfo(catalogDatabase="s3_eventbridge_glue_db",catalogTableName="processed_data")
AmazonS3_node1717754793354.setFormat("glueparquet", compression="snappy")
AmazonS3_node1717754793354.writeFrame(DropNullFields_node1717754572606)
job.commit()