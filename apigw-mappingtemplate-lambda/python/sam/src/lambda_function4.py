import json

def lambda_handler(event, context):
  print(event)
  return {
    "statuscode":200,
    "body": "error1"
  }