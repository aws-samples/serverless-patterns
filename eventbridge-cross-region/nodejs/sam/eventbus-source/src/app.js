/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

const { EventBridgeClient, PutEventsCommand } = require('@aws-sdk/client-eventbridge')
const eventBridge = new EventBridgeClient()

exports.handler = async (event) => {
	console.log(JSON.stringify(event, null, 2))

	const ebEvent = { 
		Entries: [{
			Detail: JSON.stringify({
				apiEvent: event.queryStringParameters
			}),
			EventBusName: process.env.EVENT_BUS_NAME,
			DetailType: 'Request',
			Source: process.env.EVENTSOURCE,
			Time: new Date
		}]
	}

	console.log('Sending to EventBridge: ', ebEvent)
	const result = await eventBridge.send(new PutEventsCommand(ebEvent))

	console.log('Result: ', JSON.stringify(result, null, 2))

	return {
		statusCode: 200
	}
}
