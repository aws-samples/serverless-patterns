import json

def handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))

    # Get the product details from the event
    event_data = event.get('detail').get('key')
    account = event.get('account')
    time  = event.get('time')
    detail_type = event.get('detail-type')

    try:
        # You can perform any additional processing or send the order events to other services here!
        response = f"At " + time + " in account " + account + " the " + detail_type + " event is " + event_data
        print(response)
        return response

    except Exception as e:
        return e