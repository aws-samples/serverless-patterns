/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

const { RekognitionClient, DetectTextCommand } = require('@aws-sdk/client-rekognition')


exports.handler = async (event) => {

    console.log('Received s3 event:', JSON.stringify(event, null, 2));

    bucketName = event['detail']['requestParameters']['bucketName']
    imageName = event['detail']['requestParameters']['key']

    rekognition_client = new RekognitionClient({ region: process.env.AWS_REGION });

    // Analyze image to see if there is text in the image
    try {
        const textDetectionResponse = await rekognition_client.send(new DetectTextCommand({
            Image: {
                S3Object: {
                    Bucket: bucketName,
                    Name: imageName,
                },
            },
        }));
        console.log("textDetectionResponse: ", textDetectionResponse);

        console.log(`========== Detected Text for: ${imageName} ==========`);
        textDetectionResponse.TextDetections.forEach(label => {
            if(label.ParentId == undefined)
                console.log(`Detected Text: ${label.DetectedText}`)
        });
    } catch (error) {
        console.log("Error in Text Detection from Rekognition: ", error.message, error.stack);
    }
}
