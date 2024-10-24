import json
import boto3
import os

def handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    message = event.get('detail')

    print("From Stripe: " + str(message))

    # Get the payment intent ID from the Stripe event
    payment_intent_id = message.get('data').get('object').get('payment_intent')

    # Get the timestamp of the event
    time_stamp = message.get('created')

    # Get the customer email
    customer_email = message.get('data').get('object').get('email')
    
    # Get the payment method details
    payment_method_details = message.get('data').get('object').get('payment_method_details')

    try:
        # Send the failed payment event to DynamoDB
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table(os.environ.get('StripeFailedPayments'))
        table.put_item(
            Item={
                'payment_intent_id': payment_intent_id,
                'customer_email': customer_email,
                'payment_method': payment_method_details,
                'timestamp': time_stamp,
                'event_type': 'payment_failed'
            }
        )

        response = {
            "statusCode": 200,
            "body": f"A failed payment attempt with payment intent ID {payment_intent_id} occurred for the customer {customer_email} using {payment_method}."
        }
        print(response)
        return response

    except Exception as e:
        return {
            "statusCode": 500,
            "body": str(e)
        }