# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import boto3
dynamodb_client = boto3.client('dynamodb')

def lambda_handler(event, context):
  dynamodb_client.put_item(TableName='WeatherData', Item={'id': {'S': '1'}, 'Weather': {'S': 'Sunny'}})
  return {
      'statusCode': 200,
      'body': 'Successfully inserted data!'
  }
