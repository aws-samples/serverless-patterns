/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

const { SNSClient, PublishCommand } = require('@aws-sdk/client-sns')

const snsClient = new SNSClient({
  region: process.env.AWS_REGION
})

// The Lambda handler
exports.handler = async (event) => {
  // Params object for SNS
  const params = {
    Message: `Message at ${Date()}`,
    Subject: 'New message from publisher',
    TopicArn: process.env.SNStopic
  }
  
  // Send to SNS
  const result = await snsClient.send(new PublishCommand(params))
  console.log(result)
}
