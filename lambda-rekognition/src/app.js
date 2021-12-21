/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

const AWS = require('aws-sdk')
AWS.config.update({ region: process.env.AWS_REGION })


exports.handler = (event, context, callback) => {

    console.log('Received s3 event:', JSON.stringify(event, null, 2));

    bucketName = event['detail']['requestParameters']['bucketName']
    imageName = event['detail']['requestParameters']['key']

    rekognition_client = new AWS.Rekognition();

    // Analyze image to see if there is text in the image
    rekognition_client.detectText({
        Image: {
            S3Object: {
                Bucket: bucketName,
                Name: imageName,
            },
        },
    }, function (error, textDetectionResponse) {
        if (error)
            console.log("Error in Text Detection from Rekognition: ", error.message, error.stack);
        else {
            console.log("textDetectionResponse: ", textDetectionResponse);

            console.log(`========== Detected Text for: ${imageName} ==========`);
            textDetectionResponse.TextDetections.forEach(label => {
                if(label.ParentId == undefined)
                    console.log(`Detected Text: ${label.DetectedText}`)
            });
        }
    });
}
