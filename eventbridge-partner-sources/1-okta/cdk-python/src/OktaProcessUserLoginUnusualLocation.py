import json

def handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))

    # Get the client details from the event
    client = event.get('detail').get('client')
    user_agent = client.get('userAgent').get('rawUserAgent')
    ip_address = client.get('ipAddress')
    geolocation = client.get('geographicalContext').get('geolocation')
    city = client.get('geographicalContext').get('city')
    state = client.get('geographicalContext').get('state')
    country = client.get('geographicalContext').get('country')
    postal_code = client.get('geographicalContext').get('postalCode')

    try:
        # Construct the response with the user login location details
        response = f"User logged in from {city}, {state}, {country} ({postal_code}) with IP address {ip_address} using {user_agent}"
        print(response)
        return response

    except Exception as e:
        return e