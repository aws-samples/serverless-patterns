/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

// Lambda function used as CloudFormation custom resource to create an S3 object.
//const AWS = require("aws-sdk");
//const S3 = new AWS.S3();
const { S3 } = require("aws-sdk");
const s3 = new S3();
const response = require("./cfn-response.js");

exports.handler = async (event, context) => {
  console.log("Event:\n", JSON.stringify(event));
  let responseData = {};
  let responseStatus = response.FAILED;
  // CloudFormation custom resource request types: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/crpg-ref-requesttypes.html
  if (event.RequestType == "Delete") {
    // If the CloudFormation stack is deleted:
    try {
      // To allow the CloudFormation process to continue regardless of the delete operation response,
      // set the responseStatus to SUCCESS before the delete operation begins.
      responseStatus = response.SUCCESS;
      // Required resource properties to delete an S3 object:
      const params = {
        Bucket: event.ResourceProperties.Bucket,
        Key: event.ResourceProperties.Key,
      };
      await s3.deleteObject(params).promise();
    } catch (error) {
      console.error("Error during S3 delete:\n", error);
    }
  } else {
    // If the CloudFormation stack is created or updated:
    try {
      // Required resource properties to create/update an S3 object:
      const params = {
        Bucket: event.ResourceProperties.Bucket,
        Key: event.ResourceProperties.Key,
        ContentType: event.ResourceProperties.ContentType,
        Body: event.ResourceProperties.Body,
      };
      const s3Upload = await s3.upload(params).promise();
      // Response data that is sent back to CloudFormation:
      responseData = { ObjectKey: s3Upload.Key };
      responseStatus = response.SUCCESS;
    } catch (error) {
      console.error("Error during S3 upload:\n", error);
    }
  }
  await response.send(event, context, responseStatus, responseData);
  return;
};
