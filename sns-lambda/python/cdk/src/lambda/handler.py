import json

def main(event, context):
    print("lambda invoked")
    print(json.dumps(event))
    return