/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

import { TableConfig } from "../sqs-lambda-dynamo-stack";

// This file can be edited to add needed tables and their individual limits.
export const TABLE_CONFIG: TableConfig[] = [
    {
        name: "SampleTable1",
        writeCapacity: 1, // DynamoDB table WCU allocation.
        lambdaReservedConcurrency: 1, // Maximum concurrency of the AWS Lambda Function.
        retryAttempts: 1, // Gives lambda time to retry before sending message to DLQ.
        lambdaRetryAttempts: 0, // Maximum number of times to retry when the function returns an error.
        alarmThreshold: 1, // Value against which the DLQ alarm will trigger .
        alarmEvaluationPeriods: 1, // Number of periods over which data is compared to the DLQ threshold.
    },
    // {
    //     name: "SampleTable2",
    //     writeCapacity: 1,
    //     lambdaReservedConcurrency: 1,
    //     retryAttempts: 20,
    //     lambdaRetryAttempts: 0,
    //     alarmThreshold: 1,
    //     alarmEvaluationPeriods: 1,
    // },
    // {
    //     name: "SampleTable3",
    //     writeCapacity: 1,
    //     lambdaReservedConcurrency: 1,
    //     retryAttempts: 1,
    //     lambdaRetryAttempts: 0,
    //     alarmThreshold: 1,
    //     alarmEvaluationPeriods: 1,
    // },
]

