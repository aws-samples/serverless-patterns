import json
import boto3, random
from datetime import datetime

client = boto3.client('events')

# Multiple EventBridge Buses to different SNS Topics same account pattern.

# Based on the following setup:
# All banks have their Event Buses. All bank transactions (ATM/Bank branch) emit events which must all be piped through a clearing house (EventBridge).
# All cross-border transactions from all banks must be sent to the Reserve/Central bank for BOP (Balance of Payment) reporting.
# Regardless of a transactions "BOP status", a copy of all transactons must go to their respective Banks' SNS Topic.

def lambda_handler(event, context):
    # Setup Entries values for put event
    reportable_value = str(random.choice(["Yes", "No"]))
    choice_bus = str(random.choice(["bus_a", "bus_b","bus_c"]))
    source = str(random.choice(["atm.events", "bankbranch.events"]))
    t_datetime = datetime.today().strftime('%m/%d/%Y, %H:%M:%S')

    response = client.put_events(
    Entries=[
        {       "Source": source,
                "DetailType": "Bank transaction",
                "Time": datetime.today().strftime('%Y-%m-%d'),
                "Detail": "{ \"transaction_value\": \"1,800\", \"date\": \""+t_datetime+"\",  \"customer_name\": \"John Smith\", \"bop_reportable\": \""+reportable_value+"\" }",
            "EventBusName": choice_bus,
            "TraceHeader": "atmORbanklocation"
        },
    ],
)
    #Use values to confirm delivery to respective SNS Topics
    print ('API response: ', response)
    print ('Current Bus: ', choice_bus)
    print ('Current source: ', source)
    print ('Is transaction resportable: ', reportable_value)

    return {
        'statusCode': 200,
        'body': json.dumps('Event Unterwegs!')
    }
