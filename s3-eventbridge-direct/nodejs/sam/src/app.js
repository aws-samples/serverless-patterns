/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

const { S3Client, GetObjectCommand } = require('@aws-sdk/client-s3')
const s3 = new S3Client({ region: process.env.AWS_REGION })

/* S3 Event syntax from EventBridge

    {
        "version": "0",
        "id": "5d1069c2-1234-1234-1234-123456789012",
        "detail-type": "Object Created",
        "source": "aws.s3",
        "account": "123456789012",
        "time": "2021-12-10T12:55:54Z",
        "region": "us-east-1",
        "resources": [
            "arn:aws:s3:::eb-s3-test-sourcebucket-123456789012"
        ],
        "detail": {
            "version": "0",
            "bucket": {
                "name": "eb-s3-test-sourcebucket-123456789012"
            },
            "object": {
                "key": "small-test-file.txt",
                "size": 2726,
                "etag": "123456789012123456789012123456789012",
                "sequencer": "123456789012"
            },
            "request-id": "123456789012",
            "requester": "123456789012",
            "source-ip-address": "123.123.123.123",
            "reason": "PutObject"
        }
    }
*/

// Load the object from S3.
exports.handler = async (event) => {
    console.log(JSON.stringify(event, null, 2))

    // Read the object from S3
    const s3Object = await s3.send(new GetObjectCommand({
        Bucket: event.detail.bucket.name,
        Key: decodeURIComponent(event.detail.object.key.replace(/\+/g, " "))
    }))

    // Logs out the buffer
    console.log(s3Object.Body)
}
