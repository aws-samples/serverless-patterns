/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

import { TableConfig } from "../sqs-lambda-dynamo-stack";

// This file can be edited to add needed tables and their individual limits.
export const TABLE_CONFIG: TableConfig[] = [
    {
        name: "SampleTable1",
        writeCapacity: 5, // DynamoDB table WCU allocation.
        sqsMaxConcurrency: 10, // Maximum concurrency the SQS queue uses for Lambda.
        retryAttempts: 1, // Gives lambda time to retry before sending message to DLQ.
        lambdaRetryAttempts: 0, // Maximum number of times to retry when the function returns an error.
    },
    // {
    //     name: "SampleTable2",
    //     writeCapacity: 5,
    //     sqsMaxConcurrency: 10,
    //     retryAttempts: 1,
    //     lambdaRetryAttempts: 0,
    // },
    // {
    //     name: "SampleTable3",
    //     writeCapacity: 1,
    //     lambdaReservedConcurrency: 1,
    //     retryAttempts: 1,
    //     lambdaRetryAttempts: 0,
    // },
]

