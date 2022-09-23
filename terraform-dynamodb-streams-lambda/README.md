# Amazon Dynamodb Streams to AWS Lambda

The Terraform template deploys a Lambda function, a DynamoDB table, and the minimum IAM resources required to run the application.

When items are written or updated in the DynamoDB table, the changes are sent to a stream. This pattern configures a Lambda function to poll this stream. The function is invoked with a payload containing the contents of the table item that changed.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/dynamodb-lambda.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Testing

After deployment, add an item to the DynamoDB table. Go to the CloudWatch Logs for the deployed Lambda function. You will see the event is logged out containing the item data.


/*

aws dynamodb put-item --table-name primary-killdeer-table-with-stream --item "{\"id\": {\"N\": \"37\"}}"

aws dynamodb scan --table-name primary-killdeer-table-with-stream
*/


----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
