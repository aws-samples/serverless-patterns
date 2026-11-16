def lambda_handler(event, context):
    print("AWS Lambda is triggered by the AWS Step Function")
    return {"status": "Success"}
