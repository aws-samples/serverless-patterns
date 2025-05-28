
# Amazon DynamoDB Stream to AWS Step Functions Trigger

This Pattern is a  CDK construct to automatically trigger AWS Step Functions workflows in response to changes in DynamoDB tables. The `DynamoWorkflowTrigger` construct bridges DynamoDB streams and Step Functions by allowing you to define event handlers that monitor specific changes in your DynamoDB tables and trigger workflows in response. It leverages Lambda functions to evaluate conditions and start Step Functions state machines with inputs derived from the DynamoDB events.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/{}

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Node and NPM](https://nodejs.org/en/download/) installed
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd ddbstream-lambda-sfn-cdk-ts
    ```
3. To deploy from the command line use the following:
    ```bash
      npm install
      npx cdk bootstrap aws://accountnumber/region
      npm run lambda
      npx cdk synth
      npx cdk deploy --all
    ```


## Cleanup

1. From the command line, use the following in the source folder
    ```bash
    npx cdk destroy
    ```
2. Confirm the removal and wait for the resource deletion to complete.
----




## Example Stack Explanation

The `DdbstreamLambdaSfnExampleStack` demonstrates how to use the `DynamoWorkflowTrigger` construct:

1. It creates a DynamoDB table (`TestTable`) with streaming enabled
2. It creates a simple Step Functions state machine (`TestStateMachine`)
3. It sets up a trigger with the following behavior:
   - It applies a filter to ignore events where a `SkipMe` attribute exists in the new image
   - It only processes `MODIFY` events (updates to existing items)
   - It checks two conditions:
     - The new value of `testKey` must be "test8"
     - The old value of `testKey` must have been "test9"
   - When all conditions are met, it triggers the state machine with input parameters extracted from the DynamoDB event:
     - `Index` taken from the item's partition key
     - `MapAttribute` taken from the first element in a list attribute

This workflow allows you to respond to specific data changes in DynamoDB by executing custom workflows with Step Functions.

## Creating Your Own Stacks

### Basic Setup

1. Import necessary modules:

```typescript
import { DynamoWorkflowTrigger, EventName } from "ddbstream-lambda-sfn";
import { AttributeType, StreamViewType, Table } from "aws-cdk-lib/aws-dynamodb";
import { StateMachine } from "aws-cdk-lib/aws-stepfunctions";
```

2. Create a DynamoDB table with streaming enabled:

```typescript
const myTable = new Table(this, "MyTable", {
  partitionKey: {
    name: "Id",
    type: AttributeType.STRING
  },
  stream: StreamViewType.NEW_AND_OLD_IMAGES // Required for the trigger to work
});
```

3. Create a Step Functions state machine:

```typescript
const myStateMachine = new StateMachine(this, "MyWorkflow", {
  definition: /* your state machine definition */
});
```

4. Create the workflow trigger:

```typescript
new DynamoWorkflowTrigger(this, "MyTrigger", {
  eventHandlers: [
    {
      table: myTable,
      eventNames: [EventName.Insert], // Only trigger on inserts
      conditions: [
        { jsonPath: "$.NewImage.status.S", value: "PENDING" }
      ],
      stateMachineConfig: {
        stateMachine: myStateMachine,
        input: {
          id: "$.NewImage.Id.S",
          timestamp: "$.NewImage.createdAt.S"
        }
      }
    }
  ]
});
```



#### Using event source filters:

```typescript
new DynamoWorkflowTrigger(this, "FilteredTrigger", {
  eventSourceFilters: [
    FilterCriteria.filter({
      dynamodb: {
        NewImage: {
          status: {
            S: FilterRule.isEqual("ACTIVE"),
          },
        },
      },
    }),
  ],
  eventHandlers: [
    /* event handlers */
  ]
});
```



## Features

- Dead letter queue for failed invocations
- VPC support
- Custom security groups
- Fine-grained event filtering
- Multiple event handlers per construct
- JSONPath-based condition evaluation
- Input mapping for state machines

## Limitations

- Tables must have streams enabled with `NEW_AND_OLD_IMAGES`
- Conditions currently only support exact matches via the `value` property
- For complex filtering, use Lambda event source filters

## Troubleshooting

- Check CloudWatch Logs for the Lambda function
- Monitor the dead letter queue for failed events
- Ensure IAM permissions are correct for DynamoDB stream access and Step Functions execution


Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
