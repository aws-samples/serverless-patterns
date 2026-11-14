/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

const { S3Client, GetObjectCommand, PutObjectCommand } = require('@aws-sdk/client-s3')
const s3 = new S3Client({ region: process.env.AWS_REGION })

const gm = require('gm')
const NEW_SIZE_PX = 480

// 1. Get S3 Event from SQS Event
// 2. Load the image from S3.
// 3. Transform the image.
// 4. Save the new image in another S3 bucket.

exports.handler = async (event) => {
  // console.log(JSON.stringify(event, null, 2))

  const s3Event = JSON.parse(event.Records[0].body)

  const Key = decodeURIComponent(s3Event.Records[0].s3.object.key.replace(/\+/g, " "))

  // Read the object from S3
  const s3Object = await s3.send(new GetObjectCommand({
    Bucket: s3Event.Records[0].s3.bucket.name,
    Key
  }))

  // Resize the image
  const data = await resizeImage(Buffer.from(await s3Object.Body.transformToByteArray()))

  // Write to S3
  const result = await s3.send(new PutObjectCommand({
    Bucket: process.env.DESTINATION_BUCKETNAME,
    Key,
    ContentType: 'image/jpeg',
    Body: data,
    ACL: 'public-read'
  }))
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