//! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0
exports.lambda_handler = async (event, context) => {
    const records = event.Records;

    for (const record of records) {
        const payload = Buffer.from(record.kinesis.data, 'base64').toString('utf-8');
        console.log('Received payload:', payload);
        // Add your custom logic to process the payload here
    }

    return { statusCode: 200, body: 'Success' };
};