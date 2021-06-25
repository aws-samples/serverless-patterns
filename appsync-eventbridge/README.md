# AppSync EventBridge

This project contains a sample pattern for using an Amazon EventBridge event bus as a HTTP data source with an AWS AppSync API. The given CDK template creates an AppSync API, an event bus and an IAM role that allows your API to add events to the event bus.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deploy

1. Clone the project to your local working directory
```
git clone https://github.com/aws-samples/serverless-patterns
```

2. Change the working directory to this pattern's directory
```
cd appsync-eventbridge/cdk
```

3. Install dependencies
```
npm install
```

4. This project uses typescript as client language for AWS CDK. Run the given command to compile typescript to javascript
```
npm run build
```

5. Synthesize CloudFormation template from the AWS CDK app
```
cdk synth
```

6. Deploy the stack to your default AWS account and region. The output of this command should give you the ARN for you Lambda function, GraphQL URL and API Key for your AppSync API.
```
cdk deploy
```
## Test

You can test your AppSync API and Direct Lambda resolver by running a query from AWS AppSync console.

![](mutation.png)

You can run a query directly from your terminal:

```
# install curl. https://curl.se/
# optional: install jq. https://stedolan.github.io/jq/
# replace <graphqlUrl> and <apiKey> with the outputs values from `cdk deploy`
curl --location --request POST '<graphqlUrl>' \
--header 'x-api-key: <apiKey>' \
--header 'Content-Type: application/json' \
--data-raw '{"mutation":"mutation add { putEvent(event:"Sample event") { Entries { EventId ErrorCode ErrorMessage    } FailedEntries } }","variables":{}}' | jq
```

## Cleanup

Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.
```
cdk destroy
```

## References

1. https://docs.aws.amazon.com/appsync/latest/devguide/tutorial-http-resolvers.html

----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
