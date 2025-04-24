# AWS Service 1 to AWS Service 2

This pattern << explain usage >>

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.



## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/v2/guide/getting-started.html) (AWS CDK) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd apigw-lambda-powertools-openapi-cdk
    ```
1. Authenticate to the AWS account you want to deploy in.
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    cdk deploy
    ```

1. With successful deployment, cdk will print three Outputs to the terminal ("ApiGatewayEndpoint", "UserPoolClientId" and "UserPoolId"). Copy them to your text editor for later user.

## How it works

![Diagram of pattern](pattern.png)

Explain how the service interaction works.

## Testing

You will create an Amazon Cogntio user for authenticating against the API. Then, you will execute some requests against the Order API to generate events. Finally, you will observe the Logging, Tracing, Metrics and Parameters functionalities of the Powertools for AWS Lambda in the AWS console.

1. Set environment variables for the following commands. You will need the values of the Outputs you copied as last step of the Deployment Instructions:

    ```bash
    API_GATEWAY_ENDPOINT=<Value of the "ApiGatewayEndpoint" Output>
    USER_POOL_ID=<Value of the "UserPoolId" Output>
    USER_POOL_CLIENT_ID=<Value of the "UserPoolClientId" Output>
    USER_NAME=testuser
    USER_EMAIL=user@example.com
    USER_PASSWORD=MyUserPassword123!
    ```

1. Create a user in Cognito that will be used for authenticating test requests:

    ```bash
    aws cognito-idp admin-create-user \
        --user-pool-id $USER_POOL_ID \
        --username $USER_NAME \
        --user-attributes Name=email,Value=$USER_EMAIL \
        --temporary-password $USER_PASSWORD \
        --message-action SUPPRESS
    aws cognito-idp admin-set-user-password \
        --user-pool-id $USER_POOL_ID \
        --username $USER_NAME \
        --password $USER_PASSWORD \
        --permanent
    ```

1. Generate a Cognito IdToken for the user that will be sent as the Authorization header. Store it in the ID_TOKEN environment variable:

    ```bash
    ID_TOKEN=$(aws cognito-idp admin-initiate-auth \
        --user-pool-id $USER_POOL_ID \
        --client-id $USER_POOL_CLIENT_ID \
        --auth-flow ADMIN_USER_PASSWORD_AUTH \
        --auth-parameters USERNAME=$USER_NAME,PASSWORD=$USER_PASSWORD \
        --query 'AuthenticationResult.IdToken' \
        --output text)
    ```

1. Send a POST request that will create an order with the body being the content of the file `test/sample_create_order.json`. Store the order ID in the environment variable ORDER_ID for further use:

    ```bash
    ORDER_ID=$(curl -sS --header "Authorization: Bearer $ID_TOKEN" \
    $API_GATEWAY_ENDPOINT/order -X POST \
    -H "Content-Type: application/json" \
    --data "@./test/sample_create_order.json" | tee /dev/tty | jq -r .orderId)
    ```

    You will get the Order json as response.

1. Update the order with new shipping information using a PUT request:

    ```bash
    curl -sS --header "Authorization: Bearer $ID_TOKEN" \
    $API_GATEWAY_ENDPOINT/order/$ORDER_ID -X PUT \
    -H "Content-Type: application/json" \
    --data '{
        "shippingMethod": "NEXT_DAY",
        "customerNotes": "Please deliver before noon",
        "shippingAddress": {
        "street": "777 Main Street",
        "city": "Anytown",
        "state": "WA",
        "postalCode": "31415",
        "country": "USA"
        }
    }'
    ```

    You will get the updated Order json as response.

1. Retrieve the order using a GET request:

    ```bash
    curl -sS --header "Authorization: Bearer $ID_TOKEN" \
    $API_GATEWAY_ENDPOINT/order/$ORDER_ID -X GET
    ```

    You will again the the Order json as response.

1. Send a POST request that will create a second order with the body being the content of the file `test/sample_create_order2.json`.

    ```bash
    curl -sS --header "Authorization: Bearer $ID_TOKEN" \
    $API_GATEWAY_ENDPOINT/order -X POST \
    -H "Content-Type: application/json" \
    --data "@./test/sample_create_order2.json"
    ```

    You will get the second Order json as response.

1. Send a request to the `/orders/search` endpoint, looking for orders containing the product ID "PROD111". 

    ```bash
    curl -sS --header "Authorization: Bearer $ID_TOKEN" \
    $API_GATEWAY_ENDPOINT/orders/search -X POST \
    -H "Content-Type: application/json" \
    --data '{
        "productIds": ["PROD111"],
        "page": 1,
        "limit": 20,
        "sortBy": "createdAt",
        "sortOrder": "desc"
    }'
    ```

    Only the second Order json will be returned as the first one does not include PROD111.

1. Delete the first order

    ```bash
    curl -sS --header "Authorization: Bearer $ID_TOKEN" \
    $API_GATEWAY_ENDPOINT/order/$ORDER_ID -X DELETE
    ```

    There will be no response.

## Cleanup
 
1. Delete the stacks
    ```bash
    cdk destroy
    ```

----
Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
