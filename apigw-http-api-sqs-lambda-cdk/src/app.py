
def handler(event, context):
    for record in event['Records']:
        payload = record["body"]
        print(str(payload))