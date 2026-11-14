/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

'use strict'

export async function handler(event, context) {
    console.log(`Received event: ${JSON.stringify(event)}`);
    for(const rec of event.Records) {
        const data = rec.kinesis.data;
        const decoded = Buffer.from(data, 'base64').toString('utf-8');
        console.log(`${rec.kinesis.partitionKey} record data: ${decoded}`);
    }
}