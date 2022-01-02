/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

const AWS = require('aws-sdk')
AWS.config.region = process.env.AWS_REGION || 'us-east-1'
const eventbridge = new AWS.EventBridge()

exports.handler = async (event) => {
  console.log(JSON.stringify(event, 0, null));
  let payload = { Entries: [] };
  event.Records.forEach((item) => {
    payload.Entries.push({
      // Event envelope fields
      Source: 'MyDynamoStream',
      EventBusName: 'MyEventBus',
      DetailType: 'transaction',
      Time: new Date(),

      // Main event body
      Detail: JSON.stringify(item)
    });
  });
  console.log("Payload to Event Bridge");
  console.log(payload);
  const result = await eventbridge.putEvents(payload).promise();
  console.log('EventBridge result');
  console.log(result);
}