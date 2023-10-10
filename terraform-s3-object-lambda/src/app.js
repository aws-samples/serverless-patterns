/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

const { S3 } = require("aws-sdk");
const axios = require("axios").default;  // Promise-based HTTP requests
const sharp = require("sharp"); // Used for image resizing

const s3 = new S3();

exports.handler = async (event) => {
  // Output the event details to CloudWatch Logs.
  console.log("Event:\n", JSON.stringify(event, null, 2));

  // Retrieve the operation context object from the event.
  // This contains the info for the WriteGetObjectResponse request.
  // Includes a presigned URL in `inputS3Url` to download the requested object.
  const { getObjectContext } = event;
  const { outputRoute, outputToken, inputS3Url } = getObjectContext;

  // Get image stored in S3 accessible via the presigned URL `inputS3Url`.
  const { data } = await axios.get(inputS3Url, { responseType: "arraybuffer" });

  // Resize the image
  // Height is optional, will automatically maintain aspect ratio.
  // withMetadata retains the EXIF data which preserves the orientation of the image.
  const resized = await sharp(data).resize({ width: 100, height: 100 }).withMetadata();

  // Send the resized image back to S3 Object Lambda.
  const params = {
    RequestRoute: outputRoute,
    RequestToken: outputToken,
    Body: resized,
  };
  await s3.writeGetObjectResponse(params).promise();

  // Exit the Lambda function.
  return { statusCode: 200 };
};
