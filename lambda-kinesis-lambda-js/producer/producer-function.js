// ! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
//   SPDX-License-Identifier: MIT-0
const AWS = require('aws-sdk');

const streamName = process.env.KINESIS_STREAM;
const kinesisClient = new AWS.Kinesis({ region: process.env.AWS_REGION });

function putToStream(propertyId, propertyValue, propertyTimestamp) {
    const payload = {
        prop: String(propertyValue),
        timestamp: String(propertyTimestamp),
        property_id: propertyId
    };

    console.log(payload);

    const params = {
        StreamName: streamName,
        Data: JSON.stringify(payload),
        PartitionKey: propertyId
    };
    //return params
    return kinesisClient.putRecord(params).promise();
}

exports.lambda_handler = async (event, context) => {
    const propertyValue = Math.floor(Math.random() * (120 - 40 + 1)) + 40;
    const propertyTimestamp = Math.floor(new Date().getTime() / 1000);
    const propertyId = 'Property11';

    try {
        await putToStream(propertyId, propertyValue, propertyTimestamp);
        return { statusCode: 200, body: 'Successfully posted' };
    } catch (error) {
        console.error('Error:', error);
        return { statusCode: 500, body: 'Error posting to stream' };
    }
};