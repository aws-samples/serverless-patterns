# EventBridge triggers AppSync GraphQl API using API destination

This project contains a sample AWS CDK template for triggering [AWS AppSync](https://aws.amazon.com/appsync/) from an [Amazon EventBridge](https://aws.amazon.com/eventbridge/).

In this pattern, AWS AppSync is configured with a schema to manage and read todos. The pattern uses an EventBridge bus and an EventBridge [API destination](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-api-destinations.html) to trigger the AppSync GraphQL `updateTodo` mutation when an event that matches the defined rule is received. The AppSync [API KEY](https://docs.aws.amazon.com/appsync/latest/devguide/security-authz.html#api-key-authorization) is used as the mode of authorization.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deploy

1. Clone the project to your local working directory

   ```sh
   git clone https://github.com/aws-samples/serverless-patterns
   ```

2. Change the working directory to this pattern's directory

   ```sh
   cd cdk-eventbridge-appsync/cdk
   ```

3. Install the project dependencies

   ```sh
   npm install
   ```

4. Deploy the stack to your default AWS account and region. The output of this command shows the GraphQL API id, URL, api key, and the name of the EventBridge bus.

   ```sh
   cdk deploy
   ```

## Test

You can test the pattern by publishing an event to the `todos` bus.

Create a file `todo-update.json` with the following content:

```json
[
  {
    "EventBusName": "todos",
    "Source": "todos.system",
    "DetailType": "todos update",
    "Detail": "{ \"todo-id\": \"todo-id-123\", \"name\": \"my todo\", \"description\": \"update from event-bridge\" }"
  }
]
```

In your terminal, enter the following command:

```sh
aws events put-events --entries file://todo-update.json
```

You can see your subscription triggered by your mutation by starting a subscription from the console as shown below:

```graphql
subscription MySubscription {
  onUpdateTodo {
    createdAt
    description
    id
    name
    updatedAt
  }
}
```

![Listen for subscriptions in the console console](console.png)

## Cleanup

Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.

```sh
cdk destroy
```

## References

1. [Simplify out of band AWS AppSync real-time subscriptions with Amazon EventBridge](https://aws.amazon.com/blogs/mobile/appsync-eventbridge/)
2. [Real-Time Data](https://docs.aws.amazon.com/appsync/latest/devguide/aws-appsync-real-time-data.html)

----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
