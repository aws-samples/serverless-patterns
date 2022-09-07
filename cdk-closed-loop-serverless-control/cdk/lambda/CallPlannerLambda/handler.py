import json
from datetime import datetime
import boto3

def handler(event, context):
    print(json.dumps(event))
    cw_client = boto3.client('cloudwatch')
    eb_client = boto3.client('events')

    cw_response = cw_client.describe_alarms(
        AlarmNames=['ThirdPartyCallStatus'],
        StateValue='ALARM',
        AlarmTypes=["CompositeAlarm"]
    )
    
    if len(cw_response['CompositeAlarms'])>0:
        return {"status": "ThirdPartyCallStatus is on ALARM, skipping the EventBridge put"}

    else:
        response = eb_client.put_events(
                Entries=[
                    {
                        'Time': datetime.now(),
                        'Source': "thirdPartyCalls",
                        'Detail': json.dumps(event),
                        'DetailType': "Planned third party call event",
                    }
                ]
            )

        if response['FailedEntryCount'] == 0:
            return {"status": "Message put to EventBridge", "event":event}
        else:
            return {"status": "Message put failed to EventBridge", "event":event, "response": response}

