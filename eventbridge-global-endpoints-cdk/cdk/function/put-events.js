const {
	EventBridgeClient,
	PutEventsCommand,
} = require('@aws-sdk/client-eventbridge');

const ebClient = new EventBridgeClient();

exports.handler = async (event) => {
	console.log('hello from testing lambda');
	var eventId = 0;

	while (eventId < 900) {
		eventId = eventId + 1;
		console.log(eventId);

		const detail = {
			orderDate: new Date(),
			eventId: eventId,
		};

		console.log(detail);

		const params = {
			Entries: [
				{
					Detail: JSON.stringify(detail),
					DetailType: 'test',
					EventBusName: process.env.EVENTBUS_NAME,
					Source: 'test',
				},
			],
			EndpointId: process.env.ENDPOINT,
		};

		console.log(params);

		try {
			await ebClient.send(new PutEventsCommand(params));
		} catch (e) {
			console.log(e);
		}

		sleep(1000);
	}
};

function sleep(milliseconds) {
	const date = Date.now();
	let currentDate = null;
	do {
		currentDate = Date.now();
	} while (currentDate - date < milliseconds);
}
