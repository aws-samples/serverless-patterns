/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

const { EventBridgeClient, PutEventsCommand } = require('@aws-sdk/client-eventbridge');
const eventbridge = new EventBridgeClient();

exports.handler = async (event) => {
  console.log(JSON.stringify(event, 0, null));
  const entries = event.Records.map((item) => ({
    Source: 'MyDynamoStream',
    EventBusName: 'MyEventBus',
    DetailType: 'transaction',
    Time: new Date(),
    Detail: JSON.stringify(item)
  }));
  console.log("Payload to Event Bridge");
  console.log(entries);
  const result = await eventbridge.send(new PutEventsCommand({ Entries: entries }));
  console.log('EventBridge result');
  console.log(result);
}