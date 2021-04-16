# Amazon API Gateway REST API to Amazon DynamoDB

This pattern creates an Amazon API Gateway REST API that integrates with an Amazon DynamoDB table.

Learn more about this pattern at Serverless Land Patterns: http://serverlessland.com/patterns/apigw-dynamodb.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd apigw-rest-api-dynamodb
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern creates an Amazon API Gateway REST API that integrates with an Amazon DynamoDB table named "Music". The API includes an API key and usage plan. The DynamoDB table includes a Global Secondary Index named "Artist-Index". The API integrates directly with the DynamoDB API and supports [PutItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutItem.html) and [Query](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Query.html) actions.

## Testing

Once the application is deployed, use [Postman](https://www.postman.com/) to test the API using the following instructions.

1. Launch the AWS Management Console and open the API Gateway console. Select the API named "api-music".
	* In the Stages section, copy the Invoke URL from the stage named "v1".
	* In the API Keys section, copy the API key named "api-music-apikey".
1. Launch Postman
1. Choose the **Authorization** tab. Choose **API Key** for the authorization type. Enter **x-api-key** as the Key name. Enter the API key as the Value.
1. Invoke the DynamoDB **PutItem** action to add a new item to the DynamoDB table:
	* Enter the Invoke URL in the address bar. Add the **/music** path to the URL.
	```
	https://{ApiId}.execute-api.{Region}.amazonaws.com/v1/music
	```
	* Select **POST** as the HTTP method from the drop-down list to the left of the address bar.
	* Choose the **Body** tab. Choose **raw** and select **JSON** from the drop-down list. Enter the following into the text box: 
	```
	{
		"artist": "The Beatles",
		"album": "Abbey Road"
	}
	```
	* Choose **Send** to submit the request and receive a "200 OK" response.
	* Open the DynamoDB console and select the table named "Music" to confirm that the item has been added.
	* Change the values for artist or album and repeat this process to add multiple items to the DynamoDB table.
1. Invoke the DynamoDB **Query** action to query items by artist in the DynamoDB table:
	* Enter the Invoke URL in the address bar. Add **/music** to the URL path.
	* Add **/The+Beatles** to the URL path. This defines the artist name that you want to query. The **+** represents a space.
	```
	https://{ApiId}.execute-api.{Region}.amazonaws.com/v1/music/The+Beatles
	```
	* Select **GET** as the HTTP method from the drop-down list to the left of the address bar.
	* Choose the **Body** tab. Choose **none**.
	* Choose **Send** to submit the request and receive a "200 OK" response with a list of the matching results. Example: 
	```
	{
		"music": [
			{
				"id": "9cd966d3-b161-45cf-ab07-ce39178c05b5",
				"artist": "The Beatles",
				"album": "Abbey Road"
			}
		]
	}
	```
## Documentation
- [Tutorial: Build an API Gateway REST API with AWS integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-aws-proxy.html)
- [How do I use API Gateway as a proxy for another AWS service?](https://aws.amazon.com/premiumsupport/knowledge-center/api-gateway-proxy-integrate-service/)
- [Using Amazon API Gateway as a proxy for DynamoDB](https://aws.amazon.com/blogs/compute/using-amazon-api-gateway-as-a-proxy-for-dynamodb/)
- [Setting up data transformations for REST APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-data-transformations.html)
- [Amazon API Gateway API request and response data mapping reference](https://docs.aws.amazon.com/apigateway/latest/developerguide/request-response-data-mappings.html)
- [API Gateway mapping template and access logging variable reference](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html)

## Cleanup
 
1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0