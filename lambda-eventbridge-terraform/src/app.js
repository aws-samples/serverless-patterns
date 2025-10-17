/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

'use strict'

const { EventBridgeClient, PutEventsCommand } = require('@aws-sdk/client-eventbridge')
const eventbridge = new EventBridgeClient({ region: process.env.AWS_REGION })

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
  const result = await eventbridge.send(new PutEventsCommand(params))
  console.log(result)
}
