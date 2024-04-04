import os
from enum import Enum


def getTransformationByName(name):
    if name == 'transform_testtable':
        return TransformationType['transform_testtable'].value
    
    #if another transformation needs to be added, add an additional entry for it here, liek the sample below
    elif name == 'ADDITIONAL_SAMPLE_TRANSFORM':
        return TransformationType['ADDITIONAL_SAMPLE_TRANSFORM'].value

class Transformations:
    def __init__(self, source_table_arn, transformation_name, s3_bucket_name):
        self.source_table_arn = source_table_arn
        self.transformation_name = transformation_name
        self.s3_bucket_name = s3_bucket_name

    def getSourceTableArn(self):
        return self.source_table_arn

    def getTransformationName(self):
        return self.transformation_name

    def getS3BucketName(self):
        return self.s3_bucket_name


class TransformationType(Enum):
    transform_testtable = Transformations(
        f"arn:aws:dynamodb:{os.getenv('AWS_DEFAULT_REGION')}:{os.getenv('ACCOUNT')}:table/TestTable",
        "transform_testtable",
        f"testtable-aws-glue-assets-{os.getenv('ACCOUNT')}-{os.getenv('AWS_DEFAULT_REGION')}"
    )

    # if another transformation needs to be added, add the required data here

    ADDITIONAL_SAMPLE_TRANSFORM = Transformations(
        f"arn:aws:dynamodb:{os.getenv('AWS_DEFAULT_REGION')}:{os.getenv('ACCOUNT')}:table/<insert-table-name>", # table ARN where transformations will be done
        "script_name", # script/transformation name, this script should be found under the glue_jobs folder
        f"<insert-table-name>-aws-glue-assets-{os.getenv('ACCOUNT')}-{os.getenv('AWS_DEFAULT_REGION')}" # glue assets s3 bucket for the table
    )