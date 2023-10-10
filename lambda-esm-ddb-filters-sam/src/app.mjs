/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

'use strict'

export async function handler(event, context) {
    console.log(`Received event: ${JSON.stringify(event)}`);
    for(const rec of event.Records) {
        console.log(JSON.stringify(rec.dynamodb));
    }
}