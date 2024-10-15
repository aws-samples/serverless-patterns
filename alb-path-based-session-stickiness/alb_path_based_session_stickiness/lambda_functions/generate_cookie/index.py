import json
import re
import requests
import datetime
def lambda_handler(event, context):
    """
    Lambda function handler to generate and set a cookie based on the requested path.
    This function also proxies the request to the target URL.

    :param event: AWS Lambda uses this parameter to pass in event data to the handler.
    :param context: AWS Lambda uses this parameter to provide runtime information to your handler.
    :return: The response from the proxied request, including the Set-Cookie header.
    """
    print(event)
    # Return 200 for ELB health checks
    if event.get('headers', {}).get('user-agent') == 'ELB-HealthChecker/2.0':
        return {'statusCode': 200}
    try:
        # Extract the request path
        path = event.get('path', '')

        # Construct the target URL for the proxied request
        headers = event.get('headers', {})
        url = f"{headers.get('x-forwarded-proto', 'https')}://{headers.get('host')}{path}"
        
        # Create cookie with the path
        cookie = f'AWSALBAPP={path}'
        
        # Prepare headers for the proxied request, including the cookie and tracing ID
        proxy_headers = {
            'Cookie': cookie,
            'X-Amzn-Trace-Id': headers.get('x-amzn-trace-id', '')
        }
        
        # Extract method and body from the original request for proxying
        method = event.get('httpMethod', 'GET')
        body = event.get('body', '')
        try:
            response = requests.request(method, url, headers=proxy_headers, data=body, timeout=1)
            response.raise_for_status()  # This will raise an exception for 4xx and 5xx status codes
            
            # Prepare the response
            response_headers = dict(response.headers)
            expiration = (datetime.datetime.now() + datetime.timedelta(minutes=30)).strftime('%a, %d %b %Y %H:%M:%S GMT')
            response_headers['Set-Cookie'] = f'{cookie}; Secure; SameSite=None; Expires={expiration};'

            
            return {
                'statusCode': response.status_code,
                'headers': response_headers,
                'body': f"FROM LAMBDA: {response.text}"
            }
        except requests.exceptions.Timeout:
            return {
                'statusCode': 200,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'message': 'The endpoint did not respond within 1 second.'})
            }
        except requests.exceptions.RequestException as e:
            # Handle other request exceptions
            return {
                'statusCode': 500,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'error': f'Request failed: {str(e)}'})
            }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }
