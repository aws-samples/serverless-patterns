# Amazon DocumentDB Stream To EventBridge via AWS Lambda Integration

This project contains a sample AWS Cloud Development Kit (AWS CDK) template for configuring and deploying a CDC Stream (Similar to DynamoDB Stream) for Amazon DocumentDB using AWS Lambda and EventBridge. The stream will processes changes and send them to an EventBridge Bus for further processing.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/documentdb-stream-lambda-eventbridge-cdk.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed and configured

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```bash
   git clone https://github.com/aws-samples/serverless-patterns
   ```
2. Change directory to the pattern directory:
   ```bash
   cd serverless-patterns/documentdb-stream-lambda-eventbridge-cdk/cdk
   ```
3. Install dependencies:
   ```bash
   npm install
   ```
4. From the command line, configure AWS CDK:
   ```bash
   cdk bootstrap ACCOUNT-NUMBER/REGION # e.g.
   cdk bootstrap 9999999999/us-east-1
   cdk bootstrap --profile test 9999999999/us-east-1
   ```
5. From the command line, use AWS CDK to deploy the AWS resources for the pattern as specified in the `lib/cdk-stack.ts` file:
   ```bash
   cdk deploy
   ```
6. Note: The AWS CDK deployment process will output the Amazon DocumentDB name, the Lambda ARN used as a CDC Stream, the EventBridge Bus used for receiving the changes from the stream

## How it works

This pattern will use an already existing Amazon DocumentDB Database and attach a lambda function that will stream any change detected to the items in the aforementioned database.
Technically, there are 2 parts to attach and configure the stream:

1. Enable Change Stream on the Mongo database collection in DocumentDB
2. Create and configure an Event Source Mapping on a specific lambda for that database collection

This solution creates an AWS CDK Custom Resource backed by a Lambda. This CR lambda does the following:

1. Takes a lambda function name as an input to use it as the DocumentDB Stream
2. Fetches the DocDB secret from Secrets Manager
3. Creates a connection with DocDB Cluster
4. Enables the Change Stream on a specific database-collection combination
5. Creates and configures an Event Source mapping on the given lambda from step(1)

The following resources will be provisioned:

- A Lambda Function that processes the changes from an already existing Amazon DocumentDB Database and sends them to an EventBridge Bus
- An AWS CDK Custom Resource Lambda Function that enables the CDC of Amazon DocumentDB onto the stream Lambda Function
- A VPC Endpoint for the AWS Lambda Service (This is crucial to enabling the Lambda Event Source Mapping off of the Amazon DocumentDB Database)
- A VPC Endpoint for the AWS Secret Manager Service (This is crucial to allow the Lambda Event Source Mapping off of the Amazon DocumentDB Database)
- An EventBridge Bus that will receive changes from the Lambda and publish them to an EventBridge Rule
- An EventBridge Rule that receives the changes for the bus and publishes them to given targets for further processing
- A Lambda Function that acts as a target for the EventBridge Rule and further processes the changes

## Testing

There are multiple ways to test this pattern. A convenient way to test it is using AWS Cloud9 Environment from the AWS Console & using the AWS CLI in conjunction.

### Inputs

This pattern attaches a CDC Lambda Stream to an already existing Amazon DocumentDB Stream. So, it requires the following:

1. Amazon DocumentDB Cluster ARN
2. AWS Secret Manager ARN for the Database
3. AWS VPC ID where the Amazon DocumentDB Cluster is provisioned (if not provided will use default VPC)
4. AWS Security Group ID for the Amazon DocumentDB Cluster
5. Amazon DocumentDB Database Name
6. Amazon DocumentDB Collection Name

### AWS Console Part

If you don't have a functioning AWS Cloud9 Environment you can follow the first 2 steps in [this tutorial](https://docs.aws.amazon.com/lambda/latest/dg/with-documentdb-tutorial.html#docdb-cloud9-environment) to create one. NOTE: make sure your DocumentDB Cluster Security Group allow TCP communication to your AWS Cloud9 Security Group on port 27017

1. Open the AWS Cloud9 Console and connect to the database. NOTE: connection guidelines can be found on the DocumentDB specific cluster Console
2. Deploy the solution using the [deployment instructions](#Delployment_Instructions) and wait for the deployment to finish
3. In the AWS Cloud9 Console run the following command to insert a new item

```bash
db.products.insert({"TestProduct":"Cool Product"})
```

4. Check the AWS Console for the Stream Lambda for logs on the streamed item

#### Useful Commands on Cloud9

command to list items in a database collection (e.g. products collection)

```bash
 db.products.find( {} ).pretty()
```

command to insert a new item in a database collection (e.g. products collection)

```bash
db.products.insert({"TestProduct":"Cool Product"})
```

command to list change streams in a cluster

```bash
 cursor = new DBCommandCursor(db, db.runCommand({aggregate: 1,pipeline: [{$listChangeStreams: 1}], cursor:{}}));
```

command to enable the change stream on a database collection (e.g. products collection)

```bash
db.adminCommand({modifyChangeStreams: 1,database: "docdb",collection: "products", enable: true});
```

command to disable the change stream on a database collection (e.g. products collection)

```bash
db.adminCommand({modifyChangeStreams: 1,database: "docdb",collection: "products", enable: false});
```

#### Useful Commands on AWS CLI

command to list Event Source Mappings for all lambdas in the account

```bash
aws lambda list-event-source-mappings
```

command to delete Event Source Mappings for all lambdas in the account

```bash
aws lambda delete-event-source-mapping --uuid=f2799dc0-55a4-4b7b-bbd7-95e3dc4e51f7
```

## Cleanup

1. Delete the stack
   ```bash
   cdk destroy
   ```

## Resources

1. [Get Started with Amazon DocumentDB](https://docs.aws.amazon.com/documentdb/latest/developerguide/get-started-guide.html)
2. [Enabling Amazon DocumentDB Change Streams](https://docs.aws.amazon.com/documentdb/latest/developerguide/change_streams.html#change_streams-enabling)
3. [Tutorial: Using AWS Lambda with Amazon DocumentDB Streams](https://docs.aws.amazon.com/lambda/latest/dg/with-documentdb-tutorial.html)

---

Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
