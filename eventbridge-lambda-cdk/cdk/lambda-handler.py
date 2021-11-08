import json

def main(event, context):
    print("invoked")
    print(json.dumps(event))
    return