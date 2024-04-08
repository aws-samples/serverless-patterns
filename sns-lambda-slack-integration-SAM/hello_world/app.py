import json
import urllib3
http = urllib3.PoolManager()


def lambda_handler(event, context):
    print(event)

    # Enter slack URL below.
    url = 'https://hooks.slack.com/workflows/{your webhook url}'
    msg = {
        'channel': '#sns-topic-slack-integration',
        'Message': event['Records'][0]['Sns']['Message'],
        # 'Message': 'SAM - Hello',
        # 'Subject' : 'SAM ',
        'Subject' : event['Records'][0]['Sns']['Subject'],
        'icon_emoji': '',
        }

    encoded_msg = json.dumps(msg).encode('utf-8')
    resp = http.request('POST', url, body=encoded_msg)
    print(resp)
    print({
        # "message": event["Records"][0]["Sns"]["Message"],
        "message" : 'Hello',
        "status_code": 'status',
        "response": 'data',
        "status_code": resp.status,
        "response": resp.data,
        })