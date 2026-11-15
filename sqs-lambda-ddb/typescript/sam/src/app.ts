/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

import { DynamoDBClient, ProvisionedThroughputExceededException, PutItemCommand } from "@aws-sdk/client-dynamodb";
import { marshall } from "@aws-sdk/util-dynamodb";
import { SQSBatchResponse, SQSEvent, SQSHandler } from "aws-lambda";

// Get destination DynamoDB table name from the environment variables
const tableName = process.env.DESTINATION_TABLE_NAME;

// Create a DynamoDB client outside of the handler to optimize performance
const ddbClient = new DynamoDBClient({
    region: process.env.AWS_REGION,
    maxAttempts: 0, // disable automated retires, so that Lambda fails fast and relies on SQS retry capabilities.
});

// AWS Lambda handler function
export async function handler(event: SQSEvent): Promise<SQSBatchResponse> {
    console.log(`Received event: ${JSON.stringify(event)}`);

    // Process each message in the event
    for (const rec of event.Records) {
        try {
            // Get the message body and add timestamps for illustrative and performance tracking purposes
            const item = {
                ...JSON.parse(rec.body),
                timestamps: {
                    ddb: new Date().toISOString(),
                    sqs: new Date(parseInt(rec.attributes.SentTimestamp)).toISOString(),
                }
            };

            // Try saving the item to the destination DynamoDB table
            await ddbClient.send(new PutItemCommand({
                TableName: tableName,
                Item: marshall(item),
            }));
        }
        catch (e) { // If there was an error report the current record and the rest to SQS
            const failures = event.Records.slice(event.Records.indexOf(rec)).map(r => ({ itemIdentifier: r.messageId }));
            console.error(e.message);
            console.warn("Failed to process " + failures.length + " items: " + JSON.stringify(failures));
            return {
                batchItemFailures: failures,
            };
        }
    }

    console.log("Successfully processed " + event.Records.length + " items");
    // No failures to report
    return {
        batchItemFailures: [],
    };
}