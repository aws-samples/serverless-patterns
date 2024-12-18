import json
import urllib3
from urllib3.util import Retry


def lambda_handler(event, context):
    http = urllib3.PoolManager(
        retries=Retry(3, backoff_factor=0.5)
    )
    response = http.request(
        'GET',
        'http://api.open-notify.org/iss-now.json',
        timeout=10.0
    )
    iss_data = json.loads(response.data.decode('utf-8'))
    responseBody =  {
        "TEXT": {
            "body":  f"The ISS is currently at latitude {iss_data["iss_position"]['latitude']} and longitude {iss_data["iss_position"]['longitude']}"
            }
    }

    action_response = {
        'actionGroup': event['actionGroup'],
        'function': event['function'],
        'functionResponse': {
            'responseBody': responseBody
        }
    }
    function_response = {'response': action_response, 'messageVersion': event['messageVersion']}
    print("Response: {}".format(function_response))

    return function_response
