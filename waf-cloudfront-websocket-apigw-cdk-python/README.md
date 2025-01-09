# Protecting WebSocket API with CloudFront and WAF Integration 

This pattern implements a secure WebSocket API using AWS CDK, integrating CloudFront for distribution and WAF for protection through AWS CDK with Python. It makes use of API keys to ensure that the Websocket endpoint can only be accessed via the CloudFront distribution by passing the API key as custom header from CloudFront.

The WebSocket API provides real-time communication capabilities, while CloudFront ensures low-latency content delivery. The Web Application Firewall (WAF) adds an extra layer of security by protecting against common web exploits and controlling access based on configurable rules.

![Alt text](images/architecturediagram.png?raw=true "Architecture Diagram for WebSocket API with CloudFront and WAF Integration")


Learn more about this pattern at [Serverless Land Patterns](https://serverlessland.com/patterns/waf-cloudfront-websocket-apigw-cdk-python).

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

### Prerequisites

- Python 3.9 or later
- AWS CDK CLI
- AWS CLI configured with appropriate credentials 

***Please note that AWS WAF is available globally for CloudFront distributions. So you must use the Region us-east-1 region while deploying the stack (N. Virginia)***

### Installation

1. Clone the repository and change directory to pattern directory:
   ```
   git clone https://github.com/aws-samples/serverless-patterns
   cd serverless-patterns/waf-cloudfront-websocket-apigw-cdk-python
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate  
   ```

3. Install dependencies:
   ```
   python -m pip install -r requirements.txt
   ```


4. Deploy the stack:
   ```
   cdk bootstrap
   cdk deploy
   ```
   

### Configuration

The main configuration for the WebSocket API and related services is defined in `my_websocket_api/my_websocket_api_stack.py`. Key configurations include:

- WebSocket API settings
- Lambda function for handling WebSocket events
- CloudFront distribution settings
- WAF Web ACL rules



### Troubleshooting

1. Connection Issues:
   - Ensure you're using the correct CloudFront URL with the "wss://" protocol.
   - Verify that the API key is correctly set in the CloudFront distribution's custom headers.

2. Lambda Function Errors:
   - Check CloudWatch Logs for the Lambda function to see detailed error messages.
   - Ensure the Lambda function has the necessary permissions to execute and access required resources.

3. WAF Blocking Requests:
   - Review the WAF rules in the AWS Console to ensure they're not unintentionally blocking legitimate traffic.
   - Check the WAF logs in CloudWatch for details on blocked requests.



## Data Flow

The WebSocket API handles data flow as follows:

1. Client initiates a WebSocket connection to the CloudFront distribution URL.
2. WAF validates the request against the configured rules
3. CloudFront forwards the request to the API Gateway WebSocket API with the "x-api-key" as custom header.
4. Websocket API validates the API key and routes the request based on the route selection expression.

![Alt text](images/RequestFlow.png?raw=true "Request Flow for WebSocket API with CloudFront and WAF Integration")

## Testing

Copy the "DistributionURL" value from the Cloudformation Stack's output section. Use it to connect to your Webosocket API. When you connect to your API, API Gateway invokes the $connect route. 
```
wscat -c <DistributionURL>
```

Alternatively, you may also use Postman's Websocket Client to test the connection:

![Alt text](images/PostmanScreenshot.png?raw=true "Postman Screenshot for Websocket Connection via CloudFront URL")

After the connection is successful, you may verify the AWS Lambda execution logs to validate the messages that were sent.


## Cleanup
 
1. Delete the stack
    ```bash
   cdk destroy STACK-NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    cdk list
    ```
----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0