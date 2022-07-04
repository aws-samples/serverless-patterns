/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

const AWS = require('aws-sdk')
AWS.config.region = process.env.AWS_REGION 
const sqs = new AWS.SQS({apiVersion: '2012-11-05'})

// The Lambda handler
exports.handler = async (event) => {
  // Params object for SQS
  const params = {
    MessageBody: `Message at ${Date()}`,
    QueueUrl: process.env.SQSqueueName
  }
  
  // Send to SQS
  const result = await sqs.sendMessage(params).promise()
  console.log(result)
}