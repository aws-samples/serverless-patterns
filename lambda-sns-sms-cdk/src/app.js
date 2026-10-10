/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */
const { SNSClient, PublishCommand } = require('@aws-sdk/client-sns')
const sns = new SNSClient()

// The Lambda handler
exports.handler = async (event) => {
  // Params object for SNS
  const params = {
    Message: `Message at ${Date()}`,
    Subject: 'New message from publisher',
    PhoneNumber: process.env.phoneNumber,
    MessageAttributes:{
      'AWS.MM.SMS.OriginationNumber':{
        'DataType':'String',
        'StringValue':process.env.tenDLC
      }
    }
  }

  // Send to SNS
  const result = await sns.send(new PublishCommand(params))
  console.log(result)
}
