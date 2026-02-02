# Amazon API Gateway as a proxy to GraphQL API on AWS AppSync with Amazon DynamoDB as the data source

This pattern shows how to access a GraphQL API on AWS AppSync using API Gateway HTTP API as a proxy to the GraphQL API. Amazon API Gateway HTTP API is setup via integration to route all requests to the AppSync API GraphQL endpoint. This implementation will support all GraphQL `queries` and `mutations` defined in the AppSync API GraphQL schema however will not support `subscriptions`. To demonstrate this pattern, the template will deploy a simple Restaurant API with Amazon DynamoDB as a data source.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigateway-appsync-dynamodb-sam

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```
   git clone https://github.com/aws-samples/serverless-patterns
   ```
2. Change directory to the pattern directory:
   ```
   cd apigateway-appsync-dynamodb-sam
   ```
3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
   ```
   sam deploy --guided
   ```
4. During the prompts:

   - Enter a stack name
   - Enter the desired AWS Region
   - Allow SAM CLI to create IAM roles with the required permissions.

   Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

5. Note the outputs from the SAM deployment process. Two of the outputs `AppSync API Key` and `API Gateway Endpoint` will be used to test this pattern.

## How it works

This patterns creates Amazon API Gateway HTTP API which is used as a proxy to AWS AppSync GraphQL API with Amazon DynamoDB as the data source. To demonstrate the pattern, we have built a simple Restaurant API where users can add, delete, update, get and list restaurants. All requests to the API Gateway endpoint is sent to the AppSync API endpoint where the request is fulfilled and the response sent back to the requester.

API Key is used as the authorization mode for the AppSync API however it is not recommended to use API Key for production application, kindly refer to other authorization modes supported by AppSync in the [documentation](https://docs.aws.amazon.com/appsync/latest/devguide/security-authz.html)

## Testing

You can easily test this pattern using any command prompt that supports the `curl` command. Refer to the outputs from deploying the SAM application which will be used for testing.

1. Open your command prompt
2. To add a new restaurant entry, run the `curl` command below by pasting it in your command prompt. Remember to replace the values for {ApiGatewayEndpoint} and {AppSyncApiKey} which are part of the output generated after deploying the SAM template

   ```curl {ApiGatewayEndpoint} \
   -H "x-api-key:{AppSyncApiKey}" \
   -H "Content-Type: application/json" \
   -d '{
      "query": "mutation AddRestaurant($input: AddRestaurantInput!) { addRestaurant(input: $input) { cuisine name restaurantId state zip } }",
      "variables": {
        "input": {
          "cuisine": "Chinese",
          "name": "My food",
          "state": "NY",
          "zip": "234"
        }
      }
    }'
   ```

3. To get the list of restaurants, paste the following command in your command prompt. Remember to replace the values for {ApiGatewayEndpoint} and {AppSyncApiKey} which are part of the output generated after deploying the SAM template

```curl {ApiGatewayEndpoint} \
 -H "x-api-key:{AppSyncApiKey}" \
 -H "Content-Type: application/json" \
 -d '{"query": "query MyQuery {listRestaurants {items {name state restaurantId zip cuisine }}}","variables":"{}"}'
```

4. To get restaurant based on restaurant ID, paste the following command in your command prompt. Remember to replace the values for {ApiGatewayEndpoint} and {AppSyncApiKey} which are part of the output generated after deploying the SAM template and also {RestaurantID} for an existing restaurant you have already created.

   ```curl '{ApiGatewayEndpoint}' \
    -H 'x-api-key: {AppSyncApiKey}' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "query MyQuery($restaurantId: ID!) { getRestaurant(restaurantId: $restaurantId) { cuisine name restaurantId state zip } }",
      "variables": {
        "restaurantId": "{RestaurantID}"
      }
    }'
   ```

## Cleanup

1. Delete the stack
   ```bash
   sam delete
   ```

---

Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
