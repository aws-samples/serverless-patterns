/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

const { SQSClient, SendMessageCommand } = require('@aws-sdk/client-sqs')

const sqsClient = new SQSClient({
  region: process.env.AWS_REGION
})

// The Lambda handler
exports.handler = async (event) => {
  // Params object for SQS
  const params = {
    MessageBody: `Message at ${Date()}`,
    QueueUrl: process.env.SQSqueueName
  }
  
  // Send to SQS
  const command = new SendMessageCommand(params)
  const result = await sqsClient.send(command)
  console.log(result)
}
