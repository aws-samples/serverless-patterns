/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

const { GetObjectCommand, PutObjectCommand, S3Client } = require("@aws-sdk/client-s3");
const s3 = new S3Client({ region: process.env.AWS_REGION });

const gm = require('gm')
const NEW_SIZE_PX = 480

// 1. Load the image from S3.
// 2. Transform the image.
// 3. Save the new image in another S3 bucket.

exports.handler = async (event) => {
    // console.log(JSON.stringify(event, null, 2))
    const Key = decodeURIComponent(event.Records[0].s3.object.key.replace(/\+/g, " "))


    // Read the object from S3
    const commandGet = new GetObjectCommand({
        Bucket: event.Records[0].s3.bucket.name,
        Key
      });
    const s3Object = await s3.send(commandGet);

    // Resize the image
    const data = await resizeImage(s3Object.Body)
    
    // Write to S3
    const commandPut = new PutObjectCommand({
        Bucket: process.env.DESTINATION_BUCKETNAME,
        Key,
        ContentType: 'image/jpeg',
        Body: data,
      });
    const result = await s3.send(commandPut);
    console.log('Write result: ', result)
}



// Resize - takes and returns a image buffer
const resizeImage = async (buffer) => {
    return new Promise((resolve, reject) => {
    gm(buffer)
        .resize(NEW_SIZE_PX, NEW_SIZE_PX)
        .toBuffer('jpg', function (err, data) {
            if (err) return reject(err)
            resolve(data)
        })
    })
}