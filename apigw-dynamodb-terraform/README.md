# Amazon API Gateway REST API to Amazon DynamoDB

This pattern creates an Amazon API Gateway REST API that integrates with an Amazon DynamoDB table.

Learn more about this pattern at Serverless Land Patterns: http://serverlessland.com/patterns/apigw-dynamodb-terraform

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli?in=terraform/aws-get-started) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/apigw-dynamodb-terraform
    ```
1. From the command line, initialize terraform to  to downloads and installs the providers defined in the configuration:
    ```
    terraform init
    ```
1. From the command line, apply the configuration in the main.tf file:
    ```
    terraform apply
    ```
1. During the prompts:
    * Enter yes
1. Note the outputs from the deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern creates an Amazon API Gateway REST API that integrates with an Amazon DynamoDB table named "Pets". The API includes an API key and usage plan. The DynamoDB table includes a Global Secondary Index named "PetsType-index". The API integrates directly with the DynamoDB API and supports [PutItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutItem.html) and [Query](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Query.html) actions.

## Testing

Once the application is deployed, you can test it using the following instructions.

1. The terraform outout included two things:
	* The url to the deployed API.
	* The Key to use with the deployed API.
1. To invoke the DynamoDB **PutItem** action to add a new item to the DynamoDB table:
	* Run the below command after you replace <KEY> and <URL> with the terraform output from earlier.
	```
	curl -H 'x-api-key: <KEY>' -H 'Content-Type: application/json' --request POST '<URL>' --data-raw '{ "PetType": "dog", "PetName": "tito", "PetPrice": 250 }'

	```
	* Repeate the process as many times as you can, try doing it with different Pet Types
1. Invoke the DynamoDB **Query** action to query items by PetType in the DynamoDB table:
	* Run the below command after you replace <KEY> and <URL> with the terraform output from earlier.
	```
	curl -H 'x-api-key: <KEY>' --request GET '<URL>'
	```
	* Repeate the process as many times as you can with different Pet Types
	* You should receive a "200 OK" response with a list of the matching results. Example: 
	```
	{
		"music": [
			{
				"id": "45b33352-fea0-4e8b-8c7a-6be11ec4ff80",
				"PetType": "dog",
				"PetName": "tito",
                "PetPrice": "250"
			}
		]
	}
	```

## Cleanup
 
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/apigw-dynamodb-terraform
    ```
1. Delete all created resources
    ```bash
    terraform destroy
    ```
1. During the prompts:
    * Enter yes
1. Confirm all created resources has been deleted
    ```bash
    terraform show
    ```
----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
