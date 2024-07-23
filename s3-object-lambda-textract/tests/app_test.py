import boto3

import sys

# Read Bucket arn from command line argument
bucket_arn = sys.argv[1]
print (bucket_arn)
s3 = boto3.client('s3')
print('Object processed by S3 Object Lambda:')
transformed = s3.get_object(
  Bucket=bucket_arn,
  Key='Drivers_License.pdf')
print(transformed['Body'].read().decode('utf-8'))