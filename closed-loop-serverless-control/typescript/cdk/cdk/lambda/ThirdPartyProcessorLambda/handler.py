import time
import random
import boto3
cloudwatch = boto3.client('cloudwatch')
def handler(event, context):
    incoming_event = event['detail']

    if "simulated_response" in incoming_event:
        wait_ms = incoming_event["simulated_response"]["response_time"]*random.randrange(900, 1100)/1000 # wait for input response time ± 10%
        status_code = incoming_event["simulated_response"]["status_code"]
    else:
        wait_ms = 100*random.randrange(900, 1100)/1000 # default: wait for 100ms ± 10%
        status_code = 200 # default: HTTP 200 OK

    time.sleep(wait_ms/1000)

    cloudwatch.put_metric_data(
        MetricData = [
            { 
                'MetricName': 'APIResponseTime',
                'Dimensions': [
                    {
                        'Name': 'Function',
                        'Value': 'ThirdPartyProcessor'
                    }
                ],
                'Unit': 'Milliseconds',
                'Value': wait_ms
            },
            {
                'MetricName': 'APIResponseCode',
                'Dimensions': [
                    {
                        'Name': 'StatusCode',
                        'Value': str(status_code)
                    },
                    {
                        'Name': 'Function',
                        'Value': 'ThirdPartyProcessor'
                    }
                ],
                'Unit': 'Count',
                'Value': 1
            },

        ],
        Namespace='ThirdPartyCalls'
    )

    print("Function finished, APIResponseTime: {}, StatusCode: {}".format(wait_ms, status_code))

    return True