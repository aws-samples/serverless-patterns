# HTTP API Gateway to SQS for passing custom http headers as message attributes.

This pattern enables you to pass custom HTTP headers as message attributes when sending messages from HTTP API Gateway to an SQS queue. The headers can be configured either as static values or dynamically passed from the incoming request headers. In the default configuration, the message attribute name is set as 'MessageAttribute1' which maps to the header name 'header1' in the integration request mapping. You can customize these message attribute, header names and static values, according to your requirements by updating the requestParameters section in the SqsIntegration configuration within your SAM template. You can set the name for API Gateway and the SQS queue. 

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the AWS Pricing page for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

Create an AWS account if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- AWS CLI installed and configured
- Git Installed
- AWS Serverless Application Model (AWS SAM) installed
- In the default configuration, the message attribute name is set as 'MessageAttribute1' which maps to the header name 'header1' in the integration request mapping. You can customize these message attribute, header names and static values, according to your requirements by updating the requestParameters section in the SqsIntegration configuration within your SAM template. You can set the name for API Gateway and the SQS queue. 

## Deployment Instructions:

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:

```
git clone https://github.com/aws-samples/serverless-patterns
```
2. Change directory to the pattern directory:

```
cd _patterns-model custom-http-headers-to-sqs-message-attributes-using-http-api-gateway
```
3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:

```
sam deploy --guided --capabilities CAPABILITY_AUTO_EXPAND CAPABILITY_IAM CAPABILITY_NAMED_IAM
```

4. During the prompts enter the values corresponding to each field. The values in the square brackets are the default values, which can be overwritten once you enter the inputs.

	Stack Name: 
	AWS Region: 
	Parameter ApiGatewayName: 
	Parameter QueueName: 
	#Shows you resources changes to be deployed and require a 'Y' to initiate deploy
	Confirm changes before deploy [Y/n]: Y
	#SAM needs permission to be able to create roles to connect to the resources in your template
	Allow SAM CLI IAM role creation [Y/n]: 
	#Preserves the state of previously provisioned resources when an operation fails
	Disable rollback [y/N]: 
	Save arguments to configuration file [Y/n]: 
	SAM configuration file [samconfig.toml]: 
	SAM configuration environment [default]: 


5. Allow SAM CLI to create IAM roles with the required permissions.
Once you have run sam deploy --guided mode once and saved arguments to a configuration file (samconfig.toml), you can use sam deploy in future to use these defaults.

6. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for later review.

## How it works:

This pattern sets up the following resources:

A HTTP API Gateway with SQS integration with configurations to map the http headers to message attributes for SQS. The HTTP API will have custom logging enabled and the logs will be sent to the Cloudwatch log group created by the pattern. An SQS queue will be created by the pattern and attached to the API Gateway with default parameters.

In the output section, the SAM deployment returns ProvidedInputs, HttpApiEndpoint, HttpApiArn, HttpApiId, LogGroupArn, QueueArn, ApiUsageInformation, Required headers, Message body sample, RoleArn and QueueUrl.

## Testing:

Invoke the API Gateway with required headers and body and see the message being received with the headers as message attributes.

- Example: (The following example is for the default configuration, you can modify the values based on your custom configuration)
	CLI: curl --location 'https://<HTTP-API-ID>.execute-api.<region>.amazonaws.com/sqs' \
	--header 'header1: value for header1 which will go as MessageAttribute1' \
	--header 'header2: value for header2 which will go as MessageAttribute2' \
	--header 'Content-Type: application/json' \
	--data '{
		"MessageBody": "Payload from client via HTTP API Gateway"
	}'

- Use Case requirements:
	- Required Headers:
		The following headers and their corresponding values are expected to passed along with the request when using this template
			- header1's (key and value) is required for MessageAttribute1
			- header2's (key and value) is required for MessageAttribute2
			- 'static_header3' is the static value being configured for MessageAttribute3's header. Since is it configured this header is not mandatory when sending the request.
	- Request Body Format:
        {
          "MessageBody": "Your message here"
        }

	- Message received in SQS will have the following attributes.
		Attributes (3)
		Name: MessageAttribute1 | Type: String | Value: value for header1 which will go as MessageAttribute1
		Name: MessageAttribute2 | Type: String | Value: value for header2 which will go as MessageAttribute2
		Name: MessageAttribute3 | Type: String | Value: static_header3

## Cleanup
- Delete the stack:

	```
	sam delete
	```

- Confirm the stack has been deleted

    ```
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```


Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0