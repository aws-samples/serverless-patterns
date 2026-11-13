/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

const { SQSClient, SendMessageCommand } = require('@aws-sdk/client-sqs')
const sqs = new SQSClient()

// The Lambda handler
exports.handler = async (event) => {
  // Params object for SQS
  const params = {
    MessageBody: `Message at ${Date()}`,
    QueueUrl: process.env.SQSqueueName
  }
  
  // Send to SQS
  const result = await sqs.send(new SendMessageCommand(params))
  console.log(result)
}