/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

const { S3Client, GetObjectCommand, PutObjectCommand } = require('@aws-sdk/client-s3')
const sharp = require('sharp')

const s3 = new S3Client({})
const NEW_SIZE_PX = 480

// For each SQS message:
// 1. Read the S3 event from the message body.
// 2. Load the image from the source bucket.
// 3. Resize the image with sharp.
// 4. Save the new image in the destination bucket. The object stays private.
// Failed messages are returned in batchItemFailures, so only they are retried.

exports.handler = async (event) => {
  const batchItemFailures = []

  for (const record of event.Records) {
    try {
      const s3Event = JSON.parse(record.body)
      // S3 sends an s3:TestEvent with no Records when the notification is created
      for (const s3Record of s3Event.Records ?? []) {
        await processObject(s3Record)
      }
    } catch (err) {
      console.error(`Failed to process message ${record.messageId}`, err)
      batchItemFailures.push({ itemIdentifier: record.messageId })
    }
  }

  return { batchItemFailures }
}

const processObject = async (s3Record) => {
  const Bucket = s3Record.s3.bucket.name
  const Key = decodeURIComponent(s3Record.s3.object.key.replace(/\+/g, ' '))

  const s3Object = await s3.send(new GetObjectCommand({ Bucket, Key }))
  const data = await resizeImage(Buffer.from(await s3Object.Body.transformToByteArray()))

  await s3.send(new PutObjectCommand({
    Bucket: process.env.DESTINATION_BUCKETNAME,
    Key,
    ContentType: 'image/jpeg',
    Body: data
  }))
  console.log(`Resized s3://${Bucket}/${Key} to s3://${process.env.DESTINATION_BUCKETNAME}/${Key}`)
}

// Resize - takes and returns an image buffer (JPEG, fits inside NEW_SIZE_PX x NEW_SIZE_PX)
const resizeImage = (buffer) =>
  sharp(buffer)
    .rotate()
    .resize(NEW_SIZE_PX, NEW_SIZE_PX, { fit: 'inside', withoutEnlargement: true })
    .jpeg()
    .toBuffer()

exports.resizeImage = resizeImage
