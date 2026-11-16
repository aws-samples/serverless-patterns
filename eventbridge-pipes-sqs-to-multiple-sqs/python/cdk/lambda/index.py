import json

def handler(event, context):
    records = []
    for record in event:
        records.append(json.loads(record['body']))

    return records