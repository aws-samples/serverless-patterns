/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

const AWS = require('aws-sdk')
AWS.config.region = process.env.AWS_REGION 
const sns = new AWS.SNS({apiVersion: '2012-11-05'})

// The Lambda handler
exports.handler = async (event) => {
  // Params object for SNS
  const params = {
    Message: `Message at ${Date()}`,
    Subject: 'New message from publisher',
    TopicArn: process.env.SNStopic
  }
  
  // Send to SNS
  const result = await sns.publish(params).promise()
  console.log(result)
}