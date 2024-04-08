# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import boto3
import json
dynamodb_client = boto3.resource('dynamodb')

def lambda_handler(event, context):
  table = dynamodb_client.Table('Transaction')
  print(event)
  item = json.loads(event['body'])
  print(item)
  table.put_item(
        Item={
          'id': item['id'],
          'name': item['name'],
          'description': item['description'],
          'customer': item['customer']
          }
        )
  return {
      'statusCode': 200,
      'body': 'Successfully inserted data!'
  }
