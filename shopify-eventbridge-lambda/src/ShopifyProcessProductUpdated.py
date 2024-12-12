import json

def handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))

    # Get the product details from the event
    product = event.get('detail').get('payload').get('product')
    product_id = product.get('id')
    product_title = product.get('title')
    product_vendor = product.get('vendor')
    product_type = product.get('product_type')
    product_handle = product.get('handle')

    try:
        # You can perform any additional processing or send the product details to other services here
        response = f"Product " + product_title + " " + product_type + " by " + product_vendor + " with handle " + product_handle + " has been updated."
        print(response)
        return response

    except Exception as e:
        return e