import boto3
import os
import json

s3_client = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")
sfn = boto3.client('stepfunctions')
ddbtable = os.environ['TableName']
print("Table name :", ddbtable)
table = dynamodb.Table(ddbtable)

def lambda_handler(event, context):
   
    parsed_data = json.loads(json.dumps(event))

    # Extract bucket name and key
    bucket_name =  parsed_data["data"]["detail"]["bucket"]["name"]
    s3_file_name =  parsed_data["data"]["detail"]["object"]["key"]
    resp = s3_client.get_object(Bucket=bucket_name,Key=s3_file_name)
    data = resp['Body'].read().decode("utf-8")
    
    # Below code is customized as per the provided example csv Kindly customize it as per your requirement.
    Students = data.split("\n")
    for friend in Students:
        print(friend)
        friend_data = friend.split(",")
        # add to dynamodb
        try:
            put = table.put_item(
                Item = {
                    "transaction_id": friend_data[0],
                    "N": friend_data[1],
                    "S": friend_data[2] 
                }
            )
            print("Response: ", put)
        except Exception as e:
            print("End of file", e)
            
    output = {"outcome":"success"}
    output_str = json.dumps(output)
    response = sfn.send_task_success(
    taskToken=event['token'],
    output=  output_str
    )
    
    return {
        "statusCode": 200,
        "body":"uploaded successfully"
    }
