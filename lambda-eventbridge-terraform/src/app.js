/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

'use strict'

const AWS = require('aws-sdk')
AWS.config.update({ region: process.env.AWS_REGION })
const eventbridge = new AWS.EventBridge()

exports.handler = async (event) => {
  const params = {
    Entries: [ 
      {
        Detail: JSON.stringify({
          "message": "Hello from publisher",
          "state": "new"
        }),
        DetailType: 'Message',
        EventBusName: 'default',
        Source: 'demo.event',
        Time: new Date 
      }
    ]
  }
  // Publish to EventBridge
  const result = await eventbridge.putEvents(params).promise()
  console.log(result)
}